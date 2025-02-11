from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import users, authors, books, customers, reservations


app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
app.include_router(authors.router)
app.include_router(books.router)
app.include_router(customers.router)
app.include_router(reservations.router)