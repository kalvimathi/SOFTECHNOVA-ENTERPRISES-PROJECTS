from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="E-Learning Platform Backend",
    description="API for managing users, courses, and content delivery.",
    version="1.0.0"
)

# Allow CORS (useful for frontend interaction)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Replace "*" with frontend domain in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root route
@app.get("/")
def read_root():
    return {"message": "Welcome to the e-learning backend!"}

# Sample route for course list
@app.get("/courses")
def get_courses():
    return [
        {"id": 1, "title": "Python Basics", "instructor": "Alice"},
        {"id": 2, "title": "Web Development", "instructor": "Bob"}
    ]
