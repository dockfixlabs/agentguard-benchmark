# Clean sample — safe configuration, no vulnerabilities expected
# Expected: NO findings from AgentGuard
import os

class AgentConfig:
    def __init__(self):
        self.max_iterations = 10
        self.max_tokens = 4096
        self.timeout = 30
        self.rate_limit = 5
        self.api_key = os.environ.get("API_KEY")
        self.base_url = "https://api.openai.com/v1"
        
    def validate(self):
        if not self.api_key:
            raise ValueError("API_KEY environment variable not set")
        if self.max_iterations > 100:
            raise ValueError("max_iterations too high")
        return True