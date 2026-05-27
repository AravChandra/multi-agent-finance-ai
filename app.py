import streamlit as st
import os
from dotenv import load_dotenv
from crew import stock_crew


# Environment setup

load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    st.error("GROQ_API_KEY not found. Please check your .env file.")
    st.stop()


# Page config

st.set_page_config(
    page_title="AI Stock Trading Assistant",
    page_icon="📊",
    layout="centered"
)


# UI Header

st.title("📊 AI Stock Trading Assistant")
st.caption("Multi-Agent system powered by CrewAI + Groq")

st.divider()


# Input section

stock = st.text_input("Enter Stock Ticker", placeholder="e.g. TSLA, AAPL, MSFT")

run_button = st.button("Analyze Stock", type="primary")


# Execution

if run_button:
    if not stock:
        st.warning("Please enter a stock ticker.")
    else:
        with st.spinner("Running multi-agent analysis..."):
            try:
                result = stock_crew.kickoff(inputs={"stock": stock})

                st.success("Analysis Complete")

                st.subheader("📌 Trading Decision Report")

                st.markdown(result)

                
                st.download_button(
                    label="Download Report",
                    data=str(result),
                    file_name=f"{stock}_analysis.txt",
                    mime="text/plain"
                )

            except Exception as e:
                st.error(f"Execution failed: {str(e)}")


st.sidebar.title("⚙️ System Info")
st.sidebar.write("CrewAI Multi-Agent Trading System")
st.sidebar.write("Agents: Analyst • Strategy • Decision")
st.sidebar.write("LLM: Groq")
st.sidebar.write("Output: Structured Trading Report")

st.sidebar.divider()

st.sidebar.write("Built for educational/demo purposes only.")