from pathlib import Path
from tkinter import Button

import streamlit as st # pip install streamlit
from PIL import Image # pip install pillow 

#-----PATH SETTINGS ----

THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"

# --- GENERAL SETTINGS ----

STRIPE_CHECKOUT = "https://buy.stripe.com/6oE8yhaN4eArb2EbII"
CONTACT_EMAIL = "samissampro@gmail.com"
DEMO_VIDEO = "https://youtu.be/PmJ9rkKGqrI" 
PRODUCT_NAME = "Big Data in Finance : From Zero to Master"
PRODUCT_TAGLINE = "Unlock the power of Big Data in the world of finance"
PRODUCT_DESCRIPTION = """ 
Unlock the power of Big Data in the world of finance with our revolutionary digital product: "Big Data in Finance: From Zero to Hero." 
This comprehensive and cutting-edge program is designed to empower finance professionals, analysts, and enthusiasts with the knowledge 
and skills to harness the potential of vast datasets, transforming them into actionable insights and strategic advantages.

**Key Features:**

- **Comprehensive Learning:**
Dive deep into the realm of Big Data in finance through a meticulously curated curriculum. Understand the fundamentals of Big Data,
data collection, storage, and processing, while exploring its potential applications in financial markets, risk management,
fraud detection, and customer behavior analysis.

- **Practical Application:** 
Gain hands-on experience and real-world expertise through practical projects and case studies. From parsing and analyzing 
financial data to developing predictive models, this program ensures you can confidently apply Big Data techniques to address
 complex financial challenges.


**Embark on Your Big Data Journey Today!**

Join thousands of professionals who have already embarked on their journey to become Big Data heroes in the world of finance. Embrace the future of data-driven finance and unlock unprecedented growth and success. Enroll now in "Big Data in Finance: From Zero to Hero" and step into the realm of limitless possibilities.
"""


def load_css_file(css_file_path):
    with open(css_file_path) as f:
        return st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# --- PAGE CONFIG ---

st.set_page_config(
    page_title=PRODUCT_NAME,
    page_icon=":star:",
    layout="centered",
    initial_sidebar_state="collapsed",
)
load_css_file(CSS_FILE)

#----- MAIN SECTION ----

st.header(PRODUCT_NAME)
st.subheader(PRODUCT_TAGLINE)
left_col, right_col = st.columns((1 , 1))
with left_col:
    st.text("")
    st.write(PRODUCT_DESCRIPTION)
    st.markdown(
        f'<a href={STRIPE_CHECKOUT} class="button"> 👉 Get the add-in</a>',
        unsafe_allow_html=True,
    )
with right_col:
    product_image = Image.open(ASSETS_DIR / "product.png")
    st.image(product_image, width=450)
             
# ---- FEATURES ----
st.write("")
st.write("---")
st.subheader(":rocket: Features")
features = {
    "Feature_1.png": [
        "Run Python Files From Excel",
        "After locating your Python interpreter, you can execute Python files directly from Excel. In the Pro Version, you can also add several Python interpreter paths. This is helpful when you need to execute your Python code from different virtual environments.",
    ],
    "Feature_2.png": [
        "Create Pandas Dataframes",
        "Generate Python files with a click of a button. Select the cell range you want to transform, and the add-in creates the Python code to read in the Excel data as a pandas dataframe.Instead of messing around with all of the available options in the pandas ‘read_excel’ method, the add-in does it for you.",
    ],
    "Feature_3.png": [
        "Create Jupyter Notebooks",
        "Have you ever wanted to do some quick analysis of your Excel data in a Jupyter Notebook? MyToolBelt can convert an Excel cell range into a Jupyter Notebook. Just select the cell range, and the add-in will create a new Jupyter Notebook in the workbook’s directory. Inside the Jupyter Notebook, you will find your ready-to-use dataframe based on your selection. This feature is a real time saver!",
    ],
}
for image, description in features.items():
    image = Image.open(ASSETS_DIR / image)
    st.write("")
    left_col, right_col = st.columns(2)
    left_col.image(image, use_column_width=True)
    right_col.write(f"**{description[0]}**")
    right_col.write(description[1])


# --- DEMO ---
st.write("")
st.write("---")
st.subheader(":tv: Demo")
st.video(DEMO_VIDEO, format="video/mp4", start_time=0)

# --- FAQ ---
st.write("")
st.write("---")
st.subheader(":raising_hand: FAQ")
faq = {
    "Question 1": "Some text goes here to answer question 1",
    "Question 2": "Some text goes here to answer question 2",
    "Question 3": "Some text goes here to answer question 3",
    "Question 4": "Some text goes here to answer question 4",
    "Question 5": "Some text goes here to answer question 5",
}
for question, answer in faq.items():
    with st.expander(question):
        st.write(answer)


# --- CONTACT FORM ---
# video tutorial: https://youtu.be/FOULV9Xij_8
st.write("")
st.write("---")
st.subheader(":mailbox: Have A Question? Ask Away!")
contact_form = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL}" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="Your message here"></textarea>
     <button type="submit" class="button">Send ✉</button>
</form>
"""
st.markdown(contact_form, unsafe_allow_html=True)