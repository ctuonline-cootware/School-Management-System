import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Routes, RouterModule } from '@angular/router';
import { FacultyClassRosterComponent } from './faculty-class-roster/faculty-class-roster.component';
import { FacultyClassesListComponent } from './faculty-classes-list/faculty-classes-list.component';
import { FacultyDashboardComponent } from './faculty-dashboard/faculty-dashboard.component';
import { FacultyGradeEntryComponent } from './faculty-grade-entry/faculty-grade-entry.component';

const routes: Routes = [
  { path: "", component: FacultyDashboardComponent },
  { path: "classes", component: FacultyClassesListComponent },
  { path: "classes/:id/roster", component: FacultyClassRosterComponent },
  { path: "classes/:id/grades", component: FacultyGradeEntryComponent },
];

@NgModule({
  declarations: [
    FacultyDashboardComponent,
    FacultyClassesListComponent,
    FacultyClassRosterComponent,
    FacultyGradeEntryComponent,
  ],
  imports: [CommonModule, RouterModule.forChild(routes)],
})
export class FacultyModule {}