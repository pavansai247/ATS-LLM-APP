import streamlit
import dotenv
import io
import base64
from PIL import Image
import pdf2image 
import streamlit as st
from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai

genai.configure(api_key = os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content,prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    resonse = model.generate_content([input,pdf_content[0],prompt])
    return resonse.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        ## Convert the pdf to image:
        images = pdf2image.convert_from_bytes(uploaded_file.read())
        
        first_page = images[0]
        
        ##Convert to bytes
        img_byte_arr = io.BytesIO()
        first_page.save(img_byte_arr, format= 'JPEG')
        img_byte_arr = img_byte_arr.getvalue()
        
        pdf_parts =[
            {
                "mime_type" : 'image/jpeg',
                "data":base64.b64encode(img_byte_arr).decode()
            }
        ]
        return pdf_parts
    else:
        raise FileNotFoundError("file not uploaded")
    
## Streamlit app
    
st.set_page_config(page_title='ATS Resume')
st.header("ATS Tracking System")
input_text=st.text_area("Job Description: ",key="input")
uploaded_file=st.file_uploader("upload your resume(PDF)...",type=["PDF"])

if uploaded_file is not None:
    st.write("PDF uploaded successfully")

submit1 = st.button("Tell me about my resume")
submit2 = st.button("How can i Improve my skills")
submit3 = st.button("what are the keywords that are missing")
submit4 = st.button("Percentage match")
submit5 = st.button("Create me the sample resume based on the job Description")

input_prompt1 = """ You are an experience Hr with tech Experience in the field of any one job role form  Data Science or Full stack or Devops or Data Analytics or Cloud Developer or
Wed developer or Data Engineering or Java Developer. Your task is to review the provied resume based on the Job Description.
Please share the professional evalutation on whether the candidate's profile align with the role.
Highlight the strenths and weeknesses of applicant in relation to the specified resume."""

input_prompt2 = """you are an techinal Expert in the field of  Data Science, Full stack, Devops, Data Analytics, Cloud Developer,
Wed developer, Data Engineering, Java Developer. Your task is to review the provied resume based on the Job Description.
Please share the professional evalutation on whether the candidate's profile align with the role. Give the suggestion to improve the skills in Job Description.
Highlight the strenths and weeknesses of applicant in relation to the specified jod Description.And Provide the skills to learn which is not 
align to the Job Description."""

input_prompt3 = """You are an Skilled ATS (Application Tracking System) scanner with deep understanding of  Data Science or Full stack or Devops or Data Analytics or Cloud Developer or
Wed developer or Data Engineering or Java Developer and deep ATS Functionality. Your task is to evalute resume againest the provieded job Description.
Give me the missing keywords or skills in provided resume."""

input_prompt4 = """You are an Skilled ATS (Application Tracking System) scanner with deep understanding of  Data Science, Full stack, Devops, Data Analytics, Cloud Developer,
Wed developer, Data Engineering, Java Developer and deep ATS Functionality. Your task is to evalute resume against the provided job Description.
Give me the percentage of match if the resume matches Job Description."""

input_prompt5 = """You are skilled resume maker in the field of Data Science, Full stack, Devops, Data Analytics, Cloud Developer,
Wed developer, Data Engineering, Java Developer. Your task is to evalute Job Description , Give the two resume samples based on the Job Description."""

if submit1:
    if uploaded_file is not None:
        pdf_content= input_pdf_setup(uploaded_file)
        response= get_gemini_response(input_prompt1,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please upload the resume ")
            
elif submit2:
    if uploaded_file is not None:
        pdf_content= input_pdf_setup(uploaded_file)
        response= get_gemini_response(input_prompt2,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please upload the resume ")
            
elif submit3:
    if uploaded_file is not None:
        pdf_content= input_pdf_setup(uploaded_file)
        response= get_gemini_response(input_prompt3,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please upload the resume ")
            
elif submit4:
    if uploaded_file is not None:
        pdf_content= input_pdf_setup(uploaded_file)
        response= get_gemini_response(input_prompt4,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please upload the resume ")
            
elif submit5:
    if uploaded_file is not None:
        pdf_content= input_pdf_setup(uploaded_file)
        response= get_gemini_response(input_prompt5,pdf_content,input_text)
        st.subheader("The response is ")
        st.write(response)
    else:
        st.write("Please upload the resume ")