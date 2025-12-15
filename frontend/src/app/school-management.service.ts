import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { AcademicProgram, AcademicProgramCreate, AcademicProgramUpdate, 
         Assignment, AssignmentCreate, AssignmentUpdate, 
         CourseAssignment, CourseAssignmentCreate, CourseAssignmentUpdate,
         CourseInstance, CourseInstanceCreate, CourseInstanceUpdate,
         Course, CourseCreate, CourseUpdate,
         Department, DepartmentCreate, DepartmentUpdate, 
         EnrollStudentRequest, 
         Faculty, FacultyCreate, FacultyUpdate, 
         Job, JobCreate, JobUpdate, 
         ProgramCourseRequirement, ProgramCourseRequirementCreate, ProgramCourseRequirementUpdate, 
         Student, 
         StudentCreate, 
         StudentUpdate, Users, UsersCreate, UsersUpdate, 
         Roles,
         RolesUpdate,
         RolesCreate} from '../types/aliases';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class SchoolManagementService {
  private baseUrl = "http://127.0.0.1:8000";

  constructor(private http: HttpClient) { }

  listAcademicPrograms(): Observable<AcademicProgram[]> {
    // GET /academic_programs/ 
    return this.http.get<AcademicProgram[]>(this.baseUrl + "/academic_programs");
  }

  createAcademicProgram(payload: AcademicProgramCreate): Observable<AcademicProgram> {
    // POST /academic_programs/ 
    return of(); // Placeholder implementation
  }

  getAcademicProgram(id: number): Observable<AcademicProgram> {
    // GET /academic_programs/{academic_program_id} 
    return this.http.get<AcademicProgram>(this.baseUrl + "/academic_programs/" +  id);
  }
 
  updateAcademicProgram(id: number, payload: AcademicProgramUpdate): Observable<AcademicProgram> {
      // PUT /academic_programs/{academic_program_id}
      return of(); // Placeholder implementation
  }

  // GET /assignments/ 
  listAssignments(): Observable<Assignment[]> {
      return this.http.get<Assignment[]>(this.baseUrl + "/assignments");
  }

  // POST /assignments/ 
  createAssignment(payload: AssignmentCreate): Observable<Assignment> {
      return this.http.post<Assignment>(this.baseUrl + "/assignments", payload);
  }

  // GET /assignments/{assignment_id} 
  getAssignment(id: number): Observable<Assignment> {
    return this.http.get<Assignment>(this.baseUrl + "/assignments/" + id);
  }

  // PUT /assignments/{assignment_id} 
  updateAssignment(id: number, payload: AssignmentUpdate): Observable<Assignment> {
    return this.http.put<Assignment>(this.baseUrl + "/assignments/" + id, payload);
  }

  // GET /course_assignments/ 
  listCourseAssignments(): Observable<CourseAssignment[]> { 
    return this.http.get<CourseAssignment[]>(this.baseUrl + "/course_assignments");
  }

  // POST /course_assignments/ 
  createCourseAssignment(payload: CourseAssignmentCreate): Observable<CourseAssignment> {
    return this.http.post<CourseAssignment>(this.baseUrl + "/course_assignments", payload);
  }

  // GET /course_assignments/{student_id} 
  listCourseAssignmentsByStudent(studentId: number): Observable<CourseAssignment[]> {
    return this.http.get<CourseAssignment[]>(this.baseUrl + `/course_assignments/?student_id=${studentId}`);
  }

  // GET /course_assignments/{course_assignment_id} 
  getCourseAssignment(id: number): Observable<CourseAssignment> {
    return this.http.get<CourseAssignment>(this.baseUrl + "/course_assignments/" + id);
  }

  // PUT /course_assignments/{course_assignment_id} 
  updateCourseAssignment(id: number, payload: CourseAssignmentUpdate): Observable<CourseAssignment> {
    return this.http.put<CourseAssignment>(this.baseUrl + "/course_assignments/" + id, payload);
  }


  // GET /course_instances/ 
  listCourseInstances(): Observable<CourseInstance[]> {
    return this.http.get<CourseInstance[]>(this.baseUrl + "/course_instances");
  }

  // POST /course_instances/ 
  createCourseInstance(payload: CourseInstanceCreate): Observable<CourseInstance> {
    return this.http.post<CourseInstance>(this.baseUrl + "/course_instances", payload);
  }

  // GET /course_instances/{course_instance_id} 
  getCourseInstance(id: number): Observable<CourseInstance> { 
    return this.http.get<CourseInstance>(this.baseUrl + "/course_instances/" + id);
  }

  // PUT /course_instances/{course_instance_id} 
  updateCourseInstance(id: number, payload: CourseInstanceUpdate): Observable<CourseInstance> {
    return this.http.put<CourseInstance>(this.baseUrl + "/course_instances/" + id, payload);
  }

  // POST /course_instances/{course_instance_id}/enroll-student 
  enrollStudent(courseInstanceId: number, payload: EnrollStudentRequest): Observable<any> {
    return this.http.post<any>(this.baseUrl + `/course_instances/${courseInstanceId}/enroll-student`, payload);
  }

  // GET /courses/ 
  listCourses(): Observable<Course[]> { 
    return this.http.get<Course[]>(this.baseUrl + "/courses");
  }

  // POST /courses/ 
  createCourse(payload: CourseCreate): Observable<Course> { 
    return this.http.post<Course>(this.baseUrl + "/courses", payload);
  }

  // GET /courses/{course_id} 
  getCourse(id: number): Observable<Course> {
    return this.http.get<Course>(this.baseUrl + "/courses/" + id);  
  }

  // PUT /courses/{course_id} 
  updateCourse(id: number, payload: CourseUpdate): Observable<Course> {
    return this.http.put<Course>(this.baseUrl + "/courses/" + id, payload); 
  }


  // GET /deparments/ 
  listDepartments(): Observable<Department[]> { 
    return this.http.get<Department[]>(this.baseUrl + "/departments");  
  }

  // POST /deparments/ 
  createDepartment(payload: DepartmentCreate): Observable<Department> { 
    return this.http.post<Department>(this.baseUrl + "/departments", payload);
  }

  // GET /deparments/{department_id} 
  getDepartment(id: number): Observable<Department> { 
    return this.http.get<Department>(this.baseUrl + "/departments/" + id);  
  }

  // PUT /deparments/{department_id} 
  updateDepartment(id: number, payload: DepartmentUpdate): Observable<Department> { 
    return this.http.put<Department>(this.baseUrl + "/departments/" + id, payload);
  }


  // GET /faculty/ 
  listFaculty(): Observable<Faculty[]> { 
    return this.http.get<Faculty[]>(this.baseUrl + "/faculty");
  }

  // POST /faculty/ 
  createFaculty(payload: FacultyCreate): Observable<Faculty> { 
    return this.http.post<Faculty>(this.baseUrl + "/faculty", payload);
  }

  // GET /faculty/{faculty_id} 
  getFaculty(id: number): Observable<Faculty> { 
    return this.http.get<Faculty>(this.baseUrl + "/faculty/" + id);
  }

  // PUT /faculty/{faculty_id} 
  updateFaculty(id: number, payload: FacultyUpdate): Observable<Faculty> { 
    return this.http.put<Faculty>(this.baseUrl + "/faculty/" + id, payload);
  }

  // GET /faculty/{faculty_id}/classes 
  getFacultyClasses(id: number): Observable<any> { 
    return this.http.get<any>(this.baseUrl + `/faculty/${id}/classes`);
  }


  // GET /jobs/ 
  listJobs(): Observable<Job[]> { 
    return this.http.get<Job[]>(this.baseUrl + "/jobs");  
  }

  // POST /jobs/ 
  createJob(payload: JobCreate): Observable<Job> { 
    return this.http.post<Job>(this.baseUrl + "/jobs", payload);
  }

  // GET /jobs/{job_id} 
  getJob(id: number): Observable<Job> { 
    return this.http.get<Job>(this.baseUrl + "/jobs/" + id);
  }

  // PUT /jobs/{job_id} 
  updateJob(id: number, payload: JobUpdate): Observable<Job> { 
    return this.http.put<Job>(this.baseUrl + "/jobs/" + id, payload); 
  }


  // GET /program_course_requirements/ 
  listProgramCourseRequirements(): Observable<ProgramCourseRequirement[]> { 
    return this.http.get<ProgramCourseRequirement[]>(this.baseUrl + "/program_course_requirements");
  }

  // POST /program_course_requirements/ 
  createProgramCourseRequirement(payload: ProgramCourseRequirementCreate): Observable<ProgramCourseRequirement> { 
    return this.http.post<ProgramCourseRequirement>(this.baseUrl + "/program_course_requirements", payload);  
  }

  // GET /program_course_requirements/{program_course_requirement_id} 
  getProgramCourseRequirement(id: number): Observable<ProgramCourseRequirement> {
    return this.http.get<ProgramCourseRequirement>(this.baseUrl + "/program_course_requirements/" + id);  
  }

  // PUT /program_course_requirements/{program_course_requirement_id} 
  updateProgramCourseRequirement(id: number, payload: ProgramCourseRequirementUpdate): Observable<ProgramCourseRequirement> {
    return this.http.put<ProgramCourseRequirement>(this.baseUrl + "/program_course_requirements/" + id, payload);
  }

  // GET /students/ 
  listStudents(): Observable<Student[]> {
    return this.http.get<Student[]>(this.baseUrl + "/students");  
  }

  // POST /students/ 
  createStudent(payload: StudentCreate): Observable<Student> {
    return this.http.post<Student>(this.baseUrl + "/students", payload);
  }

  // GET /students/{student_id} 
  getStudent(id: number): Observable<Student> { 
    return this.http.get<Student>(this.baseUrl + "/students/" + id);
  }

  // PUT /students/{student_id} 
  updateStudent(id: number, payload: StudentUpdate): Observable<Student> { 
    return this.http.put<Student>(this.baseUrl + "/students/" + id, payload);
  }


  // GET /users/ 
  listUsers(): Observable<Users[]> { 
    return this.http.get<Users[]>(this.baseUrl + "/users");
  }

  // POST /users/ 
  createUser(payload: UsersCreate): Observable<Users> { 
    return this.http.post<Users>(this.baseUrl + "/users", payload);
  }

  // GET /users/{job_id} 
  getUserByJob(jobId: number): Observable<Users> { 
    return this.http.get<Users>(this.baseUrl + `/users/?job_id=${jobId}`);
  }

  // PUT /users/{user_id} 
  updateUser(id: number, payload: UsersUpdate): Observable<Users> {
    return this.http.put<Users>(this.baseUrl + "/users/" + id, payload);
  }


  // GET /roles/ 
  listRoles(): Observable<Roles[]> { 
    return this.http.get<Roles[]>(this.baseUrl + "/roles");
  }

  // POST /roles/ 
  createRole(payload: RolesCreate): Observable<Roles> { 
    return this.http.post<Roles>(this.baseUrl + "/roles", payload);
  }

  // GET /roles/{job_id} 
  getRoleByJob(jobId: number): Observable<Roles> {
    return this.http.get<Roles>(this.baseUrl + `/roles/?job_id=${jobId}`);
  }

  // PUT /roles/{role_id} 
  updateRole(id: number, payload: RolesUpdate): Observable<Roles> {
    return this.http.put<Roles>(this.baseUrl + "/roles/" + id, payload);
  }

}
