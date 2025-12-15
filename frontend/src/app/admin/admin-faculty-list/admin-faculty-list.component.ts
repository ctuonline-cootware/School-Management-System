import { Component } from '@angular/core';
import { SchoolManagementService } from '../../school-management.service';

@Component({
  selector: 'app-admin-faculty-list',


  templateUrl: './admin-faculty-list.component.html',
  styleUrls: ['./admin-faculty-list.component.scss']
})
export class AdminFacultyListComponent {
  readonly faculty$ = this.service.listFaculty(); 
  constructor(private service: SchoolManagementService) { }
}
