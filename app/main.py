from fastapi import FastAPI
from app.api.v1.endpoints import items, assignments, courses

app = FastAPI(
    title="School Management - API",
    description="API for the School Management System",
    docs_url="/docs",            # Swagger UI (default)
    redoc_url="/redoc",          # ReDoc (default)
    openapi_url="/openapi.json", # OpenAPI schema URL
)

app.include_router(items.router, prefix="/items", tags=["items"])
app.include_router(assignments.router, prefix="/assignments", tags=["assignments"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])