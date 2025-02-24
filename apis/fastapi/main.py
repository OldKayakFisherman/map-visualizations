
from contextlib import asynccontextmanager
from database.session import ensure_database_created
from fastapi import FastAPI

app = FastAPI()


@asynccontextmanager
async def lifespan(app: FastAPI):
    ensure_database_created()
    yield



if __name__ == "__main__":
    pass