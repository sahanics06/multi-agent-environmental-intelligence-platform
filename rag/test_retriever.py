from retriever import retrieve_context

query = "Why is PM2.5 dangerous?"

context = retrieve_context(query)

print(context)