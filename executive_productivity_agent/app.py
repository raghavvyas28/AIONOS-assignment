"""
Executive Productivity Agent — Streamlit Prototype
Assignment 1 | AIONOS Agentic AI Factory

Run: streamlit run app.py
"""

import streamlit as st
from datetime import date
from agent import generate_daily_brief, answer_question, get_all_actions_summary
from data import WEEK_DAYS, DAY_NAMES, PEOPLE

st.set_page_config(
    page_title="Executive Productivity Agent | Arjun Malhotra",
    page_icon="📋",
    layout="wide",
)

# ---------- Sidebar ----------
st.sidebar.title("📋 Executive Productivity Agent")
st.sidebar.markdown("**User:** Arjun Malhotra (VP Sales)")
st.sidebar.markdown("---")

selected_day = st.sidebar.selectbox(
    "As-of date (for status & deadlines)",
    options=WEEK_DAYS,
    format_func=lambda d: DAY_NAMES[d],
    index=3,  # default to Thursday 24 Sep
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Quick Tips")
st.sidebar.markdown(
    """
- Change the **as-of date** to see how statuses evolve across the week.
- Ask natural questions in the Q&A tab.
- All answers are grounded only in the provided data pack — no invented facts.
"""
)

# ---------- Header ----------
st.title("Executive Productivity Agent")
st.caption(f"Daily brief & commitments tracker for Arjun Malhotra  ·  Week of 21–25 Sep 2026  ·  Viewing as of **{DAY_NAMES[selected_day]}**")

tab1, tab2, tab3, tab4 = st.tabs(["📅 Daily Brief", "💬 Ask the Agent", "📊 All Actions", "ℹ️ About & Architecture"])

# ========== TAB 1: Daily Brief ==========
with tab1:
    brief = generate_daily_brief(selected_day)

    # Summary metrics
    c1, c2, c3, c4, c5 = st.columns(5)
    c1.metric("Open (My Actions)", brief["summary_counts"]["open_my_actions"])
    c2.metric("Due Today", brief["summary_counts"]["due_today"])
    c3.metric("⚠️ Overdue", brief["summary_counts"]["overdue"])
    c4.metric("Waiting on Others", brief["summary_counts"]["waiting"])
    c5.metric("Unclear Ownership", brief["summary_counts"]["unclear"])

    st.markdown("---")

    # Calendar today
    st.subheader(f"Today’s Calendar — {brief['day_name']}")
    if brief["calendar"]:
        for e in brief["calendar"]:
            st.markdown(f"- **{e['start']}–{e['end']}** · {e['event']}")
    else:
        st.info("No events on calendar for this day.")

    st.markdown("---")

    # Overdue first (high priority)
    if brief["overdue"]:
        st.subheader("⚠️ Overdue Items")
        for a in brief["overdue"]:
            with st.expander(f"🔴 {a['title']}  (deadline: {a['deadline']})", expanded=True):
                st.markdown(a["description"])
                st.markdown(f"**Notes:** {a['notes']}")
                st.markdown("**Sources:**")
                for s in a["sources"]:
                    st.markdown(f"- {s}")

    # Due today
    if brief["due_today"]:
        st.subheader("📌 Due Today")
        for a in brief["due_today"]:
            with st.expander(f"🟡 {a['title']}", expanded=True):
                st.markdown(a["description"])
                st.markdown(f"**Notes:** {a['notes']}")

    # My open actions
    st.subheader("✅ My Open Actions")
    if brief["my_actions"]:
        for a in brief["my_actions"]:
            icon = "🟡" if a["due_today"] else "⬜"
            with st.expander(f"{icon} {a['title']}  [{a['status']}]"):
                st.markdown(a["description"])
                st.markdown(f"**Deadline:** {a['deadline']}")
                st.markdown(f"**Notes:** {a['notes']}")
                st.markdown("**Sources:**")
                for s in a["sources"]:
                    st.markdown(f"- {s}")
    else:
        st.success("No open actions owned by you right now.")

    # Waiting
    st.subheader("⏳ Waiting on Others")
    if brief["waiting_on_others"]:
        for a in brief["waiting_on_others"]:
            with st.expander(f"⏳ {a['title']}  [{a['status']}]"):
                st.markdown(a["description"])
                st.markdown(f"**Notes:** {a['notes']}")
    else:
        st.info("Nothing currently waiting on others.")

    # Unclear ownership
    st.subheader("🚨 Unclear Ownership (Flagged)")
    if brief["unclear_ownership"]:
        for a in brief["unclear_ownership"]:
            with st.expander(f"🚨 {a['title']}  — deadline {a['deadline']}", expanded=True):
                st.warning("Ownership is unclear. Agent does **not** invent an owner.")
                st.markdown(a["description"])
                st.markdown(f"**Notes:** {a['notes']}")
                st.markdown("**Sources:**")
                for s in a["sources"]:
                    st.markdown(f"- {s}")
    else:
        st.success("No unclear-ownership items.")

    # Recently completed
    if brief["recently_completed"]:
        st.subheader("✔️ Recently Completed")
        for a in brief["recently_completed"]:
            st.markdown(f"- ~~{a['title']}~~ ({a['status']})")

# ========== TAB 2: Q&A ==========
with tab2:
    st.subheader("Ask the Agent")
    st.markdown("Examples: *What did I promise Raghav?* · *What needs action today?* · *Who owns the Mumbai lease?* · *Status of vendor list*")

    # Suggested buttons
    cols = st.columns(4)
    suggestions = [
        "What did I promise Raghav?",
        "What needs action today?",
        "What is overdue?",
        "Who owns the Mumbai lease?",
    ]
    for i, s in enumerate(suggestions):
        if cols[i].button(s, use_container_width=True):
            st.session_state["query"] = s

    query = st.text_input("Your question:", value=st.session_state.get("query", ""), key="q_input")
    if st.button("Ask", type="primary") or query:
        if query.strip():
            with st.spinner("Thinking..."):
                answer = answer_question(query, as_of=selected_day)
            st.markdown("### Answer")
            st.markdown(answer)
        else:
            st.info("Type a question or click a suggestion.")

# ========== TAB 3: All Actions ==========
with tab3:
    st.subheader("All Extracted Actions (Deduplicated)")
    st.caption("Actions identified across transcript, emails, calendars and voice notes. Deduplicated and status tracked over time.")
    rows = get_all_actions_summary(selected_day)
    for r in rows:
        status_color = {
            "open": "🔵",
            "waiting": "🟡",
            "completed": "🟢",
            "unclear": "🔴",
        }.get(r["status"], "⚪")
        overdue_tag = " ⚠️ OVERDUE" if r["overdue"] else ""
        st.markdown(
            f"{status_color} **{r['title']}**  \n"
            f"Owner: `{r['owner']}` · Type: `{r['type']}` · Deadline: `{r['deadline']}` · "
            f"Status: **{r['status']}**{overdue_tag}"
        )
        st.caption(r["notes"])
        st.markdown("---")

# ========== TAB 4: About ==========
with tab4:
    st.subheader("Architecture & Process Flow")
    st.markdown(
        """
### High-level Architecture
```
┌─────────────────┐     ┌──────────────────┐     ┌─────────────────┐
│  Data Pack      │────▶│  Structured KB   │────▶│  Agent Logic    │
│  (PDF sources)  │     │  (data.py)       │     │  (agent.py)     │
└─────────────────┘     └──────────────────┘     └────────┬────────┘
                                                          │
                                                          ▼
                                                 ┌─────────────────┐
                                                 │  Streamlit UI   │
                                                 │  Daily Brief +  │
                                                 │  Q&A            │
                                                 └─────────────────┘
```

### Process Flow
1. **Ingest** – Manually structured the raw transcript, 5 email threads, calendars and 2 voice notes into a clean action registry (no LLM hallucination).
2. **Extract & Deduplicate** – Same commitment appearing in meeting + email + voice note is collapsed into one action with multiple source citations.
3. **Classify** – Each action tagged as `my_action` / `waiting` / `unclear_ownership`.
4. **Temporal Status** – Status tracked per day of the week so the brief changes realistically as the week progresses.
5. **Deadline & Overdue detection** – Simple date comparison against the selected “as-of” day.
6. **Daily Brief generation** – Prioritised view: Overdue → Due Today → My Actions → Waiting → Unclear.
7. **Q&A** – Keyword + intent matching over the same grounded knowledge base (extensible to an LLM later).

### Inputs, Sources & Assumptions
- **Inputs used:** Leadership Sync transcript (Mon 21), all 5 email threads, personal calendars of Arjun/Neha/Raghav/Divya, 2 voice notes from Arjun.
- **Assumption 1:** “As-of” date is user-selectable; default Thursday 24 Sep (mid/late week) so both open and completed items are visible.
- **Assumption 2:** If no explicit confirmation of completion exists in the data (e.g. vendor list never marked sent), the item stays **open**.
- **Assumption 3:** Unclear ownership is **never invented** — the agent only flags it (Mumbai lease).
- **Assumption 4:** Calendar events are treated as context, not as new commitments unless corroborated by other sources.

### AI / Tools Used
- **Cursor / Claude / ChatGPT** – Used for rapid scaffolding of Streamlit UI, data modelling and clean code structure.
- **Manual extraction** – All facts, dates, commitments and ownership statements were read and structured by hand from the data pack to guarantee zero hallucination.
- No external LLM is called at runtime; answers are deterministic and fully auditable against the sources listed under each action.

### How to run
```bash
cd executive_productivity_agent
pip install streamlit
streamlit run app.py
```
"""
    )

    st.subheader("People in scope")
    for p in PEOPLE.values():
        st.markdown(f"- **{p['name']}** ({p['role']}) — `{p['email']}`")
