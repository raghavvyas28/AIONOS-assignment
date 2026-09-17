"""
Executive Productivity Agent logic.
Grounded only in the provided data pack. No hallucination of facts.
"""

from datetime import date, timedelta
from data import ACTIONS, CALENDARS, DAY_NAMES, WEEK_DAYS, PEOPLE


def get_status(action, as_of: date) -> str:
    """Return status of an action as of a given date."""
    status_map = action.get("status_as_of", {})
    # Find the latest status on or before as_of
    candidates = [d for d in status_map if d <= as_of]
    if not candidates:
        return "open"
    latest = max(candidates)
    return status_map[latest]


def is_overdue(action, as_of: date) -> bool:
    status = get_status(action, as_of)
    if status in ("completed",):
        return False
    deadline = action.get("deadline")
    if deadline and as_of > deadline:
        return True
    return False


def is_due_today(action, as_of: date) -> bool:
    deadline = action.get("deadline")
    return deadline == as_of and get_status(action, as_of) not in ("completed",)


def generate_daily_brief(as_of: date) -> dict:
    """
    Produce a structured daily action brief for Arjun as of the given date.
    Separates: My Actions (open), Waiting on Others, Unclear Ownership, Overdue, Completed recently.
    """
    my_actions = []
    waiting = []
    unclear = []
    overdue = []
    completed = []
    due_today = []

    for action in ACTIONS:
        status = get_status(action, as_of)
        overdue_flag = is_overdue(action, as_of)
        due = is_due_today(action, as_of)

        item = {
            "id": action["id"],
            "title": action["title"],
            "description": action["description"],
            "deadline": action.get("deadline"),
            "status": status,
            "overdue": overdue_flag,
            "due_today": due,
            "notes": action.get("notes", ""),
            "sources": action.get("sources", []),
        }

        if overdue_flag:
            overdue.append(item)

        if status == "completed":
            # only show recently completed if relevant
            if action["deadline"] and action["deadline"] >= as_of - timedelta(days=2):
                completed.append(item)
            continue

        if action["type"] == "unclear_ownership" or action["owner"] == "unclear":
            unclear.append(item)
        elif status == "waiting":
            waiting.append(item)
        elif action["owner"] == "arjun" or action["type"] == "my_action":
            my_actions.append(item)
            if due:
                due_today.append(item)

    # Calendar for the day
    day_events = [e for e in CALENDARS.get("arjun", []) if e["date"] == as_of]

    return {
        "as_of": as_of,
        "day_name": DAY_NAMES.get(as_of, str(as_of)),
        "my_actions": my_actions,
        "due_today": due_today,
        "waiting_on_others": waiting,
        "unclear_ownership": unclear,
        "overdue": overdue,
        "recently_completed": completed,
        "calendar": day_events,
        "summary_counts": {
            "open_my_actions": len(my_actions),
            "waiting": len(waiting),
            "unclear": len(unclear),
            "overdue": len(overdue),
            "due_today": len(due_today),
        },
    }


