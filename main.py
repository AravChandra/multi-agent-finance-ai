import os
from dotenv import load_dotenv
from crew import stock_crew

load_dotenv()
load_dotenv(dotenv_path=".env")

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

def run(stock: str):
    try:
        result = stock_crew.kickoff(inputs={"stock": stock})
        print(result)
    except Exception as e:
        print("Crew execution failed:", str(e))

if __name__ == "__main__":
    run("APPLE")