"""
Structured data extracted strictly from the Assignment Data Pack.
No invented information.
Week: Mon 21 Sep 2026 – Fri 25 Sep 2026
"""

from datetime import datetime, date

PEOPLE = {
    "arjun": {"name": "Arjun Malhotra", "role": "VP Sales", "email": "arjun.malhotra@veridian-corp.example"},
    "neha": {"name": "Neha Kapoor", "role": "Marketing Lead", "email": "neha.kapoor@veridian-corp.example"},
    "raghav": {"name": "Raghav Sethi", "role": "Ops Manager", "email": "raghav.sethi@veridian-corp.example"},
    "divya": {"name": "Divya Rao", "role": "Finance", "email": "divya.rao@veridian-corp.example"},
    "priya": {"name": "Priya Nair", "role": "Meridian Logistics (external)", "email": "priya.nair@meridianlogistics.example"},
    "facilities": {"name": "Facilities", "role": "Internal distribution list", "email": "facilities@veridian-corp.example"},
}

# Parsed calendar events (relevant ones)
CALENDARS = {
    "arjun": [
        {"date": date(2026, 9, 21), "start": "09:00", "end": "09:35", "event": "Leadership Sync"},
        {"date": date(2026, 9, 21), "start": "14:00", "end": "14:30", "event": "1:1 with Neha"},
        {"date": date(2026, 9, 21), "start": "16:00", "end": "17:00", "event": "Blocked"},
        {"date": date(2026, 9, 22), "start": "11:00", "end": "12:00", "event": "Internal Budget Review"},
        {"date": date(2026, 9, 22), "start": "15:00", "end": "15:30", "event": "Blocked"},
        {"date": date(2026, 9, 23), "start": "15:00", "end": "15:30", "event": "Call — Meridian Logistics"},
        {"date": date(2026, 9, 23), "start": "18:00", "end": "18:15", "event": "Blocked"},
        {"date": date(2026, 9, 24), "start": "09:00", "end": "10:00", "event": "Board Prep Session"},
        {"date": date(2026, 9, 24), "start": "16:00", "end": "17:00", "event": "Hiring Panel — Sales Associate"},
        {"date": date(2026, 9, 25), "start": "10:00", "end": "10:30", "event": "Facilities Check-in"},
        {"date": date(2026, 9, 25), "start": "13:00", "end": "14:00", "event": "Blocked"},
    ],
    "neha": [
        {"date": date(2026, 9, 24), "start": "09:30", "end": "10:00", "event": "Deck Review with Arjun"},
    ],
}

