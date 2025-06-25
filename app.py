# # import streamlit as st
# # from utils.groq_helper import ask_groq

# # st.set_page_config(page_title="PrepSmart - AI Interview Coach", layout="wide")
# # st.title("🎓 PrepSmart: Your AI Interview Preparation Assistant")

# # # Apply custom styling
# # st.markdown("<style>" + open("assets/styles.css").read() + "</style>", unsafe_allow_html=True)

# # # Sidebar Navigation
# # st.sidebar.title("📚 Navigation")
# # section = st.sidebar.radio("Go to", [
# #     "Random DSA Question",
# #     "Computer Fundamentals",
# #     "Aptitude & Reasoning",
# #     "Startup Product/Service Prep",
# #     "🎯 I'm Feeling Lucky!"
# # ])

# # # Random DSA
# # if section == "Random DSA Question":
# #     st.header("🔢 Random DSA Problem")
# #     response = ask_groq(
# #         "Give me a random DSA coding problem from LeetCode, GFG, or HackerRank with title, platform, and URL. "
# #         "Also include a short description."
# #     )
# #     st.markdown(response)

# # # Computer Fundamentals
# # elif section == "Computer Fundamentals":
# #     st.header("💻 CS Fundamental Question")
# #     topic = st.selectbox("Choose Topic", ["OS", "DBMS", "CN", "OOPs"])
# #     response = ask_groq(
# #         f"Give me one interview-level question with answer from {topic}."
# #     )
# #     st.markdown(response)

# # # Aptitude & Reasoning
# # elif section == "Aptitude & Reasoning":
# #     st.header("🧠 Aptitude & Reasoning")
# #     company = st.selectbox("Select Company", ["TCS", "Infosys", "Wipro", "Cognizant"])
# #     response = ask_groq(
# #         f"Give me one aptitude or reasoning question with answer that is typically asked in {company} interviews."
# #     )
# #     st.markdown(response)

# # # Startup Product/Service
# # elif section == "Startup Product/Service Prep":
# #     st.header("🚀 Startup Product or Service Idea")
# #     response = ask_groq(
# #         "Generate a unique startup product or service idea and explain it in 2-3 sentences for an interview pitch."
# #     )
# #     st.markdown(response)

# # # I'm Feeling Lucky
# # elif section == "🎯 I'm Feeling Lucky!":
# #     st.header("🎯 Surprise Combo Round")

# #     st.subheader("DSA:")
# #     st.markdown(ask_groq(
# #         "Give me a random DSA coding problem from LeetCode, GFG, or HackerRank with title, platform, and URL."
# #     ))

# #     st.subheader("CS Fundamentals:")
# #     st.markdown(ask_groq(
# #         "Give me a CS fundamentals question with answer. Randomly pick from OS, DBMS, CN, or OOPs."
# #     ))

# #     st.subheader("Aptitude:")
# #     st.markdown(ask_groq(
# #         "Give me a company-specific aptitude or reasoning interview question with solution."
# #     ))

# #     st.subheader("Startup Idea:")
# #     st.markdown(ask_groq(
# #         "Generate a random startup product or service idea and explain it briefly."
# #     ))












# import streamlit as st
# from utils.groq_helper import ask_groq

# st.set_page_config(page_title="PrepSmart - AI Interview Coach", layout="wide")
# st.title("🎓 PrepSmart: Your AI Interview Preparation Assistant")

# st.markdown("<style>" + open("assets/styles.css").read() + "</style>", unsafe_allow_html=True)

# st.sidebar.title("📚 Navigation")
# section = st.sidebar.radio("Go to", [
#     "Random DSA Question",
#     "Computer Fundamentals",
#     "Aptitude & Reasoning",
#     "Startup Product/Service Prep",
#     "🎯 I'm Feeling Lucky!"
# ])

# def show_code_ide_links():
#     st.markdown("""
#         **Try this on:**
#         - [💻 Replit](https://replit.com/)
#         - [👨‍💻 CodeChef IDE](https://www.codechef.com/ide)
#         - [⚡ LeetCode Playground](https://leetcode.com/playground)
#     """)

# # ------------------- DSA Section -------------------
# if section == "Random DSA Question":
#     st.header("🔢 Random DSA Problem")
#     if st.button("🎲 Get New DSA Question"):
#         st.session_state.dsa_q = ask_groq(
#             "Give me a random DSA coding problem from LeetCode, GFG, or HackerRank with title, platform, description, and URL."
#         )

