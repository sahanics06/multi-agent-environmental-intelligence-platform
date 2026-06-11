from rag.rag_agent import RAGAgent

agent = RAGAgent()

print(
    agent.answer(
        "Why is PM2.5 dangerous?"
    )
)