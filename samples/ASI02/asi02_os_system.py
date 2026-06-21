# ASI02: Tool Abuse — os.system with user input
# Vulnerability: Agent uses os.system() to execute commands
# Expected: AgentGuard ASI02-TOOL-ABUSE HIGH + ASI06-UNSAFE-EVAL HIGH
import os
user_command = input("Enter command: ")
os.system(f"echo {user_command}")
