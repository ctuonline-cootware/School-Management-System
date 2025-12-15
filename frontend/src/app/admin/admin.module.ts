import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule, Routes } from "@angular/router";
import { ReactiveFormsModule } from '@angular/forms';

import { AdminDashboardComponent } from "./admin-dashboard/admin-dashboard.component";
import { AdminStudentsListComponent } from "./admin-students-list/admin-students-list.component";
import { AdminStudentFormComponent } from "./admin-student-form/admin-student-form.component";
import { AdminExamsListComponent } from "./admin-exams-list/admin-exams-list.component";
import { AdminExamFormComponent } from "./admin-exam-form/admin-exam-form.component";
import { AdminFacultyListComponent } from "./admin-faculty-list/admin-faculty-list.component";
import { AdminFacultyFormComponent } from "./admin-faculty-form/admin-faculty-form.component";
import { AdminClassesListComponent } from "./admin-classes-list/admin-classes-list.component";
import { AdminClassDetailComponent } from "./admin-class-detail/admin-class-detail.component";
import { AdminClassAssignmentsComponent } from "./admin-class-assignments/admin-class-assignments.component";
import { AdminClassInstanceListComponent } from './admin-class-instance-list/admin-class-instance-list.component';
import { AdminClassInstanceFormComponent } from './admin-class-instance-form/admin-class-instance-form.component';

const routes: Routes = [
  { path: "", component: AdminDashboardComponent },
  { path: "students", component: AdminStudentsListComponent },
  { path: "students/new", component: AdminStudentFormComponent },
  { path: "students/:id/edit", component: AdminStudentFormComponent },
  { path: "exams", component: AdminExamsListComponent },
  { path: "exams/new", component: AdminExamFormComponent },
  { path: "exams/:id/edit", component: AdminExamFormComponent },
  { path: "faculty", component: AdminFacultyListComponent },
  { path: "faculty/new", component: AdminFacultyFormComponent },
  { path: "faculty/:id/edit", component: AdminFacultyFormComponent },
  { path: "classes", component: AdminClassesListComponent },
  { path: "classes/new", component: AdminClassDetailComponent },
  { path: "class-instances", component: AdminClassInstanceListComponent },
  { path: "class-instances/new", component: AdminClassInstanceFormComponent },
  { path: "classes/new", component: AdminClassDetailComponent },
  { path: "classes/:id/assignments", component: AdminClassAssignmentsComponent },
];

@NgModule({
  declarations: [
    AdminDashboardComponent,
    AdminStudentsListComponent,
    AdminStudentFormComponent,
    AdminExamsListComponent,
    AdminExamFormComponent,
    AdminFacultyListComponent,
    AdminFacultyFormComponent,
    AdminClassesListComponent,
    AdminClassDetailComponent,
    AdminClassAssignmentsComponent,
    AdminClassInstanceListComponent,
    AdminClassInstanceFormComponent
  ],
  imports: [CommonModule, RouterModule.forChild(routes), ReactiveFormsModule],
})
export class AdminModule {}