# Action items / commitments extracted and deduplicated across sources
# status: open | completed | waiting | unclear
# owner: arjun | other | unclear
ACTIONS = [
    {
        "id": "vendor_list",
        "title": "Send updated vendor list to Raghav",
        "description": "Arjun committed to send updated vendor list to Raghav Sethi.",
        "owner": "arjun",
        "type": "my_action",
        "deadline": date(2026, 9, 23),  # last promise: Wednesday morning
        "sources": [
            "Leadership Sync (Mon 21): 'I told Raghav I’d send him the updated vendor list. I’ll get that to him by end of day tomorrow.'",
            "Email Thread 1 (Vendor List): multiple follow-ups; Arjun last promised 'will send by tomorrow (Wednesday) morning for sure.'",
            "Voice Note 1 (Mon 21 18:40): 'need to get Raghav that vendor list... remind me.'",
            "Email from Raghav Wed 23 08:45: 'Just checking — still good for this morning?'",
        ],
        "status_as_of": {
            # status by end of day
            date(2026, 9, 21): "open",
            date(2026, 9, 22): "open",
            date(2026, 9, 23): "open",  # no confirmation of delivery in data
            date(2026, 9, 24): "open",
            date(2026, 9, 25): "open",
        },
        "notes": "No email confirmation that the list was actually sent. Still appears open.",
    },
    {
        "id": "meridian_call",
        "title": "Reconfirm / lock Meridian Logistics call time with Priya",
        "description": "Client call with Meridian Logistics was pushed; Arjun needed to reconfirm new time himself.",
        "owner": "arjun",
        "type": "my_action",
        "deadline": date(2026, 9, 23),
        "sources": [
            "Leadership Sync (Mon 21): 'client call with Meridian Logistics got pushed. I need to reconfirm the new time with their team myself.'",
            "Voice Note 2 (Wed 23 08:15): 'Meridian call — I owe Priya a time, need to lock that in today.'",
            "Email Thread 3: Arjun proposed Wed 3:00 PM (Tue 22), Priya confirmed, both reconfirmed Wed 23.",
            "Calendar: Wed 23 15:00–15:30 Call — Meridian Logistics",
        ],
        "status_as_of": {
            date(2026, 9, 21): "open",
            date(2026, 9, 22): "open",  # proposed but not yet fully locked from Arjun side until confirmations
            date(2026, 9, 23): "completed",
            date(2026, 9, 24): "completed",
            date(2026, 9, 25): "completed",
        },
        "notes": "Fully confirmed for Wednesday 3:00 PM. Call is on calendar.",
    },
    {
        "id": "deck_review",
        "title": "Review Q3 Campaign Deck with Neha",
        "description": "Review the Q3 campaign deck (originally targeted Wed, moved to Thu morning).",
        "owner": "arjun",
        "type": "my_action",
        "deadline": date(2026, 9, 24),
        "sources": [
            "Leadership Sync: Neha to send by Wednesday; later noted Thursday morning safer.",
            "Email Thread 2: shifted to Thursday morning 9:30 AM before board prep.",
            "Neha calendar + email Thu 24 08:00: Deck ready, attaching draft for 9:30 review.",
            "Calendar: Thu 24 09:30–10:00 Deck Review with Arjun (Neha side)",
        ],
        "status_as_of": {
            date(2026, 9, 21): "waiting",  # waiting on Neha
            date(2026, 9, 22): "waiting",
            date(2026, 9, 23): "waiting",
            date(2026, 9, 24): "open",     # deck arrived, review scheduled
            date(2026, 9, 25): "completed", # assume after the meeting
        },
        "notes": "Deck received morning of Thu 24. Review at 9:30 AM.",
    },
    {
        "id": "expense_report_review",
        "title": "Review July Expense Variance Report before Board Prep",
        "description": "Divya to deliver report; Arjun requested by Wed evening to review before Thu board prep.",
        "owner": "arjun",
        "type": "my_action",
        "deadline": date(2026, 9, 23),  # receive by Wed eve; review before Thu
        "sources": [
            "Leadership Sync: Divya to pull July expense variance report before Thursday’s board prep; Divya: Wednesday evening.",
            "Email Thread 4: Arjun asked for Wed evening; Divya confirmed and delivered Wed 23 18:00; Arjun acknowledged.",
            "Voice Note 2: 'expense variance report from Divya needs to be in my hands by Wednesday evening...'",
        ],
        "status_as_of": {
            date(2026, 9, 21): "waiting",
            date(2026, 9, 22): "waiting",
            date(2026, 9, 23): "open",      # received, needs review
            date(2026, 9, 24): "completed", # board prep happens
            date(2026, 9, 25): "completed",
        },
        "notes": "Report received Wed 23 18:00. Review intended before Thu 09:00 Board Prep.",
    },
    {
        "id": "mumbai_lease",
        "title": "Mumbai Office Lease Renewal – Signature / Ownership",
        "description": "Mumbai office lease renewal requires authorized signature by Friday 25 Sep EOD. Ownership is unclear.",
        "owner": "unclear",
        "type": "unclear_ownership",
        "deadline": date(2026, 9, 25),
        "sources": [
            "Leadership Sync (Mon 21): Raghav flagged; Divya thinks Facilities; Arjun: 'flag it, don’t assume.'",
            "Facilities email Mon 21: reminder signature by Friday 25 Sep.",
            "Raghav email Tue 22: has anyone confirmed who’s signing? Don’t think assigned.",
            "Divya email Wed 23: Not on my end — typically Facilities.",
            "Facilities email Thu 24 16:00: Second reminder, signature still pending, deadline Friday EOD.",
            "Raghav email Thu 24 16:45: one day out and still unowned — can you confirm who’s handling it?",
            "Voice Note 1 (Mon 21): 'still haven’t heard back on the Mumbai lease thing, someone needs to own that, I don’t think it’s me.'",
        ],
        "status_as_of": {
            date(2026, 9, 21): "unclear",
            date(2026, 9, 22): "unclear",
            date(2026, 9, 23): "unclear",
            date(2026, 9, 24): "unclear",
            date(2026, 9, 25): "unclear",
        },
        "notes": "CRITICAL: Ownership never assigned in the data. Facilities keeps reminding; Raghav escalates to Arjun. Arjun does not claim ownership. Flag only — do not invent an owner.",
    },
]

# Helper: days of the week for UI
WEEK_DAYS = [
    date(2026, 9, 21),  # Mon
    date(2026, 9, 22),  # Tue
    date(2026, 9, 23),  # Wed
    date(2026, 9, 24),  # Thu
    date(2026, 9, 25),  # Fri
]

DAY_NAMES = {
    date(2026, 9, 21): "Monday 21 Sep 2026",
    date(2026, 9, 22): "Tuesday 22 Sep 2026",
    date(2026, 9, 23): "Wednesday 23 Sep 2026",
    date(2026, 9, 24): "Thursday 24 Sep 2026",
    date(2026, 9, 25): "Friday 25 Sep 2026",
}
