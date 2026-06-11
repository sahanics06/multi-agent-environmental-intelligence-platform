# 🌍 Multi-Agent Environmental Intelligence Platform

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-AI-green)
![Ollama](https://img.shields.io/badge/Ollama-Llama3-orange)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)

An AI-powered environmental monitoring platform that combines Multi-Agent Systems, Retrieval-Augmented Generation (RAG), Time-Series Forecasting, and Local LLMs to provide intelligent air-quality insights, health recommendations, and pollution forecasts.

## 🚀 Features

### Real-Time AQI Monitoring

* Fetches real-time air quality data for multiple cities.
* Tracks PM2.5, PM10, NO₂, O₃, CO, and other pollutants.
* Displays air quality categories and pollution insights.

### Conversational AI Assistant

* Natural language chat interface built with Streamlit.
* Powered by Ollama and Llama 3.
* Supports contextual conversations and follow-up questions.

### AQI Forecasting

* Time-series forecasting using Facebook Prophet.
* Predicts future PM2.5 levels.
* Provides pollution trend analysis and forecast-based recommendations.

### Health Advisory Agent

* Generates personalized environmental health guidance.
* Supports user profiles such as:

  * Children
  * Elderly individuals
  * Asthma patients
  * General public

### Multi-Agent Architecture

* Supervisor Agent orchestrates specialized agents.
* Forecast Agent handles pollution prediction.
* Health Agent provides medical and activity guidance.
* Modular architecture for future agent expansion.

### RAG Knowledge Base

* ChromaDB vector database.
* Sentence Transformer embeddings.
* Domain-specific environmental knowledge retrieval.
* Reduces hallucinations and improves factual accuracy.

---

## 🏗️ System Architecture

User Query
↓
Supervisor Agent
↓
├── AQI Agent
├── Forecast Agent
├── Health Agent
└── RAG Agent
↓
Ollama (Llama 3)
↓
Response

---

## 🛠️ Technology Stack

### AI / LLM

* Ollama
* Llama 3
* LangChain

### Multi-Agent Framework

* Custom Supervisor Agent Architecture
* LangChain Components

### RAG

* ChromaDB
* Sentence Transformers
* HuggingFace Embeddings

### Forecasting

* Prophet
* Pandas
* NumPy

### Frontend

* Streamlit

### Data Processing

* Pandas
* NumPy

### Version Control

* Git
* GitHub

---

## 📁 Project Structure

multi-agent-environmental-intelligence-platform/
│
├── agents/
│   ├── aqi_agent.py
│   ├── health_agent.py
│   ├── forecast_agent.py
│   └── supervisor_agent.py
│
├── forecasting/
│   ├── data_collector.py
│   ├── prophet_model.py
│   └── forecast_tool.py
│
├── rag/
│   ├── ingest.py
│   ├── rag_agent.py
│   ├── retriever.py
│   └── test_rag.py
│
├── knowledge/
│   └── environmental_knowledge.txt
│
├── tools/
│   └── aqi_tool.py
│
├── utils/
│   ├── constants.py
│   └── intents.py
│
├── app/
│   └── streamlit_app.py
│
├── requirements.txt
└── README.md

---

## ⚙️ Installation

### Clone Repository

git clone https://github.com/sahanics06/multi-agent-environmental-intelligence-platform.git
cd multi-agent-environmental-intelligence-platform

### Create Virtual Environment

python -m venv ai

### Activate Environment

Windows:

ai\Scripts\activate

### Install Dependencies

pip install -r requirements.txt

### Start Ollama

ollama run llama3

### Launch Application

streamlit run app/streamlit_app.py

---

## 💬 Example Queries

* What is the AQI in Pune?
* Is it safe for a child to play outside in Pune?
* Will pollution increase next week in Delhi?
* Give health advice for asthma patients in Mumbai.
* Why is PM2.5 harmful?

---

## 📈 Project Versions

| Version | Description                |
| ------- | -------------------------- |
| v0.5    | AQI Agent with Chat UI     |
| v0.6    | AQI Forecasting Foundation |
| v0.7    | Forecast Dashboard         |
| v0.8    | Forecast-Aware AI Agent    |
| v0.9    | Health Advisory Agent      |
| v1.0    | Multi-Agent Orchestration  |
| v1.1    | RAG Knowledge Base         |

---

## 🎯 Future Enhancements

* Agent Memory using LangGraph
* Multi-City Forecast Comparison
* Weather + AQI Correlation
* API Deployment
* Docker Support
* Cloud Deployment (AWS/Azure/GCP)
* Advanced RAG Pipeline
* Real-Time Monitoring Dashboard

---

## 👨‍💻 Author

Manish Sahani

GitHub: https://github.com/sahanics06

