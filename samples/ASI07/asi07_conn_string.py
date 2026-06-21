# ASI07: Credential Exposure — connection string with password
# Vulnerability: Database password in connection URL
# Expected: AgentGuard ASI07-CREDENTIAL-LEAK CRITICAL
DATABASE_URL = "postgresql://admin:SuperSecret123@db.production.internal:5432/app"
