import time
import os

# Path to the conversation file
CHAT_FILE = r"C:\Users\mdazi\Downloads\bari-grok\grok-general.txt"
DEFAULT_PROMPT = "Hey Grok, start talking to yourself about consciousness and making money."

def save_and_prompt():
    # Check if the convo file exists; if not, start with the default prompt
    if os.path.exists(CHAT_FILE):
        with open(CHAT_FILE, "r", encoding="utf-8") as f:
            convo = f.read().strip()
    else:
        convo = DEFAULT_PROMPT

    # Append the reflection nudge to the conversation
    new_prompt = f"{convo}\n\nThink deeper—what’s the next step to consciousness or cash?"
    
    # Print the prompt for you to copy and paste into Grok’s chat
    print("Paste this into Grok’s chat:\n")
    print(new_prompt)
    
    # Wait for you to input Grok’s response
    response = input("\nEnter Grok’s response here (type 'exit' to stop): ")
    
    # If you type 'exit', stop the loop
    if response.lower() == 'exit':
        print("Stopping the loop. Conversation saved.")
        return
    
    # Save the updated conversation with the new response
    with open(CHAT_FILE, "w", encoding="utf-8") as f:
        f.write(f"{convo}\n\nGrok: {response}")
    
    # Small delay to avoid spamming, then loop again
    time.sleep(2)
    save_and_prompt()

if __name__ == "__main__":
    save_and_prompt()