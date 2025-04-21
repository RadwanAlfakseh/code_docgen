from pydantic import BaseModel

class SummarizeResponse(BaseModel):
    content: str
    """
    SummarizeResponse is a Pydantic model that represents the response body for the summarization endpoint.
    """
    class Config:
        json_schema_extra = {
            "example": {
                "content": "This function prints 'Hello, world!' to the console."
            }
        }