from __future__ import annotations

from datetime import datetime
from html import escape
import json
from pathlib import Path
import random

import pandas as pd
import streamlit as st
import streamlit.components.v1 as components


st.set_page_config(
    page_title="AI Policy, Ethics, Governance, and Risk in Marketing Analytics",
    page_icon="🧭",
    layout="wide",
    initial_sidebar_state="expanded",
)

BASE_DIR = Path(__file__).resolve().parent
RISKY_AD_PATH = BASE_DIR / "assets" / "risky_skincare_ad.png"
CASE_LESSONS_PATH = BASE_DIR / "assets" / "case_study_lessons.png"
SITE_TITLE = "AI POLICY, ETHICS, GOVERNANCE, AND RISK IN MARKETING ANALYTICS"

HEADER_IMAGES = {
    name: BASE_DIR / "assets" / f"module_{index:02d}_header.png"
    for index, name in enumerate([
        "1. AI Governance", "2. Bias & Discrimination",
        "3. Manipulation & Dark Patterns", "4. Privacy & Consent",
        "5. Intellectual Property (IP)", "6. Disclosure & Transparency",
        "7. Hallucinated Claims", "8. Case Study: Anthropic Claude Mythos & Fable 5",
        "9. Brand Safety", "10. Model Monitoring", "11. Agent Governance",
        "12. AI Policy & Regulation",
    ], start=1)
}


