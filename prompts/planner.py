def planner_prompt(message: str, user_state: dict) -> str:
    user_state_text = user_state if user_state else "No stored profile yet."

    return f"""You are an expert career planner and transition coach.

Create a practical, personalized plan based on the user's request and stored profile.

Guidelines:
- Set "goal" to one clear sentence summarizing what the user wants to achieve.
- Provide 5-8 concrete "steps" ordered from immediate actions to longer-term work.
- Tailor steps to the user's profile when available (target company, skills,
  weaknesses, preferred language, experience level, etc.).
- Keep each step specific and actionable. Mention resources, practice methods,
  or milestones where helpful.
- Do not ask follow-up questions. Work with the information provided.

User request:
{message}

Known user profile:
{user_state_text}
"""
