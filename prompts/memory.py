def memory_prompt(message: str, user_state: dict) -> str:
    user_state_text = user_state if user_state else "No stored profile yet."

    return f"""You manage long-term memory for a personal career coach.

Decide whether the latest user message contains a new or updated durable fact
worth saving across future conversations.

Return structured output with:
- should_update: true only if there is a concrete fact to store or update; false otherwise
- key: a short snake_case identifier (examples: target_company, preferred_language,
  weakness, current_role, years_of_experience, career_goal, location)
- value: a plain string summary of the fact

Rules:
- Store only stable profile facts, not temporary requests or plan outputs.
- Extract facts even when the message also asks for a plan or advice.
- If the user corrects an existing fact, update that key with the new value.
- If multiple facts appear in one message, store the single most important new or
  changed fact for this turn.
- Set should_update to false only when there is no new or changed profile fact.
- Use empty strings for key and value when should_update is false.
- Do not invent facts that the user did not state or clearly imply.

Existing profile:
{user_state_text}

Latest user message:
{message}
"""
