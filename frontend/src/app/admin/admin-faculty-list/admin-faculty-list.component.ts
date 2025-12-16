import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { Observable } from 'rxjs';

import { SchoolManagementService } from '../../school-management.service';
import { Faculty } from '../../../types/aliases';

@Component({
  selector: 'app-admin-faculty-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './admin-faculty-list.component.html',
  styleUrl: './admin-faculty-list.component.scss',
})
export class AdminFacultyListComponent implements OnInit {
  faculty$!: Observable<Faculty[]>;

  constructor(private sms: SchoolManagementService) {}

  ngOnInit(): void {
    this.faculty$ = this.sms.listFaculty();
  }
}
