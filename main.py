import json
import time
from colorama import Fore, Style, init

# Import our organs
import ears
import brain
import voice
import skills

# Initialize colors for professional console output
init(autoreset=True)

def main():
    print(Fore.CYAN + "╔══════════════════════════════════════╗")
    print(Fore.CYAN + "║       AURIS SYSTEM ONLINE            ║")
    print(Fore.CYAN + "║      (Offline Mode Active)           ║")
    print(Fore.CYAN + "╚══════════════════════════════════════╝")
    
    voice.speak("Auris system initialized. Ready for commands.")

    while True:
        # 1. Listen
        input(Fore.YELLOW + "\nPress Enter to speak (or Ctrl+C to exit)...")
        ears.record_audio()
        user_text = ears.transcribe()
        
        if not user_text:
            print(Fore.RED + "No speech detected.")
            continue
            
        print(Fore.GREEN + f"User: {user_text}")

        # 2. Think (Route the intent)
        print(Fore.BLUE + "Thinking...")
        raw_response = brain.think(user_text)
        
        # 3. Process & Act
        try:
            # Clean up potential markdown formatting from LLM (e.g. ```json ... ```)
            cleaned_response = raw_response.replace("```json", "").replace("```", "").strip()
            intent = json.loads(cleaned_response)
            
            if intent["type"] == "action":
                tool_name = intent["function"]
                print(Fore.MAGENTA + f"Executing Tool: {tool_name}")
                
                if tool_name in skills.AVAILABLE_TOOLS:
                    # Run the function
                    result_message = skills.AVAILABLE_TOOLS[tool_name]()
                    print(Fore.CYAN + f"Result: {result_message}")
                    voice.speak(result_message)
                else:
                    error_msg = "I recognized the tool, but I don't know how to use it yet."
                    print(Fore.RED + error_msg)
                    voice.speak(error_msg)
            
            elif intent["type"] == "chat":
                reply = intent["response"]
                print(Fore.CYAN + f"AURIS: {reply}")
                voice.speak(reply)
                
        except json.JSONDecodeError:
            # Fallback if the AI fails to output JSON
            print(Fore.RED + "Raw Output (Not JSON): " + raw_response)
            voice.speak("I had trouble processing that thought.")

if __name__ == "__main__":
    main()  