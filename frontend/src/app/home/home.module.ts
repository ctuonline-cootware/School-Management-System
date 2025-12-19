import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AppShellLayoutComponent } from './app-shell-layout/app-shell-layout.component';
import { LoginComponent } from './login/login.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { UnauthorizedComponent } from './unauthorized/unauthorized.component';
import { FormsModule } from '@angular/forms';
import { RouterModule } from '@angular/router';
import { ChangePasswordComponent } from './change-password/change-password.component';



@NgModule({
  declarations: [AppShellLayoutComponent, LoginComponent, NotFoundComponent, UnauthorizedComponent, ChangePasswordComponent],
  imports: [
    CommonModule,
    FormsModule,
    RouterModule
  ]
})
export class HomeModule { }
