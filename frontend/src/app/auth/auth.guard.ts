import { CanActivateFn } from '@angular/router';

export const authGuard: CanActivateFn = (route, state) => {
  return true;
};

import { Injectable } from "@angular/core";
import { CanActivate, Router, ActivatedRouteSnapshot } from "@angular/router";
import { AuthService } from "./auth.service";

@Injectable({
  providedIn: "root",
})
export class AuthGuard implements CanActivate {
  constructor(private authService: AuthService, private router: Router) {}

  canActivate(route: ActivatedRouteSnapshot): boolean {
    if (this.authService.isTokenExpired()) {
      this.router.navigate(["/login"]);
      return false;
    }

    const requiredRoles = route.data["roles"] as string[] | undefined;
    if (requiredRoles && !requiredRoles.some((r) => this.authService.hasRole(r))) {
      this.router.navigate(["/unauthorized"]);
      return false;
    }

    return true;
  }
}