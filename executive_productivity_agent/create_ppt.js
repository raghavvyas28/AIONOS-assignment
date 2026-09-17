const pptxgen = require("pptxgenjs");

const pres = new pptxgen();
pres.layout = "LAYOUT_16x9";
pres.author = "AIONOS Candidate";
pres.title = "Executive Productivity Agent — Assignment 1";
pres.subject = "AIONOS Agentic AI Factory";

// Color palette — professional dark navy + teal accent
const C = {
  bg: "0F172A",
  card: "1E293B",
  accent: "14B8A6",
  accentDark: "0D9488",
  white: "FFFFFF",
  muted: "94A3B8",
  light: "E2E8F0",
  danger: "F87171",
  warning: "FBBF24",
  success: "34D399",
};

function addFooter(slide, num) {
  slide.addText("AIONOS  |  Executive Productivity Agent  |  Assignment 1", {
    x: 0.5, y: 5.25, w: 8, h: 0.25,
    fontSize: 10, color: C.muted, fontFace: "Calibri",
  });
  slide.addText(String(num), {
    x: 9.2, y: 5.25, w: 0.5, h: 0.25,
    fontSize: 10, color: C.muted, fontFace: "Calibri", align: "right",
  });
}

// ========== SLIDE 1: Title ==========
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0, y: 0, w: 0.15, h: 5.625, fill: { color: C.accent },
  });
  s.addText("EXECUTIVE PRODUCTIVITY AGENT", {
    x: 0.6, y: 1.6, w: 9, h: 0.5,
    fontSize: 14, color: C.accent, fontFace: "Calibri", bold: true, charSpacing: 3,
  });
  s.addText("Turning Messy Executive Inputs\ninto a Daily Action Brief", {
    x: 0.6, y: 2.2, w: 9, h: 1.2,
    fontSize: 32, color: C.white, fontFace: "Calibri", bold: true,
  });
  s.addText("Assignment 1  ·  AIONOS Agentic AI Factory\nUser: Arjun Malhotra (VP Sales)  ·  Week of 21–25 Sep 2026", {
    x: 0.6, y: 3.7, w: 9, h: 0.7,
    fontSize: 14, color: C.muted, fontFace: "Calibri",
  });
}

// ========== SLIDE 2: Problem & Goal ==========
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  addFooter(s, 2);
  s.addText("The Problem & Goal", {
    x: 0.5, y: 0.3, w: 9, h: 0.5,
    fontSize: 26, color: C.white, fontFace: "Calibri", bold: true,
  });
  s.addShape(pres.shapes.RECTANGLE, {
    x: 0.5, y: 1.0, w: 4.3, h: 3.8, fill: { color: C.card },
  });
  s.addText("Messy Inputs", {
    x: 0.7, y: 1.2, w: 4, h: 0.4,
    fontSize: 16, color: C.accent, fontFace: "Calibri", bold: true,
  });
  s.addText([
    { text: "Meeting transcript (Leadership Sync)", options: { bullet: true, breakLine: true } },
    { text: "5 email threads (25 messages)", options: { bullet: true, breakLine: true } },
    { text: "Personal calendars of 4 people", options: { bullet: true, breakLine: true } },
    { text: "2 personal voice notes from Arjun", options: { bullet: true, breakLine: true } },
    { text: "Scattered commitments, shifting deadlines, unclear ownership", options: { bullet: true } },
  ], { x: 0.7, y: 1.7, w: 3.9, h: 2.8, fontSize: 13, color: C.light, fontFace: "Calibri" });

  s.addShape(pres.shapes.RECTANGLE, {
    x: 5.2, y: 1.0, w: 4.3, h: 3.8, fill: { color: C.card },
  });
  s.addText("Required Outcomes", {
    x: 5.4, y: 1.2, w: 4, h: 0.4,
    fontSize: 16, color: C.accent, fontFace: "Calibri", bold: true,
  });
  s.addText([
    { text: "Identify commitments by the executive", options: { bullet: true, breakLine: true } },
    { text: "Separate My Actions vs Waiting on Others", options: { bullet: true, breakLine: true } },
    { text: "Detect deadlines & overdue items", options: { bullet: true, breakLine: true } },
    { text: "Deduplicate across sources", options: { bullet: true, breakLine: true } },
    { text: "Flag unclear ownership (never invent it)", options: { bullet: true, breakLine: true } },
    { text: "Produce a daily brief + answer questions", options: { bullet: true } },
  ], { x: 5.4, y: 1.7, w: 3.9, h: 2.8, fontSize: 13, color: C.light, fontFace: "Calibri" });
}

