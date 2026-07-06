import random

def magic_8ball():
    responses = [
        "It is certain ✨", "Without a doubt 🌟", "You may rely on it 💫",
        "Definitely yes 🔥", "As I see it, yes ☀️", "Most likely 💎",
        "Outlook good 🎯", "Yes 🎉", "Signs point to yes 🌈",
        "Reply hazy, try again 🤔", "Ask again later ⏳", "Better not tell you now 🤫",
        "Cannot predict now 🌀", "Don't count on it 💔", "My reply is no 🚫",
        "No ❌", "Very doubtful 😔", "Not in your favor. 🎲"
    ]
    
    print("\n" + "="*45)
    print("    🎱MAGIC 8-BALL🎱")
    print("="*40)
    
    while True:
        question = input("\n❓ Ask a yes/no question (or 'quit' to exit): ").strip()
        if question.lower() in ['quit', 'exit', 'q']:
            print("🔮 Goodbye!")
            break
        if question:
            print("\n🌀 Shaking...", end="")
            for _ in range(4):
                print(".", end="", flush=True)
                import time; time.sleep(0.3)
            print()
            print(f"\n💬 {random.choice(responses)}\n")

if __name__ == "__main__":
    magic_8ball()