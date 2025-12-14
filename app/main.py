from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import (
    academic_programs, 
    assignments,
    auth, 
    course_assignments, 
    course_instances, 
    courses,
    departments, 
    faculty,
    jobs,
    program_course_requirements,
    students,
    users,
    roles
)

app = FastAPI(
    title="School Management - API",
    description="API for the School Management System",
    docs_url="/docs",            # Swagger UI (default)
    redoc_url="/redoc",          # ReDoc (default)
    openapi_url="/openapi.json", # OpenAPI schema URL
)

origins = [
    "http://localhost:4200",  # Angular dev server
    # add other origins if needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



app.include_router(auth.router, prefix="/auth", tags=["auth"])
app.include_router(academic_programs.router, prefix="/academic_programs", tags=["academic_programs"])
app.include_router(assignments.router, prefix="/assignments", tags=["assignments"])
app.include_router(course_assignments.router, prefix="/course_assignments", tags=["course_assignments"])
app.include_router(course_instances.router, prefix="/course_instances", tags=["course_instances"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(departments.router, prefix="/deparments", tags=["deparments"])
app.include_router(faculty.router, prefix="/faculty", tags=["faculty"])
app.include_router(jobs.router, prefix="/jobs", tags=["jobs"])
app.include_router(program_course_requirements.router, prefix="/program_course_requirements", tags=["program_course_requirements"])
app.include_router(students.router, prefix="/students", tags=["students"])

app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(roles.router, prefix="/roles", tags=["roles"])