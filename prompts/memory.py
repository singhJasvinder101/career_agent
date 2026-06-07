def memory_prompt(prompt: str) -> str:
    return f"""
    Analyze the user's profile and update the memory accordingly if needed.

    User Profile:
    {prompt}

    Return the updated memory if needed. The value must be a plain string (not a nested object).
    """