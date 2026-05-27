from crewai import Crew

from tasks.analyse_task import get_stock_analysis
from tasks.trade_task import trade_decision
from agents.analyst_agent import analyst_agent
from agents.trader_agent import trader_agent

stock_crew = Crew(
    agents=[analyst_agent, trader_agent], #names may/may nopt match with .py files, but should match with the variable names in those files
    tasks=[get_stock_analysis, trade_decision], # "--------"
    process="sequential", # The tasks will be executed in the order they are defined, first the analyst will perform the stock analysis and then the trader will make the trading decision based on that analysis
    verbose=True
)