// ========== SLIDE 3: Architecture ==========
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  addFooter(s, 3);
  s.addText("Architecture & Process Flow", {
    x: 0.5, y: 0.3, w: 9, h: 0.5,
    fontSize: 26, color: C.white, fontFace: "Calibri", bold: true,
  });

  // Boxes
  const boxes = [
    { x: 0.4, label: "1. Data Pack", sub: "Transcript\nEmails\nCalendars\nVoice notes" },
    { x: 2.7, label: "2. Structured KB", sub: "data.py\nDeduplicated\nactions + status" },
    { x: 5.0, label: "3. Agent Logic", sub: "Status · Overdue\nClassify · Brief\nQ&A matching" },
    { x: 7.3, label: "4. Streamlit UI", sub: "Daily Brief\nAsk Agent\nAll Actions" },
  ];
  boxes.forEach((b, i) => {
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: b.x, y: 1.3, w: 2.1, h: 2.6,
      fill: { color: C.card }, rectRadius: 0.1,
    });
    s.addShape(pres.shapes.RECTANGLE, {
      x: b.x, y: 1.3, w: 2.1, h: 0.08, fill: { color: C.accent },
    });
    s.addText(b.label, {
      x: b.x + 0.1, y: 1.55, w: 1.9, h: 0.5,
      fontSize: 14, color: C.accent, fontFace: "Calibri", bold: true, align: "center",
    });
    s.addText(b.sub, {
      x: b.x + 0.1, y: 2.2, w: 1.9, h: 1.4,
      fontSize: 12, color: C.light, fontFace: "Calibri", align: "center",
    });
    if (i < 3) {
      s.addText("→", {
        x: b.x + 2.0, y: 2.3, w: 0.5, h: 0.4,
        fontSize: 20, color: C.accent, fontFace: "Calibri",
      });
    }
  });

  s.addText("No runtime LLM for core answers → fully auditable, zero hallucination risk.", {
    x: 0.5, y: 4.2, w: 9, h: 0.4,
    fontSize: 13, color: C.muted, fontFace: "Calibri", italic: true,
  });
}

// ========== SLIDE 4: Inputs & Assumptions ==========
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  addFooter(s, 4);
  s.addText("Inputs, Sources & Assumptions", {
    x: 0.5, y: 0.3, w: 9, h: 0.5,
    fontSize: 26, color: C.white, fontFace: "Calibri", bold: true,
  });

  s.addText("Sources Used (strictly from data pack)", {
    x: 0.5, y: 0.95, w: 9, h: 0.35,
    fontSize: 15, color: C.accent, fontFace: "Calibri", bold: true,
  });
  s.addText([
    { text: "Leadership Sync transcript (Mon 21 Sep, 09:00–09:35)", options: { bullet: true, breakLine: true } },
    { text: "5 email threads × 5 messages each (Vendor List, Q3 Deck, Call Reschedule, Expense Report, Mumbai Lease)", options: { bullet: true, breakLine: true } },
    { text: "Calendars of Arjun, Neha, Raghav, Divya for the full week", options: { bullet: true, breakLine: true } },
    { text: "2 personal voice notes recorded by Arjun (Mon 21 & Wed 23)", options: { bullet: true } },
  ], { x: 0.5, y: 1.35, w: 9, h: 1.6, fontSize: 13, color: C.light, fontFace: "Calibri" });

  s.addText("Key Assumptions", {
    x: 0.5, y: 3.1, w: 9, h: 0.35,
    fontSize: 15, color: C.accent, fontFace: "Calibri", bold: true,
  });
  s.addText([
    { text: "As-of date is user-selectable; default Thursday 24 Sep so both open & completed items are visible.", options: { bullet: true, breakLine: true } },
    { text: "If no explicit confirmation of completion exists → item stays OPEN (vendor list).", options: { bullet: true, breakLine: true } },
    { text: "Unclear ownership is NEVER invented — only flagged (Mumbai lease).", options: { bullet: true, breakLine: true } },
    { text: "Calendar events = context unless corroborated by other sources.", options: { bullet: true } },
  ], { x: 0.5, y: 3.5, w: 9, h: 1.5, fontSize: 13, color: C.light, fontFace: "Calibri" });
}

