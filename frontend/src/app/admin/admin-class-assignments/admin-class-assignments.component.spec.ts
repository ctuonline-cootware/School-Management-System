import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminClassAssignmentsComponent } from './admin-class-assignments.component';

describe('AdminClassAssignmentsComponent', () => {
  let component: AdminClassAssignmentsComponent;
  let fixture: ComponentFixture<AdminClassAssignmentsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminClassAssignmentsComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminClassAssignmentsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
