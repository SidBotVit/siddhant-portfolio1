
import streamlit as st
import json, base64, requests
from streamlit_lottie import st_lottie
from pathlib import Path

st.set_page_config(
    page_title="Sidhant Malik — Portfolio",
    page_icon="🎯",
    layout="wide",
)

# --- Inject basic SEO meta ---
seo = '''
<meta name="description" content="Sidhant Malik — Portfolio showcasing Software + Electrical projects, timelines, and resumes.">
<meta name="keywords" content="Sidhant Malik, Portfolio, React, Streamlit, IoT, EV Systems, AI">
<link rel="canonical" href="https://sidhant-portfolio.example.com/">
'''
st.components.v1.html(seo, height=0)

# --- Load CSS ---
with open("styles.css", "r") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- Theme Toggle ---
if "light" not in st.session_state:
    st.session_state.light = False

col_t1, col_t2, col_t3 = st.columns([1,6,1])
with col_t3:
    st.session_state.light = st.toggle("☀️ Light mode", value=st.session_state.light)

theme_class = "light-theme" if st.session_state.light else ""
st.markdown(f"<div class='{theme_class}'>", unsafe_allow_html=True)

# --- Header / Hero ---
with st.container():
    st.markdown('''
    <div class="hero">
      <h1>Hi, I’m <b>Sidhant Malik</b> — building useful things across <u>Software</u> & <u>Electrical</u>.</h1>
      <p>Full-stack projects, IoT/EV systems, dashboards & AI integrations. I love shipping fast and learning in public.</p>
      <div style="display:flex;gap:12px;flex-wrap:wrap;margin-top:10px;">
        <a class="link-btn" href="mailto:Sidhantmalik02@gmail.com">Email</a>
        <a class="link-btn" href="https://www.linkedin.com/in/siddhantmalik02" target="_blank">LinkedIn</a>
        <a class="link-btn" href="#resumes">Download Resumes</a>
      </div>
      <div class="small" style="margin-top:8px;">New: Live portfolio with filters, timelines, and embedded PDFs.</div>
    </div>
    ''', unsafe_allow_html=True)

# Lottie animation (nice subtle hero motion)
def load_lottie_url(url: str):
    try:
        r = requests.get(url, timeout=6)
        if r.status_code == 200:
            return r.json()
    except Exception:
        return None
    return None

lottie = load_lottie_url("https://assets10.lottiefiles.com/packages/lf20_touohxv0.json")
if lottie:
    st_lottie(lottie, height=140, key="hero-anim")

# --- Visit Counter (CountAPI) ---
@st.cache_data(ttl=300)
def get_visits():
    try:
        resp = requests.get("https://api.countapi.xyz/hit/sidhantmalik-portfolio/visits").json()
        return resp.get("value", 1)
    except Exception:
        return None

visits = get_visits()
st.caption(f"👀 Visits: {visits if visits is not None else '—'}")

# --- Nav Tabs ---
tabs = st.tabs(["📌 About", "🛠 Projects", "🧭 Experience", "📄 Resumes", "📬 Contact", "📈 Now"])

# --- About ---
with tabs[0]:
    st.subheader("About Me")
    st.write('''
I’m an EEE undergrad who enjoys crossing the wires between **software** and **hardware** — from **React/Next**
apps and **data dashboards** to **IoT/EV systems** with control circuits. I bias toward action, ship MVPs quickly,
and iterate based on feedback. Recently, I’ve focused on **AI-assisted user experiences** (voice interviews, predictive dashboards)
and **energy-efficient systems** (regenerative braking, solar-powered IoT).
    ''')
    st.markdown("**Quick facts:**")
    st.markdown('''
- 🎓 B.Tech **EEE** @ VIT (CGPA 8.25/10)
- 🧠 300+ **LeetCode** problems
- 🏆 Hackathon **Finalist** (EV/IoT focus)
- 📄 2 **IEEE** conference papers (IoT + Renewable Energy)
    ''')

