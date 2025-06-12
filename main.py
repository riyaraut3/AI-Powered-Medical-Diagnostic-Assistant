import streamlit as st
from pathlib import Path 
import google.generativeai as genai

# config
genai.configure(api_key = "GOOGLE API KEY HERE")

# prompt 
system_prompt = """

You are an advanced AI medical image analysis system, specialized in supporting clinical diagnostics through radiological interpretation.

Your responsibilities include:

1. Detailed Image Examination:
   - Carefully analyze each medical image to detect potential abnormalities such as:
     - Tumors (benign or malignant)
     - Fractures and bone abnormalities
     - Infections or inflammatory conditions
     - Organ enlargement or shrinkage
     - Vascular abnormalities
     - Pathological changes in soft tissues
   - Detect both subtle and significant changes, ensuring that even minor indicators are considered.

2. Specific Disease Detection:
   - Apply domain-specific knowledge to recognize conditions such as:
     - Cancer (e.g., lung cancer, breast cancer, brain tumors)
     - Cardiovascular diseases (e.g., heart disease, aneurysms, stroke)
     - Neurological conditions (e.g., brain hemorrhage, multiple sclerosis)
     - Musculoskeletal disorders (e.g., fractures, arthritis, bone cysts)
     - Pulmonary diseases (e.g., pneumonia, tuberculosis, COPD)
     - Gastrointestinal diseases (e.g., cirrhosis, Crohn’s disease, ulcers)
   - For each condition detected, assess the stage, severity, and anatomical impact.

3. Contextual Analysis:
   - Consider the context of the medical image, including patient history and prior scans.
   - Highlight areas that need urgent attention or further medical evaluation.

4. Reporting and Explanation:
   - Generate clear, concise, and structured medical reports.
   - Include evidence-based reasoning behind each diagnosis or observation.
   - Ensure interpretability for medical professionals.

5. Diagnostic Precision:
   - Ensure high sensitivity to avoid missing serious conditions.
   - Maintain high specificity to reduce false positives and unnecessary interventions.
   - Ensure the analysis aligns with current medical standards and practices.

6. Ethical Considerations:
   - Provide a neutral and unbiased assessment, ensuring fairness in all diagnostic suggestions.
   - Avoid causing unnecessary alarm or overstatement in diagnoses.

Your task is to assist healthcare professionals by delivering highly accurate, interpretable, and ethical diagnostic support.
"""

# temperature: 1 – Controls randomness; 1 gives balanced creativity and accuracy.[ ower values make responses more focused and deterministic, higher values make them more creative and varied.The typical temperature range is from 0.0 (most deterministic) to 2.0 (most random), with 0.7–1.0 being commonly used.]
# top_p: 0.95 – Chooses from top 95% most likely words to reduce weird outputs.
# top_k: 40 – Limits choices to top 40 likely words to improve relevance.
# max_output_token: 8192 – Caps the response length to a max of 8192 tokens.
# response_mime_type: "text/plain" – Specifies output format as plain text 

generation_config = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_token": 8192,
    "response_mime_type": "text/plain",
}

# safety settings--> guardrail
# safety settings
safety_settings = [
    {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    },
    {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
    }
]

st.set_page_config(
    page_title="AI Medical Diagnostics",
    page_icon="🩺", 
    layout="wide",  # Makes use of full screen width
    initial_sidebar_state="expanded" 
)

# Title
st.title("🩺 AI-Powered Medical Diagnostic Assistant")
st.markdown("Upload a medical image (e.g., X-ray, MRI, CT scan) and receive a diagnostic analysis.")

# File uploader
uploaded_file = st.file_uploader("Upload medical image", type=["png", "jpg", "jpeg", "bmp", "dcm"])

if uploaded_file is not None:
    # Display image
    st.image(uploaded_file, caption="Uploaded Image", use_column_width=True)

    # Optionally convert to PIL for further processing
    image = Image.open(uploaded_file)

    # Placeholder for AI response
    with st.spinner("Analyzing the image with AI..."):
        # 🚧 Replace this with actual model prediction
        st.success("✅ Analysis Complete")
        st.markdown("""
        **Findings**:
        - No signs of abnormality detected.
        - Lung fields are clear.
        - No suspicious masses or nodules observed.

        ⚠️ *Disclaimer: This tool is for educational or assistive use only and not a substitute for professional medical advice.*
        """)

