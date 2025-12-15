import { Component } from '@angular/core';
import { SchoolManagementService } from '../../school-management.service';

@Component({
  selector: 'app-admin-classes-list',


  templateUrl: './admin-classes-list.component.html',
  styleUrls: ['./admin-classes-list.component.scss']
})
export class AdminClassesListComponent {
  readonly classes$ = this.service.listCourses();
  
  constructor(private service: SchoolManagementService) { }
}
