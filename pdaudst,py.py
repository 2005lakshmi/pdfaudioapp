import streamlit as st
import os
import time
import datetime as dt
import random

def text_audio_file(text):

    with st.spinner("please wait..."):
        
        current_datetime = dt.datetime.now()
        cdt = current_datetime
        start = time.time()
        data = gtts.gTTS(text,tld = 'co.in')
        file_name = f"sample{cdt.year}{cdt.month}{cdt.day}{cdt.hour}{str(random.randint(1,999))}.mp3"
        if path.exists(file_name):
            os.remove(file_name)
        data.save(file_name)
        end = time.time()
    st.write("time taken...",(end - start),"seconds")
    st.success(f"congratulations file created as {file_name}")
    return file_name

st.title(":red[Pdf] to :blue[Audio file]")

st.subheader("no time to read then listen")
st.write("upload your pdf file and enter the page number and get your audio file")

upload = st.file_uploader("upload your pdf file:")

if upload is not None:
    st.write("succesfully uploaded")
    if upload.type == "application/pdf":
        st.success("pdf file is uploaded")

        from PyPDF2 import PdfReader
        import gtts , playsound as mic
        from os import path

        pdf = PdfReader(upload)
        pdf_text = []
        for i in range(0,len(pdf.pages)):
            print(f"Page {i+1}:")
            page = pdf.pages[i].extract_text()
            pdf_text.append(page)


        cho = st.radio("select the type",["audio file of particular page","audio file of complete pdf"])

        if cho == "audio file of particular page":

            page_num = st.number_input("enter the page number from pdf whose audio to be generated: ",1,len(pdf.pages),step=1,)
            page_num = int(page_num)
            c = st.radio("preview the text",["NO","YES"])
            if c == "YES":
                st.write(f"the text in pgno {page_num} is \n\n {pdf_text[int(page_num)-1]}")

            ch = st.radio("generate audio file",["NO","YES"])
            if ch == "YES":
                
                fileN = text_audio_file(pdf_text[int(page_num)-1])
                st.audio(fileN,format = "audio/mp3")


        else:
            text = ''
            for i in range(0,len(pdf.pages)):
                text = text + pdf.pages[i].extract_text()
            choi = st.radio("preview the text: ",["NO","YES"])
            if choi == "YES":
                st.write(f"The text in pdf as below: \n\n\n {text}")

            choic = st.radio("Generate the Audio ?",["NO","YES"])
            if choic == "YES":
                fileName = text_audio_file(text)
                st.audio(fileName,format="audio/mp3")










    else:
        st.error("not a pdf file")
        st.error("kindly upload a pdf file!,.")