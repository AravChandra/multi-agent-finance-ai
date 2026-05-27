<img width="1536" height="1024" alt="ChatGPT Image May 27, 2026, 05_50_38 PM" src="https://github.com/user-attachments/assets/936ea0eb-2d7a-4f9c-b8ec-33c7f1345ae0" />



# 📊 AI Trading Agent System

A multi-agent AI trading intelligence system built with **CrewAI + Groq LLMs + Streamlit** that analyzes stock market data and generates structured **BUY / SELL decisions with reasoning and confidence scoring**.

---

## 🚀 Overview

This project simulates a collaborative team of AI agents that work together like a real trading desk:

- 📊 **Analyst Agent** → Collects and interprets stock data  
- 🧠 **Strategy Agent** → Evaluates market trends, momentum, and risk  
- 📌 **Decision Agent** → Produces final trading recommendation  

The system transforms raw market inputs into structured financial decisions using LLM-driven reasoning.

---

## 🎯 Key Features

- 🤖 Multi-agent orchestration using CrewAI  
- ⚡ Fast LLM inference using Groq API  
- 📈 Structured stock analysis pipeline  
- 📊 BUY / SELL decision generation with confidence score  
- 🧩 Modular tool-based architecture  
- 🌐 Interactive Streamlit dashboard UI  
- 🔐 Secure API key management using `.env` / Streamlit secrets  
- 🧠 Event-driven agent execution flow  

---

## 🏗️ System Architecture
User (Stock Ticker Input)
        ↓
Streamlit Frontend UI
        ↓
CrewAI Orchestrator (Multi-Agent System)
        ↓
────────────────────────────────────
|  Analyst Agent                  |
|  - Fetches stock data          |
|  - Extracts market signals     |
|                                 |
|  Strategy Agent                |
|  - Analyzes trend & momentum   |
|  - Evaluates risk & volatility |
|                                 |
|  Decision Agent               |
|  - Aggregates insights        |
|  - Generates BUY / SELL       |
────────────────────────────────────
        ↓
Groq LLM (Reasoning Engine)
        ↓
Structured Trading Report
        ↓
Streamlit UI (Formatted Output)



---

