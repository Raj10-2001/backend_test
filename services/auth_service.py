import uuid
from datetime import datetime
import random

# Hardcoded users
users = {
    "alice": "password123",
    "bob": "secret"
}

# In-memory token and history storage
tokens = {}
history = {}

ai_responses = [
    "Interesting... Let's explore that idea.",
    "Let me think...",
    "Great question!",
    "I’m not sure about that, but let’s see.",
    "Good one!",
    "Why did the Python programmer wear glasses? Because he couldn't C!"
]

def authenticate_user(username, password):
    if username in users and users[username] == password:
        token = str(uuid.uuid4())
        tokens[token] = username
        return token
    return None

def get_username_from_token(token):
    return tokens.get(token)

def add_prompt(username, prompt):
    response = random.choice(ai_responses)
    timestamp = datetime.now().isoformat()

    if username not in history:
        history[username] = []
    history[username].append({
        "timestamp": timestamp,
        "prompt": prompt,
        "response": response
    })
    return response

def get_user_history(username):
    return history.get(username, [])
