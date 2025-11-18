from typing import Optional
import datetime

from sqlalchemy import Boolean, Column, Date, ForeignKeyConstraint, Integer, PrimaryKeyConstraint, String, Table, Text, UniqueConstraint, text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass


class Assignment(Base):
    __tablename__ = 'assignment'
    __table_args__ = (
        PrimaryKeyConstraint('assignment_id', name='assignment_pkey'),
        {'schema': 'school'}
    )

    assignment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    max_points: Mapped[int] = mapped_column(Integer, nullable=False)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    course_assignment: Mapped[list['CourseAssignment']] = relationship('CourseAssignment', back_populates='assignment')


class Course(Base):
    __tablename__ = 'course'
    __table_args__ = (
        PrimaryKeyConstraint('course_id', name='course_pkey'),
        {'schema': 'school'}
    )

    course_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean)

    course_instance: Mapped[list['CourseInstance']] = relationship('CourseInstance', back_populates='course')
    program_course_requirement: Mapped[list['ProgramCourseRequirement']] = relationship('ProgramCourseRequirement', back_populates='course')


class Department(Base):
    __tablename__ = 'department'
    __table_args__ = (
        PrimaryKeyConstraint('department_id', name='department_pkey'),
        {'schema': 'school'}
    )

    department_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)

    academic_program: Mapped[list['AcademicProgram']] = relationship('AcademicProgram', back_populates='department_')
    faculty: Mapped[list['Faculty']] = relationship('Faculty', back_populates='department')


class Job(Base):
    __tablename__ = 'job'
    __table_args__ = (
        PrimaryKeyConstraint('job_id', name='job_pkey'),
        {'schema': 'school'}
    )

    job_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, nullable=False)
    is_management: Mapped[bool] = mapped_column(Boolean, nullable=False)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    faculty: Mapped[list['Faculty']] = relationship('Faculty', back_populates='job')


