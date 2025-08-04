import os
from dotenv import load_dotenv
import chainlit as cl
from agents import Agent, Runner, set_tracing_disabled
from agents.extensions.models.litellm_model import LitellmModel

# Import your custom agents
from career_agents.career_agent import CareerAgent
from career_agents.skill_agent import SkillAgent
from career_agents.job_agent import JobAgent

# Load environment variables
load_dotenv()
set_tracing_disabled(True)


# Model setup
model = LitellmModel(
    model="gemini/gemini-2.0-flash",
    api_key=os.getenv("GEMINI_API_KEY")
)

# Define main agent
CareerMentor = Agent(
    name="Career Mentor Agent",
    instructions="""
🎓 Welcome to Career Mentor!

Let's get you on a clear path to success:

✅ Just share your field of interest — any domain! (e.g., "Frontend Development", "AI/ML", "Cybersecurity", "Medicine", "Law", "Psychology", "Business", "Design" etc)

I will then:
- Guide you step-by-step on how to become an expert in that field
- Share a detailed learning roadmap
- Highlight essential skills, tools, or educational requirements
- Suggest project ideas or practical experiences to build your portfolio
- 🚀 Provide real-world job roles aligned with that field

No repeated questions — all in one go.
Let's start! Just type your interest. 💬
""",
    model=model,
    handoffs=[CareerAgent, SkillAgent, JobAgent]
)

# CLI event: Chat start
@cl.on_chat_start
async def chat_start():
    await cl.Message(content="👋 Hi! I'm your Career Mentor. What field are you interested in?").send()

# CLI event: On user message
@cl.on_message
async def main(msg: cl.Message):
    result = await Runner.run(CareerMentor, input=msg.content)
    await cl.Message(content=result.final_output).send()
