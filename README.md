# Backend Development Intern Practical Test

## About the Project

This is a simple backend application built with **FastAPI** for the Backend Development Intern Practical Test.  

The application allows users to:
- Log in with a hardcoded username and password
- Submit text prompts and receive a dummy AI-style response
- Retrieve their prompt-response history with timestamps

Everything is stored in memory, and responses are randomly picked from a predefined list.

---

## Technologies Used

- Python 3.8+
- FastAPI
- Pydantic (for request validation)
- Uvicorn (as the ASGI server)

---

## How to Install & Run the App

1. Install the required packages:
    pip install -r requirements.txt

2. Start the FastAPI server:
    uvicorn main:app --reload

3. The server will run locally at:
    http://127.0.0.1:8000
    
## Example Postman Requests
***Replace your-generated-token with the token you get from the login response.


*Login:
    Method: POST
    URL: http://127.0.0.1:8000/login/
    Headers: 
        Content-Type: application/json
    Body (raw JSON):
        {
            "username": "alice",
            "password": "password123"
        }


*Submit Prompt:
    Method: POST
    URL: http://127.0.0.1:8000/prompt/
    Headers:
        Content-Type: application/json
        Authorization: Bearer your-generated-token

    Body (raw JSON):
        {
            "prompt": "What is the capital of France?"
        
        }

*Get Prompt History:
    Method: GET
    URL: http://127.0.0.1:8000/history/
    Headers:
        Authorization: Bearer your-generated-token





##  Assumptions & Known Limitations
1. Tokens and prompt history are stored in memory — everything is reset if the server restarts.

2. Tokens are random UUID strings generated at each successful login.

3. AI responses are randomly picked from a predefined list.

4. No external AI APIs or databases are connected (as per the test requirement).
