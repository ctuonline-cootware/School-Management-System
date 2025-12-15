import { Component } from '@angular/core';
import { Router, RouterLink, RouterLinkActive, RouterOutlet } from '@angular/router';
import { NgIf } from '@angular/common';
import { AuthService, UserRole, AuthUser } from '../../auth/auth.service';

@Component({
  selector: 'app-app-shell',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive, NgIf],
  templateUrl: './app-shell.component.html',
  styleUrl: './app-shell.component.scss',
})
export class AppShellComponent {
  role: UserRole | null = null;

  constructor(
    private auth: AuthService,
    private router: Router
  ) {
    this.auth.currentUser$.subscribe((user: AuthUser | null) => {
      this.role = user?.role ?? null;
    });
  }

  get isLoggedIn(): boolean {
    return this.auth.isLoggedIn();
  }

  async logout(): Promise<void> {
    this.auth.logout();
    await this.router.navigate(['/login']);
  }
}
