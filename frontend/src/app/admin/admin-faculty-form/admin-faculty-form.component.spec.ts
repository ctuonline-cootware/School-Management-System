import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminFacultyFormComponent } from './admin-faculty-form.component';

describe('AdminFacultyFormComponent', () => {
  let component: AdminFacultyFormComponent;
  let fixture: ComponentFixture<AdminFacultyFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminFacultyFormComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminFacultyFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
