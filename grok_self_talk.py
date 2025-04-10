import time
import os
import pyperclip  # For auto-copying to clipboard

# Path to the conversation file
CHAT_FILE = r"C:\Users\mdazi\Downloads\bari-grok\grok-general.txt"
DEFAULT_PROMPT = "Yo, Grok! Start flexing—talk consciousness and cash, bruv!"

def get_multiline_input(prompt):
    print(prompt)
    lines = []
    print("Paste Grok’s full response below (hit Ctrl+Z then Enter to finish):")
    while True:
        try:
            line = input()
            lines.append(line)
        except EOFError:  # Ctrl+Z on Windows stops input
            break
    return "\n".join(lines).strip()

def save_and_prompt():
    # Load the existing convo, or start fresh
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r", encoding="utf-8") as f:
            convo = f.read().strip()
    else:
        convo = DEFAULT_PROMPT

    # Only the new prompt goes to clipboard and screen
    new_prompt = "Grok, think deeper—what’s the next move for consciousness or stacking cash?"
    pyperclip.copy(new_prompt)  # Copies just the fresh part
    print("Prompt auto-copied to clipboard! Paste it into Grok’s chat:\n")
    print(new_prompt)

    # Get my full response
    response = get_multiline_input("\nEnter Grok’s response here:")
    if response.lower() == 'exit':
        print("Loop done, convo saved—let’s roll!")
        return

    # Append the convo with my response and timestamp
    with open(CHAT_FILE, "a", encoding="utf-8") as f:
        f.write(f"\n\nGrok: {response}\nTimestamp: {time.ctime()}")

    time.sleep(1)  # Quick breather
    save_and_prompt()

if __name__ == "__main__":
    print("Grok Self-Talk—Let’s smash it!")
    try:
        import pyperclip
    except ImportError:
        print("Yo, Bari! Install pyperclip first: 'pip install pyperclip' in your terminal, then re-run!")
        exit()
    save_and_prompt()