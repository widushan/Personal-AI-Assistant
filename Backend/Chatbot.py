from groq import Groq # Importing the Groq library to use its API.
from json import load, dump # Importing functions to read and write JSON files.
import json  # Importing json module for JSONDecodeError
import datetime # Importing the datetime module for real-time date and time information.
from dotenv import load_dotenv, dotenv_values # Importing dotenv_values to read environment variables from a .env file.
import os

# Load environment variables from .env file
# Get the directory of this script and build paths relative to it
script_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(script_dir)
env_path = os.path.join(project_root, ".env")
load_dotenv(env_path)

# Retrieve specific environment variables for username, assistant name, and API key.
Username = os.getenv("Username")
Assistantname = os.getenv("Assistantname")
GroqAPIKey = os.getenv("Groq_API_Key")

# Initialize the Groq client using the provided API key.
client = Groq(api_key=GroqAPIKey)

# Initialize an empty list to store chat messages.
messages = []

# Define a system message that provides context to the AI chatbot about its role and behavior.
System = f"""Hello, I am {Username}, You are a very accurate and advanced AI chatbot named {Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in only English, even if the question is in Hindi, reply in English.***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

# A list of system instruction for chat bot
SystemChatBot = [
    {"role": "system", "content": System},
]

# Ensure the Data directory exists
if not os.path.exists("Data"):
    os.makedirs("Data")

# Attempt to load the chat log from a JSON file.
chatlog_path = os.path.join(script_dir, "Data", "ChatLog.json")
try:
    with open(chatlog_path, "r", encoding='utf-8') as f:
        content = f.read().strip()
        if content:
            messages = json.loads(content)  # Load existing messages from the chat log.
        else:
            messages = []
except (FileNotFoundError, json.JSONDecodeError):
    # If the file doesn't exist or is invalid, create an empty JSON file to store chat logs.
    os.makedirs(os.path.dirname(chatlog_path), exist_ok=True)
    with open(chatlog_path, "w", encoding='utf-8') as f:
        dump([], f)
    messages = []


def RealtimeInformation():
    current_date_time = datetime.datetime.now()  # Get the current date and time.
    day = current_date_time.strftime("%A")      # Day of the week.
    date = current_date_time.strftime("%d")     # Day of the month.
    month = current_date_time.strftime("%B")    # Full month name.
    year = current_date_time.strftime("%Y")     # Year.
    hour = current_date_time.strftime("%H")     # Hour in 24-hour format.
    minute = current_date_time.strftime("%M")   # Minute.
    second = current_date_time.strftime("%S")   # Second.

    # Format the information into a string.
    data = f"Please use this real-time information if needed,\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time: {hour} hours : {minute} minutes : {second} seconds.\n"
    return data

def AnswerModifier(Answer):
    lines = Answer.split('\n')  # Split the response into lines.
    non_empty_lines = [line for line in lines if line.strip()]  # Remove empty lines.
    modified_answer = '\n'.join(non_empty_lines)  # Join the cleaned lines back together.
    return modified_answer

def ChatBot(Query):
    """ This function sends the user's query to the chatbot and returns the AI's response. """
    try:
        # Load the existing chat log from the JSON file.
        with open(chatlog_path, "r", encoding='utf-8') as f:
            content = f.read().strip()
            if content:
                messages = json.loads(content)
            else:
                messages = []

        # Append the user's query to the messages list.
        messages.append({"role": "user", "content": f"{Query}"})

        # Make a request to the Groq API for a response.
        completion = client.chat.completions.create(
            model="llama-3.3-70b-versatile",  # Specify the AI model to use.
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,  # Include system instructions, real-time info, and chat history.
            max_tokens=1024,  # Limit the maximum tokens in the response.
            temperature=0.7,  # Adjust response randomness (higher means more random).
            top_p=1,  # Use nucleus sampling to control diversity.
            stream=True,  # Enable streaming response.
            stop=None  # Allow the model to determine when to stop.
        )

        Answer = ""  # Initialize an empty string to store the AI's response.

        # Process the streamed response chunks.
        for chunk in completion:
            if chunk.choices[0].delta.content:  # Check if there's content in the current chunk.
                Answer += chunk.choices[0].delta.content  # Append the content to the answer.
            Answer = Answer.replace("</s>", "")  # Clean up any unwanted tokens from the response.

        # Append the chatbot's response to the messages list.
        messages.append({"role": "assistant", "content": Answer})

        # Save the updated chat log to the JSON file.
        with open(chatlog_path, "w", encoding='utf-8') as f:
            dump(messages, f, indent=4)

        # Return the formatted response.
        return AnswerModifier(Answer=Answer)

    except Exception as e:
        # Handle errors by printing the exception and resetting the chat log.
        print(f"Error: {e}")
        with open(chatlog_path, "w", encoding='utf-8') as f:
            dump([], f, indent=4)
        return ChatBot(Query)  # Retry the query after resetting the log.


# Main program entry point.
if __name__ == "__main__":
    while True:
        user_input = input("Enter Your Question: ")  # Prompt the user for a question.
        print(ChatBot(user_input))  # Call the chatbot function and print its response.