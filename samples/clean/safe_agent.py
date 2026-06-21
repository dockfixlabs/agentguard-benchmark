# Clean sample — safe agent code, no vulnerabilities expected
# Expected: NO findings from AgentGuard
from pathlib import Path
import os

def get_config(key, default=None):
    return os.environ.get(key, default)

def process_data(data):
    result = []
    for item in data:
        if isinstance(item, dict) and "value" in item:
            result.append(item["value"])
    return result

class SafeAgent:
    def __init__(self):
        self.api_key = get_config("API_KEY")
        self.base_url = "https://api.openai.com/v1"
        self.max_tokens = 1000

    def run(self, query):
        if not self.api_key:
            raise ValueError("API_KEY not set")
        if len(query) > self.max_tokens:
            query = query[:self.max_tokens]
        return query
