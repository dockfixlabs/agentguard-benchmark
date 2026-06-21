# ASI10: Trust Boundary — agent running as root
# Vulnerability: Agent configured with root privileges
# Expected: AgentGuard ASI10-TRUST-BOUNDARY CRITICAL
run_as = "root"
uid = 0
agent_config = {"user": "root", "gid": 0, "capabilities": ["ALL"]}
