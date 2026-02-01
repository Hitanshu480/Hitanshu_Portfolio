import streamlit as st
from data import PROFILE, ABOUT, SKILLS, PROJECTS, EXPERIENCE, HIGHLIGHTS

st.set_page_config(
    page_title=f"{PROFILE['name']} | Portfolio",
    page_icon="📊",
    layout="wide"
)

# ---------------- SIDEBAR ----------------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio(
    "",
    ["Home", "About", "Skills", "Projects", "Experience", "Contact"]
)

# ---------------- HOME ----------------
if page == "Home":
    st.markdown(f"## Hi, I'm **{PROFILE['name']}**")
    st.markdown(f"### {PROFILE['title']}")
    st.write(PROFILE["tagline"])

    col1, col2 = st.columns(2)
    with col1:
        with open("resume.pdf", "rb") as f:
            st.download_button(
                "📄 Download Resume",
                f,
                file_name="https://docs.google.com/document/d/1_TUECkdoy8eLqGF57wC2QbBbALr2uTZW/edit?usp=sharing&ouid=107557019213644948399&rtpof=true&sd=true"
            )
    with col2:
        st.info("📩 Go to Contact section to connect")

# ---------------- ABOUT ----------------
elif page == "About":
    st.markdown("## About Me")
    st.write(ABOUT)

    cols = st.columns(len(HIGHLIGHTS))
    for col, item in zip(cols, HIGHLIGHTS):
        col.success(item)

# ---------------- SKILLS ----------------
elif page == "Skills":
    st.markdown("## My Skills")

    cols = st.columns(len(SKILLS))
    for col, (skill, data) in zip(cols, SKILLS.items()):
        with col:
            st.subheader(skill)
            st.progress(data["level"])
            for i in data["items"]:
                st.write(f"• {i}")

# ---------------- PROJECTS ----------------
elif page == "Projects":
    st.markdown("## My Projects")

    for p in PROJECTS:
        st.subheader(p["title"])
        st.write(p["description"])
        st.caption("Tech Used: " + ", ".join(p["tech"]))

        c1, c2 = st.columns(2)
        c1.markdown(f"[🔗 View Demo]({p['demo']})")
        c2.markdown(f"[💻 GitHub Repo]({p['code']})")
        st.divider()

# ---------------- EXPERIENCE ----------------
elif page == "Experience":
    st.markdown("## Work Experience")

    for exp in EXPERIENCE:
        st.subheader(f"{exp['role']} – {exp['company']}")
        st.caption(exp["duration"])
        for point in exp["points"]:
            st.write(f"• {point}")

# ---------------- CONTACT ----------------
elif page == "Contact":
    st.markdown("## Get In Touch")

    with st.form("contact_form"):
        st.text_input("Your Name")
        st.text_input("Email Address")
        st.text_area("Your Message")
        if st.form_submit_button("Send Message"):
            st.success("Message sent successfully 🚀")

    st.markdown("---")
    st.write(f"📍 **Location:** {PROFILE['location']}")
    st.write(f"📧 **Email:** {PROFILE['email']}")
    st.write(f"🔗 **GitHub:** {PROFILE['github']}")
    st.write(f"🔗 **LinkedIn:** {PROFILE['linkedin']}")

    st.markdown(f"© 2026 Created By {PROFILE['name']}. All rights reserved.")
