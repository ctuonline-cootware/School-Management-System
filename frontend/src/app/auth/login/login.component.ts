// src/app/auth/login/login.component.ts
import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, FormGroup, Validators, ReactiveFormsModule } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthService, UserRole } from '../auth.service';

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './login.component.html',
  styleUrl: './login.component.scss',
})
export class LoginComponent {
  form: FormGroup;
  loading = false;
  error: string | null = null;

  constructor(
    private fb: FormBuilder,
    private auth: AuthService,
    private router: Router
  ) {
    this.form = this.fb.group({
      username: ['', [Validators.required]],
      password: ['', [Validators.required]],
    });
  }

  onSubmit(): void {
    if (this.form.invalid) {
      this.form.markAllAsTouched();
      return;
    }

    this.loading = true;
    this.error = null;

    const { username, password } = this.form.value;

    this.auth.login(username, password).subscribe({
      next: (user) => {
        this.loading = false;
        this.redirectForRole(user.role);
      },
      error: () => {
        this.loading = false;
        this.error = 'Login failed. Please try again.';
      },
    });
  }

  private redirectForRole(role: UserRole): void {
    if (role === 'admin') {
      this.router.navigate(['/admin']);
    } else if (role === 'student') {
      this.router.navigate(['/student']);
    } else if (role === 'faculty') {
      this.router.navigate(['/faculty']);
    } else {
      this.router.navigate(['/login']);
    }
  }
}
