"""CSIT 349 | Autobiography and Portfolio - Louis Francis Lim.

Personalize the biography, project details, section, and self-assessment ratings
before submitting. The feedback form is a demo, not an email sender.
"""

from pathlib import Path

import numpy as np
import pandas as pd
import streamlit as st


# ------------------------ Edit your details here ---------------------------
NAME = "Louis Francis Lim"
SECTION = "G01"  
PROGRAM = "BS Information Technology · 4th Year"
SCHOOL = "Cebu Institute of Technology – University"
CITY = "Cebu City, Philippines"
PHOTO = Path(__file__).parent / "profile.jpg" 
FALLBACK_PHOTO = Path(__file__).parent / "avatar_placeholder.png"


SKILLS = [
    {"Skill": "Java", "Category": "Programming", "Self-rating": 4},
    {"Skill": "Python", "Category": "Programming", "Self-rating": 3},
    {"Skill": "C", "Category": "Programming", "Self-rating": 3},
    {"Skill": "JavaScript", "Category": "Web", "Self-rating": 3},
    {"Skill": "HTML & CSS", "Category": "Web", "Self-rating": 4},
    {"Skill": "SQL", "Category": "Database", "Self-rating": 3},
    {"Skill": "Git & GitHub", "Category": "Tools & Cloud", "Self-rating": 3},
    {"Skill": "React", "Category": "Web", "Self-rating": 3},
    {"Skill": "Spring Boot", "Category": "Programming", "Self-rating": 3},
    {"Skill": "PostgreSQL", "Category": "Database", "Self-rating": 3},
]

PROJECTS = [
    {
        "title": "DormScout",
        "category": "Web Application",
        "icon": "🏠",
        "role": "Team developer",
        "tools": "React.js, React Router, Context API, Axios / Fetch, CSS",
        "problem": "Help users browse dorm listings and manage a dorm booking experience in one application.",
        "work": "Contributed to a team project built around dorm listings, accounts, bookings, messages, notifications, and user profiles. The repository documents the application's frontend and its main features.",
        "outcome": "A GitHub-hosted React-based dorm booking project with a documented feature set and source code.",
        "lesson": "Building an application as a team involves organizing reusable interface components and connecting different parts of the user experience.",
        "note": "The public GitHub repository was reviewed for this project description.",
        "repo": "https://github.com/louisflim/dormscout",
        "repo_verified": True,
    },
    {
        "title": "GymTrack",
        "category": "Web & Mobile System",
        "icon": "🏋️",
        "role": "Project developer",
        "tools": "Java, Spring Boot, React, Supabase / PostgreSQL, Kotlin (Android plan)",
        "problem": "Help small and medium-sized gyms organize membership registration, subscriptions, attendance, and payments.",
        "work": "Designed and documented a gym membership management system covering administrator, staff, and member roles. The repository describes QR-based attendance, subscription plans, an admin dashboard, and PayMongo payment integration among its requirements.",
        "outcome": "A GitHub project containing system requirements and web, backend, and mobile work areas. Some README items describe planned features rather than independently verified deployments.",
        "lesson": "Planning roles, data flows, authentication, and integration requirements makes a larger software project easier to structure.",
        "note": "The public GitHub repository was reviewed; some README items describe planned functionality rather than verified deployments.",
        "repo": "https://github.com/louisflim/gymtrack",
        "repo_verified": True,
    },
    {
        "title": "Hotel System",
        "category": "Hotel Project",
        "icon": "🏨",
        "role": "Student project",
        "tools": "Python",
        "problem": "A hotel-related software project. Add the exact problem addressed in my own words.",
        "work": "Add the parts I developed, such as the interface, database, or business logic, after checking the original project.",
        "outcome": "Outcome details are pending verification of the original project repository.",
        "lesson": "Learned how to use Python",
        "repo": "https://github.com/louisflim/hotel-system",
        "repo_verified": True,
    },
]

SKILL_NOTES = {
    "Java": "Used for OOP learning and a Swing desktop application.",
    "Python": "Learning Python for scripts, data work, and applications such as this Streamlit site.",
    "C": "Practiced arrays, pointers, lists, stacks, queues, and trees.",
    "JavaScript": "Used when studying interactive web application development.",
    "HTML & CSS": "Practiced structuring and styling web pages.",
    "SQL": "Learning how to query and organize relational data.",
    "Git & GitHub": "Used for version control and organizing code projects.",
    "React": "Used in DormScout, and listed as a web framework for GymTrack.",
    "Spring Boot": "Listed as GymTrack's Java backend framework.",
    "PostgreSQL": "Listed as GymTrack's database through Supabase.",
}

