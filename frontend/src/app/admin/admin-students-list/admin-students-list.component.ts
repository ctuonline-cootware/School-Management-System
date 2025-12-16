import { Component } from '@angular/core';
import { SchoolManagementService } from '../../school-management.service';

@Component({
  selector: 'app-admin-students-list',


  templateUrl: './admin-students-list.component.html',
  styleUrls: ['./admin-students-list.component.scss']
})
export class AdminStudentsListComponent {
  readonly students$ = this.service.listStudents();
  constructor(private service: SchoolManagementService) { }
}
