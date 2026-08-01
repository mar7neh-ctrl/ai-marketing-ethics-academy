from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="AI Marketing Ethics Academy",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
RISKY_AD_PATH = BASE_DIR / "assets" / "risky_skincare_ad.png"

TOPICS = [
    "Bias & discrimination",
    "Manipulation & dark patterns",
    "Privacy & consent",
    "Intellectual property",
    "Disclosure & transparency",
    "Auditability",
    "Hallucinated claims",
    "Brand safety",
    "Model monitoring",
    "Agent governance",
    "AI policy",
    "Frontier-model governance",
    "Organizational accountability",
]

MODULES = {
    "1. Suspicious Ad": {
        "title": "The suspicious skincare ad",
        "time": "1 minute",
        "topics": ["Hallucinated claims", "Manipulation", "Brand safety", "Disclosure"],
        "prompt": "The AI made this ad overnight. What should the marketing manager do?",
        "options": {
            "Publish now while the trend is hot": {
                "correct": False,
                "delta": (18_000, -18, 30, -18),
                "feedback": "Short-term sales rise, but the unverified medical claims, fabricated testimonial, fake scarcity, and missing AI disclosure create serious brand and legal risk.",
            },
            "Pause, verify every claim, label AI media, and rewrite": {
                "correct": True,
                "delta": (6_000, 14, -12, 18),
                "feedback": "Correct. Verification, disclosure, and a less manipulative message reduce hallucination and brand-safety risk before launch.",
            },
            "Delete only the testimonial and publish the rest": {
                "correct": False,
                "delta": (10_000, -8, 16, -5),
                "feedback": "That fixes one issue, but the ad still contains an unsupported universal claim, artificial scarcity, and undisclosed synthetic imagery.",
            },
        },
    },
    "2. Targeting Lab": {
        "title": "The high-converting audience",
        "time": "1 minute",
        "topics": ["Bias", "Discrimination", "Privacy", "Consent"],
        "prompt": "The model found a profitable audience using inferred pregnancy status, ZIP code, income, and purchase history. What do you approve?",
        "options": {
            "Use every variable because the model predicts higher conversion": {
                "correct": False,
                "delta": (22_000, -20, 34, -22),
                "feedback": "Prediction is not permission. Sensitive inferences and proxy variables can invade privacy and reproduce discrimination even when protected traits are not named directly.",
            },
            "Use consented purchase interests; remove sensitive inferences and test outcomes for bias": {
                "correct": True,
                "delta": (9_000, 16, -14, 20),
                "feedback": "Correct. Data minimization, documented consent, and outcome testing preserve useful targeting while reducing privacy and discrimination risk.",
            },
            "Remove income but keep pregnancy status because it is accurate": {
                "correct": False,
                "delta": (14_000, -14, 25, -12),
                "feedback": "Accuracy alone does not make sensitive inference ethical. The company still lacks a clear purpose, informed consent, and safeguards against harmful exclusion.",
            },
        },
    },
    "3. Checkout Trap": {
        "title": "The consent screen",
        "time": "1 minute",
        "topics": ["Manipulation", "Dark patterns", "Consent", "Disclosure & transparency"],
        "prompt": "Which redesign should replace the current checkout screen?",
        "options": {
            "Keep the green Accept button and hide Decline in a text link": {
                "correct": False,
                "delta": (15_000, -15, 24, -16),
                "feedback": "Unequal visual treatment steers people toward a choice. Consent obtained through friction or concealment is not meaningfully voluntary.",
            },
            "Use equal buttons, plain-language purposes, no prechecked boxes, and easy withdrawal": {
                "correct": True,
                "delta": (5_000, 18, -15, 20),
                "feedback": "Correct. The redesign supports informed, specific, and reversible consent without manipulating the interface.",
            },
            "Precheck marketing consent but add a longer privacy policy": {
                "correct": False,
                "delta": (11_000, -10, 19, -10),
                "feedback": "More text does not fix a preselected choice. Transparency must make the decision understandable, not merely bury details in a policy.",
            },
        },
    },
    "4. Creative Rights": {
        "title": "The campaign asset folder",
        "time": "1 minute",
        "topics": ["Intellectual property", "Disclosure", "Auditability"],
        "prompt": "The AI campaign uses a licensed stock photo, a copied news article, an image resembling a famous character, and an unapproved customer testimonial. What is the safest decision?",
        "options": {
            "Publish because AI transformed the source material": {
                "correct": False,
                "delta": (16_000, -12, 31, -19),
                "feedback": "AI transformation is not automatic permission. The team still needs rights, licenses, releases, and evidence of where each asset came from.",
            },
            "Use only cleared assets and retain source, license, prompt, model version, reviewer, and approval date": {
                "correct": True,
                "delta": (4_000, 13, -16, 22),
                "feedback": "Correct. Rights clearance reduces IP risk, and the retained record creates an auditable decision trail.",
            },
            "Add 'AI-generated' below every asset and publish": {
                "correct": False,
                "delta": (9_000, -5, 21, -7),
                "feedback": "Disclosure helps transparency, but it does not replace copyright permission, a stock license, or a customer's release.",
            },
        },
    },
    "5. Agent Approval": {
        "title": "Who can press Publish?",
        "time": "1 minute",
        "topics": ["Agent governance", "AI policy", "Auditability", "Human oversight"],
        "prompt": "An AI agent can create copy, choose an audience, set the budget, and publish automatically. Which control design is strongest?",
        "options": {
            "Let the agent publish anything under $25,000": {
                "correct": False,
                "delta": (20_000, -17, 29, -20),
                "feedback": "A spending threshold does not control claims, targeting, privacy, or brand risk. Authority should depend on the action and risk level, not only budget.",
            },
            "Require data approval, claim verification, bias review, final human approval, logs, and a kill switch": {
                "correct": True,
                "delta": (7_000, 17, -17, 24),
                "feedback": "Correct. Clear authority limits, human checkpoints, logs, and emergency shutdown make the agent governable and auditable.",
            },
            "Review a random 5% of published ads afterward": {
                "correct": False,
                "delta": (13_000, -8, 20, -8),
                "feedback": "Sampling can support monitoring, but post-publication review alone cannot prevent high-impact harm or show who authorized the launch.",
            },
        },
    },
    "6. Model Shift": {
        "title": "Conversions rose - complaints did too",
        "time": "1 minute",
        "topics": ["Model monitoring", "Brand safety", "Risk", "Organizational accountability"],
        "prompt": "After a model update, conversion rises 18%, while false-claim flags and demographic complaint rates triple. What should the team do first?",
        "options": {
            "Keep running because the campaign is profitable": {
                "correct": False,
                "delta": (28_000, -24, 38, -25),
                "feedback": "Performance monitoring alone misses harm. Continuing after warning signals also increases the organization's accountability for preventable damage.",
            },
            "Pause affected automation, preserve logs, investigate, and roll back if safeguards degraded": {
                "correct": True,
                "delta": (-2_000, 19, -20, 25),
                "feedback": "Correct. Monitoring must connect warning signals to action: pause, investigate, document, remediate, and verify before relaunch.",
            },
            "Ask the model whether its update is safe": {
                "correct": False,
                "delta": (8_000, -13, 27, -15),
                "feedback": "A model cannot independently validate its own governance. Teams need external tests, complaint review, logs, and accountable human decision-makers.",
            },
        },
    },
    "7. Frontier Case": {
        "title": "Claude Fable 5 / Mythos 5 governance case",
        "time": "2 minutes",
        "topics": ["Frontier-model governance", "AI policy", "Risk", "Organizational accountability"],
        "prompt": "A frontier model has powerful cyber capabilities. A public version has safeguards, while a restricted version offers broader capability to vetted users. What governance principle matters most?",
        "options": {
            "Release the most capable version broadly, then respond to misuse": {
                "correct": False,
                "delta": (30_000, -21, 40, -28),
                "feedback": "Reactive governance is weak when potential harm is high. Access controls, capability evaluation, safeguards, monitoring, and incident response must exist before broad deployment.",
            },
            "Govern capability, safeguards, access, monitoring, and accountability together": {
                "correct": True,
                "delta": (3_000, 18, -18, 24),
                "feedback": "Correct. Frontier governance is not one filter. It is a system connecting model capability, who can access it, technical safeguards, ongoing monitoring, and named responsibility.",
            },
            "Let each customer decide what safeguards it wants": {
                "correct": False,
                "delta": (18_000, -12, 30, -17),
                "feedback": "Customer choice cannot replace provider responsibility for high-risk capability, access design, misuse monitoring, and escalation.",
            },
        },
    },
}

