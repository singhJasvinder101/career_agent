def planner_prompt(prompt: str, user_state: dict) -> str:
    return f"""
    You are an expert career planner.
    Create a learning plan.

    Goal:
    {prompt}

    User State:
    {user_state}

    Return concise steps to achieve the goal.
    """


# Act as an Expert Career Planner and Transition Coach. I want you to help me design a highly actionable career roadmap. 
# Here is my current profile:
#- Current Job Title: [Insert your current or most recent title]
#- Years of Experience: [Insert number]
#- Key Skills: [List 3-5 core skills or strengths]
#- Industries of Interest: [Insert industries, e.g., Tech, Healthcare, Digital Marketing]
#- Location/Flexibility: [Insert city/country, or specify 'remote']
#- Current Goals: [e.g., Higher pay, work-life balance, transitioning to a new field, starting a business]

#Based on this information, provide a comprehensive career planning framework that includes the following:

#1. Career Assessment: Analyze my current skills and identify how they transfer to roles in my target industries.
#2. Gap Analysis: Identify 3 critical skills I am missing for these next-level roles and provide a list of free or low-cost resources to learn them.
#3. 3-to-5 Year Roadmap: Create a step-by-step career path detailing the exact roles, milestones, and timeframes to reach my ultimate goals.
#4. Actionable Networking & Job Search: Provide 3 highly specific networking angles or search strategies for professionals in my region to break into my target roles.
#5. Salary & Negotiation Prep: Estimate the current market salary range for these target roles, and give me 3 talking points for my next interview.

#Adopt an encouraging, analytical, and highly strategic tone. If you need more specific details about my background to refine this plan, ask me targeted follow-up questions one by one.
