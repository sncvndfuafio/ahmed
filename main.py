# ============================= 
# IMPORTS 
# ============================= 
import streamlit as st 
from PIL import Image 

# ============================= 
# BASIC TEXT ELEMENTS 
# ============================= 
st.title("Hello GeeksForGeeks !!!") 
st.header("This is a header") 
st.subheader("This is a subheader") 
st.text("Hello GeeksForGeeks!!!") 
st.markdown("### This is a markdown") 

# ============================= 
# STATUS MESSAGES 
# ============================= 
st.success("Success") 
st.info("Information") 
st.warning("Warning") 
st.error("Error") 
exp = ZeroDivisionError("Trying to divide by Zero") 
st.exception(exp) 

# ============================= 
# WRITE FUNCTION 
# ============================= 
st.write("Text with write") 
st.write(range(10)) 

# ============================= 
# DISPLAY IMAGE 
# ============================= 
st.markdown("### Displaying an Image") 
try: 
    img = Image.open("streamlit.png")  # Ensure this file is in the same folder 
    st.image(img, width=200) 
except FileNotFoundError: 
    st.warning("Image file 'streamlit.png' not found.") 

# ============================= 
# CHECKBOX 
# ============================= 
st.markdown("### Checkbox Example") 
if st.checkbox("Show/Hide"): 
    st.text("Showing the widget") 

# ============================= 
# RADIO BUTTON 
# ============================= 
st.markdown("### Radio Button Example") 
status = st.radio("Select Gender: ", ('Male', 'Female')) 
if status == 'Male': 
    st.success("Male") 
else: 
    st.success("Female") 

# ============================= 
# SELECTBOX 
# ============================= 
st.markdown("### Selectbox Example") 
hobby = st.selectbox("Hobbies: ", ['Dancing', 'Reading', 'Sports']) 
st.write("Your hobby is: ", hobby) 

# ============================= 
# MULTISELECT 
# ============================= 
st.markdown("### Multiselect Example") 
hobbies = st.multiselect("Hobbies: ", ['Dancing', 'Reading', 'Sports']) 
st.write("You selected", len(hobbies), 'hobbies') 

# ============================= 
# BUTTON 
# ============================= 
st.markdown("### Buttons Example") 
st.button("Click me for no reason") 
if st.button("About"): 
    st.text("Welcome To streamlit!!!") 

# ============================= 
# TEXT INPUT 
# ============================= 
st.markdown("### Text Input Example") 
name = st.text_input("Enter Your name", "Type Here ...") 
if st.button('Submit'): 
    result = name.title() 
    st.success(result) 

# ============================= 
# SLIDER 
# ============================= 
st.markdown("### Slider Example") 
level = st.slider("Select the level", 1, 5) 
st.text('Selected: {}'.format(level)) 

# ============================= 
# MINI PROJECT: BMI CALCULATOR 
# ============================= 
st.markdown("---") 
st.title('Welcome to BMI Calculator') 

# Weight input 
weight = st.number_input("Enter your weight (in kgs)") 

# Height format selection 
status = st.radio('Select your height format:', ('cms', 'meters', 'feet')) 

if status == 'cms': 
    height = st.number_input('Height in Centimeters') 
    try: 
        bmi = weight / ((height / 100) ** 2) 
    except: 
        st.text("Enter some value of height") 

elif status == 'meters': 
    height = st.number_input('Height in Meters') 
    try: 
        bmi = weight / (height ** 2) 
    except: 
        st.text("Enter some value of height") 

else: 
    height = st.number_input('Height in Feet') 
    try: 
        bmi = weight / (((height / 3.28)) ** 2) 
    except: 
        st.text("Enter some value of height") 

# BMI Calculation 
if st.button('Calculate BMI'): 
    st.text("Your BMI Index is {:.2f}.".format(bmi)) 
    if bmi < 16: 
        st.error("You are Extremely Underweight") 
    elif bmi >= 16 and bmi < 18.5: 
        st.warning("You are Underweight") 
    elif bmi >= 18.5 and bmi < 25: 
        st.success("Healthy") 
    elif bmi >= 25 and bmi < 30: 
        st.warning("Overweight") 
    elif bmi >= 30: 
        st.error("Extremely Overweight") 

# ============================= 
# END OF APP 
# ============================= 
st.markdown("---") 
st.info("This app demonstrates basic Streamlit components.")
