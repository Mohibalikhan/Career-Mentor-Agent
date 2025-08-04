# career_agents/job_agent.py

import os
from dotenv import load_dotenv
from agents import Agent
from agents.extensions.models.litellm_model import LitellmModel

# Load environment variables
load_dotenv()

# Model setup
model = LitellmModel(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Define JobAgent
JobAgent = Agent(
    name="Job Role Explorer",
    instructions="""
💼 You are a job role expert.

Based on the user’s chosen field, you will:
- List 5–10 real-world job titles related to that field
- Give a short description of each role
- Mention average salaries if possible
- Suggest career growth paths (e.g., Junior → Senior → Lead)

Keep it concise but informative.
""",
    model=model
)
