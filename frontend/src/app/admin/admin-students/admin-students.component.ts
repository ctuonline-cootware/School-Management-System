import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import {
  FormBuilder,
  FormGroup,
  ReactiveFormsModule,
  Validators,
} from '@angular/forms';

interface Student {
  id: number;
  firstName: string;
  lastName: string;
  email: string;
  status: 'Active' | 'Inactive';
}

@Component({
  selector: 'app-admin-students',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './admin-students.component.html',
  styleUrl: './admin-students.component.scss',
})
export class AdminStudentsComponent {
  students: Student[] = [
    {
      id: 1,
      firstName: 'Laura',
      lastName: 'Elliott',
      email: 'laura.elliott@school.edu',
      status: 'Active',
    },
    {
      id: 2,
      firstName: 'James',
      lastName: 'Cootware',
      email: 'james.cootware@school.edu',
      status: 'Active',
    },
    {
      id: 3,
      firstName: 'Jarred',
      lastName: 'David',
      email: 'jared.david@school.edu',
      status: 'Inactive',
    },
  ];

  studentForm: FormGroup;
  isEditMode = false;
  editingStudentId: number | null = null;

  constructor(private fb: FormBuilder) {
    this.studentForm = this.fb.group({
      firstName: ['', [Validators.required, Validators.maxLength(50)]],
      lastName: ['', [Validators.required, Validators.maxLength(50)]],
      email: ['', [Validators.required, Validators.email]],
      status: ['Active', Validators.required],
    });
  }

  get firstName() {
    return this.studentForm.get('firstName');
  }
  get lastName() {
    return this.studentForm.get('lastName');
  }
  get email() {
    return this.studentForm.get('email');
  }
  get status() {
    return this.studentForm.get('status');
  }

  startCreate() {
    this.isEditMode = false;
    this.editingStudentId = null;
    this.studentForm.reset({
      status: 'Active',
    });
  }

  startEdit(student: Student) {
    this.isEditMode = true;
    this.editingStudentId = student.id;
    this.studentForm.setValue({
      firstName: student.firstName,
      lastName: student.lastName,
      email: student.email,
      status: student.status,
    });
  }

  submitForm() {
    if (this.studentForm.invalid) {
      this.studentForm.markAllAsTouched();
      return;
    }

    const formValue = this.studentForm.value as Omit<Student, 'id'>;

    if (this.isEditMode && this.editingStudentId !== null) {
      this.students = this.students.map((s) =>
        s.id === this.editingStudentId ? { ...s, ...formValue } : s
      );
    } else {
      const newId =
        this.students.length > 0
          ? Math.max(...this.students.map((s) => s.id)) + 1
          : 1;

      this.students = [
        ...this.students,
        {
          id: newId,
          ...formValue,
        },
      ];
    }

    this.startCreate();
  }

  deleteStudent(student: Student) {
    if (!confirm(`Delete ${student.firstName} ${student.lastName}?`)) {
      return;
    }

    this.students = this.students.filter((s) => s.id !== student.id);

    if (this.editingStudentId === student.id) {
      this.startCreate();
    }
  }
}
