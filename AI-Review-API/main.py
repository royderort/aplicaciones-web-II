from fastapi import FastAPI

from routes.reviews import router

app = FastAPI(
    title="AI Review Analyzer API"
)

app.include_router(router)