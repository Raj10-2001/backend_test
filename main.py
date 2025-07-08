from fastapi import FastAPI
from routes import auth_routes, prompt_routes

app = FastAPI()


app.include_router(auth_routes.router)
app.include_router(prompt_routes.router)
