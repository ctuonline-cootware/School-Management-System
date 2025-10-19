from sqlalchemy.orm import Session
from app.models.item import Assignment, Course, Department, Job, \
                            AcademicProgram, Faculty, CourseAssignment, \
                            CourseInstance, ProgramCourseRequirement, Student
from app.schemas.item import ItemCreate, ItemUpdate

def get_item(db: Session, item_id: int):
    return db.query(ItemModel).filter(ItemModel.id == item_id).first()

def create_item(db: Session, item: ItemCreate):
    db_obj = ItemModel(title=item.title, description=item.description)
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def update_item(db: Session, item_id: int, item: ItemUpdate):
    db_obj = get_item(db, item_id)
    if not db_obj:
        return None
    if item.title is not None:
        db_obj.title = item.title
    if item.description is not None:
        db_obj.description = item.description
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_item(db: Session, item_id: int):
    db_obj = get_item(db, item_id)
    if not db_obj:
        return None
    db.delete(db_obj)
    db.commit()
    return db_obj