st.set_page_config(
    page_title=f"{NAME} | Portfolio",
    page_icon="💻",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Small design layer. Main content remains native Streamlit components.
st.markdown(
    """
    <style>
    .stApp { background: #f6f8fb; color: #15253d; }
    [data-testid="stSidebar"] { background-color: #101c32; }
    [data-testid="stSidebar"] * { color: #f2f6fb; }
    [data-testid="stSidebar"] [data-baseweb="radio"] label { color: #f2f6fb; }
    .block-container { max-width: 1120px; padding-top: 2.1rem; padding-bottom: 4rem; }
    .hero {
        background: linear-gradient(125deg, #132a49 0%, #18465a 72%, #187b78 100%);
        border-radius: 22px; padding: 2rem 2.2rem; color: #ffffff;
        box-shadow: 0 10px 28px rgba(22, 46, 66, .12);
        margin-bottom: .8rem;
    }
    .hero .eyebrow { letter-spacing: .14em; text-transform: uppercase;
        font-size: .72rem; color: #9ce6dc; font-weight: 800; }
    .hero h1 { font-size: clamp(2rem, 4vw, 3.4rem); line-height: 1.12;
        color: #fff; margin: .5rem 0 1rem; }
    .hero p { color: #dcecf3; font-size: 1.03rem; line-height: 1.7; }
    .pill { display: inline-block; background: rgba(255,255,255,.12);
        border: 1px solid rgba(255,255,255,.18); border-radius: 99px;
        padding: .35rem .75rem; font-size: .78rem; color: #efffff; margin: .2rem .25rem .1rem 0; }
    .section-lead { color: #53677a; margin-top: -.2rem; margin-bottom: 1.2rem; }
    .mini-card { background: white; border: 1px solid #e0e9ed; border-radius: 16px;
        padding: 1.1rem 1.2rem; margin: .55rem 0 1rem; }
    .mini-card b { color: #145e65; }
    .footer { text-align: center; color: #627488; font-size: .82rem;
        margin-top: 3rem; border-top: 1px solid #dbe3ed; padding-top: 1.1rem; }
    div[data-testid="stMetric"] { background: white; border: 1px solid #e1e9ef;
        border-radius: 14px; padding: .7rem 1rem; }
    </style>
    """,
    unsafe_allow_html=True,
)

if "feedback" not in st.session_state:
    st.session_state.feedback = []
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ---------------------------- Sidebar --------------------------------------
st.sidebar.markdown("## 💻 My Portfolio")
st.sidebar.caption(f"{NAME} · Section {SECTION}")
st.sidebar.divider()
st.sidebar.radio(
    "Navigate",
    ["Home", "My Story", "Skills", "Projects", "Contact & Feedback"],
    key="page",
)
st.sidebar.divider()
st.sidebar.markdown("**Currently exploring**")
st.sidebar.write("Software development, databases, AI, and hands-on cloud tools.")
st.sidebar.info("Tip: Use the sidebar to explore the different pages.")


def go_to_projects():
    st.session_state.page = "Projects"


def project_details(project):
    """Render a project using several native components."""
    st.subheader(f"{project['icon']} {project['title']}")
    st.caption(project["category"])
    left, right = st.columns(2)
    with left:
        st.markdown(f"**My role:** {project['role']}")
        st.markdown(f"**Tools:** {project['tools']}")
    with right:
        st.markdown("**Goal**")
        st.write(project["problem"])
    st.markdown("**What I did**")
    st.write(project["work"])
    st.success("Outcome: " + project["outcome"])
    with st.expander("What I learned"):
        st.write(project["lesson"])
    with st.expander("Source and verification note"):
        if project.get("note"):
            st.caption(project["note"])


# ---------------------------- Home -----------------------------------------
if st.session_state.page == "Home":
    st.markdown(
        f"""
        <div class="hero">
          <div class="eyebrow">Welcome to my digital portfolio</div>
          <h1>Hello, I'm {NAME} 👋</h1>
          <p>A {PROGRAM} student at {SCHOOL}. I enjoy building practical
          software, solving programming problems, and exploring new technologies.</p>
          <span class="pill">📍 {CITY}</span>
          <span class="pill">🎓 Section {SECTION}</span>
          <span class="pill">✨ Learning by building</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    photo_col, intro_col = st.columns([1, 2], gap="large")
    with photo_col:
        st.image(str(PHOTO if PHOTO.exists() else FALLBACK_PHOTO), width=250)
        if not PHOTO.exists():
            st.caption("Illustrated placeholder — replace with your own profile.jpg.")
    with intro_col:
        st.header("A little about me")
        st.write(
            "I'm an Information Technology student who enjoys turning what I learn "
            "in class into small, working programs. I started by practicing programming "
            "fundamentals and gradually became interested in desktop applications, "
            "web development, and creating small apps."
        )
        st.write(
            "My goal is to keep improving how I design, test, and explain software "
            " not just how I write code."
        )
        st.button("Explore my projects →", on_click=go_to_projects, type="primary")

    st.divider()
    a, b, c = st.columns(3)
    a.metric("Featured projects", len(PROJECTS))
    b.metric("Skill categories", len(set(x["Category"] for x in SKILLS)))
    c.metric("Current program", "BSIT - 4")
    st.subheader("Projects I am featuring")
    st.caption("Browse the Projects page for goals, tools, outcomes, and GitHub links.")
    for featured in PROJECTS:
        st.markdown(f"**{featured['icon']} {featured['title']}** — {featured['category']}")
    st.subheader("My interests")
    interest_cols = st.columns(3)
    for col, (title, detail) in zip(
        interest_cols,
        [
            ("🖥️ Development", "Desktop and web applications"),
            ("🧠 Problem-solving", "Algorithms and practical debugging"),
            ("☁️ New technology", "Cloud services and AI fundamentals"),
        ],
    ):
        with col:
            st.markdown(
                f'<div class="mini-card"><b>{title}</b><p>{detail}</p></div>',
                unsafe_allow_html=True,
            )
    if st.toggle("Show a fun fact"):
        st.info("I became interested in IT partly because I wanted to program and create PC games.")

# --------------------------- Autobiography ---------------------------------
elif st.session_state.page == "My Story":
    st.title("📖 My autobiography")
    st.markdown('<p class="section-lead">My background, learning journey, and milestones.</p>', unsafe_allow_html=True)
    st.write(
        "My name is Louis Francis Lim, and I am currently a fourth-year BS Information "
        "Technology student at Cebu Institute of Technology – University. "
        "I've always been interested in understanding how computers work and how "
        "ideas can become software that people can actually use."
    )
    st.write(
        "As I progressed through college, I became more comfortable working with "
        "programming languages, interfaces, data structures, and databases. "
        "Not every project worked on the first try; testing, finding mistakes, "
        "and trying again have become important parts of how I learn."
    )
    st.write(
        "Today, I want to strengthen my software development skills and gain more "
        "experience building reliable, useful applications. I'm especially curious "
        "about using technology to make learning more interactive."
    )

    st.subheader("My learning journey")
    selected_stage = st.radio(
        "Choose a chapter",
        ["Beginning", "University", "Today"],
        horizontal=True,
    )
    chapters = {
        "Beginning": ("🎮 Curiosity", "I was drawn to programming because I wanted to understand and create PC games."),
        "University": ("📚 Building foundations", "I practiced C, Java, data structures, networking, databases, and graphical interfaces through course activities."),
        "Today": ("🚀 Building confidence", "I am working toward stronger skills in software development, practical APIs, testing, and cloud technologies."),
    }
    chapter_title, chapter_description = chapters[selected_stage]
    st.info(f"**{chapter_title}** — {chapter_description}")

    st.subheader("Milestones")
    with st.expander("See milestones from my studies", expanded=True):
        st.markdown(
            """
            - **Programming foundations:** Practiced C programming and data structures.
            - **DormScout:** Collaborated on a React-based dorm booking project.
            - **GymTrack:** Worked on a gym membership system covering web, backend, and mobile requirements.
            - **Hotel System:** One of my software projects.
            - **Present:** Studying as a fourth-year BSIT student and building my portfolio.
            """
        )

    st.subheader("Beyond the code")
    subjects = st.multiselect(
        "Interests I enjoy exploring",
        ["Software development", "PC games", "AI", "Database systems", "Cloud technology", "UI design"],
        default=["Software development", "PC games", "AI"],
    )
    if subjects:
        st.write("Some interests on my radar: " + ", ".join(subjects) + ".")
    else:
        st.caption("Select an interest to explore the list.")

# ------------------------------ Skills -------------------------------------
elif st.session_state.page == "Skills":
    st.title("🧰 Skills & tools")
    st.markdown(
        '<p class="section-lead">An interactive look at the tools I have practiced. Ratings are editable self-assessments, not test results.</p>',
        unsafe_allow_html=True,
    )
    data = pd.DataFrame(SKILLS)
    f1, f2 = st.columns([2, 1])
    with f1:
        chosen_categories = st.multiselect(
            "Filter by category",
            sorted(data["Category"].unique().tolist()),
            default=sorted(data["Category"].unique().tolist()),
        )
    with f2:
        minimum = st.slider("Minimum confidence", 1, 5, 1, help="1 = beginner; 5 = confident")

    filtered = data[
        data["Category"].isin(chosen_categories) & (data["Self-rating"] >= minimum)
    ].copy()
    m1, m2, m3 = st.columns(3)
    m1.metric("Skills shown", len(filtered))
    m2.metric("Categories shown", filtered["Category"].nunique())
    m3.metric("Average rating", f"{np.mean(filtered['Self-rating']):.1f} / 5" if not filtered.empty else "—")

    chart_tab, table_tab = st.tabs(["📊 Chart", "📋 Table"])
    with chart_tab:
        if not filtered.empty:
            st.bar_chart(filtered.set_index("Skill")["Self-rating"], y_label="Self-rating (1 to 5)")
        else:
            st.warning("No skills match these filters. Lower the slider or choose more categories.")
    with table_tab:
        st.dataframe(filtered, hide_index=True, use_container_width=True)

    st.caption("Review the ratings at the top of app.py and adjust them to match your actual experience.")
    selected_skill = st.selectbox("Learn more about a skill", [item["Skill"] for item in SKILLS])
    st.info(SKILL_NOTES[selected_skill])
    if st.checkbox("Show my current learning priorities", value=True):
        st.markdown("**Current focus:** practical API concepts, software testing, and more cloud experience.")
        st.progress(0.65, text="Portfolio preparation — illustrative progress indicator")

# ------------------------------ Projects -----------------------------------
elif st.session_state.page == "Projects":
    st.title("🚀 Featured projects")
    st.markdown(
        '<p class="section-lead">Three projects from my GitHub portfolio: DormScout, GymTrack, and Hotel System.</p>',
        unsafe_allow_html=True,
    )
    st.info("These are my selected portfolio projects.")
    categories = ["All", *sorted(set(p["category"] for p in PROJECTS))]
    category = st.selectbox("Choose a project category", categories)
    matching = [p for p in PROJECTS if category == "All" or p["category"] == category]
    tabs = st.tabs([p["icon"] + " " + p["category"] for p in matching])
    for tab, project in zip(tabs, matching):
        with tab:
            project_details(project)
    st.divider()
    if st.checkbox("Show the project workflow I usually follow"):
        st.markdown("**Plan → Build → Test → Debug → Improve → Document**")
        st.caption("A simple reminder of the development habits I want to keep practicing.")

# --------------------------- Contact and feedback --------------------------
else:
    st.title("✉️ Contact & feedback")
    st.markdown(
        '<p class="section-lead">Try the interactive form and leave a message for this portfolio demo.</p>',
        unsafe_allow_html=True,
    )
    with st.form("feedback_form", clear_on_submit=True):
        visitor_name = st.text_input("Your name", placeholder="Enter a first name or nickname")
        topic = st.selectbox("What would you like to comment on?", ["Portfolio design", "Projects", "Skills", "General feedback"])
        rating = st.radio("How was your visit?", ["Great", "Good", "Could be better"], horizontal=True)
        message = st.text_area("Your message", placeholder="What stood out to you?", max_chars=400)
        acknowledge = st.checkbox("I understand this is a demo form, not a message to the student")
        submitted = st.form_submit_button("Submit feedback", type="primary")

    if submitted:
        if not visitor_name.strip() or not message.strip():
            st.error("Please enter your name and a message.")
        elif not acknowledge:
            st.warning("Please check the demo-form confirmation.")
        else:
            st.session_state.feedback.append(
                {"Name": visitor_name.strip(), "Topic": topic, "Visit": rating, "Message": message.strip()}
            )
            st.success("Thanks! Your feedback was added to this session's guestbook.")
            st.balloons()

    if st.session_state.feedback:
        st.subheader("Session guestbook")
        st.dataframe(pd.DataFrame(st.session_state.feedback), hide_index=True, use_container_width=True)
        if st.button("Clear my guestbook"):
            st.session_state.feedback.clear()
            st.rerun()

st.markdown(
    f'<div class="footer">Made with Streamlit · CSIT 349 Applied AI · {NAME} · Section {SECTION}</div>',
    unsafe_allow_html=True,
)
