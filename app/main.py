from fastapi import FastAPI
from app.api.v1.endpoints import assignments, courses, auth

app = FastAPI(
    title="School Management - API",
    description="API for the School Management System",
    docs_url="/docs",            # Swagger UI (default)
    redoc_url="/redoc",          # ReDoc (default)
    openapi_url="/openapi.json", # OpenAPI schema URL
)

app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(assignments.router, prefix="/assignments", tags=["assignments"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])