from typing import Optional
import datetime

from sqlalchemy import (
    Boolean,
    Column,
    Date,
    ForeignKey,
    ForeignKeyConstraint,
    Integer,
    PrimaryKeyConstraint,
    String,
    Table,
    Text,
    UniqueConstraint,
    text,
)
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Assignment(Base):
    __tablename__ = "assignment"
    __table_args__ = (
        PrimaryKeyConstraint("assignment_id", name="assignment_pkey"),
    )

    assignment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    max_points: Mapped[int] = mapped_column(Integer, nullable=False)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    course_assignment: Mapped[list["CourseAssignment"]] = relationship(
        "CourseAssignment", back_populates="assignment"
    )


class Course(Base):
    __tablename__ = "course"
    __table_args__ = (
        PrimaryKeyConstraint("course_id", name="course_pkey"),
    )

    course_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean)
    code: Mapped[str] = mapped_column(String(20), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=False)
    credits: Mapped[float] = mapped_column(Integer, nullable=False)

    course_instance: Mapped[list["CourseInstance"]] = relationship(
        "CourseInstance", back_populates="course"
    )
    program_course_requirement: Mapped[list["ProgramCourseRequirement"]] = relationship(
        "ProgramCourseRequirement", back_populates="course"
    )


class Department(Base):
    __tablename__ = "department"
    __table_args__ = (
        PrimaryKeyConstraint("department_id", name="department_pkey"),
    )

    department_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    academic_program: Mapped[list["AcademicProgram"]] = relationship(
        "AcademicProgram", back_populates="department_"
    )
    faculty: Mapped[list["Faculty"]] = relationship("Faculty", back_populates="department")


class Job(Base):
    __tablename__ = "job"
    __table_args__ = (
        PrimaryKeyConstraint("job_id", name="job_pkey"),
    )

    job_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_management: Mapped[bool] = mapped_column(Boolean, nullable=False)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    faculty: Mapped[list["Faculty"]] = relationship("Faculty", back_populates="job")


