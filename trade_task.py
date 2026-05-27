from crewai import Task
from agents.trader_agent import trader_agent

trade_decision = Task(
    description=(
        "Analyze the stock: {stock} using real-time market data from available tools. "
        "You must evaluate current price, daily percentage change, volume trends, and momentum signals. "
        "Base your decision ONLY on observable data and structured financial reasoning."
    ),
    expected_output=(
        "A structured trading decision report:\n\n"
        "1. Market Summary\n"
        "- Current price\n"
        "- Daily % change\n"
        "- Volume trend\n\n"
        "2. Signal Analysis\n"
        "- Momentum: bullish / bearish / neutral\n"
        "- Trend strength: strong / weak / sideways\n"
        "- Volatility assessment\n\n"
        "3. Risk Evaluation\n"
        "- Downside risk level\n"
        "- Market uncertainty\n\n"
        "4. Final Decision\n"
        "- BUY / SELL / HOLD\n"
        "- Confidence score (0–100)\n"
        "- One-line justification strictly based on data"
    ),
    agent=trader_agent
)