import { Component } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { SchoolManagementService } from '../../school-management.service';

@Component({
  selector: 'app-admin-class-instance-form',
  templateUrl: './admin-class-instance-form.component.html',
  styleUrl: './admin-class-instance-form.component.scss'
})
export class AdminClassInstanceFormComponent {
  readonly faculty$ = this.service.listFaculty();
  readonly courses$ = this.service.listCourses();
  
  courseInstanceForm: FormGroup;
  successMessage: string | null = null;
  errorMessage: string | null = null;

  constructor(private service: SchoolManagementService, private fb: FormBuilder) { 
    this.courseInstanceForm = this.buildFormGroup();
  }

  buildFormGroup(): FormGroup {
    return this.fb.group({
      courseId: [''],
      facultyId: [''],
      term: [''],
      startDate: [''],
      location: ['']
    });
  }

  resetForm(): void {
    this.courseInstanceForm.reset();
    this.successMessage = null;
    this.errorMessage = null;
  }

  submitForm(): void {
    this.successMessage = null;
    this.errorMessage = null;

    if (this.courseInstanceForm.invalid) {
      this.courseInstanceForm.markAllAsTouched();
      return;
    }
    
    if (this.courseInstanceForm.valid) {
      let model = {
        course_id: this.courseInstanceForm.value.courseId,
        faculty_id: this.courseInstanceForm.value.facultyId,
        term: this.courseInstanceForm.value.term,
        start_date: new Date(this.courseInstanceForm.value.startDate).toISOString(),
        location: this.courseInstanceForm.value.location,
        end_date: null
      };

      this.service.createCourseInstance(model).subscribe({
        next: (v) => {
          this.successMessage = "Class instance added successfully.";

          let timer = setTimeout(() => {
            this.resetForm();
            clearTimeout(timer);
          }, 2000);
        },
        error: (e) => {
          this.errorMessage = "Error adding class instance. Please try again.";
          console.error("Error adding class instance", e);
        }
      });
    }
  }
}
