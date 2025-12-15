import { Routes } from '@angular/router';

import { FacultyDashboardComponent } from './faculty-dashboard/faculty-dashboard.component';
import { FacultyClassesComponent } from './faculty-classes/faculty-classes.component';
import { FacultyExamsComponent } from './faculty-exams/faculty-exams.component';

export const FACULTY_ROUTES: Routes = [
  { path: '', component: FacultyDashboardComponent },      // /faculty
  { path: 'classes', component: FacultyClassesComponent }, // /faculty/classes
  { path: 'exams', component: FacultyExamsComponent },     // /faculty/exams
];
