import streamlit as st

from src.ai_engine import generate_ai_assessment
from src.risk_scoring import calculate_risk_score
from src.validators import is_valid_use_case

st.set_page_config(page_title="Treasury AI Risk Review Assistant")

st.title("Treasury AI Risk & Use Case Review Assistant")

st.write(
    "This prototype evaluates proposed AI use cases for risk, controls, "
    "and deployment readiness. It supports live AI mode when an API key is "
    "configured and mock mode when no key is available."
)

st.divider()

with st.form("ai_use_case_form"):
    use_case_name = st.text_input(
        "AI Use Case Name",
        placeholder="Example: Automated document classification",
    )

    business_objective = st.text_area(
        "Business Objective",
        placeholder="Example: Reduce manual review time for internal policy documents.",
    )

    data_sensitivity = st.selectbox(
        "Data Sensitivity",
        [
            "Public",
            "Internal",
            "Confidential",
            "Financial",
            "PII",
            "Taxpayer-related",
        ],
    )

    deployment_environment = st.selectbox(
        "Deployment Environment",
        [
            "Prototype",
            "Test",
            "Production",
        ],
    )

    planned_controls = st.text_area(
        "Controls Already Planned",
        placeholder="Example: Human review, access control, logging, cybersecurity review.",
    )

    submitted = st.form_submit_button("Generate AI Risk Review")

if submitted:
    if not is_valid_use_case(use_case_name):
        st.warning("Please enter an AI use case name.")
    else:
        risk_score = calculate_risk_score(data_sensitivity, deployment_environment)

        with st.spinner("Generating assessment..."):
            assessment, mode = generate_ai_assessment(
                use_case_name=use_case_name,
                business_objective=business_objective,
                data_sensitivity=data_sensitivity,
                deployment_environment=deployment_environment,
                planned_controls=planned_controls,
            )

        st.subheader("Assessment Results")
        st.caption(mode)

        st.metric("Deterministic Risk Score", f"{risk_score} / 5")

        if risk_score >= 4:
            st.error("Risk Level: High")
        elif risk_score >= 3:
            st.warning("Risk Level: Medium")
        else:
            st.success("Risk Level: Low")

        st.markdown(assessment)

st.divider()

st.caption(
    "Prototype only. AI-generated recommendations are advisory and require human review "
    "before any operational or production decision."
)