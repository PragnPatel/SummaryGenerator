# from flask import Flask, request, jsonify, render_template
# from summarizer import *

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return render_template('index.html')

# @app.route('/summarize',methods=['POST'])
# def summarize():
    
#     if request.method == 'POST':
        
#         text = request.form['originalText']
#         if not request.form['numOfLines']:
#             numOfLines = 3
#         else:
#             numOfLines = int(request.form['numOfLines'])
            
#         summary, original_length = generate_summary(text,numOfLines)
        
#         return render_template('result.html',
#                                text_summary=summary,
#                                lines_original = original_length,
#                                lines_summary = numOfLines)
    
# if __name__ == '__main__':
#     app.run(debug=True)


import streamlit as st
from summarizer import *

st.title("Text Summarizer")
input = st.text_area("Enter the text to summarize")

if st.button("Summarize"):
    if input.strip():
        with st.spinner("Generating Sumary"):
            summary, original_length = generate_summary(input, len(input))
        st.subheader("Summary")
        st.write(summary)
        st.subheader("Original Length")
        st.write(original_length)
    else:
        st.warning("Please enter some text to summarize")

