import json
import hmac
import hashlib
import datetime
import requests

SECRET = b"hello-there-from-b12"
URL = "https://b12.io/apply/submission"

payload = {
    "action_run_link": "https://github.com/JayanthThota07/b12-application/actions/runs/RUN_ID",
    "email": "venkatajayanththota@gmail.com",
    "name": "Venkata Jayanth Thota",
    "repository_link": "https://github.com/JayanthThota07",
    "resume_link": "https://www.linkedin.com/in/venkata-jayanth-thota-947212358/",
    "timestamp": datetime.datetime.utcnow().isoformat(timespec="milliseconds") + "Z",
}

body = json.dumps(payload, separators=(",", ":"), sort_keys=True).encode("utf-8")

signature = hmac.new(SECRET, body, hashlib.sha256).hexdigest()

headers = {
    "Content-Type": "application/json",
    "X-Signature-256": f"sha256={signature}",
}

response = requests.post(URL, data=body, headers=headers)

print("Status:", response.status_code)
print("Response:", response.text)

if response.status_code == 200:
    print("RECEIPT:", response.json()["receipt"])
