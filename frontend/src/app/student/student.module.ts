import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { StudentAssignmentsComponent } from './student-assignments/student-assignments.component';
import { StudentDashboardComponent } from './student-dashboard/student-dashboard.component';
import { StudentProfileComponent } from './student-profile/student-profile.component';
import { StudentScheduleComponent } from './student-schedule/student-schedule.component';

const routes: Routes = [
  { path: "", component: StudentDashboardComponent },
  { path: "schedule", component: StudentScheduleComponent },
  { path: "assignments", component: StudentAssignmentsComponent },
  { path: "profile", component: StudentProfileComponent },
];

@NgModule({
  declarations: [
    StudentDashboardComponent,
    StudentScheduleComponent,
    StudentAssignmentsComponent,
    StudentProfileComponent,
  ],
  imports: [CommonModule, RouterModule.forChild(routes)],
})
export class StudentModule {}