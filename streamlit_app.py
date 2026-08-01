from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="AI Policy, Ethics, Governance, and Risk in Marketing Analytics",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
RISKY_AD_PATH = BASE_DIR / "assets" / "risky_skincare_ad.png"
SITE_TITLE = "AI POLICY, ETHICS, GOVERNANCE, AND RISK IN MARKETING ANALYTICS"


def option(correct, revenue, trust, risk, readiness, feedback):
    return {
        "correct": correct,
        "delta": (revenue, trust, risk, readiness),
        "feedback": feedback,
    }


MODULES = {
    "1. AI Governance": {
        "definition": "AI governance is the use of frameworks, policies, controls, and human oversight to ensure that AI systems are developed and used responsibly, ethically, and in compliance with regulations.",
        "slide_title": "Examples",
        "slide_items": [
            "Policies & Standards",
            "Data Governance",
            "Risk Management",
            "Transparency & Accountability",
            "Human Oversight",
            "Compliance & Regulation",
        ],
        "activity_title": "Build the governance foundation",
        "prompt": "NovaGlow wants to use AI for content creation, customer targeting, and automatic publishing. Which governance foundation should leadership approve?",
        "options": {
            "Let each marketing employee decide when AI is appropriate": option(False, 15000, -12, 24, -18, "Individual judgment alone does not create consistent policies, controls, documentation, or accountability."),
            "Create policies, data controls, risk reviews, human approval, documentation, and compliance checks": option(True, 6000, 16, -16, 22, "Correct. This connects the frameworks, policies, controls, and human oversight described in AI governance."),
            "Use AI freely until a customer complains": option(False, 22000, -20, 34, -24, "Waiting for harm is reactive. Governance must define responsibilities and controls before deployment."),
        },
    },
    "2. Bias & Discrimination": {
        "definition": "AI can inherit biases from historical training data. This can produce unfair marketing outcomes for certain groups.",
        "slide_title": "Example",
        "slide_text": "An AI advertising system learns from past campaigns and primarily shows high-paying job ads to men because historical data reflects more male applicants.",
        "slide_items": ["Use diverse datasets, regularly audit models for bias, and include human oversight to reduce bias & discrimination."],
        "activity_title": "Audit the targeting model",
        "prompt": "A recruiting campaign predicts higher clicks from men and begins limiting high-paying job ads to male audiences. What should the team do?",
        "options": {
            "Keep the targeting because it maximizes clicks": option(False, 19000, -20, 32, -22, "Historical performance can reproduce discrimination. Higher clicks do not make unequal access fair."),
            "Expand the audience, test outcomes across groups, audit the data, and require human review": option(True, 8000, 16, -15, 21, "Correct. Diverse data, bias auditing, and human oversight reduce the chance of unfair marketing outcomes."),
            "Remove gender but continue using strongly correlated proxy variables without testing": option(False, 13000, -12, 22, -12, "Removing one field does not prevent proxy discrimination. The team must test actual outcomes."),
        },
    },
    "3. Manipulation & Dark Patterns": {
        "definition": "AI-driven personalization can become manipulative if used unethically. Dark patterns steer users toward decisions they may not have intended.",
        "slide_title": "Key Ideas",
        "slide_text": "Note all the callouts, extreme ‘deals’, urgency indicators that could influence someone to make a purchase they might not otherwise using misleading/false data.",
        "activity_title": "Redesign the checkout trap",
        "prompt": "The checkout page uses a fake countdown, a bright Accept button, a hidden Decline link, and ‘Only 3 left’ when inventory is unlimited. What should replace it?",
        "options": {
            "Keep the screen because urgency increases conversions": option(False, 18000, -18, 28, -20, "Conversion does not justify misleading urgency or interface choices designed to steer users."),
            "Use truthful inventory, equal choices, plain language, and no preselected options": option(True, 5000, 18, -16, 20, "Correct. The redesign allows a voluntary choice without false urgency or visual manipulation."),
            "Keep the fake countdown but add a terms-and-conditions link": option(False, 13000, -13, 22, -12, "A buried link does not correct false information or manipulative design."),
        },
    },
    "4. Privacy & Consent": {
        "definition": "AI personalizes ads using browsing, purchase, and location data. Organizations must obtain clear, informed user consent.",
        "slide_title": "Key Information",
        "slide_text": "75% of consumers say they will not purchase from organizations they don't trust with their personal data. – Cisco",
        "slide_items": [
            "Privacy laws (GDPR & CCPA) regulate responsible data collection.",
            "Ethical data practices build customer trust and brand loyalty.",
            "Strong AI governance balances personalization with privacy!",
        ],
        "activity_title": "Choose a responsible personalization plan",
        "prompt": "The marketing model wants browsing history, purchases, precise location, health interests, and inferred pregnancy status. Which approach should be approved?",
        "options": {
            "Collect every available signal because personalization benefits customers": option(False, 21000, -21, 35, -23, "Personalization does not remove the need for purpose limits, data minimization, and clear informed consent."),
            "Use only necessary data for a stated purpose after clear consent and provide withdrawal controls": option(True, 7000, 19, -18, 22, "Correct. The approach balances useful personalization with privacy, consent, and customer trust."),
            "Collect everything now and ask permission after the campaign": option(False, 17000, -19, 31, -20, "Consent must come before the data is used, not after the campaign has already launched."),
        },
    },
    "5. Intellectual Property (IP)": {
        "definition": "Protects original creative works.",
        "slide_title": "Key Information",
        "slide_text": "The U.S. Copyright Office received over 10,000 public comments on AI and copyright, reflecting growing concerns about how generative AI creates and uses copyrighted content.",
        "slide_items": [
            "AI-generated marketing content",
            "Copyright ownership",
            "Human creative oversight",
            "Legal & brand protection",
        ],
        "activity_title": "Clear the campaign assets",
        "prompt": "The campaign includes a licensed stock photo, copied article text, an AI image resembling a famous character, and a testimonial used without permission. What should the team publish?",
        "options": {
            "Publish everything because AI transformed the material": option(False, 17000, -13, 32, -20, "AI transformation does not automatically create permission or ownership."),
            "Use only cleared assets and retain the source, license, release, prompt, model, reviewer, and approval date": option(True, 5000, 14, -17, 23, "Correct. Rights clearance and human creative oversight protect the company legally and support an auditable record."),
            "Label every asset AI-generated and publish it": option(False, 10000, -7, 22, -10, "Disclosure does not replace copyright permission, licenses, ownership, or customer releases."),
        },
    },
    "6. Disclosure & Transparency": {
        "definition": "Disclosure = Telling people AI is being used. Transparency = Explaining how or why AI is being used.",
        "slide_title": "FTC Guidance",
        "slide_text": "AI disclosures should be ‘clear and conspicuous’ so consumers know when AI influences marketing content.",
        "slide_items": [
            "AI use disclosure",
            "Explain AI decisions",
            "Build consumer trust",
            "Ethical communication",
            "Policy compliance",
        ],
        "activity_title": "Make the AI disclosure clear",
        "prompt": "An AI-generated influencer and recommendation model are used in an advertisement. Which disclosure is strongest?",
        "options": {
            "Put ‘AI may be used’ at the bottom of a 20-page privacy policy": option(False, 14000, -13, 23, -16, "A buried and vague statement is not clear and conspicuous."),
            "Place a clear label beside the content and explain that AI created the person and influenced the recommendation": option(True, 5000, 17, -14, 20, "Correct. This tells people AI is being used and explains how it influenced the marketing content."),
            "Do not disclose because the product itself is real": option(False, 18000, -18, 29, -21, "The reality of the product does not remove the need to disclose synthetic people or AI-influenced recommendations."),
        },
    },
    "7. Hallucinated Claims": {
        "definition": "Hallucinated claims are AI responses that confidently present incorrect or fabricated information as fact.",
        "slide_title": "Key Information",
        "slide_text": "Hallucinated claims are false or fabricated AI outputs presented as if they were true.",
        "slide_items": [
            "Generates false insights",
            "Sounds completely confident and agreeable",
            "Misguides marketing decisions",
            "Requires human review",
            "Continuous model monitoring",
        ],
        "activity_title": "Verify the suspicious skincare ad",
        "prompt": "The AI writes: ‘Erase every blemish in 48 hours. Clinically proven for every skin type. Dermatologists call it a miracle.’ What should happen next?",
        "options": {
            "Publish immediately because the wording sounds confident": option(False, 20000, -20, 34, -23, "Confidence is not evidence. The claims may be fabricated and could mislead customers and decision-makers."),
            "Pause, verify every claim against evidence, rewrite unsupported language, and require human approval": option(True, 5000, 16, -17, 22, "Correct. Human review and continuous monitoring are needed because AI can present false information as fact."),
            "Remove only the word ‘miracle’ and publish the remaining claims": option(False, 12000, -10, 22, -11, "The 48-hour and universal clinical claims still require evidence."),
        },
    },
    "8. Case Study: Anthropic Claude Mythos & Fable 5": {
        "definition": "Capability, access, and safeguards must be governed together.",
        "slide_title": "Case Timeline",
        "timeline": [
            ("April 7", "MYTHOS PREVIEW — Limited access through Project Glasswing for defensive cybersecurity."),
            ("June 9", "FABLE 5 — The same underlying model, with stronger safeguards for public use."),
            ("June 12", "ACCESS SUSPENDED — A government order followed reports that Fable’s safeguards could be bypassed."),
            ("July 1", "REDEPLOYED — Fable returned globally; Mythos remained limited to approved organizations."),
        ],
        "slide_items": [
            "ACCESS SHOULD MATCH RISK — Higher-risk AI capabilities require tiered access, identity controls, and approved-use restrictions.",
            "SAFETY CONTINUES AFTER LAUNCH — Companies must watch results, review problems, and pause systems when needed.",
            "PEOPLE REMAIN RESPONSIBLE — Marketing, legal, data, and security teams must share clear roles.",
        ],
        "activity_title": "Set the frontier-model controls",
        "prompt": "A powerful model can perform high-risk cyber tasks. Which deployment approach best applies the lessons from the case?",
        "options": {
            "Release the unrestricted model publicly and respond if misuse occurs": option(False, 28000, -22, 42, -27, "Reactive governance is weak when capability is high and safeguards may be bypassed."),
            "Use risk-tiered access, identity checks, approved uses, safeguards, monitoring, pause procedures, and shared responsibility": option(True, 4000, 19, -20, 25, "Correct. This governs capability, access, safeguards, monitoring, and accountability together."),
            "Allow customers to choose whether they want safeguards": option(False, 18000, -15, 31, -18, "Customer preference cannot replace provider responsibility for high-risk capability."),
        },
    },
    "9. Brand Safety": {
        "definition": "Companies must ensure that their AI use for content, ads, and customer interactions creates a positive reputation for their brand.",
        "slide_title": "Key Information",
        "slide_text": "71% of customers prefer speaking to a human representative than chatting with an AI bot for customer service- TheConversation",
        "slide_items": [
            "Content and ads must be accurate and appropriate",
            "Balance of AI and human interaction",
            "Failing to properly use AI could result in negatively impact their reputation",
        ],
        "activity_title": "Protect the customer experience",
        "prompt": "The AI customer-service bot gives an insensitive response during a product complaint and refuses to transfer the customer to a person. What should the company do?",
        "options": {
            "Keep the bot active because it reduces service costs": option(False, 16000, -25, 28, -20, "Cost savings do not offset inappropriate content, poor customer experience, and reputational harm."),
            "Escalate to a human, correct the response, pause the harmful workflow, review logs, and update safeguards": option(True, 3000, 21, -18, 22, "Correct. Brand safety requires accurate and appropriate interactions plus a responsible balance of AI and human support."),
            "Delete the customer's complaint from the dashboard": option(False, 9000, -22, 35, -23, "Removing evidence hides the warning signal and makes accountability and monitoring weaker."),
        },
    },
    "10. Model Monitoring": {
        "definition": "To ensure that marketing campaigns remain profitable, customer data is safe, and that models remain accurate, companies regularly monitor their AI models.",
        "slide_title": "Key Information",
        "slide_items": [
            "Data drift detection: customer and model behavioral changes",
            "Anomaly detection: Data collection errors",
            "Track performance",
        ],
        "activity_title": "Respond to the model shift",
        "prompt": "After an update, conversion rises 18%, while false-claim flags and demographic complaint rates triple. What should happen first?",
        "options": {
            "Keep running because the campaign is more profitable": option(False, 26000, -24, 39, -26, "Profit monitoring alone misses accuracy, fairness, customer-data, and brand risks."),
            "Pause affected automation, preserve logs, investigate drift and anomalies, and roll back if safeguards degraded": option(True, -2000, 20, -21, 25, "Correct. Monitoring must connect performance, drift, anomalies, complaints, and accuracy to action."),
            "Ask the model whether its own update is safe": option(False, 9000, -14, 27, -15, "Independent testing and accountable human review are still required."),
        },
    },
    "11. Agent Governance": {
        "definition": "AI agents take actions, not just generate responses.",
        "slide_title": "What is Agent Governance?",
        "slide_text": "“Advanced AI agents don’t just think—they do.” (IBM 2022)",
        "slide_items": [
            "Can complete complex tasks autonomously.",
            "Adapt and make decisions in real time.",
            "Require new governance because they act independently.",
        ],
        "activity_title": "Decide who can press Publish",
        "prompt": "An AI agent can create copy, select an audience, set the budget, and publish campaigns automatically. Which control system is strongest?",
        "options": {
            "Let the agent publish anything under $25,000": option(False, 21000, -18, 31, -22, "A spending threshold does not control claims, privacy, targeting, or brand risk."),
            "Define authority limits, require risk-based human approvals, keep action logs, monitor outcomes, and provide a kill switch": option(True, 6000, 18, -18, 24, "Correct. Agents that act independently require clear authority, oversight, auditability, monitoring, and shutdown controls."),
            "Review a random 5% of campaigns after publication": option(False, 13000, -9, 22, -10, "Sampling can support monitoring, but post-publication review alone cannot prevent high-impact harm."),
        },
    },
    "12. AI Policy & Regulation": {
        "definition": "Creates rules for the development, deployment, and oversight of AI systems.",
        "slide_title": "Key Information",
        "slide_items": [
            "Addresses risks involving privacy, bias, transparency, and accountability.",
            "U.S. AI legislation is rapidly evolving, with many proposals still under review.",
            "Regulation faces challenges balancing innovation with public protection.",
            "Industry influence raises concerns about potential conflicts of interest.",
            "RISK-BASED RULES — Higher-risk AI systems will need stronger testing, tighter access, and clearer limits.",
            "CONTINUOUS MONITORING — Companies must keep checking AI systems after launch as data, users, and business goals change.",
            "HUMAN ACCOUNTABILITY — People must remain responsible for AI decisions and their effects on customers.",
            "Responsible AI will become a core business practice, not just a legal requirement.",
        ],
        "activity_title": "Approve the company AI policy",
        "prompt": "Which policy is most prepared for evolving regulation and responsible AI practice?",
        "options": {
            "Use one general rule: employees should use AI carefully": option(False, 12000, -10, 22, -17, "A vague statement does not assign responsibility, define risk levels, or create testing and monitoring requirements."),
            "Create risk-based rules, testing, access limits, privacy and bias controls, disclosures, continuous monitoring, incident response, and named human accountability": option(True, 5000, 19, -19, 25, "Correct. This addresses the development, deployment, oversight, and changing risks of AI systems."),
            "Wait until every U.S. law is finalized before creating a policy": option(False, 16000, -15, 29, -21, "Organizations still need responsible internal rules while legislation evolves."),
        },
    },
}

