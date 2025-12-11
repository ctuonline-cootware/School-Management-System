import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AppShellLayoutComponent } from './app-shell-layout/app-shell-layout.component';
import { LoginComponent } from './login/login.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { UnauthorizedComponent } from './unauthorized/unauthorized.component';
import { FormsModule } from '@angular/forms';



@NgModule({
  declarations: [AppShellLayoutComponent, LoginComponent, NotFoundComponent, UnauthorizedComponent],
  imports: [
    CommonModule,
    FormsModule
  ]
})
export class HomeModule { }
