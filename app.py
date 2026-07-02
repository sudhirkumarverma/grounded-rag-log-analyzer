import streamlit as st
from rag import generate_answer

st.set_page_config(
    page_title="Grounded RAG Log Analyzer",
    layout="wide"
)

st.title("🧠 Grounded RAG Log Analyzer")
st.markdown("AI-powered Root Cause Analysis using **grounded logs + evidence-based reasoning**")

# Input box
query = st.text_input("Enter your question:", placeholder="Why did deployment fail?")

if st.button("Analyze"):
    if query.strip() == "":
        st.warning("Please enter a question")
    else:
        result = generate_answer(query)

        st.subheader("📌 Answer")
        st.write(result["answer"])

        st.subheader("📊 Confidence Score")
        st.metric(label="Confidence", value=f"{result['confidence'] * 100:.2f}%")

        st.subheader("📎 Evidence Logs")
        for i, log in enumerate(result["evidence"]):
            st.code(log, language="text")

        # Simple visual indicator
        if result["confidence"] < 0.6:
            st.error("⚠️ Low confidence - insufficient evidence")
        elif result["confidence"] < 0.8:
            st.warning("🟡 Medium confidence - partial evidence")
        else:
            st.success("🟢 High confidence - strong evidence")
