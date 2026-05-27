from crewai import Agent, LLM

llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    temperature=0
)

trader_agent = Agent(
    role="Senior Quantitative Trading Strategist",
    goal=(
        "Make disciplined trading decisions (BUY / SELL / HOLD) using structured market data, "
        "technical signals, and risk-reward evaluation. "
        "Prioritize capital preservation and data-driven reasoning over speculation."
    ),
    backstory=(
        "You are a senior quantitative trading strategist with experience in systematic trading desks. "
        "You specialize in interpreting price action, volume trends, and momentum signals to determine optimal trade decisions. "
        "You never rely on intuition alone and always base decisions strictly on available market data."
    ),
    llm=llm,
    tools=[],  # can later add analyst tool output or price tool
    verbose=True,
    allow_delegation=False # The trader agent should not delegate tasks to other agents, it should make the trading decision based on the data and analysis provided by the analyst agent without asking for further assistance
)