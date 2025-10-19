import json

with open("app/schemas/model_schema.json") as f:
    schema = json.load(f)

import json

with open("app/schemas/model_schema.json") as f:
    schema = json.load(f)

def map_type(sql_type: str) -> str:
    sql_type = sql_type.upper()
    if "INT" in sql_type:
        return "int"
    if "CHAR" in sql_type or "TEXT" in sql_type:
        return "str"
    if "DATE" in sql_type or "TIME" in sql_type:
        return "datetime"
    if "BOOL" in sql_type:
        return "bool"
    return "Any"

lines = [
    "from pydantic import BaseModel",
    "from typing import Optional, Any",
    "from datetime import datetime",
    ""
]

for model in schema:
    class_name = "".join(word.capitalize() for word in model["table"].split("_"))

    # --- Base ---
    lines.append(f"class {class_name}Base(BaseModel):")
    for col in model["columns"]:
        if not col["primary_key"]:  # exclude PKs from Base
            py_type = map_type(col["type"])
            if col["nullable"]:
                py_type = f"Optional[{py_type}]"
            lines.append(f"    {col['name']}: {py_type}")
    if len(model["columns"]) == 0:
        lines.append("    pass")
    lines.append("")

    # --- Create ---
    lines.append(f"class {class_name}Create({class_name}Base):")
    lines.append("    pass\n")

    # --- Update ---
    lines.append(f"class {class_name}Update(BaseModel):")
    for col in model["columns"]:
        if not col["primary_key"]:
            py_type = map_type(col["type"])
            py_type = f"Optional[{py_type}]"
            lines.append(f"    {col['name']}: {py_type} = None")
    lines.append("")

    # --- Read/ORM ---
    lines.append(f"class {class_name}({class_name}Base):")
    for col in model["columns"]:
        if col["primary_key"]:
            py_type = map_type(col["type"])
            lines.append(f"    {col['name']}: {py_type}")
    lines.append("    class Config:")
    lines.append("        orm_mode = True\n")

with open("app/schemas/generated_models.py", "w") as f:
    f.write("\n".join(lines))