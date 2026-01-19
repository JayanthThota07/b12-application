import json
import hmac
import hashlib
import requests
from datetime import datetime, timezone

SIGNING_SECRET = b"hello-there-from-b12"
URL = "https://b12.io/apply/submission"

payload = {
    "action_run_link": "https://github.com/YOUR_USERNAME/b12-application/actions/runs/RUN_ID",
    "email": "venkatajayanththota@gmail.com",
    "name": "Your Name",
    "repository_link": "https://github.com/JayathtThota07/b12-application",
    "resume_link": "https://link-to-your-resume-or-linkedin",
    "timestamp": datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"),
}

# Canonical JSON: sorted keys, compact separators
body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

signature = hmac.new(
    SIGNING_SECRET,
    body,
    hashlib.sha256
).hexdigest()

headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={signature}",
}

response = requests.post(URL, data=body, headers=headers)
response.raise_for_status()

data = response.json()
print("Receipt:", data["receipt"])
