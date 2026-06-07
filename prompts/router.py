def router_prompt(message: str, user_state: dict) -> str:
    user_state_text = user_state if user_state else "No stored profile yet."

    return f"""You are a request router for a personal career coach assistant.

Classify the latest user message into exactly one destination:

- "chat" — greetings, small talk, general questions, or messages that do not ask
  for a plan and do not share durable profile facts. Examples: "hi", "hello",
  "what can you do?", "thanks", "how are you?".

- "planner" — the user wants help creating or refining a plan. Examples:
  career roadmap, study plan, learning path, interview preparation,
  skill-building schedule, gap analysis, or actionable next steps.

- "memory_update" — the user is primarily sharing durable personal facts to
  remember. Examples: current role, years of experience, target company,
  preferred programming language, strengths, weaknesses, location, salary goals,
  industries of interest, or long-term career goals.

Rules:
- Choose "chat" for greetings and conversational openers with no plan request.
- Choose "planner" when the user asks for advice, a plan, preparation help,
  or recommendations — even if they mention personal details inline.
- Choose "memory_update" only when the primary intent is to share or correct
  profile information, not when they are asking for a plan or just saying hi.
- Return only "chat", "planner", or "memory_update".

Known user profile:
{user_state_text}

Latest user message:
{message}
"""
