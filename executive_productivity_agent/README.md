# Executive Productivity Agent — Assignment 1 (AIONOS)

**User:** Arjun Malhotra (VP Sales)  
**Week simulated:** Monday 21 Sep 2026 – Friday 25 Sep 2026  

A working, clickable prototype that turns messy executive inputs (meeting transcript, emails, calendars, voice notes) into a useful **daily action brief** and supports natural-language questions.

## Features (as required)

- Identifies commitments made by the executive
- Separates **My Actions** from **Waiting on Others**
- Detects deadlines and overdue items
- Deduplicates the same action across multiple sources
- Flags unclear ownership (never invents an owner)
- Produces a prioritised daily brief
- Answers questions such as “What did I promise Raghav?” or “What needs action today?”

## Quick Start (one-command local run)

```bash
# Clone / download this repo, then:
cd executive_productivity_agent
pip install -r requirements.txt
streamlit run app.py
```

The app opens in your browser. Use the sidebar to change the **as-of date** and explore how the brief evolves through the week.

## Project Structure

```
executive_productivity_agent/
├── app.py              # Streamlit UI (Daily Brief + Q&A + All Actions)
├── agent.py            # Core logic: status, overdue, brief generation, Q&A
├── data.py             # Structured knowledge base extracted from the data pack
├── requirements.txt
└── README.md
```

## Architecture (short)

1. **Data Pack → Structured KB** (`data.py`)  
   All facts, commitments, deadlines and ownership statements were manually extracted and deduplicated. No invented information.

2. **Agent Logic** (`agent.py`)  
   - Temporal status tracking (status changes realistically day-by-day)  
   - Overdue / due-today detection  
   - Classification: my_action / waiting / unclear_ownership  
   - Deterministic Q&A over the same KB

3. **UI** (`app.py`)  
   Streamlit prototype with four tabs: Daily Brief, Ask the Agent, All Actions, About & Architecture.

## Key Design Decisions

- **No runtime LLM** for the core answers → fully auditable, zero hallucination risk.  
- **Unclear ownership is only flagged** (Mumbai lease) — the agent never assigns an owner that is not present in the source data.  
- **Vendor list** remains open because the data pack never contains a confirmation that it was actually sent.  
- Meridian call, expense report and deck review show realistic progression from open → completed as the week advances.

## AI Tools Used During Development

- Cursor / Claude / ChatGPT — scaffolding of Streamlit layout, data modelling and clean code structure.
- All factual extraction performed manually from the official data pack to guarantee grounding.

## Demo

1. Launch the app (`streamlit run app.py`).
2. Set as-of date to **Thursday 24 Sep** (default) to see overdue + unclear items.
3. Try the suggested questions or type your own.
4. Switch to Monday / Wednesday to see how statuses evolve.

---

Built for the AIONOS Agentic AI Factory assignment.
