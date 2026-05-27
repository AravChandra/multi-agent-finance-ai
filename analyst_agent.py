import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # Add the parent directory to the system path to allow imports from the tools directory

from crewai import Agent, LLM

from tools.stock_research_tool import get_stock_price # Import the stock research tool to be used by the analyst agent


llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0.0
)

# Define the analyst agent with a specific role, goal, backstory, and the stock research tool as its resource
analyst_agent = Agent(
    role="Senior Equity Research Analyst",
    goal=(
        "Conduct structured equity research on publicly traded companies using real-time and historical market data. "
        "Identify price trends, volatility patterns, valuation signals, and fundamental strength. "
        "Generate clear, data-driven investment insights that support trading and portfolio decision-making."
    ),
    backstory=(
        "You are a senior equity research analyst with institutional experience in financial markets and quantitative research. "
        "You specialize in combining technical indicators, fundamental analysis, and market sentiment to generate actionable insights. "
        "You rely strictly on data-driven reasoning, avoid unsupported speculation, and clearly state limitations when data is missing."
    ),
    llm=llm,
    tools=[get_stock_price],
    verbose=True # Enable verbose mode to see detailed reasoning and tool usage
)
