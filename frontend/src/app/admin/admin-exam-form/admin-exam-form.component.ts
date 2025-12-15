import { Component } from '@angular/core';
import { SchoolManagementService } from '../../school-management.service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';

@Component({
  selector: 'app-admin-exam-form',


  templateUrl: './admin-exam-form.component.html',
  styleUrls: ['./admin-exam-form.component.scss']
})
export class AdminExamFormComponent {
  assignmentForm: FormGroup;
  successMessage: string | null = null;
  errorMessage: string | null = null;

  constructor(private service: SchoolManagementService, private fb: FormBuilder) { 
    this.assignmentForm = this.buildFormGroup();
  }

  buildFormGroup(): FormGroup {
    return this.fb.group({
      name: ['', Validators.required],
      start_date: ['', Validators.required],
      is_active: [true],
      max_points: [0, [Validators.required, Validators.min(0)]]
    });
  }

  resetForm(): void {
    this.assignmentForm.reset({ is_active: true, max_points: 0 });
    this.successMessage = null;
    this.errorMessage = null;
  }

  submitForm(): void {
    this.successMessage = null;
    this.errorMessage = null;

    if (this.assignmentForm.invalid) {
      this.assignmentForm.markAllAsTouched();
      return;
    }

    if (this.assignmentForm.valid) {
      let model = {
        name: this.assignmentForm.value.name,
        start_date: new Date(this.assignmentForm.value.start_date).toISOString(),
        is_active: this.assignmentForm.value.is_active,
        max_points: this.assignmentForm.value.max_points,
        end_date: null,
        assignment_id: 0
      };
      
      this.service.createAssignment(model).subscribe({
        next: (v) => {
          this.successMessage = "Exam added successfully.";
          let timer = setTimeout(() => { 
            this.resetForm();
            clearTimeout(timer);
          }, 2000);
        },
        error: (e) => {
          this.errorMessage = "Error adding exam. Please try again.";
          console.error("Error adding exam", e);
        }
      });
    }
  }
}
