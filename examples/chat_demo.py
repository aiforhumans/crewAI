import os
from crewai import Agent, LLM


def main():
    llm = LLM(
        model=os.getenv("OPENAI_MODEL_NAME", "openai/your-model"),
        api_key=os.getenv("OPENAI_API_KEY", "lmstudio"),
        base_url=os.getenv("OPENAI_API_BASE", "http://localhost:1234/v1"),
    )

    assistant = Agent(
        role="Local Chat Assistant",
        goal="Answer user questions",
        backstory="Runs locally using LM Studio",
        llm=llm,
    )

    messages = []
    print("Start chatting with the local model. Type 'exit' to quit.")
    while True:
        user = input("You: ")
        if user.lower() in {"exit", "quit"}:
            break
        messages.append({"role": "user", "content": user})
        reply = assistant.llm.call(messages=messages)
        messages.append({"role": "assistant", "content": reply})
        print(f"Assistant: {reply}\n")


if __name__ == "__main__":
    main()
