# black-onyx-matrix
# 🛡️ Black Onyx Advisory - Developer Security Protocol
### Security Status: CRITICAL OVERRIDE ACTIVE (Development Sandbox)

## 🚨 Current Security Risk Exposure
The `app.py` script currently exposes an explicit, cleartext `CSV_URL` variable pointing directly to a published cloud data pipeline. While this bypasses connection and synchronization constraints during rapid prototyping inside GitHub web editors, **this architecture is strictly prohibited from entering production.** 

If pushed to a public production deployment, it exposes sensitive first-mile grower identities, tax numbers, and proprietary pricing structures to unauthorized scraping and network interception.

## 🛠️ Required Developer Actions: Transitioning to Local & Cloud Secrets

To lock down the system architecture before pushing to a live production environment, the development team must execute the following migration:

### Phase 1: Localizing Development Environment (Moving off GitHub Web Editor)
1. Clone the repository to a local, secure developer workstation.
2. At the root directory, create a hidden folder named `.streamlit/`.
3. Inside that folder, initialize a local configuration file named `secrets.toml`.
4. Inject your private streaming link into the local configuration file using the following format:
   ```toml
   # .streamlit/secrets.toml (This file must NEVER be pushed to GitHub)
   GOOGLE_SECURE_CSV_LINK = "https://google.com"
   ```

### Phase 2: Updating the Main Application Code
Replace the exposed `CSV_URL` engine in `app.py` with the following rigid, zero-tolerance server-side vault injection rule:
```python
import os
import streamlit as st

if "GOOGLE_SECURE_CSV_LINK" in st.secrets:
    SECURE_URL = st.secrets["GOOGLE_SECURE_CSV_LINK"]
else:
    try:
        SECURE_URL = os.environ["GOOGLE_SECURE_CSV_LINK"]
    except KeyError:
        st.error("🔒 **Security Policy Exception:** Master Sourcing API Token Is Encrypted or Missing. System Access Revoked.")
        st.stop()
```

### Phase 3: Committing the Repository Safety Shield
1. Open the project's `.gitignore` file.
2. Append the following lines to ensure that no developer accidentally publishes the local secret values:
   ```text
   # Black Onyx Security Shield
   .streamlit/secrets.toml
   .streamlit/config.toml
   ```

