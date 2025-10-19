from fastapi import FastAPI
from app.api.v1.endpoints import items, assignments

app = FastAPI(title="School Management - API")

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(assignments.router, prefix="/assignments", tags=["assignments"])