// ========== SLIDE 5: Extracted Actions ==========
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  addFooter(s, 5);
  s.addText("Extracted & Deduplicated Actions", {
    x: 0.5, y: 0.3, w: 9, h: 0.5,
    fontSize: 26, color: C.white, fontFace: "Calibri", bold: true,
  });

  const actions = [
    { title: "Send vendor list to Raghav", type: "My Action", dl: "Wed 23", note: "Overdue by Thu" },
    { title: "Reconfirm Meridian call", type: "My Action", dl: "Wed 23", note: "Completed" },
    { title: "Review Q3 Campaign Deck", type: "My Action", dl: "Thu 24", note: "Due / scheduled" },
    { title: "Review Expense Variance Report", type: "My Action", dl: "Wed 23", note: "Received & reviewed" },
    { title: "Mumbai Lease Signature", type: "Unclear", dl: "Fri 25", note: "Ownership never assigned" },
  ];

  // Header row
  s.addShape(pres.shapes.RECTANGLE, { x: 0.4, y: 1.0, w: 9.2, h: 0.4, fill: { color: C.accentDark } });
  s.addText("Action", { x: 0.5, y: 1.05, w: 4, h: 0.3, fontSize: 12, color: C.white, fontFace: "Calibri", bold: true });
  s.addText("Type", { x: 4.5, y: 1.05, w: 1.8, h: 0.3, fontSize: 12, color: C.white, fontFace: "Calibri", bold: true });
  s.addText("Deadline", { x: 6.3, y: 1.05, w: 1.5, h: 0.3, fontSize: 12, color: C.white, fontFace: "Calibri", bold: true });
  s.addText("Status note", { x: 7.8, y: 1.05, w: 1.7, h: 0.3, fontSize: 12, color: C.white, fontFace: "Calibri", bold: true });

  actions.forEach((a, i) => {
    const y = 1.45 + i * 0.55;
    const bg = i % 2 === 0 ? C.card : "162032";
    s.addShape(pres.shapes.RECTANGLE, { x: 0.4, y: y, w: 9.2, h: 0.55, fill: { color: bg } });
    s.addText(a.title, { x: 0.5, y: y + 0.1, w: 4, h: 0.35, fontSize: 13, color: C.light, fontFace: "Calibri" });
    s.addText(a.type, { x: 4.5, y: y + 0.1, w: 1.8, h: 0.35, fontSize: 13, color: a.type === "Unclear" ? C.danger : C.accent, fontFace: "Calibri" });
    s.addText(a.dl, { x: 6.3, y: y + 0.1, w: 1.5, h: 0.35, fontSize: 13, color: C.light, fontFace: "Calibri" });
    s.addText(a.note, { x: 7.8, y: y + 0.1, w: 1.7, h: 0.35, fontSize: 12, color: C.muted, fontFace: "Calibri" });
  });
}

// ========== SLIDE 6: Daily Brief Example ==========
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  addFooter(s, 6);
  s.addText("Sample Daily Brief (as of Thu 24 Sep)", {
    x: 0.5, y: 0.3, w: 9, h: 0.5,
    fontSize: 26, color: C.white, fontFace: "Calibri", bold: true,
  });

  // Metrics
  const metrics = [
    { label: "Open My Actions", val: "2", color: C.accent },
    { label: "Due Today", val: "1", color: C.warning },
    { label: "Overdue", val: "1", color: C.danger },
    { label: "Unclear Ownership", val: "1", color: C.danger },
  ];
  metrics.forEach((m, i) => {
    const x = 0.5 + i * 2.35;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: x, y: 1.0, w: 2.2, h: 1.1, fill: { color: C.card }, rectRadius: 0.08,
    });
    s.addText(m.val, {
      x: x, y: 1.15, w: 2.2, h: 0.5,
      fontSize: 28, color: m.color, fontFace: "Calibri", bold: true, align: "center",
    });
    s.addText(m.label, {
      x: x, y: 1.65, w: 2.2, h: 0.3,
      fontSize: 11, color: C.muted, fontFace: "Calibri", align: "center",
    });
  });

  s.addText([
    { text: "⚠️ Overdue: ", options: { bold: true, color: C.danger } },
    { text: "Send updated vendor list to Raghav (deadline Wed 23 — no send confirmation in data)", options: { breakLine: true } },
    { text: "📌 Due Today: ", options: { bold: true, color: C.warning } },
    { text: "Review Q3 Campaign Deck with Neha (9:30 AM)", options: { breakLine: true } },
    { text: "🚨 Unclear: ", options: { bold: true, color: C.danger } },
    { text: "Mumbai Office Lease — signature still unowned, deadline Fri 25 EOD", options: { breakLine: true } },
    { text: "✔️ Completed earlier: ", options: { bold: true, color: C.success } },
    { text: "Meridian call locked; Expense report received & acknowledged", options: {} },
  ], { x: 0.5, y: 2.4, w: 9, h: 2.4, fontSize: 14, color: C.light, fontFace: "Calibri" });
}

