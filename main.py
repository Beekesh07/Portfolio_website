import streamlit as st

# Set page configuration
st.set_page_config(page_title="Beekesh Singh Portfolio", layout="wide")

# Define custom CSS for styling
st.markdown("""
    <style>
        /* Center image styling */
        .profile-img {
            display: block;
            margin: 0 auto;
            border-radius: 50%;
            width: 250px;
        }

        /* Circle Skills */
        .circle {
            display: inline-block;
            background-color: #32CD32; /* Default Color */
            color: white;
            border-radius: 50%;
            width: 120px;
            height: 120px;
            line-height: 120px;
            text-align: center;
            margin: 10px;
            font-size: 15px;
            font-weight: bold;
        }
        .ml { background-color: #FFA500; }
        .dl { background-color: #1E90FF; }
        .llm { background-color: #808080; }

        /* Section Header Styling */
        .section-header {
            font-size: 32px;
            font-weight: bold;
            color: #4E79A7;
            text-align: center;
            margin-top: 30px;
        }
    </style>
""", unsafe_allow_html=True)

# Home Section

st.markdown('<h1 style="text-align: center;">Beekesh Singh</h1>', unsafe_allow_html=True)
st.image("PIC.jpg", width=250, caption="Aspiring Data Scientist", use_container_width=False)


st.write(
    """
    <div style='text-align: center; font-size: 18px;'>
        <p><b>Python | Machine Learning | Deep Learning | LLM Models</b></p>
        <p>Hi! I'm Beekesh Singh, an aspiring Data Scientist with a BSc in Computer Science and an MCA degree.</p>
        <p>I specialize in solving real-world problems through data-driven approaches and actively share my insights on Medium.</p>
    </div>
    """, unsafe_allow_html=True
)

# Skills Section
st.markdown('<div class="section-header">My Skills</div>', unsafe_allow_html=True)
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown('<div class="circle">Python</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="circle ml">Machine Learning</div>', unsafe_allow_html=True)
with col3:
    st.markdown('<div class="circle dl">Deep Learning</div>', unsafe_allow_html=True)
with col4:
    st.markdown('<div class="circle llm">LLM Models</div>', unsafe_allow_html=True)

st.write("---")

# Resume Section
st.markdown('<div class="section-header">Resume</div>', unsafe_allow_html=True)
st.write("📄 [Download My Resume](./Resume_Beekesh_Singh.pdf)")  # Add your resume file path here

st.write("---")

# Projects Section
st.markdown('<div class="section-header">Projects</div>', unsafe_allow_html=True)
projects = [
    {
        "name": "Credit Risk Prediction",
        "image": "credit_risk_prediction.jpg",  # Replace with your image file path
        "link": "https://credit-risk-model-by-beekesh-singh.streamlit.app/"
    },
    {
        "name": "Healthcare Premium Price Prediction",
        "image": "healthcare_premium_prediction.jpg",  # Replace with your image file path
        "link": "https://healthcare-premium-prediction-by-beekesh-singh.streamlit.app/"
    },
    {
        "name": "Flower Classification Project",
        "image": "flower_classification.jpg",  # Replace with your image file path
        "link": "https://flowers-classification-by-beekesh.streamlit.app/"
    }
]

# Display projects in a clean grid
for project in projects:
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image(project["image"], caption=project["name"], width=150)
    with col2:
        st.subheader(project["name"])
        st.write(f"[View Project]({project['link']})")
    st.write("---")

# Contact Section
st.markdown('<div class="section-header">Contact Me</div>', unsafe_allow_html=True)
st.write("📧 **Email**: [beekeshsingh0007@gmail.com](mailto:beekeshsingh0007@gmail.com)")
st.write("📞 **Phone**: 9871172408")
st.write("🔗 **LinkedIn**: [My LinkedIn](https://www.linkedin.com/in/your-linkedin-profile)")  # Replace with your LinkedIn link
st.write("✍️ **Medium**: [My Medium](https://medium.com/@your-medium-profile)")  # Replace with your Medium link

st.markdown("""
    <div style="background-color:#f0f2f6;padding:10px;border-radius:10px; text-align: center;">
        <h3 style="color:#4e79a7;">Let's Connect!</h3>
        <p>Feel free to reach out for collaborations, projects, or just to connect!</p>
    </div>
""", unsafe_allow_html=True)
