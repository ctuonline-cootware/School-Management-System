import { Component } from "@angular/core";
import { Router } from "@angular/router";
import { AuthService, UserRole } from "../../auth/auth.service";

@Component({
  selector: "app-login",
  templateUrl: "./login.component.html",
  styleUrls: ["./login.component.scss"]
})
export class LoginComponent {
  username = "";
  password = "";
  errorMessage = "";

  constructor(private authService: AuthService, private router: Router) {}

  login() {
    this.authService.login(this.username, this.password).subscribe({
      next: (user) => {
        this.redirectForRole(user.role);
      },
      error: () => {
        this.errorMessage = "Invalid credentials";
      }
    });
  }

  private redirectForRole(role: UserRole): void {
    if (role === "admin") {
      this.router.navigate(["/admin"]);
    } else if (role === "student") {
      this.router.navigate(["/student"]);
    } else if (role === "faculty") {
      this.router.navigate(["/faculty"]);
    } else {
      this.router.navigate(["/login"]);
    }
  }
}