// ========== SLIDE 7: Q&A Capability ==========
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  addFooter(s, 7);
  s.addText("Natural Language Q&A", {
    x: 0.5, y: 0.3, w: 9, h: 0.5,
    fontSize: 26, color: C.white, fontFace: "Calibri", bold: true,
  });

  const qa = [
    { q: "What did I promise Raghav?", a: "Send the updated vendor list. Original by Tue EOD → delayed to Wed morning. Still OPEN / OVERDUE." },
    { q: "What needs action today?", a: "Due today: Deck review. Overdue: Vendor list. Unclear: Mumbai lease ownership." },
    { q: "Who owns the Mumbai lease?", a: "Ownership is UNCLEAR. Facilities reminds, Raghav escalates, Divya points to Facilities, Arjun says “not me”. Agent only flags." },
    { q: "Status of Meridian call?", a: "Fully confirmed for Wed 23, 3:00 PM. On calendar. Status: COMPLETED." },
  ];
  qa.forEach((item, i) => {
    const y = 0.95 + i * 1.0;
    s.addShape(pres.shapes.RECTANGLE, { x: 0.5, y: y, w: 9, h: 0.9, fill: { color: C.card } });
    s.addText("Q: " + item.q, {
      x: 0.7, y: y + 0.1, w: 8.6, h: 0.3,
      fontSize: 13, color: C.accent, fontFace: "Calibri", bold: true,
    });
    s.addText("A: " + item.a, {
      x: 0.7, y: y + 0.42, w: 8.6, h: 0.4,
      fontSize: 12, color: C.light, fontFace: "Calibri",
    });
  });
}

// ========== SLIDE 8: Design Decisions ==========
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  addFooter(s, 8);
  s.addText("Key Design Decisions", {
    x: 0.5, y: 0.3, w: 9, h: 0.5,
    fontSize: 26, color: C.white, fontFace: "Calibri", bold: true,
  });

  const decisions = [
    { t: "Grounded Extraction", d: "All facts manually structured from the data pack. No invented commitments or owners." },
    { t: "Temporal Status", d: "Each action carries a day-by-day status map so the brief evolves realistically through the week." },
    { t: "Deduplication", d: "Vendor list appears in transcript + 5 emails + voice note → collapsed to one action with full source list." },
    { t: "Unclear = Flag Only", d: "Mumbai lease never assigned. Agent surfaces the risk and cites every source; never invents an owner." },
    { t: "Deterministic Q&A", d: "Keyword + intent matching over the same KB. Extensible to an LLM later without changing the data layer." },
    { t: "Clickable Prototype", d: "Streamlit app — one-command local run. Reviewer can change as-of date and ask questions immediately." },
  ];
  decisions.forEach((d, i) => {
    const col = i % 2;
    const row = Math.floor(i / 2);
    const x = 0.5 + col * 4.7;
    const y = 1.0 + row * 1.3;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: x, y: y, w: 4.5, h: 1.15, fill: { color: C.card }, rectRadius: 0.08,
    });
    s.addText(d.t, {
      x: x + 0.2, y: y + 0.15, w: 4.1, h: 0.3,
      fontSize: 14, color: C.accent, fontFace: "Calibri", bold: true,
    });
    s.addText(d.d, {
      x: x + 0.2, y: y + 0.5, w: 4.1, h: 0.55,
      fontSize: 12, color: C.light, fontFace: "Calibri",
    });
  });
}

