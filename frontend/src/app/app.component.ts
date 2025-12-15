import { Component } from '@angular/core';
import { Router } from '@angular/router';
import { RouterOutlet } from '@angular/router';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  title = 'frontend';
  constructor(private router: Router) {}

  get currentModule(): string {
    const url = this.router.url.split('?')[0] || '/';
    // extract first path segment
    const seg = url.split('/').filter(Boolean)[0];
    return seg ? seg : 'dashboard';
  }
}
