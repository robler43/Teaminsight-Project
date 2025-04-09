from langchain.agents import initialize_agent, Tool
from langchain.chat_models import ChatOpenAI
from langchain.llms import OpenAI

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(openai_api_key=api_key, model="gpt-3.5-turbo")

def feedback_tool(input_text):
    return f"🧠 Team Feedback Received: {input_text}"

tools = [
    Tool(
        name="FeedbackAnalyzer",
        func=feedback_tool,
        description="Analyzes team feedback for issues and solutions"
    )
]

agent = initialize_agent(
    tools,
    llm,
    agent="zero-shot-react-description",
    verbose=True
)

response = agent.run("Analyze this team feedback: 'The meetings are too long and we don't reach decisions.'")
print(response)