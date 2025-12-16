import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { tap, map } from "rxjs/operators";
import { jwtDecode } from "jwt-decode";

export type UserRole = "admin" | "faculty" | "student";

export interface TokenPayload {
  sub: string;
  user_id: number;
  roles: string[];
  exp: number; // expiry timestamp (seconds since epoch)
}

@Injectable({
  providedIn: "root",
})
export class AuthService {
  private apiUrl = "http://localhost:8000/auth/token"; // adjust to your backend

  constructor(private http: HttpClient) {}

login(username: string, password: string) {
  const body = new URLSearchParams();
  body.set("grant_type", "password");  // ✅ required for OAuth2PasswordRequestForm
  body.set("username", username);
  body.set("password", password);
  body.set("scope", "");              // optional, matches Swagger

  return this.http
    .post<{ access_token: string; token_type: string }>(this.apiUrl, body.toString(), {
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
    })
    .pipe(
      tap((res) => {
        localStorage.setItem("access_token", res.access_token);
      }),
      map(() => {
        const decoded = this.getDecodedToken();
        const roles = decoded?.roles ?? [];

        const role: UserRole =
          roles.includes("admin") ? "admin" :
          roles.includes("faculty") ? "faculty" :
          "student";

        return { role };
      })
    );
}

  logout() {
    localStorage.removeItem("access_token");
  }

  getToken(): string | null {
    return localStorage.getItem("access_token");
  }

  getDecodedToken(): TokenPayload | null {
    const token = this.getToken();
    if (!token) return null;
    try {
      return jwtDecode<TokenPayload>(token);
    } catch {
      return null;
    }
  }

  isTokenExpired(): boolean {
    const decoded = this.getDecodedToken();
    if (!decoded) return true;
    const now = Math.floor(Date.now() / 1000);
    return decoded.exp < now;
  }

  hasRole(role: string): boolean {
    const decoded = this.getDecodedToken();
    return decoded?.roles?.includes(role) ?? false;
  }
}