#     if "dsa_q" not in st.session_state:
#         st.session_state.dsa_q = ask_groq(
#             "Give me a random DSA coding problem from LeetCode, GFG, or HackerRank with title, platform, description, and URL."
#         )

#     st.markdown(st.session_state.dsa_q)
#     show_code_ide_links()















import streamlit as st
from utils.groq_helper import ask_groq

st.set_page_config(page_title="PrepSmart - AI Interview Coach", layout="wide")
st.title("🎓 PrepSmart: Your AI Interview Preparation Assistant")

# Load styles
st.markdown("<style>" + open("assets/styles.css").read() + "</style>", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("📚 Navigation")
section = st.sidebar.radio("Go to", [
    "Random DSA Question",
    "Computer Fundamentals",
    "Aptitude & Reasoning",
    "Startup Product/Service Prep",
    "🎯 I'm Feeling Lucky!"
])

def show_code_ide_links():
    st.markdown("""
        **Try this on:**
        - [💻 Replit](https://replit.com/)
        - [👨‍💻 CodeChef IDE](https://www.codechef.com/ide)
        - [⚡ LeetCode Playground](https://leetcode.com/playground)
    """)

# --- DSA ---
if section == "Random DSA Question":
    st.header("🔢 Random DSA Problem")
    if st.button("🎲 Next DSA Question") or "dsa_q" not in st.session_state:
        st.session_state.dsa_q = ask_groq(
            "Give me a random DSA coding problem from LeetCode, GFG, or HackerRank with title, platform, description, and URL."
        )
    st.markdown(st.session_state.dsa_q)
    show_code_ide_links()

# --- CS Fundamentals ---
elif section == "Computer Fundamentals":
    st.header("💻 CS Fundamental Question")
    topic = st.selectbox("Choose Topic", ["OS", "DBMS", "CN", "OOPs"])
    key = f"cs_{topic.lower()}"
    if st.button("🔄 Next Question") or key not in st.session_state:
        st.session_state[key] = ask_groq(
            f"Give me a technical interview question with answer from {topic}."
        )
    st.markdown(st.session_state[key])

# --- Aptitude ---
elif section == "Aptitude & Reasoning":
    st.header("🧠 Aptitude & Reasoning")
    company = st.selectbox("Select Company", ["TCS", "Infosys", "Wipro", "Cognizant"])
    key = f"apt_{company.lower()}"
    if st.button("🔄 Next Aptitude Question") or key not in st.session_state:
        st.session_state[key] = ask_groq(
            f"Give me one aptitude or reasoning question with solution asked in {company} interviews."
        )
    st.markdown(st.session_state[key])

# --- Startup Ideas ---
elif section == "Startup Product/Service Prep":
    st.header("🚀 Startup Product or Service Idea")
    if st.button("💡 Next Startup Idea") or "startup_idea" not in st.session_state:
        st.session_state.startup_idea = ask_groq(
            "Generate a unique startup product or service idea and explain it in 2-3 sentences for an interview pitch."
        )
    st.markdown(st.session_state.startup_idea)

# --- I'm Feeling Lucky ---
elif section == "🎯 I'm Feeling Lucky!":
    st.header("🎯 Surprise Combo Round")
    if st.button("🎰 Shuffle All"):
        st.session_state.combo_dsa = ask_groq(
            "Give me a random DSA coding problem from LeetCode, GFG, or HackerRank with title, platform, and URL."
        )
        st.session_state.combo_cs = ask_groq(
            "Give me a CS fundamentals interview question and answer. Randomly pick from OS, DBMS, CN, or OOPs."
        )
        st.session_state.combo_apt = ask_groq(
            "Give me a company-specific aptitude or reasoning interview question with solution."
        )
        st.session_state.combo_startup = ask_groq(
            "Generate a random startup product or service idea and explain it briefly."
        )

    st.subheader("🔢 DSA:")
    st.markdown(st.session_state.get("combo_dsa", "Click 'Shuffle All' to begin"))

    st.subheader("💻 CS Fundamentals:")
    st.markdown(st.session_state.get("combo_cs", ""))

    st.subheader("🧠 Aptitude:")
    st.markdown(st.session_state.get("combo_apt", ""))

    st.subheader("🚀 Startup Idea:")
    st.markdown(st.session_state.get("combo_startup", ""))