class Roles(Base):
    __tablename__ = "roles"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="roles_pkey"),
        UniqueConstraint("name", name="roles_name_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)

    user: Mapped[list["Users"]] = relationship(
        "Users", secondary="user_roles", back_populates="role"
    )


class Users(Base):
    __tablename__ = "users"
    __table_args__ = (
        PrimaryKeyConstraint("id", name="users_pkey"),
        UniqueConstraint("username", name="users_username_key"),
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(Text, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text("true"))

    role: Mapped[list["Roles"]] = relationship(
        "Roles", secondary="user_roles", back_populates="user"
    )


class AcademicProgram(Base):
    __tablename__ = "academic_program"
    __table_args__ = (
        ForeignKeyConstraint(
            ["department"],
            ["department.department_id"],
            name="academic_program_department_fkey",
        ),
        PrimaryKeyConstraint("program_id", name="academic_program_pkey"),
    )

    program_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    department: Mapped[int] = mapped_column(Integer, nullable=False)
    degree_type: Mapped[str] = mapped_column(String(20), nullable=False)

    department_: Mapped["Department"] = relationship(
        "Department", back_populates="academic_program"
    )
    program_course_requirement: Mapped[list["ProgramCourseRequirement"]] = relationship(
        "ProgramCourseRequirement", back_populates="program"
    )
    student: Mapped[list["Student"]] = relationship("Student", back_populates="program")


class Faculty(Base):
    __tablename__ = "faculty"
    __table_args__ = (
        ForeignKeyConstraint(
            ["department_id"],
            ["department.department_id"],
            name="faculty_department_id_fkey",
        ),
        ForeignKeyConstraint(["job_id"], ["job.job_id"], name="faculty_job_id_fkey"),
        PrimaryKeyConstraint("faculty_id", name="faculty_pkey"),
    )

    faculty_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    hire_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, nullable=False)
    job_id: Mapped[int] = mapped_column(Integer, nullable=False)
    term_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    email_address: Mapped[Optional[str]] = mapped_column(String(100))

    department: Mapped["Department"] = relationship("Department", back_populates="faculty")
    job: Mapped["Job"] = relationship("Job", back_populates="faculty")
    course_instance: Mapped[list["CourseInstance"]] = relationship(
        "CourseInstance", back_populates="faculty"
    )


t_user_roles = Table(
    "user_roles",
    Base.metadata,
    Column("user_id", Integer, primary_key=True),
    Column("role_id", Integer, primary_key=True),
    ForeignKeyConstraint(["role_id"], ["roles.id"], name="user_roles_role_id_fkey"),
    ForeignKeyConstraint(["user_id"], ["users.id"], name="user_roles_user_id_fkey"),
    PrimaryKeyConstraint("user_id", "role_id", name="user_roles_pkey"),
)


course_instance_student = Table(
    "course_instance_student",
    Base.metadata,
    Column("instance_id", Integer, ForeignKey("course_instance.instance_id"), primary_key=True),
    Column("student_id", Integer, ForeignKey("student.student_id"), primary_key=True),
)


class CourseInstance(Base):
    __tablename__ = "course_instance"
    __table_args__ = (
        ForeignKeyConstraint(
            ["course_id"], ["course.course_id"], name="course_instance_course_id_fkey"
        ),
        ForeignKeyConstraint(
            ["faculty_id"], ["faculty.faculty_id"], name="course_instance_faculty_id_fkey"
        ),
        PrimaryKeyConstraint("instance_id", name="course_instance_pkey"),
    )

    instance_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    course_id: Mapped[int] = mapped_column(Integer, nullable=False)
    faculty_id: Mapped[int] = mapped_column(Integer, nullable=False)
    term: Mapped[str] = mapped_column(String(20), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    course: Mapped["Course"] = relationship("Course", back_populates="course_instance")
    faculty: Mapped["Faculty"] = relationship("Faculty", back_populates="course_instance")
    course_assignment: Mapped[list["CourseAssignment"]] = relationship(
        "CourseAssignment", back_populates="instance"
    )

    students: Mapped[list["Student"]] = relationship(
        "Student",
        secondary=course_instance_student,
        back_populates="course_instances",
    )


class ProgramCourseRequirement(Base):
    __tablename__ = "program_course_requirement"
    __table_args__ = (
        ForeignKeyConstraint(
            ["course_id"],
            ["course.course_id"],
            name="program_course_requirement_course_id_fkey",
        ),
        ForeignKeyConstraint(
            ["program_id"],
            ["academic_program.program_id"],
            name="program_course_requirement_program_id_fkey",
        ),
        PrimaryKeyConstraint("requirement_id", name="program_course_requirement_pkey"),
    )

    requirement_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    program_id: Mapped[int] = mapped_column(Integer, nullable=False)
    course_id: Mapped[int] = mapped_column(Integer, nullable=False)
    requirement_type: Mapped[str] = mapped_column(String(50), nullable=False)
    version: Mapped[str] = mapped_column(String(20), nullable=False)

    course: Mapped["Course"] = relationship(
        "Course", back_populates="program_course_requirement"
    )
    program: Mapped["AcademicProgram"] = relationship(
        "AcademicProgram", back_populates="program_course_requirement"
    )


class Student(Base):
    __tablename__ = "student"
    __table_args__ = (
        ForeignKeyConstraint(
            ["program_id"],
            ["academic_program.program_id"],
            name="student_program_id_fkey",
        ),
        PrimaryKeyConstraint("student_id", name="student_pkey"),
    )

    student_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    expected_graduation_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    program_id: Mapped[int] = mapped_column(Integer, nullable=False)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    email_address: Mapped[Optional[str]] = mapped_column(String(100))

    program: Mapped["AcademicProgram"] = relationship("AcademicProgram", back_populates="student")
    course_assignment: Mapped[list["CourseAssignment"]] = relationship(
        "CourseAssignment", back_populates="student"
    )

    course_instances: Mapped[list["CourseInstance"]] = relationship(
        "CourseInstance",
        secondary=course_instance_student,
        back_populates="students",
    )


class CourseAssignment(Base):
    __tablename__ = "course_assignment"
    __table_args__ = (
        ForeignKeyConstraint(
            ["assignment_id"],
            ["assignment.assignment_id"],
            name="course_assignment_assignment_id_fkey",
        ),
        ForeignKeyConstraint(
            ["instance_id"],
            ["course_instance.instance_id"],
            name="course_assignment_instance_id_fkey",
        ),
        ForeignKeyConstraint(
            ["student_id"],
            ["student.student_id"],
            name="course_assignment_student_id_fkey",
        ),
        PrimaryKeyConstraint("course_assignment_id", name="course_assignment_pkey"),
    )

    course_assignment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    instance_id: Mapped[int] = mapped_column(Integer, nullable=False)
    assignment_id: Mapped[int] = mapped_column(Integer, nullable=False)
    student_id: Mapped[int] = mapped_column(Integer, nullable=False)
    points_earned: Mapped[Optional[int]] = mapped_column(Integer)
    letter_grade: Mapped[Optional[str]] = mapped_column(String(5))

    assignment: Mapped["Assignment"] = relationship("Assignment", back_populates="course_assignment")
    instance: Mapped["CourseInstance"] = relationship("CourseInstance", back_populates="course_assignment")
    student: Mapped["Student"] = relationship("Student", back_populates="course_assignment")
