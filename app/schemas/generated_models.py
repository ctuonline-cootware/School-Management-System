from pydantic import BaseModel
from typing import Optional, Any
from datetime import datetime

class AssignmentBase(BaseModel):
    name: str
    start_date: datetime
    is_active: bool
    max_points: int
    end_date: Optional[datetime]

class AssignmentCreate(AssignmentBase):
    pass

class AssignmentUpdate(BaseModel):
    name: Optional[str] = None
    start_date: Optional[datetime] = None
    is_active: Optional[bool] = None
    max_points: Optional[int] = None
    end_date: Optional[datetime] = None

class Assignment(AssignmentBase):
    assignment_id: int
    class Config:
        orm_mode = True

class CourseBase(BaseModel):
    name: str
    start_date: datetime
    end_date: Optional[datetime]
    is_active: Optional[bool]

class CourseCreate(CourseBase):
    pass

class CourseUpdate(BaseModel):
    name: Optional[str] = None
    start_date: Optional[datetime] = None
    end_date: Optional[datetime] = None
    is_active: Optional[bool] = None

class Course(CourseBase):
    course_id: int
    class Config:
        orm_mode = True

class DepartmentBase(BaseModel):
    name: str

class DepartmentCreate(DepartmentBase):
    pass

class DepartmentUpdate(BaseModel):
    name: Optional[str] = None

class Department(DepartmentBase):
    department_id: int
    class Config:
        orm_mode = True

class JobBase(BaseModel):
    name: str
    start_date: datetime
    is_active: bool
    is_management: bool
    end_date: Optional[datetime]

class JobCreate(JobBase):
    pass

class JobUpdate(BaseModel):
    name: Optional[str] = None
    start_date: Optional[datetime] = None
    is_active: Optional[bool] = None
    is_management: Optional[bool] = None
    end_date: Optional[datetime] = None

class Job(JobBase):
    job_id: int
    class Config:
        orm_mode = True

class RolesBase(BaseModel):
    name: str

class RolesCreate(RolesBase):
    pass

class RolesUpdate(BaseModel):
    name: Optional[str] = None

class Roles(RolesBase):
    id: int
    class Config:
        orm_mode = True

class UsersBase(BaseModel):
    username: str
    password_hash: str
    is_active: Optional[bool]

class UsersCreate(UsersBase):
    pass

class UsersUpdate(BaseModel):
    username: Optional[str] = None
    password_hash: Optional[str] = None
    is_active: Optional[bool] = None

class Users(UsersBase):
    id: int
    class Config:
        orm_mode = True

class AcademicProgramBase(BaseModel):
    name: str
    department: int
    degree_type: str

class AcademicProgramCreate(AcademicProgramBase):
    pass

class AcademicProgramUpdate(BaseModel):
    name: Optional[str] = None
    department: Optional[int] = None
    degree_type: Optional[str] = None

class AcademicProgram(AcademicProgramBase):
    program_id: int
    class Config:
        orm_mode = True

class FacultyBase(BaseModel):
    first_name: str
    last_name: str
    hire_date: datetime
    department_id: int
    job_id: int
    term_date: Optional[datetime]

class FacultyCreate(FacultyBase):
    pass

class FacultyUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    hire_date: Optional[datetime] = None
    department_id: Optional[int] = None
    job_id: Optional[int] = None
    term_date: Optional[datetime] = None

class Faculty(FacultyBase):
    faculty_id: int
    class Config:
        orm_mode = True

class CourseInstanceBase(BaseModel):
    course_id: int
    faculty_id: int
    term: str
    start_date: datetime
    location: str
    end_date: Optional[datetime]

class CourseInstanceCreate(CourseInstanceBase):
    pass

class CourseInstanceUpdate(BaseModel):
    course_id: Optional[int] = None
    faculty_id: Optional[int] = None
    term: Optional[str] = None
    start_date: Optional[datetime] = None
    location: Optional[str] = None
    end_date: Optional[datetime] = None

class CourseInstance(CourseInstanceBase):
    instance_id: int
    class Config:
        orm_mode = True

class ProgramCourseRequirementBase(BaseModel):
    program_id: int
    course_id: int
    requirement_type: str
    version: str

class ProgramCourseRequirementCreate(ProgramCourseRequirementBase):
    pass

class ProgramCourseRequirementUpdate(BaseModel):
    program_id: Optional[int] = None
    course_id: Optional[int] = None
    requirement_type: Optional[str] = None
    version: Optional[str] = None

class ProgramCourseRequirement(ProgramCourseRequirementBase):
    requirement_id: int
    class Config:
        orm_mode = True

class StudentBase(BaseModel):
    first_name: str
    last_name: str
    start_date: datetime
    expected_graduation_date: datetime
    program_id: int
    end_date: Optional[datetime]

class StudentCreate(StudentBase):
    pass

class StudentUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    start_date: Optional[datetime] = None
    expected_graduation_date: Optional[datetime] = None
    program_id: Optional[int] = None
    end_date: Optional[datetime] = None

class Student(StudentBase):
    student_id: int
    class Config:
        orm_mode = True

class CourseAssignmentBase(BaseModel):
    instance_id: int
    assignment_id: int
    student_id: int
    points_earned: Optional[int]
    letter_grade: Optional[str]

class CourseAssignmentCreate(CourseAssignmentBase):
    pass

class CourseAssignmentUpdate(BaseModel):
    instance_id: Optional[int] = None
    assignment_id: Optional[int] = None
    student_id: Optional[int] = None
    points_earned: Optional[int] = None
    letter_grade: Optional[str] = None

class CourseAssignment(CourseAssignmentBase):
    course_assignment_id: int
    class Config:
        orm_mode = True
