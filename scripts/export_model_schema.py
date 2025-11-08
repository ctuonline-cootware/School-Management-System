import sys
import os
import importlib
import json
from sqlalchemy.inspection import inspect

# Add project root to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


# Dynamically import all model files from app.models
model_dir = "app.models"
model_path = os.path.join(os.path.dirname(__file__), "..", "app", "models")

for filename in os.listdir(model_path):
    if filename.endswith(".py") and filename != "__init__.py":
        module_name = f"{model_dir}.{filename[:-3]}"
        importlib.import_module(module_name)


from app.models.sqlalchemy_models import Base, Assignment, Course, Department, Job, \
                            AcademicProgram, Faculty, CourseAssignment, \
                            CourseInstance, ProgramCourseRequirement, Student


def model_to_dict(model):
    mapper = inspect(model)
    return {
        "table": model.__tablename__,
        "columns": [
            {
                "name": column.key,
                "type": str(column.type),
                "nullable": column.nullable,
                "primary_key": column.primary_key,
                "default": str(column.default.arg) if column.default else None
            }
            for column in mapper.columns
        ]
    }

models = Base.__subclasses__()
schema = [model_to_dict(m) for m in models]

with open("app\\schemas\\model_schema.json", "w") as f:
    json.dump(schema, f, indent=2)