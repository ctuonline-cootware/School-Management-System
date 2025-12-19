import { Component } from '@angular/core';
import { AuthService, TokenPayload } from '../../auth/auth.service';
import { SchoolManagementService } from '../../school-management.service';
import { map, Observable } from 'rxjs';
import { Router } from '@angular/router';

@Component({
  selector: 'app-change-password',
  templateUrl: './change-password.component.html',
  styleUrl: './change-password.component.scss'
})
export class ChangePasswordComponent {
  readonly roles$ = this.service.listRoles();
  newPassword: string = "";
  username: string = "";
  private userId: number = 0;
  private roles: number[] = [];

  errorMessage: string | null = null;
  successMessage: string | null = null;

  constructor(private authService: AuthService, private service: SchoolManagementService, private router: Router) {
    let token = this.authService.getDecodedToken();
    this.username = token ? token.sub : "";
    this.userId = token ? token.user_id : 0;
    
    if (token !== null) {
      this.getRoles(token).subscribe(roleIds => this.roles = roleIds);
    }
  }

  getRoles(token: TokenPayload): Observable<number[]> {
    return this.roles$.pipe(
      map(roles =>
        roles
          .filter(role => token.roles.includes(role.name))
          .map(role => role.id)
      )
    );
  }

  changePassword(): void {
    if (this.userId === 0) {
      this.errorMessage = "User not authenticated.";
      return;
    }

    this.service.updateUser(this.userId, {
      password: this.newPassword,
      roles: this.roles
    }).subscribe({
      next: () => {
        // Handle successful password change by navigating to login
        this.successMessage = "Password changed successfully. Please log in again.";
        this.authService.logout();
        this.router.navigate(["/login"]);
      },
      error: (err) => {
        if (err.status === 422 && err.error?.detail?.length) {
          // Take the first validation error message
          this.errorMessage = err.error.detail[0].msg;
        } else {
          this.errorMessage = "Error changing password. Please try again.";
        }
      }
    });
  }
}