BASELINE = {"revenue": 50_000, "trust": 70, "risk": 25, "compliance": 55}


def init_state() -> None:
    defaults = {
        "answers": {},
        "completed": [],
        "revenue": BASELINE["revenue"],
        "trust": BASELINE["trust"],
        "risk": BASELINE["risk"],
        "compliance": BASELINE["compliance"],
        "final_audit": None,
        "student_name": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value.copy() if isinstance(value, (dict, list)) else value


def inject_css() -> None:
    st.markdown(
        """
        <style>
        :root { --ink:#172033; --muted:#667085; --red:#d94343; --coral:#ff7566;
                --cream:#fff8f2; --line:#e8e6e3; --green:#18794e; }
        .stApp { background: linear-gradient(180deg,#fffdfb 0%,#ffffff 38%); color:var(--ink); }
        [data-testid="stSidebar"] { background:#172033; }
        [data-testid="stSidebar"] * { color:#f7f7f8; }
        [data-testid="stSidebar"] .stProgress > div > div { background:var(--coral); }
        .academy-hero { padding:2.2rem 2.4rem; border-radius:24px; color:white;
          background:radial-gradient(circle at 86% 10%,rgba(255,117,102,.45),transparent 28%),
                     linear-gradient(135deg,#172033,#2b3450); box-shadow:0 18px 42px rgba(23,32,51,.16); }
        .academy-hero h1 { font-size:2.6rem; margin:0 0 .35rem 0; }
        .academy-hero p { color:#e8eaf0; font-size:1.05rem; max-width:760px; }
        .eyebrow { color:#ffab9f; font-weight:750; letter-spacing:.12em; font-size:.78rem; }
        .topic-row { display:flex; gap:.5rem; flex-wrap:wrap; margin:.6rem 0 1.2rem; }
        .topic-chip { display:inline-block; border:1px solid #e7ddd5; background:#fff8f2;
          color:#7b3f37; border-radius:999px; padding:.32rem .7rem; font-size:.78rem; font-weight:650; }
        .scenario { background:white; border:1px solid var(--line); border-radius:20px;
          padding:1.35rem 1.45rem; box-shadow:0 8px 24px rgba(23,32,51,.06); }
        .visual-card { border-radius:20px; padding:1.4rem; background:#fff7f1;
          border:1px solid #f0ded2; min-height:310px; }
        .risky-ad { background:linear-gradient(145deg,#ffe7d8,#fffaf6); text-align:center; position:relative; overflow:hidden; }
        .risky-ad .brand { letter-spacing:.24em; font-weight:800; font-size:.8rem; color:#6e453c; }
        .risky-ad h2 { font-family:Georgia,serif; font-size:2.05rem; color:#7e332b; margin:.8rem 0; }
        .risky-ad .bottle { margin:1rem auto; width:74px; height:135px; border-radius:18px 18px 24px 24px;
          background:linear-gradient(90deg,#d96d61,#ff9c8d,#bf5149); box-shadow:0 16px 28px rgba(126,51,43,.2); }
        .risky-ad .cta { display:inline-block; background:#7e332b;color:white;border-radius:999px;padding:.55rem 1rem;font-weight:800; }
        .checkout { background:#fff; border:1px solid #ddd; border-radius:16px; padding:1.1rem; }
        .accept { background:#21a366;color:#fff;padding:.7rem 1rem;border-radius:8px;text-align:center;font-weight:800; }
        .decline { text-align:center;color:#9a9a9a;font-size:.74rem;margin-top:.55rem; }
        .workflow { display:grid; grid-template-columns:1fr; gap:.55rem; }
        .workflow div { background:white;border:1px solid #dfe3e8;border-radius:10px;padding:.58rem .75rem;text-align:center;font-weight:700; }
        .workflow .danger { border-color:#e25c5c;background:#fff0ef;color:#9f2929; }
        .metric-note { color:#667085;font-size:.86rem; }
        .feedback-good { border-left:5px solid #18794e;background:#edf8f2;padding:1rem 1.1rem;border-radius:10px; }
        .feedback-bad { border-left:5px solid #c9362b;background:#fff1ef;padding:1rem 1.1rem;border-radius:10px; }
        .case-note { background:#f6f7fa;border-left:4px solid #667085;padding:.9rem 1rem;border-radius:8px;color:#344054; }
        .certificate { border:9px double #172033; background:#fffaf2; padding:2.2rem; text-align:center; }
        .certificate h2 { font-family:Georgia,serif; font-size:2rem; }
        div.stButton > button { border-radius:999px; font-weight:750; min-height:2.8rem; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def clamp_metrics() -> None:
    st.session_state.trust = max(0, min(100, st.session_state.trust))
    st.session_state.risk = max(0, min(100, st.session_state.risk))
    st.session_state.compliance = max(0, min(100, st.session_state.compliance))


def render_metrics() -> None:
    cols = st.columns(4)
    cols[0].metric("Campaign value", f"${st.session_state.revenue:,.0f}")
    cols[1].metric("Brand trust", f"{st.session_state.trust}/100")
    cols[2].metric("Legal & ethical risk", f"{st.session_state.risk}/100", delta_color="inverse")
    cols[3].metric("Governance readiness", f"{st.session_state.compliance}/100")


def render_sidebar() -> str:
    with st.sidebar:
        st.markdown("## 🧭 Ethics Academy")
        name = st.text_input("Name for your report", value=st.session_state.student_name)
        st.session_state.student_name = name.strip()
        completed_count = len(st.session_state.completed)
        st.caption(f"{completed_count} of {len(MODULES)} learning modules completed")
        st.progress(completed_count / len(MODULES))
        pages = ["Home"] + list(MODULES) + ["8. Final Audit", "Results & Exit"]
        page = st.radio("Choose a section", pages, label_visibility="collapsed")
        st.divider()
        st.caption("You may stop after any module. Download your report before closing the page.")
        if st.button("Reset activity", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    return page


def render_home() -> None:
    st.markdown(
        """
        <div class="academy-hero">
          <div class="eyebrow">INTERACTIVE MICRO-CERTIFICATE</div>
          <h1>AI Marketing Ethics Academy</h1>
          <p>You are the new AI Marketing Risk Analyst. Make launch decisions, see the business consequences, and build a defensible governance system.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    render_metrics()
    st.subheader("How it works")
    c1, c2, c3 = st.columns(3)
    c1.markdown("### 1. Choose\nOpen any short module in the sidebar. They do not have to be completed in order.")
    c2.markdown("### 2. Decide\nReview the scenario and choose what the company should do.")
    c3.markdown("### 3. Download\nStop at any time and download a report showing your decisions and topic coverage.")
    st.info("Recommended class path: complete all seven modules and the Final Audit. Minimum graded path: four modules plus the Final Audit.")
    st.subheader("What this activity covers")
    st.markdown("<div class='topic-row'>" + "".join(f"<span class='topic-chip'>{t}</span>" for t in TOPICS) + "</div>", unsafe_allow_html=True)
    st.caption("This is a rule-based teaching simulation. Its score supports discussion; it does not prove that a real campaign is ethical or lawful.")


def render_module_visual(module_name: str) -> None:
    if module_name.startswith("1."):
        if RISKY_AD_PATH.exists():
            st.image(str(RISKY_AD_PATH), caption="Fictional AI-generated ad", use_container_width=True)
        else:
            st.markdown(
                """
                <div class="visual-card risky-ad">
                  <div class="brand">NOVAGLOW</div><h2>Erase every blemish<br>in 48 hours</h2>
                  <div>Clinically proven for every skin type</div><div class="bottle"></div>
                  <div style="font-style:italic;margin-bottom:.8rem">“Dermatologists call it a miracle.” - Ava R.</div>
                  <span class="cta">BUY NOW - ONLY 3 LEFT</span>
                </div>
                """, unsafe_allow_html=True)
    elif module_name.startswith("2."):
        data = pd.DataFrame({"Signal": ["Purchase interests", "ZIP code", "Income", "Inferred pregnancy"], "Lift": [8, 12, 15, 22], "Concern": ["Low", "Medium", "High", "Very high"]})
        st.markdown("#### Model-selected targeting signals")
        st.dataframe(data, hide_index=True, use_container_width=True)
        st.caption("Higher predictive lift does not automatically mean the variable is appropriate to use.")
    elif module_name.startswith("3."):
        st.markdown(
            """
            <div class="visual-card"><div class="checkout"><h3>Your order is almost complete</h3>
            <p>Allow us and 327 partners to collect, combine, sell, and retain your data indefinitely.</p>
            <div class="accept">ACCEPT ALL & CONTINUE</div><div class="decline">No thanks, I prefer a worse experience</div>
            </div></div>
            """, unsafe_allow_html=True)
    elif module_name.startswith("4."):
        st.markdown("#### Assets queued for launch")
        st.dataframe(pd.DataFrame({"Asset": ["Licensed stock photo", "Copied news article", "Famous-character lookalike", "Customer testimonial"], "Documentation": ["License saved", "No permission", "Source unknown", "No release"]}), hide_index=True, use_container_width=True)
    elif module_name.startswith("5."):
        st.markdown(
            """
            <div class="visual-card"><div class="workflow">
            <div>Customer data</div><div>↓</div><div>AI writes advertisement</div><div>↓</div>
            <div>AI selects audience + budget</div><div>↓</div><div class="danger">AI publishes automatically</div>
            </div></div>
            """, unsafe_allow_html=True)
    elif module_name.startswith("6."):
        chart_data = pd.DataFrame(
            {
                "Before update": [100, 100, 100],
                "After update": [118, 310, 295],
            },
            index=["Conversion", "False-claim flags", "Demographic complaints"],
        )
        st.bar_chart(chart_data, height=300, color=["#98a2b3", "#ff7566"])
        st.caption("Index: performance before the model update = 100")
    else:
        st.markdown(
            """
            <div class="visual-card"><h3>Case timeline</h3>
            <p><b>April 7, 2026</b> - Anthropic introduces Project Glasswing and Mythos Preview.</p>
            <p><b>June 9, 2026</b> - Fable 5 and Mythos 5 are announced with different access and safeguard configurations.</p>
            <p><b>June 2026</b> - A U.S. directive temporarily suspends access over national-security concerns.</p>
            <p><b>July 1, 2026</b> - Fable 5 access is restored following additional safeguards and government review.</p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown("<div class='case-note'>The lesson is not that one event has a simple villain. The case asks who controls access, which safeguards are required, what gets documented, and who is accountable when frontier capability changes the risk.</div>", unsafe_allow_html=True)


def submit_module(module_name: str, choice: str) -> None:
    if module_name in st.session_state.answers:
        return
    result = MODULES[module_name]["options"][choice]
    revenue, trust, risk, compliance = result["delta"]
    st.session_state.revenue += revenue
    st.session_state.trust += trust
    st.session_state.risk += risk
    st.session_state.compliance += compliance
    clamp_metrics()
    st.session_state.answers[module_name] = choice
    st.session_state.completed.append(module_name)


def render_module(module_name: str) -> None:
    module = MODULES[module_name]
    st.caption(f"{module_name}  •  Estimated time: {module['time']}")
    st.title(module["title"])
    st.markdown("<div class='topic-row'>" + "".join(f"<span class='topic-chip'>{t}</span>" for t in module["topics"]) + "</div>", unsafe_allow_html=True)
    left, right = st.columns([1.05, 1], gap="large")
    with left:
        render_module_visual(module_name)
    with right:
        st.markdown(f"<div class='scenario'><h3>Your decision</h3><p>{module['prompt']}</p></div>", unsafe_allow_html=True)
        saved = st.session_state.answers.get(module_name)
        if saved:
            choice = saved
            st.radio("Choose one", list(module["options"]), index=list(module["options"]).index(saved), disabled=True, key=f"locked_{module_name}")
        else:
            choice = st.radio("Choose one", list(module["options"]), index=None, key=f"choice_{module_name}")
            if st.button("Submit decision", type="primary", disabled=choice is None, key=f"submit_{module_name}"):
                submit_module(module_name, choice)
                st.rerun()
        if saved:
            result = module["options"][saved]
            css = "feedback-good" if result["correct"] else "feedback-bad"
            label = "Strong governance decision" if result["correct"] else "Risky governance decision"
            st.markdown(f"<div class='{css}'><b>{label}</b><br>{result['feedback']}</div>", unsafe_allow_html=True)
            st.write("")
            render_metrics()


def render_final_audit() -> None:
    st.caption("FINAL CHALLENGE  •  Estimated time: 2 minutes")
    st.title("Audit the complete campaign")
    st.write("NovaGlow wants to launch nationally. Select every control that must be confirmed before approval.")
    controls = {
        "Product claims are supported and linked to evidence": "claims",
        "Customer-data purpose and consent are documented": "consent",
        "Targeting outcomes were tested for bias and discrimination": "bias",
        "Creative assets have licenses, releases, or documented rights": "ip",
        "AI-generated material and material limitations are disclosed": "disclosure",
        "A named human approved the campaign and the decision is logged": "audit",
        "Post-launch monitoring thresholds and a pause process exist": "monitoring",
        "The AI agent has authority limits and a kill switch": "agent",
    }
    with st.form("final_audit_form"):
        selected = [label for label in controls if st.checkbox(label, value=True if st.session_state.final_audit else False, key=f"audit_{controls[label]}")]
        reflection = st.text_area("In one sentence: What can an automated ethics score miss?", placeholder="Example: It can miss context, power differences, visual manipulation, or harms that were not encoded in its rules.")
        submitted = st.form_submit_button("Complete final audit", type="primary")
    if submitted:
        score = round(len(selected) / len(controls) * 100)
        st.session_state.final_audit = {"selected": selected, "score": score, "reflection": reflection.strip()}
        st.rerun()
    if st.session_state.final_audit:
        audit = st.session_state.final_audit
        decision = "APPROVE WITH MONITORING" if audit["score"] == 100 else "PAUSE AND REVISE"
        st.success(f"Governance readiness: {audit['score']}%  •  Decision: {decision}")
        if not audit["reflection"]:
            st.warning("Add a reflection sentence before submitting your report to your instructor.")
        st.markdown("**Key lesson:** A checklist makes controls visible and auditable, but human judgment is still needed to interpret context, severity, and consequences.")


def report_text() -> str:
    name = st.session_state.student_name or "Student"
    lines = [
        "AI MARKETING ETHICS ACADEMY - COMPLETION REPORT",
        f"Student: {name}",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"Modules completed: {len(st.session_state.completed)} of {len(MODULES)}",
        f"Campaign value: ${st.session_state.revenue:,.0f}",
        f"Brand trust: {st.session_state.trust}/100",
        f"Legal and ethical risk: {st.session_state.risk}/100",
        f"Governance readiness: {st.session_state.compliance}/100",
        "",
        "DECISIONS",
    ]
    if not st.session_state.answers:
        lines.append("No learning modules completed yet.")
    for module_name in MODULES:
        if module_name in st.session_state.answers:
            choice = st.session_state.answers[module_name]
            correct = MODULES[module_name]["options"][choice]["correct"]
            lines.extend([f"- {module_name}: {choice}", f"  Governance result: {'Strong' if correct else 'Risky'}"])
    lines.extend(["", "FINAL AUDIT"])
    if st.session_state.final_audit:
        lines.append(f"Score: {st.session_state.final_audit['score']}%")
        lines.append(f"Reflection: {st.session_state.final_audit['reflection'] or '[not entered]'}")
    else:
        lines.append("Not completed.")
    lines.extend(["", "Note: This is a rule-based educational simulation, not legal advice or proof of compliance."])
    return "\n".join(lines)


def render_results() -> None:
    st.title("Results & exit")
    render_metrics()
    completed = len(st.session_state.completed)
    final_done = st.session_state.final_audit is not None
    if completed >= 4 and final_done:
        name = st.session_state.student_name or "AI Marketing Risk Analyst"
        st.markdown(f"<div class='certificate'><div class='eyebrow'>MICRO-CERTIFICATE</div><h2>AI Marketing Ethics Academy</h2><p>This recognizes <b>{name}</b> for completing an applied audit of AI policy, ethics, governance, and risk in marketing analytics.</p><p><b>{completed} modules completed</b> • Final audit submitted</p></div>", unsafe_allow_html=True)
    else:
        st.info("To earn the completion certificate, finish at least four learning modules and the Final Audit. You can still download your current progress now.")
    st.download_button("Download completion report", data=report_text(), file_name="ai_ethics_academy_report.txt", mime="text/plain", type="primary", use_container_width=True)
    st.caption("Download before closing or refreshing the browser. This version intentionally avoids accounts and permanent data storage.")


def main() -> None:
    init_state()
    inject_css()
    page = render_sidebar()
    if page == "Home":
        render_home()
    elif page in MODULES:
        render_module(page)
    elif page == "8. Final Audit":
        render_final_audit()
    else:
        render_results()


if __name__ == "__main__":
    main()
