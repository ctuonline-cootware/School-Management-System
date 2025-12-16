import { Component, OnDestroy, OnInit } from '@angular/core';
import { NavigationEnd, Router } from '@angular/router';
import { RouterOutlet } from '@angular/router';
import { Subject, takeUntil } from 'rxjs';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'frontend';
  currentModule: string = '';
  private destroy$ = new Subject<void>();
  showUserMenu = false;

  constructor(private router: Router) {}
  
  ngOnInit(): void {
    // update currentModule only on route navigation, not on every change detection
    this.router.events
      .pipe(takeUntil(this.destroy$))
      .subscribe((event) => {
        if (event instanceof NavigationEnd) {
          const url = event.urlAfterRedirects.split('?')[0] || '/';
          const seg = url.split('/').filter(Boolean)[0];
          this.currentModule = seg ? seg : 'dashboard';
        }
      });
  }

  ngOnDestroy(): void {
    this.destroy$.next();
    this.destroy$.complete();
  }

  toggleUserMenu(): void {
    this.showUserMenu = !this.showUserMenu;
  }

  openChangePassword(event: Event): void {
    event.preventDefault();
    this.showUserMenu = false;
    // TODO: Open password change modal or navigate to change password page
     this.router.navigate(['/change-password']);
  }

  logout(event: Event): void {
    event.preventDefault();
    this.showUserMenu = false;
    // TODO: Call logout API and clear auth token
    localStorage.removeItem('token');
    this.router.navigate(['/login']);
  }

  // get currentModule(): string {
  //   const url = this.router.url.split('?')[0] || '/';
  //   // extract first path segment
  //   const seg = url.split('/').filter(Boolean)[0];
  //   return seg ? seg : 'dashboard';
  // }
}
