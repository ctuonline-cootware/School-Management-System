import { Component } from '@angular/core';
import { SchoolManagementService } from '../../school-management.service';

@Component({
  selector: 'app-admin-class-instance-list',
  templateUrl: './admin-class-instance-list.component.html',
  styleUrl: './admin-class-instance-list.component.scss'
})
export class AdminClassInstanceListComponent {
  readonly classInstances$ = this.service.listCourseInstances();
  
  constructor(private service: SchoolManagementService) { } 
}