BASELINE = {"revenue": 50_000, "trust": 70, "risk": 25, "readiness": 55}


def init_state():
    defaults = {
        "answers": {},
        "completed": [],
        "revenue": BASELINE["revenue"],
        "trust": BASELINE["trust"],
        "risk": BASELINE["risk"],
        "readiness": BASELINE["readiness"],
        "final_audit": None,
        "student_name": "",
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value.copy() if isinstance(value, (dict, list)) else value


def inject_css():
    st.markdown(
        """
        <style>
        :root { --navy:#172033; --red:#b52a28; --coral:#e4574f; --cream:#fff5ef;
                --ink:#151a24; --muted:#667085; --green:#18794e; }
        .stApp { background:#fffdfb; }
        [data-testid="stSidebar"] { background:#172033; }
        [data-testid="stSidebar"] * { color:#ffffff; }
        [data-testid="stSidebar"] .stProgress > div > div { background:#ff7566; }
        [data-testid="stMain"] [role="radiogroup"] label p,
        [data-testid="stMain"] [data-testid="stCheckbox"] label p,
        [data-testid="stMain"] [data-testid="stWidgetLabel"] p { color:#111111 !important; }
        [data-testid="stMain"] .stAlert p { color:#111111 !important; }
        .hero { padding:2rem 2.2rem; border-radius:22px; color:white;
          background:linear-gradient(135deg,#8f201f,#c53732 58%,#8c2423);
          box-shadow:0 16px 38px rgba(90,20,20,.18); }
        .hero h1 { color:white; font-size:2.35rem; line-height:1.12; margin:.4rem 0 .7rem; }
        .hero p { color:#fff4f1; font-size:1.03rem; max-width:900px; }
        .eyebrow { color:#ffd45b; letter-spacing:.12em; font-size:.78rem; font-weight:800; }
        .lesson-card { background:white; border:1px solid #e7e2de; border-radius:18px;
          padding:1.25rem 1.4rem; box-shadow:0 7px 20px rgba(23,32,51,.05); margin-bottom:1rem; }
        .definition { background:#fff1eb; border-left:6px solid #e4574f; }
        .definition p, .slide-info p, .slide-info li, .activity-card p { color:#111 !important; }
        .slide-info { background:#f5f6f8; border-left:6px solid #172033; }
        .activity-card { background:#fff; border:2px solid #e4574f; }
        .section-label { color:#b52a28; font-size:.78rem; letter-spacing:.1em; font-weight:850; }
        .topic-title { font-size:2.1rem; color:#172033; margin:.15rem 0 .7rem; }
        .feedback-good { border-left:5px solid #18794e;background:#edf8f2;padding:1rem;border-radius:10px;color:#111; }
        .feedback-bad { border-left:5px solid #c9362b;background:#fff1ef;padding:1rem;border-radius:10px;color:#111; }
        .timeline-row { border-left:3px solid #e4574f; padding:.25rem 0 .8rem 1rem; color:#111; }
        .certificate { border:8px double #b52a28;background:#fffaf2;padding:2rem;text-align:center;color:#111; }
        .certificate h2 { color:#172033; }
        div.stButton > button { border-radius:999px; font-weight:750; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def clamp_metrics():
    for key in ("trust", "risk", "readiness"):
        st.session_state[key] = max(0, min(100, st.session_state[key]))


def metrics():
    cols = st.columns(4)
    cols[0].metric("Campaign value", f"${st.session_state.revenue:,.0f}")
    cols[1].metric("Brand trust", f"{st.session_state.trust}/100")
    cols[2].metric("Legal & ethical risk", f"{st.session_state.risk}/100", delta_color="inverse")
    cols[3].metric("Governance readiness", f"{st.session_state.readiness}/100")


def sidebar():
    with st.sidebar:
        st.markdown("## 🧭 AI Certificate")
        st.session_state.student_name = st.text_input(
            "Enter name for your certificate",
            value=st.session_state.student_name,
        ).strip()
        count = len(st.session_state.completed)
        st.caption(f"{count} of {len(MODULES)} modules completed")
        st.progress(count / len(MODULES))
        pages = ["Home"] + list(MODULES) + ["Final Audit", "Certificate & Results"]
        page = st.radio("Course navigation", pages, label_visibility="collapsed")
        st.divider()
        st.caption("You may stop after any module. Download your report before closing the page.")
        if st.button("Reset activity", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    return page


def home():
    st.markdown(
        f"""
        <div class="hero">
          <div class="eyebrow">INTERACTIVE CERTIFICATION</div>
          <h1>{SITE_TITLE}</h1>
          <p>Learn the presentation concepts, apply each one to a marketing decision, and complete a final AI governance audit.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    metrics()
    st.header("How the certification works")
    c1, c2, c3 = st.columns(3)
    c1.markdown("### 1. Learn\nRead the definition and the information from the presentation slide.")
    c2.markdown("### 2. Apply\nComplete the interactive decision at the end of each module.")
    c3.markdown("### 3. Certify\nFinish the Final Audit and download your completion report.")
    st.info("Complete the modules in any order. Each module contains the original lesson information followed by a short activity.")
    st.header("Certification modules")
    for name in MODULES:
        st.markdown(f"- **{name}**")


def lesson_content(module):
    st.markdown(
        f"<div class='lesson-card definition'><div class='section-label'>DEFINITION</div><p>{module['definition']}</p></div>",
        unsafe_allow_html=True,
    )
    body = f"<div class='lesson-card slide-info'><div class='section-label'>{module['slide_title'].upper()}</div>"
    if module.get("slide_text"):
        body += f"<p>{module['slide_text']}</p>"
    if module.get("timeline"):
        for date, event in module["timeline"]:
            body += f"<div class='timeline-row'><b>{date}</b><br>{event}</div>"
    if module.get("slide_items"):
        body += "<ul>" + "".join(f"<li>{item}</li>" for item in module["slide_items"]) + "</ul>"
    body += "</div>"
    st.markdown(body, unsafe_allow_html=True)


def submit_answer(name, choice):
    if name in st.session_state.answers:
        return
    result = MODULES[name]["options"][choice]
    revenue, trust, risk, readiness = result["delta"]
    st.session_state.revenue += revenue
    st.session_state.trust += trust
    st.session_state.risk += risk
    st.session_state.readiness += readiness
    clamp_metrics()
    st.session_state.answers[name] = choice
    st.session_state.completed.append(name)


def module_page(name):
    module = MODULES[name]
    st.caption(f"MODULE {list(MODULES).index(name) + 1} OF {len(MODULES)}")
    st.markdown(f"<h1 class='topic-title'>{name}</h1>", unsafe_allow_html=True)
    lesson_content(module)
    if name == "7. Hallucinated Claims" and RISKY_AD_PATH.exists():
        st.image(str(RISKY_AD_PATH), caption="Fictional AI-generated NovaGlow advertisement", width=520)
    st.markdown(
        f"<div class='lesson-card activity-card'><div class='section-label'>INTERACTIVE ACTIVITY</div><h3>{module['activity_title']}</h3><p>{module['prompt']}</p></div>",
        unsafe_allow_html=True,
    )
    saved = st.session_state.answers.get(name)
    choices = list(module["options"])
    if saved:
        st.radio("Choose the best response", choices, index=choices.index(saved), disabled=True, key=f"locked_{name}")
    else:
        choice = st.radio("Choose the best response", choices, index=None, key=f"choice_{name}")
        if st.button("Submit response", type="primary", disabled=choice is None, key=f"submit_{name}"):
            submit_answer(name, choice)
            st.rerun()
    if saved:
        result = module["options"][saved]
        style = "feedback-good" if result["correct"] else "feedback-bad"
        heading = "Strong governance decision" if result["correct"] else "Risky governance decision"
        st.markdown(f"<div class='{style}'><b>{heading}</b><br>{result['feedback']}</div>", unsafe_allow_html=True)
        st.write("")
        metrics()


def final_audit():
    st.title("Final AI Marketing Governance Audit")
    st.write("Select every control that should be confirmed before an AI-assisted marketing campaign launches.")
    controls = [
        "AI governance roles, policies, and approval authority are documented",
        "Bias and discrimination testing is complete",
        "The interface avoids manipulation and dark patterns",
        "Privacy purpose and informed consent are documented",
        "Creative assets have licenses, releases, or documented rights",
        "AI use is clearly disclosed and important decisions are explained",
        "Factual and product claims are linked to verified evidence",
        "Model access and safeguards match the level of risk",
        "Brand-safety escalation to a human is available",
        "Model monitoring, drift detection, and pause thresholds are active",
        "AI-agent authority limits, logs, approvals, and a kill switch are defined",
        "The company AI policy addresses privacy, bias, transparency, accountability, and changing regulation",
    ]
    with st.form("final_audit_form"):
        selected = [item for i, item in enumerate(controls) if st.checkbox(item, value=False, key=f"audit_{i}")]
        reflection = st.text_area("What can an automated ethics score miss that a human reviewer may notice?")
        submitted = st.form_submit_button("Complete Final Audit", type="primary")
    if submitted:
        st.session_state.final_audit = {
            "score": round(len(selected) / len(controls) * 100),
            "selected": selected,
            "reflection": reflection.strip(),
        }
        st.rerun()
    if st.session_state.final_audit:
        audit = st.session_state.final_audit
        decision = "READY FOR GOVERNED LAUNCH" if audit["score"] == 100 else "PAUSE AND REVISE"
        st.success(f"Final audit: {audit['score']}% • {decision}")
        st.markdown("**Key lesson:** A checklist makes governance controls visible and auditable, but people remain responsible for interpreting risks and outcomes.")


def report_text():
    name = st.session_state.student_name or "Student"
    lines = [
        SITE_TITLE,
        "CERTIFICATION COMPLETION REPORT",
        f"Student: {name}",
        f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        "",
        f"Modules completed: {len(st.session_state.completed)} of {len(MODULES)}",
        f"Campaign value: ${st.session_state.revenue:,.0f}",
        f"Brand trust: {st.session_state.trust}/100",
        f"Legal and ethical risk: {st.session_state.risk}/100",
        f"Governance readiness: {st.session_state.readiness}/100",
        "",
        "MODULE DECISIONS",
    ]
    for module_name in MODULES:
        if module_name in st.session_state.answers:
            choice = st.session_state.answers[module_name]
            result = "Strong" if MODULES[module_name]["options"][choice]["correct"] else "Risky"
            lines.extend([f"- {module_name}: {choice}", f"  Governance result: {result}"])
    lines.extend(["", "FINAL AUDIT"])
    if st.session_state.final_audit:
        lines.append(f"Score: {st.session_state.final_audit['score']}%")
        lines.append(f"Reflection: {st.session_state.final_audit['reflection'] or '[not entered]'}")
    else:
        lines.append("Not completed.")
    lines.append("\nThis is a rule-based educational simulation, not legal advice or proof of compliance.")
    return "\n".join(lines)


def results_page():
    st.title("Certificate & Results")
    metrics()
    complete = len(st.session_state.completed) == len(MODULES) and st.session_state.final_audit is not None
    if complete:
        name = st.session_state.student_name or "AI Marketing Risk Analyst"
        st.markdown(
            f"<div class='certificate'><div class='section-label'>CERTIFICATE OF COMPLETION</div><h2>{SITE_TITLE}</h2><p>This certifies that <b>{name}</b> completed all twelve learning modules and the Final AI Marketing Governance Audit.</p></div>",
            unsafe_allow_html=True,
        )
    else:
        st.info("Complete all twelve modules and the Final Audit to earn the certificate. You may download your current progress at any time.")
    st.download_button(
        "Download completion report",
        data=report_text(),
        file_name="ai_policy_ethics_governance_certificate_report.txt",
        mime="text/plain",
        type="primary",
        use_container_width=True,
    )


def main():
    init_state()
    inject_css()
    page = sidebar()
    if page == "Home":
        home()
    elif page in MODULES:
        module_page(page)
    elif page == "Final Audit":
        final_audit()
    else:
        results_page()


if __name__ == "__main__":
    main()
