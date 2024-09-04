import streamlit as st
from TextSummarizer.pipeline.prediction import PredictionPipeline
import time

# Initialize the prediction pipeline
predictor = PredictionPipeline()

# Streamlit app layout
st.set_page_config(page_title="Text Summarizer", page_icon="📝", layout="centered")

# Session state to manage input text
if 'input_text' not in st.session_state:
    st.session_state['input_text'] = ""

# Sidebar for customization
st.sidebar.title("Settings")
summary_length = st.sidebar.slider("Summary Length:", min_value=50, max_value=500, value=128)

# Example texts for quick testing
st.sidebar.subheader("Load Example Text")
if st.sidebar.button("Load Example 1"):
    st.session_state.input_text = "Dheeraj: Hey, how are you? Charan: Fine Dheeraj. What about you? Dheeraj: Yeah, cool. Do you have any updates regarding your internship? Charan: No not yet... I think I will get an update by tomorrow. Dheeraj: Okay, cool Charan but I hope you deserve the best. Charan: Thanks Dheeraj, what about you? everything alright? Dheeraj: Yes Charan, I'm preparing for my exams and hope they are going well. Charan: ohh okay... all the best"
if st.sidebar.button("Load Example 2"):
    st.session_state.input_text = "Hannah: Hey, do you have Betty's number? Amanda: Lemme check. Hannah: Okay. Amanda: Sorry, can't find it. Amanda: Ask Larry. Amanda: He called her last time we were at the park together. Hannah: I don't know him well. Amanda: Don't be shy, he's very nice. Hannah: If you say so.. Hannah: I'd rather you texted him. Amanda: Just text him. Hannah: Urgh.. Alright. Hannah: Bye. Amanda: Bye bye."

# Main section
st.title("Text Summarizer 📝")
st.write("This app summarizes any text, dialogue, conversation, or article")

# Text input area
input_text = st.text_area("Enter your text below:", 
                          value=st.session_state.input_text, 
                          height=200, 
                          placeholder="e.g., Once upon a time...", 
                          max_chars=10000)

# Update session state on text change
st.session_state.input_text = input_text

# Prediction button
if st.button("Summarize"):
    if input_text.strip():
        try:
            with st.spinner("Summarizing..."):
                predictor.gen_kwargs['max_length'] = summary_length
                
                # Generate the summary
                summary = predictor.predict(input_text)
                st.subheader("Summary")
                st.success(summary)

                # Add download button for summary
                st.download_button(label="Download Summary", 
                                   data=summary, 
                                   file_name="summary.txt", 
                                   mime="text/plain")

        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter some text to summarize.")
        st.markdown('<style>.stTextArea{border:2px solid red;}</style>', unsafe_allow_html=True)

# Clear I/O button
if st.button("Clear"):
    st.session_state.input_text = ""

# Footer
st.markdown("---")
st.write("Built with ❤️ by [Charan](https://www.linkedin.com/in/codewithcharan/), using [Streamlit](https://streamlit.io) and [Hugging Face Transformers](https://huggingface.co).")
st.markdown("<style>footer {visibility: hidden;} footer:after {content:'Built with ❤️ by Charan'; visibility: visible; display: block; text-align: center;}</style>", unsafe_allow_html=True)