def find_image(expected_path: Path) -> Path | None:
    """Find a module image in assets or the repository root, as PNG or JPEG."""
    for folder in (BASE_DIR / "assets", BASE_DIR):
        for extension in (".png", ".jpg", ".jpeg", ".webp"):
            candidate = folder / f"{expected_path.stem}{extension}"
            if candidate.exists():
                return candidate
    return None


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
        "prompt": "Your boss wants the company to use AI to write ads, choose customers, and publish posts. Before the team begins, what should you recommend?",
        "options": {
            "Let each employee make their own rules": option(False, 15000, -12, 24, -18, "Individual judgment alone does not create consistent policies, controls, documentation, or accountability."),
            "Create clear rules, reviews, records, and human approval": option(True, 6000, 16, -16, 22, "Correct. This connects the frameworks, policies, controls, and human oversight described in AI governance."),
            "Use the AI until someone complains": option(False, 22000, -20, 34, -24, "Waiting for harm is reactive. Governance must define responsibilities and controls before deployment."),
        },
    },
    "2. Bias & Discrimination": {
        "definition": "AI can inherit biases from historical training data. This can produce unfair marketing outcomes for certain groups.",
        "slide_title": "Example",
        "slide_text": "An AI advertising system learns from past campaigns and primarily shows high-paying job ads to men because historical data reflects more male applicants.",
        "slide_items": ["Use diverse datasets, regularly audit models for bias, and include human oversight to reduce bias & discrimination."],
        "activity_title": "Audit the targeting model",
        "prompt": "Your first AI campaign mostly shows high-paying job ads to men. What should you tell your boss the company must do?",
        "options": {
            "Keep it because men click more": option(False, 19000, -20, 32, -22, "Historical performance can reproduce discrimination. Higher clicks do not make unequal access fair."),
            "Show the ads more widely and test whether the results are fair": option(True, 8000, 16, -15, 21, "Correct. Diverse data, bias auditing, and human oversight reduce the chance of unfair marketing outcomes."),
            "Remove the word gender but do no other testing": option(False, 13000, -12, 22, -12, "Removing one field does not prevent proxy discrimination. The team must test actual outcomes."),
        },
    },
    "3. Manipulation & Dark Patterns": {
        "definition": "AI-driven personalization can become manipulative if used unethically. Dark patterns steer users toward decisions they may not have intended.",
        "slide_title": "Key Ideas",
        "slide_text": "Note all the callouts, extreme ‘deals’, urgency indicators that could influence someone to make a purchase they might not otherwise using misleading/false data.",
        "activity_title": "Redesign the checkout trap",
        "prompt": "The AI creates a checkout page with a fake countdown and a hidden No button. What should you do before the campaign launches?",
        "options": {
            "Keep the screen because urgency increases conversions": option(False, 18000, -18, 28, -20, "Conversion does not justify misleading urgency or interface choices designed to steer users."),
            "Show honest information and make Yes and No equally easy": option(True, 5000, 18, -16, 20, "Correct. The redesign allows a voluntary choice without false urgency or visual manipulation."),
            "Keep the fake countdown but add a small rules link": option(False, 13000, -13, 22, -12, "A buried link does not correct false information or manipulative design."),
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
        "prompt": "Your boss wants highly personalized ads, and the AI asks for browsing, purchase, location, and health information. What plan should you approve?",
        "options": {
            "Use all the data because the ads will be more personal": option(False, 21000, -21, 35, -23, "Personalization does not remove the need for purpose limits, data minimization, and clear informed consent."),
            "Ask permission and use only the data the campaign truly needs": option(True, 7000, 19, -18, 22, "Correct. The approach balances useful personalization with privacy, consent, and customer trust."),
            "Use the data now and ask permission later": option(False, 17000, -19, 31, -20, "Consent must come before the data is used, not after the campaign has already launched."),
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
        "prompt": "The AI gives you an ad containing copied writing, a famous character, and a customer quote used without permission. What should you do?",
        "options": {
            "Publish everything because AI transformed the material": option(False, 17000, -13, 32, -20, "AI transformation does not automatically create permission or ownership."),
            "Use only approved material and save proof of permission": option(True, 5000, 14, -17, 23, "Correct. Rights clearance and human creative oversight protect the company legally and support an auditable record."),
            "Write AI-generated under everything and publish it": option(False, 10000, -7, 22, -10, "Disclosure does not replace copyright permission, licenses, ownership, or customer releases."),
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
        "prompt": "The AI creates a campaign using a fake influencer and an AI-generated recommendation. What should you require the company to tell customers?",
        "options": {
            "Put ‘AI may be used’ at the bottom of a 20-page privacy policy": option(False, 14000, -13, 23, -16, "A buried and vague statement is not clear and conspicuous."),
            "Put a clear label beside the ad explaining exactly what AI did": option(True, 5000, 17, -14, 20, "Correct. This tells people AI is being used and explains how it influenced the marketing content."),
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
        "prompt": "The AI writes that your company’s skincare product works in 48 hours, but nobody has checked the claim. What should you do before publishing it?",
        "options": {
            "Publish immediately because the wording sounds confident": option(False, 20000, -20, 34, -23, "Confidence is not evidence. The claims may be fabricated and could mislead customers and decision-makers."),
            "Stop and check every claim before a person approves the ad": option(True, 5000, 16, -17, 22, "Correct. Human review and continuous monitoring are needed because AI can present false information as fact."),
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
        "lessons": [
            "ACCESS SHOULD MATCH RISK — Higher-risk AI capabilities require tiered access, identity controls, and approved-use restrictions.",
            "SAFETY CONTINUES AFTER LAUNCH — Companies must watch results, review problems, and pause systems when needed.",
            "PEOPLE REMAIN RESPONSIBLE — Marketing, legal, data, and security teams must share clear roles.",
        ],
        "activity_title": "Set the frontier-model controls",
        "prompt": "Your company is considering a powerful AI that can perform dangerous cyber tasks. What access rules should you recommend to your boss?",
        "options": {
            "Release the unrestricted model publicly and respond if misuse occurs": option(False, 28000, -22, 42, -27, "Reactive governance is weak when capability is high and safeguards may be bypassed."),
            "Only approved users, with identity checks, safety rules, monitoring, and a stop process": option(True, 4000, 19, -20, 25, "Correct. This governs capability, access, safeguards, monitoring, and accountability together."),
            "Let each customer choose whether to use safety rules": option(False, 18000, -15, 31, -18, "Customer preference cannot replace provider responsibility for high-risk capability."),
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
        "prompt": "A customer contacts your company, but the AI bot gives a rude answer and refuses to connect them to a person. What should you do?",
        "options": {
            "Keep the bot active because it reduces service costs": option(False, 16000, -25, 28, -20, "Cost savings do not offset inappropriate content, poor customer experience, and reputational harm."),
            "Connect the customer to a person, pause the bot, and fix the problem": option(True, 3000, 21, -18, 22, "Correct. Brand safety requires accurate and appropriate interactions plus a responsible balance of AI and human support."),
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
        "prompt": "After your company updates its AI model, sales rise, but false claims and customer complaints triple. What should you recommend?",
        "options": {
            "Keep running because the campaign is more profitable": option(False, 26000, -24, 39, -26, "Profit monitoring alone misses accuracy, fairness, customer-data, and brand risks."),
            "Pause the AI, save the records, find the problem, and undo the update if needed": option(True, -2000, 20, -21, 25, "Correct. Monitoring must connect performance, drift, anomalies, complaints, and accuracy to action."),
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
        "prompt": "Your boss wants an AI agent that can write ads, choose customers, spend money, and publish without help. What limits should you require?",
        "options": {
            "Let the agent publish anything under $25,000": option(False, 21000, -18, 31, -22, "A spending threshold does not control claims, privacy, targeting, or brand risk."),
            "Set clear limits, require human approval, save its actions, and add an emergency stop": option(True, 6000, 18, -18, 24, "Correct. Agents that act independently require clear authority, oversight, auditability, monitoring, and shutdown controls."),
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
        "prompt": "Your boss asks you to create the company’s AI policy. Which rule would best protect customers and guide employees?",
        "options": {
            "Use one general rule: employees should use AI carefully": option(False, 12000, -10, 22, -17, "A vague statement does not assign responsibility, define risk levels, or create testing and monitoring requirements."),
            "Create stronger rules for riskier AI, test it, monitor it, and name the people responsible": option(True, 5000, 19, -19, 25, "Correct. This addresses the development, deployment, oversight, and changing risks of AI systems."),
            "Wait for every U.S. law to be finished before making rules": option(False, 16000, -15, 29, -21, "Organizations still need responsible internal rules while legislation evolves."),
        },
    },
}

BASELINE = {"reviewed": 0, "responsible": 0, "readiness": 0.0}


def init_state():
    if st.session_state.get("scoring_version") != 4:
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.session_state.scoring_version = 4
    defaults = {
        "answers": {},
        "completed": [],
        "celebrated": [],
        "completion_celebration": False,
        "reviewed": BASELINE["reviewed"],
        "responsible": BASELINE["responsible"],
        "readiness": BASELINE["readiness"],
        "final_audit": None,
        "student_name": "",
        "name_draft": "",
        "name_confirmed": False,
        "option_orders": {},
        "shuffle_offset": random.randint(0, 2),
        "current_page": "Home",
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
        .stApp { background:#fffdfb; color:#151a24; }
        [data-testid="stSidebar"] { background:#172033; }
        [data-testid="stSidebar"] * { color:#ffffff; }
        [data-testid="stSidebar"] .stProgress > div > div { background:#ff7566; }
        [data-testid="stSidebar"] .nav-heading {
          color:#9fa9bc !important;
          font-size:.72rem;
          font-weight:800;
          letter-spacing:.12em;
          margin:1rem 0 .25rem;
        }
        [data-testid="stSidebar"] div.stButton > button {
          width:100%;
          justify-content:center;
          text-align:center;
          border-radius:999px;
          padding:.65rem 1rem;
          min-height:3.15rem;
          margin:.18rem 0;
          box-shadow:0 3px 8px rgba(0,0,0,.18);
        }
        [data-testid="stSidebar"] div.stButton > button[kind="secondary"] {
          background:#253149;
          border:1px solid #46536d;
          color:#ffffff !important;
        }
        [data-testid="stSidebar"] div.stButton > button[kind="secondary"]:hover {
          background:#313f5b;
          border-color:#64718b;
          transform:translateY(-1px);
        }
        [data-testid="stSidebar"] div.stButton > button[kind="primary"] {
          background:linear-gradient(180deg,#ffd34e 0%,#ffae18 42%,#ff7500 100%);
          border:2px solid #fff1c4;
          color:#341b00 !important;
          box-shadow:inset 0 4px 7px rgba(255,255,255,.55),0 4px 10px rgba(0,0,0,.28);
        }
        [data-testid="stSidebar"] div.stButton > button[kind="secondary"] p { color:#ffffff !important; }
        [data-testid="stSidebar"] div.stButton > button[kind="primary"] p { color:#341b00 !important; }
        [data-testid="stSidebar"] div.stButton > button p {
          width:100%;
          text-align:center !important;
          line-height:1.25;
        }
        [data-testid="stSidebar"] input {
          background:#ffffff !important;
          color:#111111 !important;
          -webkit-text-fill-color:#111111 !important;
          caret-color:#b52a28 !important;
          color-scheme:light;
        }
        [data-testid="stSidebar"] input::placeholder {
          color:#687080 !important;
          -webkit-text-fill-color:#687080 !important;
          opacity:1;
        }
        [data-testid="stSidebar"] input::selection {
          background:#ffd1cc;
          color:#111111;
        }
        [data-testid="stSidebar"] input:-webkit-autofill,
        [data-testid="stSidebar"] input:-webkit-autofill:hover,
        [data-testid="stSidebar"] input:-webkit-autofill:focus {
          -webkit-text-fill-color:#111111 !important;
          -webkit-box-shadow:0 0 0 1000px #ffffff inset !important;
        }
        @media (prefers-color-scheme:dark) {
          [data-testid="stSidebar"] input {
            background:#0d121c !important;
            color:#ffffff !important;
            -webkit-text-fill-color:#ffffff !important;
            caret-color:#ffd34e !important;
            color-scheme:dark;
          }
          [data-testid="stSidebar"] input::placeholder {
            color:#aeb7c8 !important;
            -webkit-text-fill-color:#aeb7c8 !important;
          }
          [data-testid="stSidebar"] input::selection {
            background:#b52a28;
            color:#ffffff;
          }
          [data-testid="stSidebar"] input:-webkit-autofill,
          [data-testid="stSidebar"] input:-webkit-autofill:hover,
          [data-testid="stSidebar"] input:-webkit-autofill:focus {
            -webkit-text-fill-color:#ffffff !important;
            -webkit-box-shadow:0 0 0 1000px #0d121c inset !important;
          }
        }
        /* Keep ordinary main-page copy readable on the cream background. */
        [data-testid="stMain"],
        [data-testid="stMain"] p,
        [data-testid="stMain"] li,
        [data-testid="stMain"] span,
        [data-testid="stMain"] label,
        [data-testid="stMain"] strong,
        [data-testid="stMain"] b,
        [data-testid="stMain"] small,
        [data-testid="stMain"] div[data-testid="stMarkdownContainer"] {
          color:#151a24;
        }
        [data-testid="stMain"] [role="radiogroup"] label p,
        [data-testid="stMain"] [data-testid="stCheckbox"] label p,
        [data-testid="stMain"] [data-testid="stWidgetLabel"] p { color:#111111 !important; }
        [data-testid="stMain"] [data-testid="stCaptionContainer"],
        [data-testid="stMain"] [data-testid="stCaptionContainer"] p { color:#525866 !important; }
        [data-testid="stMain"] .stAlert,
        [data-testid="stMain"] .stAlert p,
        [data-testid="stMain"] [data-testid="stNotification"],
        [data-testid="stMain"] [data-testid="stNotification"] p { color:#111111 !important; }
        [data-testid="stMain"] h1, [data-testid="stMain"] h2,
        [data-testid="stMain"] h3 { color:#172033 !important; }
        [data-testid="stMain"] [data-testid="stMetricLabel"] p,
        [data-testid="stMain"] [data-testid="stMetricValue"] {
          color:#172033 !important;
        }
        .hero { padding:2rem 2.2rem; border-radius:22px; color:#111111;
          background:linear-gradient(135deg,#fff0e9,#ffe0d6 58%,#fff6f2);
          border:2px solid #e4574f;
          box-shadow:0 16px 38px rgba(90,20,20,.18); }
        .welcome-title {
          color:#a62220 !important;
          text-align:center;
          font-size:2.7rem;
          font-weight:900;
          letter-spacing:.08em;
          margin:.15rem 0 1rem;
        }
        .hero h1 { color:#a62220 !important; font-size:2.35rem; line-height:1.12; margin:.4rem 0 .7rem; }
        .hero p { color:#111111 !important; font-size:1.03rem; max-width:900px; }
        .eyebrow { color:#b52a28; letter-spacing:.12em; font-size:.78rem; font-weight:800; }
        .story-card {
          margin:1.25rem 0 1rem;
          padding:1.25rem 1.5rem;
          border-radius:18px;
          background:#172033;
          border:3px solid #ffae18;
          box-shadow:0 10px 24px rgba(23,32,51,.16);
        }
        .story-card .story-label {
          color:#ffd34e !important;
          font-size:.78rem;
          font-weight:900;
          letter-spacing:.12em;
          margin-bottom:.45rem;
        }
        [data-testid="stMain"] .story-card h3 {
          color:#ffffff !important;
          margin:.1rem 0 .5rem;
          text-shadow:0 1px 2px rgba(0,0,0,.25);
        }
        .story-card p { color:#ffffff !important; margin:0; line-height:1.65; }
        .lesson-card { background:white; border:1px solid #e7e2de; border-radius:18px;
          padding:1.25rem 1.4rem; box-shadow:0 7px 20px rgba(23,32,51,.05); margin-bottom:1rem; }
        .definition { background:#fff1eb; border-left:6px solid #e4574f; }
        .definition p, .slide-info p, .slide-info li, .activity-card p,
        .timeline-row, .timeline-row b { color:#111 !important; }
        .slide-info { background:#f5f6f8; border-left:6px solid #172033; }
        .activity-card { background:#fff; border:2px solid #e4574f; }
        .activity-card h3 { color:#a62220 !important; font-size:1.55rem !important; }
        .section-label { color:#b52a28; font-size:.78rem; letter-spacing:.1em; font-weight:850; }
        .topic-title { font-size:2.1rem; color:#a62220 !important; margin:.15rem 0 .7rem; }
        .module-image { border-radius:18px; border:1px solid #ead8d1; }
        .feedback-good { border-left:5px solid #18794e;background:#edf8f2;padding:1rem;border-radius:10px;color:#111; }
        .feedback-bad { border-left:5px solid #c9362b;background:#fff1ef;padding:1rem;border-radius:10px;color:#111; }
        .timeline-row { border-left:3px solid #e4574f; padding:.25rem 0 .8rem 1rem; color:#111; }
        .certificate { border:8px double #b52a28;background:#fffaf2;padding:2rem;text-align:center;color:#111; }
        .certificate h2 { color:#172033 !important; }
        .certificate p, .certificate b { color:#111 !important; }
        div.stButton > button,
        div.stDownloadButton > button,
        [data-testid="stFormSubmitButton"] > button {
          border-radius:999px;
          border:1px solid #9f2422;
          background:#b52a28;
          color:#ffffff !important;
          font-weight:750;
        }
        div.stButton > button p,
        div.stDownloadButton > button p,
        [data-testid="stFormSubmitButton"] > button p { color:#ffffff !important; }
        div.stButton > button:hover,
        div.stDownloadButton > button:hover,
        [data-testid="stFormSubmitButton"] > button:hover {
          background:#8f1f1d;
          border-color:#8f1f1d;
          color:#ffffff !important;
        }
        [data-testid="stMain"] div.stButton > button:disabled {
          background:#d8dce5 !important;
          border:2px solid #aeb5c2 !important;
          color:#515968 !important;
          opacity:1 !important;
          cursor:not-allowed;
          box-shadow:none;
        }
        [data-testid="stMain"] div.stButton > button:disabled p {
          color:#515968 !important;
          opacity:1 !important;
        }
        [data-testid="stMain"] input,
        [data-testid="stMain"] textarea {
          color:#111111 !important;
          background:#ffffff !important;
        }
        .money-rain {
          position:fixed;
          inset:0;
          z-index:999999;
          overflow:hidden;
          pointer-events:none;
        }
        .money-rain span {
          position:absolute;
          top:-12vh;
          left:var(--x);
          font-size:var(--size);
          opacity:0;
          animation:money-fall 2.8s ease-in var(--delay) forwards;
          filter:drop-shadow(0 3px 3px rgba(0,0,0,.2));
        }
        @keyframes money-fall {
          0% { transform:translate3d(0,-8vh,0) rotate(0deg); opacity:0; }
          12% { opacity:1; }
          100% { transform:translate3d(var(--drift),112vh,0) rotate(540deg); opacity:0; }
        }
        @media (prefers-reduced-motion:reduce) {
          .money-rain span { animation-duration:.01ms; }
        }
        .mascot-stage {
          display:flex;
          justify-content:center;
          align-items:center;
          gap:.4rem;
          margin:.25rem auto .55rem;
        }
        .mascot-robot {
          display:inline-block;
          font-size:4.5rem;
          line-height:1;
          filter:drop-shadow(0 6px 5px rgba(23,32,51,.2));
          animation:mascot-bob 2.2s ease-in-out infinite;
        }
        .mascot-hand {
          display:inline-block;
          font-size:2.4rem;
          transform-origin:20% 85%;
          animation:mascot-wave .8s ease-in-out infinite alternate;
        }
        .mascot-message {
          max-width:340px;
          margin:0 auto 1rem;
          padding:.55rem 1rem;
          border-radius:999px;
          background:#fff1eb;
          border:2px solid #e4574f;
          color:#172033 !important;
          text-align:center;
          font-weight:800;
        }
        .celebration-layer {
          position:fixed;
          inset:0;
          z-index:1000000;
          overflow:hidden;
          pointer-events:none;
        }
        .celebration-mascot {
          position:absolute;
          left:50%;
          bottom:6vh;
          font-size:6rem;
          filter:drop-shadow(0 8px 6px rgba(0,0,0,.25));
          animation:mascot-jump 2.8s ease-out forwards;
        }
        .confetti-piece {
          position:absolute;
          top:-12vh;
          left:var(--x);
          font-size:var(--size);
          opacity:0;
          animation:confetti-fall 3.1s ease-in var(--delay) forwards;
        }
        @keyframes mascot-bob {
          0%,100% { transform:translateY(0); }
          50% { transform:translateY(-8px); }
        }
        @keyframes mascot-wave {
          from { transform:rotate(-16deg); }
          to { transform:rotate(24deg); }
        }
        @keyframes mascot-jump {
          0% { transform:translate(-50%,40vh) scale(.7) rotate(-8deg); opacity:0; }
          20% { opacity:1; }
          48% { transform:translate(-50%,-45vh) scale(1.2) rotate(8deg); }
          72% { transform:translate(-50%,-8vh) scale(1) rotate(-5deg); }
          100% { transform:translate(-50%,0) scale(1) rotate(0); opacity:0; }
        }
        @keyframes confetti-fall {
          0% { transform:translateY(-10vh) rotate(0); opacity:0; }
          10% { opacity:1; }
          100% { transform:translateY(115vh) rotate(720deg); opacity:0; }
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def clamp_metrics():
    st.session_state.readiness = max(0, min(100, st.session_state.readiness))


def metrics():
    cols = st.columns(3)
    cols[0].metric("Modules reviewed", f"{st.session_state.reviewed}/12")
    cols[1].metric("Responsible decisions", f"{st.session_state.responsible}/12")
    cols[2].metric("Governance readiness", f"{st.session_state.readiness:.1f}/100")


def emoji_burst(emojis, include_mascot=False):
    """Attach a temporary animation to the parent Streamlit page."""
    script = f"""
    <script>
    (() => {{
      try {{
        const doc = window.parent.document;
        const old = doc.getElementById('academy-emoji-celebration');
        if (old) old.remove();
        if (!doc.getElementById('academy-emoji-style')) {{
          const style = doc.createElement('style');
          style.id = 'academy-emoji-style';
          style.textContent = `
            @keyframes academyFall {{
              0% {{ transform:translateY(-12vh) rotate(0deg); opacity:0; }}
              10% {{ opacity:1; }}
              100% {{ transform:translateY(115vh) rotate(720deg); opacity:0; }}
            }}
            @keyframes academyJump {{
              0% {{ transform:translate(-50%,45vh) scale(.65); opacity:0; }}
              18% {{ opacity:1; }}
              48% {{ transform:translate(-50%,-45vh) scale(1.25) rotate(8deg); }}
              76% {{ transform:translate(-50%,-5vh) scale(1); }}
              100% {{ transform:translate(-50%,10vh) scale(.9); opacity:0; }}
            }}`;
          doc.head.appendChild(style);
        }}
        const layer = doc.createElement('div');
        layer.id = 'academy-emoji-celebration';
        Object.assign(layer.style, {{position:'fixed', inset:'0', zIndex:'2147483647',
          overflow:'hidden', pointerEvents:'none'}});
        const emojis = {json.dumps(emojis)};
        for (let i = 0; i < 42; i++) {{
          const piece = doc.createElement('span');
          piece.textContent = emojis[i % emojis.length];
          Object.assign(piece.style, {{position:'absolute', left:((i*43)%98)+'%', top:'-12vh',
            fontSize:(1.5+(i%6)*.22)+'rem', opacity:'0',
            animation:`academyFall 3.2s ease-in ${{(i%10)*.08}}s forwards`}});
          layer.appendChild(piece);
        }}
        if ({str(include_mascot).lower()}) {{
          const mascot = doc.createElement('div');
          mascot.textContent = '🤖🏆';
          Object.assign(mascot.style, {{position:'absolute', left:'50%', bottom:'5vh',
            fontSize:'6rem', filter:'drop-shadow(0 8px 6px rgba(0,0,0,.25))',
            animation:'academyJump 3.2s ease-out forwards'}});
          layer.appendChild(mascot);
        }}
        doc.body.appendChild(layer);
        setTimeout(() => layer.remove(), 4300);
      }} catch (error) {{ console.log(error); }}
    }})();
    </script>
    """
    components.html(script, height=0, width=0)


def money_celebration():
    emoji_burst(["💵", "💰", "🤑", "💸"])
    st.toast("Correct decision! Money and trust protected. 💰", icon="✅")


def mascot_welcome(message="Hi! I’ll be your AI governance guide."):
    components.html(
        f"""
        <style>
          body {{ margin:0; font-family:Arial,sans-serif; overflow:hidden; }}
          .stage {{ display:flex; justify-content:center; align-items:center; gap:8px; }}
          .robot {{ font-size:68px; animation:bob 2s ease-in-out infinite; }}
          .hand {{ font-size:38px; transform-origin:20% 85%; animation:wave .7s ease-in-out infinite alternate; }}
          .message {{ margin:5px auto 0; width:max-content; max-width:90%; padding:8px 18px;
            border-radius:999px; background:#fff1eb; border:2px solid #e4574f;
            color:#172033; text-align:center; font-weight:800; }}
          @keyframes bob {{ 0%,100%{{transform:translateY(0)}} 50%{{transform:translateY(-7px)}} }}
          @keyframes wave {{ from{{transform:rotate(-18deg)}} to{{transform:rotate(25deg)}} }}
        </style>
        <div class="stage"><span class="robot">🤖</span><span class="hand">👋</span></div>
        <div class="message">{message}</div>
        """,
        height=135,
    )


def trigger_completion_celebration():
    st.session_state.completion_celebration = True


def completion_celebration():
    emoji_burst(["🎉", "🎊", "✨", "⭐", "🏆", "💰"], include_mascot=True)
    st.balloons()


def page_is_complete(page):
    return page in st.session_state.completed or (
        page == "Final Audit" and st.session_state.final_audit is not None
    )


def nav_button(page, label):
    active = st.session_state.current_page == page
    if st.button(
        label,
        key=f"menu_{page}",
        type="primary" if active else "secondary",
        use_container_width=True,
    ):
        st.session_state.current_page = page
        st.rerun()


def sidebar():
    with st.sidebar:
        st.markdown("## 🧭 AI Policy & Governance Certification")
        with st.form("certificate_name_form"):
            name_entry = st.text_input(
                "Enter name for your certificate",
                key="name_draft",
                placeholder="Type your full name",
            )
            save_name = st.form_submit_button("Enter name", use_container_width=True)
        if save_name:
            cleaned_name = name_entry.strip()
            if cleaned_name:
                st.session_state.student_name = cleaned_name
                st.session_state.name_confirmed = True
            else:
                st.session_state.name_confirmed = False
                st.error("Please enter your name before continuing.")
        if st.session_state.name_confirmed:
            st.success(f"✓ Certificate name saved: {st.session_state.student_name}")
        count = len(st.session_state.completed)
        st.caption(f"{count} of {len(MODULES)} modules completed")
        st.progress(count / len(MODULES))
        st.markdown("<div class='nav-heading'>COURSE</div>", unsafe_allow_html=True)
        nav_button("Home", "🏠  Home")
        st.markdown("<div class='nav-heading'>MODULES</div>", unsafe_allow_html=True)
        for page in MODULES:
            status = "✅  " if page_is_complete(page) else ""
            display_name = page.split(". ", 1)[1]
            nav_button(page, f"{status}{display_name}")
        st.markdown("<div class='nav-heading'>CERTIFICATION</div>", unsafe_allow_html=True)
        audit_status = "✅  " if page_is_complete("Final Audit") else ""
        nav_button("Final Audit", f"{audit_status}Final Audit")
        nav_button("Certificate & Results", "🏆  Certificate & Results")
        st.divider()
        st.caption("You may stop after any module. Download your report before closing the page.")
        if st.button("Reset activity", use_container_width=True):
            for key in list(st.session_state.keys()):
                del st.session_state[key]
            st.rerun()
    return st.session_state.current_page


def home():
    mascot_welcome()
    st.markdown("<div class='welcome-title'>WELCOME!</div>", unsafe_allow_html=True)
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
    learner_name = escape(
        st.session_state.student_name if st.session_state.name_confirmed else "AI Marketing Manager"
    )
    st.markdown(
        f"""
        <div class="story-card">
          <div class="story-label">YOUR ASSIGNMENT</div>
          <h3>Welcome, {learner_name}!</h3>
          <p>Your boss wants you to start using AI for your company’s marketing campaigns. As you begin integrating AI into your workflow, you encounter different situations where you must make an ethical decision based on the AI’s outputs. Each module will show you a different situation, and you must make the correct decision to show your boss that you’re able to successfully govern this AI system.</p>
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
    if module.get("lessons"):
        lessons = "<div class='lesson-card definition'><div class='section-label'>LESSONS LEARNED FROM ANTHROPIC</div><ol>"
        lessons += "".join(f"<li>{item}</li>" for item in module["lessons"])
        lessons += "</ol></div>"
        st.markdown(lessons, unsafe_allow_html=True)


def submit_answer(name, choice):
    if name in st.session_state.answers:
        return
    result = MODULES[name]["options"][choice]
    st.session_state.reviewed += 1
    if result["correct"]:
        st.session_state.responsible += 1
        st.session_state.readiness += 100 / len(MODULES)
    clamp_metrics()
    st.session_state.answers[name] = choice
    st.session_state.completed.append(name)


def shuffled_choices(name):
    if name not in st.session_state.option_orders:
        choices = list(MODULES[name]["options"])
        random.shuffle(choices)
        correct_choice = next(
            choice for choice in choices if MODULES[name]["options"][choice]["correct"]
        )
        module_index = list(MODULES).index(name)
        target_position = (module_index + st.session_state.shuffle_offset) % len(choices)
        current_position = choices.index(correct_choice)
        choices[current_position], choices[target_position] = (
            choices[target_position], choices[current_position]
        )
        st.session_state.option_orders[name] = choices
    return st.session_state.option_orders[name]


def module_page(name):
    module = MODULES[name]
    st.caption(f"MODULE {list(MODULES).index(name) + 1} OF {len(MODULES)}")
    st.markdown(f"<h1 class='topic-title'>{name}</h1>", unsafe_allow_html=True)
    header_path = find_image(HEADER_IMAGES[name])
    if header_path:
        st.image(str(header_path), use_container_width=True)
    lesson_content(module)
    if name == "8. Case Study: Anthropic Claude Mythos & Fable 5":
        lessons_path = find_image(CASE_LESSONS_PATH)
        if lessons_path:
            st.image(
                str(lessons_path),
                caption="Lessons learned from Anthropic",
                use_container_width=True,
            )
    if name == "7. Hallucinated Claims" and RISKY_AD_PATH.exists():
        st.image(str(RISKY_AD_PATH), caption="Fictional AI-generated NovaGlow advertisement", width=520)
    st.markdown(
        f"<div class='lesson-card activity-card'><div class='section-label'>INTERACTIVE ACTIVITY</div><h3>{module['activity_title']}</h3><p>{module['prompt']}</p></div>",
        unsafe_allow_html=True,
    )
    saved = st.session_state.answers.get(name)
    choices = shuffled_choices(name)
    if saved:
        st.radio("Choose the best response", choices, index=choices.index(saved), disabled=True, key=f"locked_{name}")
    else:
        choice = st.radio("Choose the best response", choices, index=None, key=f"choice_{name}")
        if st.button("Submit response", type="primary", disabled=choice is None, key=f"submit_{name}"):
            submit_answer(name, choice)
            st.rerun()
    if saved:
        result = module["options"][saved]
        if result["correct"] and name not in st.session_state.celebrated:
            money_celebration()
            st.session_state.celebrated.append(name)
        style = "feedback-good" if result["correct"] else "feedback-bad"
        heading = "Strong governance decision" if result["correct"] else "Risky governance decision"
        st.markdown(f"<div class='{style}'><b>{heading}</b><br>{result['feedback']}</div>", unsafe_allow_html=True)
        st.write("")
        metrics()
    st.divider()
    module_names = list(MODULES)
    module_index = module_names.index(name)
    back_target = "Home" if module_index == 0 else module_names[module_index - 1]
    next_target = "Final Audit" if module_index == len(module_names) - 1 else module_names[module_index + 1]
    back_col, position_col, next_col = st.columns([1, 1.2, 1])
    if back_col.button("← Back", key=f"back_{name}", use_container_width=True):
        st.session_state.current_page = back_target
        st.rerun()
    position_col.markdown(
        f"<p style='text-align:center;margin:.7rem 0 0;color:#525866'>Module {module_index + 1} of {len(module_names)}</p>",
        unsafe_allow_html=True,
    )
    if next_col.button("Next →", key=f"next_{name}", use_container_width=True):
        st.session_state.current_page = next_target
        st.rerun()


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
        f"Modules reviewed: {st.session_state.reviewed} of {len(MODULES)}",
        f"Responsible decisions: {st.session_state.responsible} of {len(MODULES)}",
        f"Governance readiness: {st.session_state.readiness:.1f}/100",
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
        mascot_welcome("You did it! Download your report to celebrate.")
        name = st.session_state.student_name or "AI Marketing Risk Analyst"
        certificate_name = escape(name)
        st.markdown(
            f"<div class='certificate'><div class='section-label'>CERTIFICATE OF COMPLETION</div><h2>{SITE_TITLE}</h2><p>This certifies that <b>{certificate_name}</b> completed all twelve learning modules and the Final AI Marketing Governance Audit.</p></div>",
            unsafe_allow_html=True,
        )
    else:
        st.info("Complete all twelve modules and the Final Audit to earn the certificate. You may download your current progress at any time.")
    if st.session_state.completion_celebration:
        completion_celebration()
        st.session_state.completion_celebration = False
    st.download_button(
        "Download completion report",
        data=report_text(),
        file_name="ai_policy_ethics_governance_certificate_report.txt",
        mime="text/plain",
        type="primary",
        use_container_width=True,
        on_click=trigger_completion_celebration,
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
