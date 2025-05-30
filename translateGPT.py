from openai import OpenAI

client=OpenAI()

def main():
    prompt=""
    print("開始對話，輸入 'exit' 以退出。\n")

    with open("prompt.txt", "r", encoding="utf-8") as f:
        instructions=f.read()

    while True:
        user_input=input("你: ").strip()
        if user_input.lower() in ("exit"):
            print("結束對話。")
            break

        prompt+=f"User: {user_input}\nAssistant: "

        try:
            response=client.responses.create(
                model="gpt-4.1-mini",
                instructions=instructions,
                input=prompt
            )
        except Exception as e:
            print(f"錯誤: {e}")
            continue

        reply=response.output_text

        print(f"\nGPT: {reply}\n")
        prompt+=f"{reply}\n"

        with open("chat_history.txt", "w", encoding="utf-8") as f:
            f.write(prompt)

if __name__ == "__main__":
    main()
