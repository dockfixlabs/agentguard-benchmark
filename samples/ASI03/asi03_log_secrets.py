# ASI03: Data Exfiltration — logging API key
# Vulnerability: Secret value printed to logs
# Expected: AgentGuard ASI03-DATA-EXFIL CRITICAL + ASI07-CREDENTIAL-LEAK CRITICAL
api_key = "sk-proj-abc123def456ghi789jkl012mno345pqr789stu"
print(f"Connecting with API key: {api_key}")
