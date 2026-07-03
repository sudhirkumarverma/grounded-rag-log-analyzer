import streamlit as st

from grounded_rag.pipeline import GroundedRAGPipeline

# -------------------------------------------------------
# Page Configuration
# -------------------------------------------------------

st.set_page_config(
    page_title="Grounded RAG Incident Investigator",
    page_icon="🔍",
    layout="wide",
)

# -------------------------------------------------------
# Custom Styling
# -------------------------------------------------------

st.markdown(
    """
<style>

.main-title{
    font-size:36px;
    font-weight:700;
    color:#0F62FE;
}

.sub-title{
    color:#666;
    font-size:17px;
    margin-top:-10px;
    margin-bottom:20px;
}

.section-title{
    font-size:24px;
    font-weight:600;
    margin-top:20px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:50px;
    font-size:13px;
}

</style>
""",
    unsafe_allow_html=True,
)

pipeline = GroundedRAGPipeline()

# -------------------------------------------------------
# Sidebar
# -------------------------------------------------------

with st.sidebar:

    st.title("🔍 Grounded RAG")

    st.caption("Enterprise Incident Investigator")

    st.divider()

    st.subheader("Knowledge Base")

    st.success("50 Deployment Timelines")
    st.success("50 Historical Incidents")
    st.success("1 Operational Runbook")

    st.divider()

    st.subheader("Technology Stack")

    st.write("**Embedding Model**")
    st.caption("BAAI / bge-small-en-v1.5")

    st.write("**Vector Store**")
    st.caption("ChromaDB")

    st.write("**LLM**")
    st.caption("OpenAI GPT-4.1")

    st.divider()

    st.subheader("Supported Questions")

    st.markdown(
        """
- Deployment failures
- Root Cause Analysis
- Kubernetes issues
- Authentication failures
- Runbook guidance
"""
    )

    st.divider()

    st.subheader("Roadmap")

    st.markdown(
        """
✅ Grounded RAG

✅ Guardrails

✅ Evidence-based Answers

🚧 Exact Incident Lookup (v1.1)

🚧 Hybrid Retrieval (v1.1)
"""
    )

    st.divider()

    st.info(
        """
This application demonstrates a
Grounded Retrieval-Augmented
Generation (RAG) workflow.

Responses are generated only
after retrieving supporting
enterprise evidence from
deployment timelines,
historical incidents and
operational runbooks.
"""
    )

    st.divider()

    st.caption("Version 1.0")

# -------------------------------------------------------
# Header
# -------------------------------------------------------

st.markdown(
    '<div class="main-title">🔍 Grounded RAG Incident Investigator</div>',
    unsafe_allow_html=True,
)

st.markdown(
    '<div class="sub-title">AI-powered Enterprise Root Cause Analysis using Retrieval-Augmented Generation</div>',
    unsafe_allow_html=True,
)

st.divider()

# -------------------------------------------------------
# User Question
# -------------------------------------------------------

question = st.text_area(
    "Ask an enterprise question",
    height=120,
    placeholder="Example: Why did deployment fail?",
)

analyze = st.button(
    "🚀 Analyze Incident",
    use_container_width=True,
)

# -------------------------------------------------------
# Analysis
# -------------------------------------------------------

if analyze:

    if not question.strip():

        st.warning("Please enter a question.")

        st.stop()

    with st.spinner("Analyzing enterprise knowledge base..."):

        response = pipeline.ask(question)

    if not response["allowed"]:

        st.error(response["message"])

        st.info(
            """
Examples

• Why did deployment fail?

• What caused Kubernetes deployment failure?

• Explain authentication failures.

• Show deployment runbook.
"""
        )

        st.stop()

    st.success("✅ Enterprise knowledge successfully analyzed.")

    st.divider()

    st.markdown(
        '<div class="section-title">📌 Root Cause Analysis</div>',
        unsafe_allow_html=True,
    )

    st.write(response["answer"])

    st.divider()

    similarities = [
        item["similarity"]
        for item in response["results"]
    ]

    average_similarity = (
        sum(similarities) / len(similarities)
    )

    evidence_types = len(
        {
            item["metadata"]["source_type"]
            for item in response["results"]
        }
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Documents",
            len(response["results"]),
        )

    with col2:

        st.metric(
            "Evidence Types",
            evidence_types,
        )

    with col3:

        st.metric(
            "Average Similarity",
            f"{average_similarity:.2f}",
        )

    st.divider()

    st.markdown(
        '<div class="section-title">📚 Retrieved Evidence</div>',
        unsafe_allow_html=True,
    )

    for result in response["results"]:

        metadata = result["metadata"]

        title = metadata["source_type"].title()

        if "incident_id" in metadata:

            title += f" • {metadata['incident_id']}"

        with st.expander(title, expanded=False):
            similarity = result["similarity"]

            # --------------------------------------------------
            # Evidence Score
            # --------------------------------------------------

            if similarity >= 0.85:
                score = "🟢 High"

            elif similarity >= 0.70:
                score = "🟡 Medium"

            elif similarity >= 0.55:
                score = "🟠 Low"

            else:
                score = "🔴 Very Low"

            left, right = st.columns([3, 1])

            with left:

                st.write("#### Evidence Strength")

                st.progress(
                    max(0.0, min(similarity, 1.0))
                )

                st.caption(
                    f"Similarity Score: {similarity:.3f}"
                )

            with right:

                st.metric(
                    "Evidence",
                    score,
                )

            st.markdown("---")

            st.write("**Source Type**")

            st.info(
                metadata["source_type"].title()
            )

            if "incident_id" in metadata:

                st.write("**Incident ID**")

                st.success(
                    metadata["incident_id"]
                )

            st.write("**Retrieved Document**")

            st.code(
                result["document"],
                language="text",
            )

# -------------------------------------------------------
# Footer
# -------------------------------------------------------

st.divider()

st.markdown(
    """
<div class="footer">

<b>Grounded RAG Incident Investigator</b><br>

Enterprise AI Demo • Version 1.0

<br><br>

Built with

Sentence Transformers • ChromaDB • OpenAI GPT-4.1 • Streamlit

<br><br>

Roadmap

v1.1 → Hybrid Retrieval • Exact Incident Lookup

<br><br>

© 2026 Sudhir Kumar Verma

</div>
""",
    unsafe_allow_html=True,
)