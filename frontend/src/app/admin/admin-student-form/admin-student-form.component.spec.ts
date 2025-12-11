import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminStudentFormComponent } from './admin-student-form.component';

describe('AdminStudentFormComponent', () => {
  let component: AdminStudentFormComponent;
  let fixture: ComponentFixture<AdminStudentFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminStudentFormComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminStudentFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
