import { Component } from '@angular/core';
import { SchoolManagementService } from '../../school-management.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { CourseCreate } from '../../../types/aliases';

@Component({
  selector: 'app-admin-class-detail',


  templateUrl: './admin-class-detail.component.html',
  styleUrls: ['./admin-class-detail.component.scss']
})
export class AdminClassDetailComponent {
  courseForm: FormGroup;
  successMessage: string | null = null;
  errorMessage: string | null = null;

  constructor(private service: SchoolManagementService, private fb: FormBuilder) {
    this.courseForm = this.buildFormGroup();
  }

  buildFormGroup(): FormGroup {
    return this.fb.group({
      name: ['', Validators.required],
      code: ['', Validators.required],
      description: ['', Validators.required],
      credits: [0, [Validators.required, Validators.min(0)]],
      start_date: ['', Validators.required]
    });
  }

  resetForm(): void {
    this.courseForm.reset({ credits: 0 });
    this.successMessage = null;
    this.errorMessage = null;
  }

  submitForm(): void {
    this.successMessage = null;
    this.errorMessage = null;

    if (this.courseForm.invalid) {
      this.courseForm.markAllAsTouched();
      return;
    }

    if (this.courseForm.valid) {
      let model: CourseCreate = {
        name: this.courseForm.value.name,
        code: this.courseForm.value.code,
        description: this.courseForm.value.description,
        credits: this.courseForm.value.credits,
        is_active: true,
        start_date: new Date(this.courseForm.value.start_date).toISOString(),
        end_date: null
      };

      this.service.createCourse(model).subscribe({
        next: (v) => {
          this.successMessage = "Course added successfully.";
          let timer = setTimeout(() => {
            this.resetForm();
            clearTimeout(timer);
          }, 2000);
        },
        error: (e) => {
          this.errorMessage = "Error adding course. Please try again.";
          console.error("Error adding course", e);
        }
      });
    }
  }
}
