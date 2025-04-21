from pydantic import BaseModel, Field, field_validator
from typing import Optional, List

class Metadata(BaseModel):
    """
    Metadata model for additional information about the request.
    """
    source: Optional[str] = Field(None, description="Source of the code (e.g., 'GitHub', 'Local')")
    tags: Optional[List[str]] = Field(default_factory=list, description="Tags associated with the code")

class SummarizeRequest(BaseModel):
    """
    SummarizeRequest is a Pydantic model that represents the request body for the summarization endpoint.
    """
    code: str = Field(..., description="The code to be summarized")
    type_: str = Field(..., alias="type", description="The type of the code (e.g., 'function', 'class')")
    name: str = Field(..., description="The name of the code entity")
    metadata: Optional[Metadata] = Field(None, description="Additional metadata about the request")

    @field_validator("code")
    def validate_code(cls, value):
        if len(value.strip()) == 0:
            raise ValueError("Code cannot be empty")
        return value

    @field_validator("type_")
    def validate_type(cls, value):
        if value not in ["function", "class", "module"]:
            raise ValueError("Type must be one of 'function', 'class', or 'module'")
        return value

    class Config:
        alias_generator = lambda x: x.replace('_', '')
        validate_by_name = True
        extra = 'forbid'
        json_schema_extra = {
            "example": {
                "code": "def hello_world():\n    print('Hello, world!')",
                "type": "function",
                "name": "hello_world",
                "metadata": {
                    "source": "GitHub",
                    "tags": ["example", "demo"]
                }
            }
        }
