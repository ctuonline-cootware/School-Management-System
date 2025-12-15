import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Observable } from 'rxjs';

import { SchoolManagementService } from '../../school-management.service';
import { Faculty } from '../../../types/aliases';

@Component({
  selector: 'app-admin-faculty',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './admin-faculty.component.html',
  styleUrl: './admin-faculty.component.scss'
})
export class AdminFacultyComponent implements OnInit {
  faculty$!: Observable<Faculty[]>;

  constructor(private sms: SchoolManagementService) {}

  ngOnInit(): void {
    this.faculty$ = this.sms.listFaculty();
  }
}