// ========== SLIDE 9: AI Tools & How to Run ==========
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  addFooter(s, 9);
  s.addText("AI Tools Used & How to Run", {
    x: 0.5, y: 0.3, w: 9, h: 0.5,
    fontSize: 26, color: C.white, fontFace: "Calibri", bold: true,
  });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 0.5, y: 1.0, w: 4.4, h: 3.5, fill: { color: C.card }, rectRadius: 0.1,
  });
  s.addText("AI / Tools During Build", {
    x: 0.7, y: 1.2, w: 4, h: 0.4,
    fontSize: 15, color: C.accent, fontFace: "Calibri", bold: true,
  });
  s.addText([
    { text: "Cursor / Claude / ChatGPT", options: { bullet: true, breakLine: true } },
    { text: "Used for scaffolding Streamlit UI, data modelling and clean code structure.", options: { breakLine: true } },
    { text: "", options: { breakLine: true } },
    { text: "Manual extraction", options: { bullet: true, breakLine: true } },
    { text: "Every commitment, deadline and ownership statement was read and structured by hand from the official data pack — zero hallucination.", options: { breakLine: true } },
    { text: "", options: { breakLine: true } },
    { text: "No runtime LLM", options: { bullet: true, breakLine: true } },
    { text: "Answers are deterministic and fully auditable against the cited sources.", options: {} },
  ], { x: 0.7, y: 1.7, w: 4, h: 2.6, fontSize: 13, color: C.light, fontFace: "Calibri" });

  s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
    x: 5.2, y: 1.0, w: 4.3, h: 3.5, fill: { color: C.card }, rectRadius: 0.1,
  });
  s.addText("One-Command Local Run", {
    x: 5.4, y: 1.2, w: 4, h: 0.4,
    fontSize: 15, color: C.accent, fontFace: "Calibri", bold: true,
  });
  s.addText("cd executive_productivity_agent\npip install -r requirements.txt\nstreamlit run app.py", {
    x: 5.4, y: 1.8, w: 3.9, h: 1.3,
    fontSize: 14, color: C.white, fontFace: "Consolas",
  });
  s.addText("Then open the browser URL shown by Streamlit. Change the as-of date in the sidebar and try the suggested questions.", {
    x: 5.4, y: 3.3, w: 3.9, h: 1.0,
    fontSize: 13, color: C.muted, fontFace: "Calibri",
  });
}

// ========== SLIDE 10: Summary & Next Steps ==========
{
  const s = pres.addSlide();
  s.background = { color: C.bg };
  addFooter(s, 10);
  s.addText("Summary & Demo Readiness", {
    x: 0.5, y: 0.3, w: 9, h: 0.5,
    fontSize: 26, color: C.white, fontFace: "Calibri", bold: true,
  });

  const points = [
    { num: "01", t: "Working prototype", d: "Streamlit app with Daily Brief, Q&A, All Actions views" },
    { num: "02", t: "Fully grounded", d: "Every fact traceable to transcript / email / calendar / voice note" },
    { num: "03", t: "Handles hard cases", d: "Overdue detection, unclear ownership flag, temporal status" },
    { num: "04", t: "Reviewer-ready", d: "One-command run + GitHub + this 10-slide deck" },
  ];
  points.forEach((p, i) => {
    const y = 1.0 + i * 0.85;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, {
      x: 0.5, y: y, w: 9, h: 0.75, fill: { color: C.card }, rectRadius: 0.08,
    });
    s.addText(p.num, {
      x: 0.7, y: y + 0.15, w: 0.8, h: 0.45,
      fontSize: 20, color: C.accent, fontFace: "Calibri", bold: true,
    });
    s.addText(p.t, {
      x: 1.6, y: y + 0.1, w: 7.5, h: 0.3,
      fontSize: 15, color: C.white, fontFace: "Calibri", bold: true,
    });
    s.addText(p.d, {
      x: 1.6, y: y + 0.4, w: 7.5, h: 0.3,
      fontSize: 13, color: C.muted, fontFace: "Calibri",
    });
  });
}

pres.writeFile({ fileName: "/home/workdir/artifacts/executive_productivity_agent/Executive_Productivity_Agent_Assignment1.pptx" })
  .then(() => console.log("PPT created successfully"))
  .catch(err => console.error(err));
