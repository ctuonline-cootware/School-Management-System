import { Component } from "@angular/core";
import { SchoolManagementService } from "../../school-management.service";
import { FormBuilder, FormGroup, Validators } from "@angular/forms";
import { FacultyCreate, Job } from "../../../types/aliases";

@Component({
  selector: "app-admin-faculty-form",


  templateUrl: "./admin-faculty-form.component.html",
  styleUrls: ["./admin-faculty-form.component.scss"]
})
export class AdminFacultyFormComponent {
  facultyForm: FormGroup;
  readonly departments$ = this.service.listDepartments();
  readonly jobs$ = this.service.listJobs();
  successMessage: string | null = null;
  errorMessage: string | null = null;
  
  constructor(private service: SchoolManagementService, private fb: FormBuilder) {
    this.facultyForm = this.buildFormGroup();
  }  

  buildFormGroup(): FormGroup {
    return this.fb.group({
      firstName: ["", Validators.required],
      lastName: ["", Validators.required],
      department_id: [0, [Validators.required, Validators.min(1)]],
      job_id: [0, [Validators.required, Validators.min(1)]],
      hire_date: ["", Validators.required]
    });
  }

  resetForm(): void { 
    this.facultyForm.reset({ department_id: 0, job_id: 0 });
    this.successMessage = null;
    this.errorMessage = null;
  }

  submitForm(): void {
    this.successMessage = null;
    this.errorMessage = null;

    if (this.facultyForm.invalid) {
      this.facultyForm.markAllAsTouched();
      return;
    }

    if (this.facultyForm.valid) {
      let email = this.facultyForm.value.firstName.toLowerCase() + "." + this.facultyForm.value.lastName.toLowerCase() + "@university.edu";
      
      let model: FacultyCreate = {
        "first_name": this.facultyForm.value.firstName,
        "last_name": this.facultyForm.value.lastName,
        "hire_date": new Date(this.facultyForm.value.hire_date).toISOString().split('T')[0],
        "department_id": this.facultyForm.value.department_id, 
        "job_id": this.facultyForm.value.job_id,
        "term_date": null,
        "email_address": email
      }
      
      this.service.createFaculty(model).subscribe(response => {
        this.successMessage = 'Faculty added successfully.';
        let timer = setTimeout(() => { 
          this.resetForm();
          clearTimeout(timer);
        }, 2000);
      }, error => {
        this.errorMessage = 'Error adding faculty. Please try again.';
        console.error("Error adding faculty", error);
      });
    }
  }
}
