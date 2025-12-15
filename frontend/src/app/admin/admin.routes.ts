import { Routes } from '@angular/router';

import { AdminDashboardComponent } from './admin-dashboard/admin-dashboard.component';
import { AdminStudentsComponent } from './admin-students/admin-students.component';
import { AdminExamsComponent } from './admin-exams/admin-exams.component';
import { AdminFacultyComponent } from './admin-faculty/admin-faculty.component';
import { AdminClassesComponent } from './admin-classes/admin-classes.component';

export const ADMIN_ROUTES: Routes = [
  { path: '', component: AdminDashboardComponent },   // /admin
  { path: 'students', component: AdminStudentsComponent }, // /admin/students
  { path: 'exams', component: AdminExamsComponent },       // /admin/exams
  { path: 'faculty', component: AdminFacultyComponent },   // /admin/faculty
  { path: 'classes', component: AdminClassesComponent },   // /admin/classes
];
