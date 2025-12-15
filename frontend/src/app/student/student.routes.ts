import { Routes } from '@angular/router';

import { StudentDashboardComponent } from './student-dashboard/student-dashboard.component';
import { StudentClassesComponent } from './student-classes/student-classes.component';
import { StudentExamsComponent } from './student-exams/student-exams.component';

export const STUDENT_ROUTES: Routes = [
  {
    path: '',
    component: StudentDashboardComponent,   // /student
  },
  {
    path: 'classes',
    component: StudentClassesComponent,     // /student/classes
  },
  {
    path: 'exams',
    component: StudentExamsComponent,       // /student/exams
  },
  {
    path: '**',
    redirectTo: '',
  },
];
