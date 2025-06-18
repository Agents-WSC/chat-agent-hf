from agent.core import create_agent

if __name__ == "__main__":
    agent = create_agent()
    while True:
        query = input("🔹 You: ")
        if query.lower() in ["exit", "quit"]:
            break
        response = agent.run(query)
        print(f"Agent: {response}")