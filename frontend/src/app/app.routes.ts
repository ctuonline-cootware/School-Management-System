import { Routes } from '@angular/router';
import { LoginComponent } from './home/login/login.component';
import { AppShellLayoutComponent } from './home/app-shell-layout/app-shell-layout.component';
import { UnauthorizedComponent } from './home/unauthorized/unauthorized.component';
import { NotFoundComponent } from './home/not-found/not-found.component';
import { AuthGuard } from './auth/auth.guard';
import { ChangePasswordComponent } from './home/change-password/change-password.component';

export const routes: Routes = [
  { path: "login", component: LoginComponent },
  { 
    path: "change-password", 
    component: ChangePasswordComponent, 
    canActivate: [AuthGuard], 
    data: { roles: ["admin", "faculty", "student"] }, 
  },
  {
    path: "",
    component: AppShellLayoutComponent,
    canActivate: [AuthGuard],
    data: { roles: ["admin", "faculty", "student"] },
    children: [
        {
        path: "admin",
        canActivate: [AuthGuard],
        data: { roles: ["admin"] },
        loadChildren: () =>
            import("./admin/admin.module").then((m) => m.AdminModule),
        },
        {
        path: "faculty",
        canActivate: [AuthGuard],
        data: { roles: ["faculty", "admin"] },
        loadChildren: () =>
            import("./faculty/faculty.module").then((m) => m.FacultyModule),
        },
        {
        path: "student",
        canActivate: [AuthGuard],
        data: { roles: ["student", "admin"] },
        loadChildren: () =>
            import("./student/student.module").then((m) => m.StudentModule),
        },
    ],
  },
  { path: "unauthorized", component: UnauthorizedComponent },
  { path: "**", component: NotFoundComponent },
];