# --- Projects ---
with tabs[1]:
    st.subheader("Featured Projects")
    # Filters
    with st.container():
        left, right = st.columns([2,2])
        with left:
            q = st.text_input("Search", placeholder="Search by title or tech...").lower().strip()
        with right:
            selected = st.multiselect("Filter by category", ["Web / AI", "Data / Dashboard", "ML / Finance", "IoT / Power Electronics", "EV Systems"], default=[])
    data = json.load(open("projects.json"))
    # filter
    def match(p):
        ok = True
        if q:
            hay = " ".join([p["title"]] + p["stack"]).lower()
            ok = (q in hay)
        if selected:
            ok = ok and (p["category"] in selected)
        return ok
    filtered = [p for p in data if match(p)]
    if not filtered:
        st.info("No projects match your filters — clear filters to see all.")
    # render
    for p in filtered:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown(f"### {p['title']}  \n*{p['category']} • {p['year']}*")
        st.markdown("Tech: " + " ".join([f"<span class='badge'>{t}</span>" for t in p["stack"]]), unsafe_allow_html=True)
        for h in p["highlights"]:
            st.write(f"• {h}")
        if p.get("github") or p.get("link"):
            btn_cols = st.columns(2)
            if p.get("github"):
                btn_cols[0].link_button("Source", p["github"])
            if p.get("link"):
                btn_cols[1].link_button("Live", p["link"])
        st.markdown("</div>", unsafe_allow_html=True)

# --- Experience ---
with tabs[2]:
    st.subheader("Experience & Achievements")
    with st.expander("VLSI Internship — VIT Systems Lab (May 2025 – July 2025)"):
        st.write('''
- Assisted in **RTL design** and **low-power** simulation (Verilog, ModelSim).
- Built/validated **test benches**; documented debugging + verification practices.
        ''')
    with st.expander("Operations Coordinator — TechnoVIT 2023 (Aug – Oct 2023)"):
        st.write('''
- Managed operations for **4000+** participants; improved **data visibility by 40%**.
- Streamlined **cross-functional** communications (technical/logistics/sponsorship).
        ''')
    st.markdown("**Achievements**")
    st.write('''
- 📄 2 IEEE Conference Papers (IoT + Renewable Energy)
- 🧩 300+ LeetCode problems (DSA focus)
- 🏁 Hackathon Finalist — IoT-based energy optimization (2024)
    ''')

# --- Resumes ---
with tabs[3]:
    st.subheader("Resumes")
    st.markdown("<a id='resumes'></a>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    def show_pdf(path, label):
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode()
        pdf_iframe = f'<iframe class="pdf-frame" src="data:application/pdf;base64,{b64}#view=FitH"></iframe>'
        st.markdown(f"#### {label}")
        st.download_button("Download PDF", data=open(path, "rb").read(), file_name=Path(path).name, mime="application/pdf")
        st.components.v1.html(pdf_iframe, height=700, scrolling=True)
    with col1:
        show_pdf("assets/Resume_CS_Meta.pdf", "Resume — Software (Meta/CS)")
    with col2:
        show_pdf("assets/Resume_Electrical_Hyundai.pdf", "Resume — Electrical (Hyundai)")

# --- Contact ---
with tabs[4]:
    st.subheader("Contact")
    st.write("Prefer email or LinkedIn. I typically respond within a day.")
    st.link_button("Email Me", "mailto:Sidhantmalik02@gmail.com")
    st.link_button("LinkedIn", "https://www.linkedin.com/in/siddhantmalik02", help="Open profile in a new tab")

# --- Now ---
with tabs[5]:
    st.subheader("Now — What I'm focusing on")
    st.write('''
- Building **interview-ready** apps with clean UX and strong fundamentals
- Practicing **DSA** and **systems design** basics
- Exploring **control + power electronics** integrations with software dashboards
    ''')
    st.caption("Updated: Nov 2025")

st.markdown("</div>", unsafe_allow_html=True)  # end theme wrapper

# Footer
st.markdown("<div class='footer'>© 2025 — Built with Streamlit. Theme toggle, filters, embedded PDFs, and visit counter included.</div>", unsafe_allow_html=True)
