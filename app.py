import streamlit as st
from TextSummarizer.pipeline.prediction import PredictionPipeline

# Initialize the prediction pipeline
predictor = PredictionPipeline()

# Streamlit app layout
st.set_page_config(page_title="Text Summarizer", page_icon="📝", layout="centered")

# Sidebar for customization
st.sidebar.title("Settings")
summary_length = st.sidebar.slider("Summary Length:", min_value=50, max_value=500, value=128)

# Main section
st.title("Text Summarizer 📝")
st.write("This app summarizes any text, dialogue, conversation or article")

# Text input
input_text = st.text_area("Enter your text below:", height=200, placeholder="e.g., Once upon a time...")

# Prediction button
if st.button("Summarize"):
    if input_text.strip():
        try:
            with st.spinner("Summarizing..."):
                # Update gen_kwargs with user-defined max_length
                predictor.gen_kwargs['max_length'] = summary_length
                # Generate the summary
                summary = predictor.predict(input_text)
                st.subheader("Summary")
                st.success(summary)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
    else:
        st.warning("Please enter some text to summarize.")

# Clear button
if st.button("Clear"):
    input_text = st.empty()

# Footer
st.markdown("---")
st.write("Built with ❤️ by Charan, using Streamlit and Hugging Face Transformers.")