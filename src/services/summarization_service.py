from services import parser
def summarize_text(code: str, type_: str, name: str) -> str:
    """
    Handles the summarization logic.
    This is a placeholder implementation that truncates the text to 100 characters.
    Replace this with actual summarization logic as needed.
    """
    if not code:
        raise ValueError("code cannot be empty")

    # Placeholder summarization logic
    parsed_text = parser.summarize_code(code, type_, name)
    if not parsed_text:
        raise ValueError("Failed to summarize the code")
    return parsed_text