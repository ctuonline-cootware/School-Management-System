import { Component } from "@angular/core";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { SchoolManagementService } from "../../school-management.service";
import { StudentCreate } from "../../../types/aliases";

@Component({
  selector: "app-admin-student-form",


  templateUrl: "./admin-student-form.component.html",
  styleUrls: ["./admin-student-form.component.scss"]
})
export class AdminStudentFormComponent {
  studentForm: FormGroup;
  readonly programs$ = this.service.listAcademicPrograms();
  successMessage: string | null = null;
  errorMessage: string | null = null;

  constructor(private service:SchoolManagementService, private fb: FormBuilder) {
    this.studentForm = this.buildFormGroup();
  }

  buildFormGroup(): FormGroup {
    return this.fb.group({
      firstName: ["", Validators.required],
      lastName: ["", Validators.required],
      startDate: ["", Validators.required],
      expectedGraduationDate: ["", Validators.required],
      programId: [0, [Validators.required, Validators.min(1)]]
    });
  }

  resetForm(): void {
    this.studentForm.reset({ programId: 0 });
    this.successMessage = null;
    this.errorMessage = null;
  }

  submitForm(): void {
    if (this.studentForm.invalid) {
      this.studentForm.markAllAsTouched();
      return;
    }

    if (this.studentForm.valid) {
      let email = this.studentForm.value.firstName.toLowerCase() + "." + this.studentForm.value.lastName.toLowerCase() + "@university.edu";
      let model: StudentCreate = {
        "first_name": this.studentForm.value.firstName,
        "last_name": this.studentForm.value.lastName,
        "start_date": new Date(this.studentForm.value.startDate).toISOString().split("T")[0],
        "end_date": null,
        "expected_graduation_date": new Date(this.studentForm.value.expectedGraduationDate).toISOString().split("T")[0],
        "program_id": this.studentForm.value.programId,
        "email_address": email,
        "course_instances": [],
        program: null
      };

      this.service.createStudent(model).subscribe({
        next: (v) => {
          this.successMessage = "student added successfully.";
          let timer = setTimeout(() => { 
            this.resetForm();
            clearTimeout(timer);
          }, 2000);
        },
        error: (e) => {
          this.errorMessage = "Error adding student. Please try again.";
          console.error("Error adding student", e);
        }
      });       
    }
  }
}
