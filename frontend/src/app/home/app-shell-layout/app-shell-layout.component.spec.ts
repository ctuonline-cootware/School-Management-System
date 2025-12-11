import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AppShellLayoutComponent } from './app-shell-layout.component';

describe('AppShellLayoutComponent', () => {
  let component: AppShellLayoutComponent;
  let fixture: ComponentFixture<AppShellLayoutComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AppShellLayoutComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AppShellLayoutComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
