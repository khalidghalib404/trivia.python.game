import random
import time
import sys

COLORS = {
    'purple': '\033[95m',
    'cyan': '\033[96m',
    'blue': '\033[94m',
    'green': '\033[92m',
    'yellow': '\033[93m',
    'red': '\033[91m',
    'reset': '\033[0m',
    'bold': '\033[1m'
}

MAGIC_SYMBOLS = ["✨", "🔮", "⭐", "🌙", "☄️", "🌟", "⚡", "🍀"]

def print_magic(text, color='cyan', delay=0.03):
    for char in text:
        print(f"{COLORS[color]}{char}{COLORS['reset']}", end='', flush=True)
        time.sleep(delay)
    print()

def print_fortune(fortune, category):
    colors = ['purple', 'blue', 'green', 'yellow', 'red']
    print(f"\n{COLORS['bold']}{'='*50}{COLORS['reset']}")
    print(f"{COLORS[colors[hash(category) % len(colors)]]}🔮 {category.upper()} FORTUNE 🔮{COLORS['reset']}")
    print(f"{COLORS['bold']}{'='*50}{COLORS['reset']}\n")
    
    lines = fortune.split('. ')
    for line in lines:
        symbol = random.choice(MAGIC_SYMBOLS)
        print_magic(f"  {symbol} {line.strip()}", 'yellow', 0.02)
        time.sleep(0.3)

def get_user_mood():
    print_magic("\n✨ How are you feeling today? ✨\n", 'purple')
    moods = {
        '1': 'happy', '2': 'curious', '3': 'adventurous', 
        '4': 'contemplative', '5': 'mysterious'
    }
    for key, mood in moods.items():
        print(f"  {key}. {mood.title()}")
    
    choice = input("\nEnter choice (1-5): ").strip()
    return moods.get(choice, random.choice(list(moods.values())))

def calculate_lucky_number(name):
    return sum(ord(c) for c in name) % 99 + 1

def main():
    print("\n" + "="*50)
    print_magic("    🔮 THE COOL FORTUNE TELLER 🔮", 'purple')
    print("="*50 + "\n")
    
    name = input("What's your name, seeker? ").strip()
    if not name:
        name = "Mystic Soul"
    
    mood = get_user_mood()
    lucky_num = calculate_lucky_number(name)
    
    print_magic(f"\n✨ Welcome, {name}! Your vibe is {mood} today...", 'cyan')
    print_magic(f"🍀 Your lucky number: {lucky_num}", 'green')
    
    fortunes = {
        'happy': [
            f"{name}, joy follows you like sunshine. Expect wonderful news soon!",
            f"Your smile lights up rooms. Someone special will notice today!",
            f"Laughter is your superpower. Use it wisely, amazing things await!"
        ],
        'curious': [
            f"The universe whispers secrets to the curious. Listen carefully, answers come!",
            f"Your questions lead to treasure. Keep exploring, {name}!",
            f"Curiosity didn't kill the cat - it gave it nine lives. Yours multiplies!"
        ],
        'adventurous': [
            f"Adventure calls your name! Pack your bags, destiny awaits!",
            f"The road less traveled chooses you today. Be bold!",
            f"Your courage opens doors. Something epic begins this week!"
        ],
        'contemplative': [
            f"Deep thoughts bring deep rewards. Your reflection shapes reality.",
            f"Wisdom grows in quiet moments. Trust your inner voice, {name}.",
            f"The answers you seek already live within you. Meditate and find them."
        ],
        'mysterious': [
            f"The shadows hold secrets for you, {name}. Something hidden comes to light.",
            f"Not all who wander are lost - you're exactly where magic happens.",
            f"The cosmos aligns in your favor. Expect the unexpected!"
        ]
    }
    
    time.sleep(1)
    print(COLORS['cyan'] + "\n🔮 Channeling cosmic energy" + COLORS['reset'], end='')
    for _ in range(3):
        time.sleep(0.5)
        print(COLORS['cyan'] + "." + COLORS['reset'], end='', flush=True)
    print()
    
    fortune = random.choice(fortunes[mood])
    print_fortune(fortune, mood)
    
    print_magic(f"\n🌟 May the odds be ever in your favor, {name}! 🌟", 'purple')
    print_magic("\n🎯 Come back tomorrow for another fortune!\n", 'green')

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n{COLORS['red']}🔮 Fortune telling interrupted... until next time!{COLORS['reset']}")
        sys.exit(0)