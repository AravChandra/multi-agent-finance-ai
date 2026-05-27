from crewai import Task
from agents.analyst_agent import analyst_agent # Import the analyst agent to be assigned the stock analysis task


get_stock_analysis = Task(
    description=(
        "Perform a real-time equity analysis for the stock: {stock}. " #{stock} will be dynamically replaced with the specific stock symbol when the task is executed
        "Use the available stock price tool to retrieve live market data including current price, "
        "daily open, high, low, volume, and percentage change. "
        "Analyze the stock's intraday performance and identify short-term trends, volatility, and momentum signals."
    ),
    expected_output=(
        "A structured market analysis report with the following sections:\n\n"
        "1. Current Market Snapshot\n"
        "- Current price\n"
        "- Daily high/low\n"
        "- Volume\n\n"
        "2. Performance Summary\n"
        "- Absolute and percentage change\n"
        "- Intraday trend (bullish/bearish/sideways)\n\n"
        "3. Market Insights\n"
        "- Volatility assessment\n"
        "- Notable price movements\n"
        "- Any abnormal activity or signals\n\n"
        "4. Final Observation\n"
        "- One-sentence interpretation of current market behavior"
    ),
    agent=analyst_agent
)
