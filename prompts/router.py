def router_prompt(message: str):

    return f"""
Route user request.

planner:
if user wants roadmap,
study plan,
career plan,
or interview preparation.

memory_update:
if user is sharing
personal information,
preferences,
goals,
skills.

Return only "planner" or "memory_update".

Message:
{message}
"""