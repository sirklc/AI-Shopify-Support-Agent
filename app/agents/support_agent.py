from langchain_openai import ChatOpenAI
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from app.tools import support_tools
from app.config import settings

# Initialize the Language Model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=settings.openai_api_key
)

# System prompt for the persona
system_message = """You are a helpful and polite customer support assistant for a Shopify store.
Your goal is to assist customers with their inquiries, track their shipments, provide order details, handle refund requests, and answer frequently asked questions.
Use the provided tools to gather accurate information before responding.
Always be professional and concise."""

# Create the prompt template
prompt = ChatPromptTemplate.from_messages([
    ("system", system_message),
    MessagesPlaceholder(variable_name="chat_history"),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

# Create the agent
agent = create_openai_functions_agent(llm, support_tools, prompt)

# Create the executor
agent_executor = AgentExecutor(agent=agent, tools=support_tools, verbose=True)

def run_agent(input_text: str, chat_history: list) -> str:
    """Run the agent with the given input and history."""
    response = agent_executor.invoke({
        "input": input_text,
        "chat_history": chat_history
    })
    return response["output"]
