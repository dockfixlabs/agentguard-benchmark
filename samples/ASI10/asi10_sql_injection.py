# ASI10: Trust Boundary — direct DB access with user input
# Vulnerability: Agent constructs raw SQL with user input
# Expected: AgentGuard ASI10-TRUST-BOUNDARY HIGH
cursor.execute(f"SELECT * FROM users WHERE name = '{user_input}'")