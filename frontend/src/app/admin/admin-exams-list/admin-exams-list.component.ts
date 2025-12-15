import { Component } from '@angular/core';
import { SchoolManagementService } from '../../school-management.service';

@Component({
  selector: 'app-admin-exams-list',


  templateUrl: './admin-exams-list.component.html',
  styleUrls: ['./admin-exams-list.component.scss']
})
export class AdminExamsListComponent {
  readonly assignments$ = this.service.listAssignments();
  
  constructor(private service: SchoolManagementService) { }
}
