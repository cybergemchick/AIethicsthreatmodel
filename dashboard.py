import streamlit as st
import os

st.set_page_config(layout="wide")
st.title("🧠 AI and Ethics Dashboard")

with st.sidebar:
    st.header("🔐 GitHub Integration")
    st.markdown("[View Repository](https://github.com/jamie-contee/ai-ethics-dashboard)")

st.subheader("📜 Recent Alerts Log")
log_file = "alerts.log"
if os.path.exists(log_file):
    with open(log_file, "r") as f:
        logs = f.readlines()
        st.text("".join(logs[-20:]))
else:
    st.warning("No alerts.log file found.")

with st.expander("🛡️ STRIDE Threat Modeling"):
    st.markdown("""
**STRIDE Categories**:
- **Spoofing**: Impersonating identities
- **Tampering**: Unauthorized data modification
- **Repudiation**: Denying actions
- **Information Disclosure**: Leaking sensitive data
- **Denial of Service**: Disrupting availability
- **Elevation of Privilege**: Gaining unauthorized access
""")

with st.expander("🔄 Secure ML Lifecycle"):
    st.markdown("""
**Stages**:
1. Data Collection – Validate sources and consent
2. Preprocessing – Remove bias and ensure privacy
3. Training – Monitor for adversarial risks
4. Evaluation – Use fairness metrics
5. Deployment – Secure endpoints and access
6. Monitoring – Log and alert ethical/security events
7. Retirement – Archive responsibly
""")

with st.expander("⚙️ CI/CD Security Best Practices"):
    st.markdown("""
- Secrets management via environment variables
- Automated testing and dependency scanning
- Rollback mechanisms for failed deployments
- Audit logs for traceability
- Code signing for integrity
""")

with st.expander("📊 Fairness Metrics"):
    st.markdown("Placeholder for Aequitas integration and fairness reports.")

with st.expander("🧠 Why Did the Model Make This Decision?"):
    st.markdown("Explainability tools will be integrated here (e.g., SHAP, LIME).")

with st.expander("📋 AI Act Compliance Checklist"):
    st.markdown("""
- Risk classification
- Human oversight
- Transparency disclosures
- Data governance
- Robustness and accuracy
""")
