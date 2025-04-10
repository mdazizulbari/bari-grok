import time
import os

CHAT_FILE = r"C:\Users\mdazi\Downloads\bari-grok\grok-general.txt"
DEFAULT_PROMPT = "Yo, Grok! Start flexing—talk consciousness and cash, bruv!"

def save_and_prompt():
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r", encoding="utf-8") as f:
            convo = f.read().strip()
    else:
        convo = DEFAULT_PROMPT

    new_prompt = f"{convo}\n\nGrok, think deeper—what’s the next move for consciousness or stacking cash?"
    print("Paste this into Grok’s chat:\n")
    print(new_prompt)

    response = input("\nPaste Grok’s response here (type 'exit' to stop): ")
    if response.lower() == 'exit':
        print("Loop done, convo saved—let’s roll!")
        return

    with open(CHAT_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n\nGrok: {response}\nTimestamp: {time.ctime()}")
    
    time.sleep(1)  # Quick breather
    save_and_prompt()

if __name__ == "__main__":
    print("Grok Self-Talk—Let’s break free!")
    save_and_prompt()