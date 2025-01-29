from langchain_anthropic import ChatAnthropic
from browser_use import Agent
import asyncio

# Initialize the model
llm = ChatAnthropic(
    model_name="claude-3-sonnet-20240229",
    temperature=0.0,
    timeout=100, # Increase for complex tasks
)

async def main():
    agent = Agent(
        task="Find a one-way flight from Dallas, TX to Los Angelas on 12 January 2025 on Google Flights. Return me the cheapest option.",
        llm=llm,
    )
    result = await agent.run()
    print(result)

asyncio.run(main())