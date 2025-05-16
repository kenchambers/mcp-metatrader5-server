"""
Utility functions and classes for MT5 MCP Server
"""

class UserMessage:
    """Message from a user in a prompt."""
    
    def __init__(self, content):
        self.role = "user"
        self.content = content
    
    def __repr__(self):
        return f"UserMessage(content={self.content!r})"
    
    def to_dict(self):
        return {"role": self.role, "content": self.content}


class AssistantMessage:
    """Message from an assistant in a prompt."""
    
    def __init__(self, content):
        self.role = "assistant"
        self.content = content
    
    def __repr__(self):
        return f"AssistantMessage(content={self.content!r})"
    
    def to_dict(self):
        return {"role": self.role, "content": self.content}