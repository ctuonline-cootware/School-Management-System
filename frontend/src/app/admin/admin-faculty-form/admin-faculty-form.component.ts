import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { ActivatedRoute, Router } from '@angular/router';

import { SchoolManagementService } from '../../school-management.service';
import { FacultyCreate, FacultyUpdate } from '../../../types/aliases';

@Component({
  selector: 'app-admin-faculty-form',
  templateUrl: './admin-faculty-form.component.html',
  styleUrls: ['./admin-faculty-form.component.scss'],
})
export class AdminFacultyFormComponent implements OnInit {
  saving = false;
  error = '';
  isEdit = false;
  facultyId: number | null = null;

  form = this.fb.group({
    first_name: ['', Validators.required],
    last_name: ['', Validators.required],
    email_address: ['', [Validators.required, Validators.email]],
    department_id: [1, [Validators.required, Validators.min(1)]],
    job_id: [1, [Validators.required, Validators.min(1)]],
    hire_date: ['', Validators.required], // yyyy-mm-dd
    term_date: [''], // optional yyyy-mm-dd
  });

  constructor(
    private fb: FormBuilder,
    private sms: SchoolManagementService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit(): void {
    const idParam = this.route.snapshot.paramMap.get('id');

    if (idParam) {
      // EDIT mode
      this.isEdit = true;
      this.facultyId = Number(idParam);

      this.sms.getFaculty(this.facultyId).subscribe({
        next: (f) => {
          this.form.patchValue({
            first_name: f.first_name,
            last_name: f.last_name,
            email_address: f.email_address,
            department_id: f.department_id,
            job_id: f.job_id,
            hire_date: (f.hire_date ?? '').toString().slice(0, 10),
            term_date: f.term_date ? f.term_date.toString().slice(0, 10) : '',
          });
        },
        error: (err: any) => {
          this.error = err?.error?.detail
            ? JSON.stringify(err.error.detail)
            : 'Failed to load faculty';
        },
      });
    } else {
      // CREATE mode
      this.isEdit = false;
      this.facultyId = null;
    }
  }

  submit(): void {
    this.error = '';

    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }

    const v = this.form.value;
    this.saving = true;

    if (this.isEdit && this.facultyId) {
      const payload: FacultyUpdate = {
        first_name: v.first_name!,
        last_name: v.last_name!,
        email_address: v.email_address!,
        department_id: Number(v.department_id),
        job_id: Number(v.job_id),
        hire_date: v.hire_date!,
        term_date: v.term_date ? v.term_date : null,
      };

      this.sms.updateFaculty(this.facultyId, payload).subscribe({
        next: () => {
          this.saving = false;
          this.router.navigate(['/admin/faculty']);
        },
        error: (err: any) => {
          this.saving = false;
          this.error = err?.error?.detail
            ? JSON.stringify(err.error.detail)
            : 'Update failed';
        },
      });
    } else {
      const payload: FacultyCreate = {
        first_name: v.first_name!,
        last_name: v.last_name!,
        email_address: v.email_address!,
        department_id: Number(v.department_id),
        job_id: Number(v.job_id),
        hire_date: v.hire_date!,
        term_date: v.term_date ? v.term_date : null,
      };

      this.sms.createFaculty(payload).subscribe({
          next: () => {
            let email = payload.email_address;

            if (email !== null && email !== undefined) {  
              // Create user with faculty role (role_id = 2)
              const userPayload = {
                username: email,
                password: email,
                roles: [2],
                is_active: true
              };
              
              this.sms.createUser(userPayload).subscribe({
                next: () => {
                  this.saving = false;
                  this.router.navigate(['/admin/faculty']);
                },
                error: (userErr: any) => {
                  this.saving = false;
                  this.error = 'Faculty created but user account creation failed: ' + 
                    (userErr?.error?.detail ? JSON.stringify(userErr.error.detail) : 'Unknown error');
                  setTimeout(() => this.router.navigate(['/admin/faculty']), 3000);
                }
              });
            }
          },
        error: (err: any) => {
          this.saving = false;
          this.error = err?.error?.detail
            ? JSON.stringify(err.error.detail)
            : 'Create failed';
        },
      });
    }
  }

  cancel(): void {
    this.router.navigate(['/admin/faculty']);
  }
}
