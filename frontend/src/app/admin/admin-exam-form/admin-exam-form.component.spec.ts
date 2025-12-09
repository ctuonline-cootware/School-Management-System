import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminExamFormComponent } from './admin-exam-form.component';

describe('AdminExamFormComponent', () => {
  let component: AdminExamFormComponent;
  let fixture: ComponentFixture<AdminExamFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminExamFormComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminExamFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
