import { ApplicationConfig, NgModule } from '@angular/core';
import { provideRouter } from '@angular/router';

import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { AppComponent } from './app.component';
import { HTTP_INTERCEPTORS, HttpClientModule } from "@angular/common/http";
import { AuthInterceptor } from "./auth/auth.interceptor";

import { routes } from './app.routes';
import { FormsModule } from '@angular/forms';
import { LoginComponent } from './home/login/login.component';
import { NotFoundComponent } from './home/not-found/not-found.component';
import { HomeModule } from './home/home.module';

// export const appConfig: ApplicationConfig = {
//   providers: [provideRouter(routes)]
// };

@NgModule({
  declarations: [AppComponent],
  imports: [BrowserModule, 
    HttpClientModule,
    FormsModule,
    HomeModule,
    RouterModule.forRoot(routes)],
  bootstrap: [AppComponent],
  providers: [
    { provide: HTTP_INTERCEPTORS, useClass: AuthInterceptor, multi: true },
  ],
})
export class AppModule {}
