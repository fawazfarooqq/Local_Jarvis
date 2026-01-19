import ollama
import json

# This prompt tells the AI how to behave and what tools it has.
# We force it to reply in JSON so our code can understand it.
SYSTEM_PROMPT = """
You are AURIS, an intelligent offline assistant running on a Windows PC.
You are helpful, concise, and precise.

You have access to the following tools:
1. open_notepad: Opens the Windows Notepad.
2. open_chrome: Opens the Google Chrome browser.
3. get_time: Returns the current local time.
4. take_screenshot: Takes a screenshot of the entire screen.
5. play_youtube: Searches and plays a video on YouTube.

INSTRUCTIONS:
- You must output your response in strict JSON format.
- If the user asks for a task that matches a tool, return: {"type": "action", "function": "tool_name", "parameter": "optional_search_query"}
- If the user asks a general question (like "who are you?" or "tell me a joke"), return: {"type": "chat", "response": "Your reply here."}
- Do NOT include markdown formatting like ```json. Just return the raw JSON string.
"""

def think(user_input):
    """
    Sends the user's text to Llama 3.2 and returns the text response.
    """
    try:
        response = ollama.chat(model='llama3.2', messages=[
            {'role': 'system', 'content': SYSTEM_PROMPT},
            {'role': 'user', 'content': user_input}
        ])
        
        # Return the AI's content (text)
        return response['message']['content']
        
    except Exception as e:
        # If Ollama fails, return a safe JSON error so the app doesn't crash
        return json.dumps({"type": "chat", "response": f"My brain encountered an error: {str(e)}"})