# Treasury AI Risk & Use Case Review Assistant

## Overview
This prototype demonstrates a secure, testable AI-enabled workflow for evaluating proposed AI use cases before deployment.

## Features
- AI use case intake form
- Structured AI-generated risk review
- Cybersecurity and data sensitivity assessment
- Human-in-the-loop recommendations
- Deployment readiness score
- Mock mode when no API key is configured

## Tools Used
- Python
- Streamlit
- OpenAI/Azure OpenAI compatible API pattern
- pytest
- GitHub
- Cloud deployment via Streamlit Cloud/Render/Hugging Face Spaces

## Setup Instructions
1. Clone the repository
2. Create a virtual environment
3. Install dependencies
4. Configure environment variables
5. Run the app locally

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py