class Roles(Base):
    __tablename__ = 'roles'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='roles_pkey'),
        UniqueConstraint('name', name='roles_name_key'),
        {'schema': 'school'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(Text, nullable=False)

    user: Mapped[list['Users']] = relationship('Users', secondary='school.user_roles', back_populates='role')


class Users(Base):
    __tablename__ = 'users'
    __table_args__ = (
        PrimaryKeyConstraint('id', name='users_pkey'),
        UniqueConstraint('username', name='users_username_key'),
        {'schema': 'school'}
    )

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(Text, nullable=False)
    password_hash: Mapped[str] = mapped_column(Text, nullable=False)
    is_active: Mapped[Optional[bool]] = mapped_column(Boolean, server_default=text('true'))

    role: Mapped[list['Roles']] = relationship('Roles', secondary='school.user_roles', back_populates='user')


class AcademicProgram(Base):
    __tablename__ = 'academic_program'
    __table_args__ = (
        ForeignKeyConstraint(['department'], ['school.department.department_id'], name='academic_program_department_fkey'),
        PrimaryKeyConstraint('program_id', name='academic_program_pkey'),
        {'schema': 'school'}
    )

    program_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    department: Mapped[int] = mapped_column(Integer, nullable=False)
    degree_type: Mapped[str] = mapped_column(String(20), nullable=False)

    department_: Mapped['Department'] = relationship('Department', back_populates='academic_program')
    program_course_requirement: Mapped[list['ProgramCourseRequirement']] = relationship('ProgramCourseRequirement', back_populates='program')
    student: Mapped[list['Student']] = relationship('Student', back_populates='program')


class Faculty(Base):
    __tablename__ = 'faculty'
    __table_args__ = (
        ForeignKeyConstraint(['department_id'], ['school.department.department_id'], name='faculty_department_id_fkey'),
        ForeignKeyConstraint(['job_id'], ['school.job.job_id'], name='faculty_job_id_fkey'),
        PrimaryKeyConstraint('faculty_id', name='faculty_pkey'),
        {'schema': 'school'}
    )

    faculty_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    hire_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    department_id: Mapped[int] = mapped_column(Integer, nullable=False)
    job_id: Mapped[int] = mapped_column(Integer, nullable=False)
    term_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    department: Mapped['Department'] = relationship('Department', back_populates='faculty')
    job: Mapped['Job'] = relationship('Job', back_populates='faculty')
    course_instance: Mapped[list['CourseInstance']] = relationship('CourseInstance', back_populates='faculty')


t_user_roles = Table(
    'user_roles', Base.metadata,
    Column('user_id', Integer, primary_key=True),
    Column('role_id', Integer, primary_key=True),
    ForeignKeyConstraint(['role_id'], ['school.roles.id'], name='user_roles_role_id_fkey'),
    ForeignKeyConstraint(['user_id'], ['school.users.id'], name='user_roles_user_id_fkey'),
    PrimaryKeyConstraint('user_id', 'role_id', name='user_roles_pkey'),
    schema='school'
)


class CourseInstance(Base):
    __tablename__ = 'course_instance'
    __table_args__ = (
        ForeignKeyConstraint(['course_id'], ['school.course.course_id'], name='course_instance_course_id_fkey'),
        ForeignKeyConstraint(['faculty_id'], ['school.faculty.faculty_id'], name='course_instance_faculty_id_fkey'),
        PrimaryKeyConstraint('instance_id', name='course_instance_pkey'),
        {'schema': 'school'}
    )

    instance_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    course_id: Mapped[int] = mapped_column(Integer, nullable=False)
    faculty_id: Mapped[int] = mapped_column(Integer, nullable=False)
    term: Mapped[str] = mapped_column(String(20), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    location: Mapped[str] = mapped_column(String(100), nullable=False)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    course: Mapped['Course'] = relationship('Course', back_populates='course_instance')
    faculty: Mapped['Faculty'] = relationship('Faculty', back_populates='course_instance')
    course_assignment: Mapped[list['CourseAssignment']] = relationship('CourseAssignment', back_populates='instance')


class ProgramCourseRequirement(Base):
    __tablename__ = 'program_course_requirement'
    __table_args__ = (
        ForeignKeyConstraint(['course_id'], ['school.course.course_id'], name='program_course_requirement_course_id_fkey'),
        ForeignKeyConstraint(['program_id'], ['school.academic_program.program_id'], name='program_course_requirement_program_id_fkey'),
        PrimaryKeyConstraint('requirement_id', name='program_course_requirement_pkey'),
        {'schema': 'school'}
    )

    requirement_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    program_id: Mapped[int] = mapped_column(Integer, nullable=False)
    course_id: Mapped[int] = mapped_column(Integer, nullable=False)
    requirement_type: Mapped[str] = mapped_column(String(50), nullable=False)
    version: Mapped[str] = mapped_column(String(20), nullable=False)

    course: Mapped['Course'] = relationship('Course', back_populates='program_course_requirement')
    program: Mapped['AcademicProgram'] = relationship('AcademicProgram', back_populates='program_course_requirement')


class Student(Base):
    __tablename__ = 'student'
    __table_args__ = (
        ForeignKeyConstraint(['program_id'], ['school.academic_program.program_id'], name='student_program_id_fkey'),
        PrimaryKeyConstraint('student_id', name='student_pkey'),
        {'schema': 'school'}
    )

    student_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    first_name: Mapped[str] = mapped_column(String(50), nullable=False)
    last_name: Mapped[str] = mapped_column(String(50), nullable=False)
    start_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    expected_graduation_date: Mapped[datetime.date] = mapped_column(Date, nullable=False)
    program_id: Mapped[int] = mapped_column(Integer, nullable=False)
    end_date: Mapped[Optional[datetime.date]] = mapped_column(Date)

    program: Mapped['AcademicProgram'] = relationship('AcademicProgram', back_populates='student')
    course_assignment: Mapped[list['CourseAssignment']] = relationship('CourseAssignment', back_populates='student')


class CourseAssignment(Base):
    __tablename__ = 'course_assignment'
    __table_args__ = (
        ForeignKeyConstraint(['assignment_id'], ['school.assignment.assignment_id'], name='course_assignment_assignment_id_fkey'),
        ForeignKeyConstraint(['instance_id'], ['school.course_instance.instance_id'], name='course_assignment_instance_id_fkey'),
        ForeignKeyConstraint(['student_id'], ['school.student.student_id'], name='course_assignment_student_id_fkey'),
        PrimaryKeyConstraint('course_assignment_id', name='course_assignment_pkey'),
        {'schema': 'school'}
    )

    course_assignment_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    instance_id: Mapped[int] = mapped_column(Integer, nullable=False)
    assignment_id: Mapped[int] = mapped_column(Integer, nullable=False)
    student_id: Mapped[int] = mapped_column(Integer, nullable=False)
    points_earned: Mapped[Optional[int]] = mapped_column(Integer)
    letter_grade: Mapped[Optional[str]] = mapped_column(String(5))

    assignment: Mapped['Assignment'] = relationship('Assignment', back_populates='course_assignment')
    instance: Mapped['CourseInstance'] = relationship('CourseInstance', back_populates='course_assignment')
    student: Mapped['Student'] = relationship('Student', back_populates='course_assignment')
