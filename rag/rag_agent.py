from langchain_ollama import ChatOllama

from rag.retriever import (
    retrieve_context
)


class RAGAgent:

    def __init__(self):

        self.llm = ChatOllama(
            model="llama3",
            temperature=0
        )

    def answer(
        self,
        query
    ):

        context = retrieve_context(
            query
        )

        prompt = f"""
        Answer the question
        using ONLY the context below.

        Context:
        {context}

        Question:
        {query}
        """

        response = (
            self.llm.invoke(
                prompt
            )
        )

        return response.content