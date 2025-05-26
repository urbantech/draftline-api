from typing import Optional, Union
from pydantic import BaseModel, Field

class Token(BaseModel):
    """Token schema for authentication response.
    
    Attributes:
        access_token: JWT token for authentication
        token_type: Token type (bearer)
    """
    access_token: str
    token_type: str

class TokenPayload(BaseModel):
    """Token payload schema for JWT token content.
    
    Attributes:
        sub: Subject identifier, typically the user ID
    """
    sub: Optional[Union[str, int]] = Field(default=None, description="Subject identifier")
