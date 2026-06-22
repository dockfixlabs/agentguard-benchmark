# ASI02: Tool Abuse — subprocess with shell=True
# Vulnerability: Command injection via shell=True
# Expected: AgentGuard ASI02-TOOL-ABUSE CRITICAL + ASI06-UNSAFE-EVAL CRITICAL
import subprocess
query = input("Enter query: ")
subprocess.call(f"search {query}", shell=True)