def answer_question(query: str, as_of: date = date(2026, 9, 24)) -> str:
    """
    Simple keyword + intent based Q&A over the grounded data.
    Supports examples like:
      - What did I promise Raghav?
      - What needs action today?
      - What is overdue?
      - Who owns the Mumbai lease?
      - Status of vendor list
      - What is on my calendar today?
    """
    q = query.lower().strip()

    # ---- Specific people / promises ----
    if "raghav" in q and ("promise" in q or "told" in q or "commit" in q or "owe" in q or "vendor" in q):
        action = next(a for a in ACTIONS if a["id"] == "vendor_list")
        status = get_status(action, as_of)
        overdue = is_overdue(action, as_of)
        lines = [
            f"**What you promised Raghav:** Send the updated vendor list.",
            f"- Original commitment (Leadership Sync Mon 21): by end of day Tuesday 22 Sep.",
            f"- Later emails: delayed to Wednesday morning 23 Sep.",
            f"- Status as of {DAY_NAMES.get(as_of, as_of)}: **{status.upper()}**",
        ]
        if overdue:
            lines.append("- ⚠️ This item is **OVERDUE** (no confirmation of delivery appears in the data).")
        lines.append("- Sources: Leadership Sync, Email Thread 1 (Vendor List), Voice Note 1.")
        return "\n".join(lines)

    if "priya" in q or "meridian" in q:
        action = next(a for a in ACTIONS if a["id"] == "meridian_call")
        status = get_status(action, as_of)
        return (
            f"**Meridian Logistics / Priya Nair call:**\n"
            f"- You needed to reconfirm the new time yourself after it was pushed.\n"
            f"- You proposed Wednesday 3:00 PM; Priya confirmed; both sides reconfirmed on Wed 23.\n"
            f"- Calendar shows Call — Meridian Logistics on Wed 23, 15:00–15:30.\n"
            f"- Status as of {DAY_NAMES.get(as_of, as_of)}: **{status.upper()}**\n"
            f"- Sources: Leadership Sync, Voice Note 2, Email Thread 3, Calendar."
        )

    if "neha" in q or "deck" in q or "campaign" in q:
        action = next(a for a in ACTIONS if a["id"] == "deck_review")
        status = get_status(action, as_of)
        return (
            f"**Q3 Campaign Deck (Neha):**\n"
            f"- Neha originally targeted Wednesday for your review; later shifted to Thursday morning (safer).\n"
            f"- Confirmed time: Thursday 24 Sep, 9:30 AM (before your Board Prep).\n"
            f"- Deck was attached and ready on Thu 24 at 08:00.\n"
            f"- Status as of {DAY_NAMES.get(as_of, as_of)}: **{status.upper()}**\n"
            f"- Sources: Leadership Sync, Email Thread 2, Calendars."
        )

    if "divya" in q or "expense" in q or "variance" in q:
        action = next(a for a in ACTIONS if a["id"] == "expense_report_review")
        status = get_status(action, as_of)
        return (
            f"**July Expense Variance Report (Divya):**\n"
            f"- You asked for it by Wednesday evening (instead of Thursday morning) so you could review before Board Prep.\n"
            f"- Divya delivered it on Wed 23 at 18:00; you acknowledged receipt.\n"
            f"- Status as of {DAY_NAMES.get(as_of, as_of)}: **{status.upper()}**\n"
            f"- Sources: Leadership Sync, Email Thread 4, Voice Note 2."
        )

    if "mumbai" in q or "lease" in q or "renewal" in q:
        action = next(a for a in ACTIONS if a["id"] == "mumbai_lease")
        return (
            f"**Mumbai Office Lease Renewal:**\n"
            f"- Deadline: Friday 25 September 2026, end of day (authorized signature required).\n"
            f"- Ownership is **UNCLEAR** — never assigned in any source.\n"
            f"- Facilities has sent two reminders (Mon + Thu).\n"
            f"- Raghav flagged it in the Leadership Sync and followed up multiple times; asked you on Thu 24 if you can confirm who is handling it.\n"
            f"- Divya: believes it sits with Facilities, not her.\n"
            f"- Your own Voice Note (Mon 21): 'someone needs to own that, I don’t think it’s me.'\n"
            f"- Agent recommendation: **Flag only — do not invent an owner.** Escalate ownership clarification today.\n"
            f"- Sources: Leadership Sync, Facilities emails, Raghav & Divya emails, Voice Note 1."
        )

    # ---- General queries ----
    if "today" in q and ("action" in q or "need" in q or "todo" in q or "do" in q):
        brief = generate_daily_brief(as_of)
        lines = [f"**What needs action on {brief['day_name']}:**\n"]
        if brief["due_today"]:
            lines.append("**Due today:**")
            for a in brief["due_today"]:
                lines.append(f"- {a['title']} (deadline today)")
        if brief["overdue"]:
            lines.append("\n**⚠️ Overdue:**")
            for a in brief["overdue"]:
                lines.append(f"- {a['title']} (deadline was {a['deadline']})")
        if brief["my_actions"]:
            lines.append("\n**Open actions owned by you:**")
            for a in brief["my_actions"]:
                lines.append(f"- {a['title']} [{a['status']}]")
        if brief["unclear_ownership"]:
            lines.append("\n**⚠️ Unclear ownership (flag):**")
            for a in brief["unclear_ownership"]:
                lines.append(f"- {a['title']} — deadline {a['deadline']}")
        if not (brief["due_today"] or brief["overdue"] or brief["my_actions"] or brief["unclear_ownership"]):
            lines.append("No open actions requiring your attention today based on the data.")
        return "\n".join(lines)

    if "overdue" in q:
        brief = generate_daily_brief(as_of)
        if not brief["overdue"]:
            return f"No overdue items as of {DAY_NAMES.get(as_of, as_of)}."
        lines = [f"**Overdue items as of {brief['day_name']}:**\n"]
        for a in brief["overdue"]:
            lines.append(f"- **{a['title']}** (deadline: {a['deadline']})\n  Notes: {a['notes']}")
        return "\n".join(lines)

    if "waiting" in q or "others" in q:
        brief = generate_daily_brief(as_of)
        if not brief["waiting_on_others"]:
            return "Nothing currently waiting on others (as of the selected day)."
        lines = ["**Waiting on others:**\n"]
        for a in brief["waiting_on_others"]:
            lines.append(f"- {a['title']} [{a['status']}]")
        return "\n".join(lines)

    if "calendar" in q or "schedule" in q or "meetings" in q:
        events = [e for e in CALENDARS.get("arjun", []) if e["date"] == as_of]
        if not events:
            return f"No calendar events for Arjun on {DAY_NAMES.get(as_of, as_of)}."
        lines = [f"**Your calendar on {DAY_NAMES.get(as_of, as_of)}:**\n"]
        for e in events:
            lines.append(f"- {e['start']}–{e['end']}: {e['event']}")
        return "\n".join(lines)

    if "brief" in q or "summary" in q or "daily" in q:
        return "Please use the **Daily Brief** tab / section for the full structured brief. You can also ask more specific questions."

    # Fallback – list available capabilities
    return (
        "I can answer questions grounded in the data pack, for example:\n"
        "- What did I promise Raghav?\n"
        "- What needs action today?\n"
        "- What is overdue?\n"
        "- Status of the Mumbai lease / vendor list / Meridian call / deck / expense report\n"
        "- What is on my calendar today?\n"
        "- Who owns the Mumbai renewal?\n\n"
        "Select a day in the sidebar to change the 'as of' date for status calculations."
    )


def get_all_actions_summary(as_of: date):
    """Return a flat list of all actions with current status for display."""
    result = []
    for a in ACTIONS:
        result.append({
            "id": a["id"],
            "title": a["title"],
            "owner": a["owner"],
            "type": a["type"],
            "deadline": a.get("deadline"),
            "status": get_status(a, as_of),
            "overdue": is_overdue(a, as_of),
            "notes": a.get("notes", ""),
        })
    return result
