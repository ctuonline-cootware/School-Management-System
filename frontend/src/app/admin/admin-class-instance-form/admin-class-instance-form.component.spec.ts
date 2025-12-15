import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminClassInstanceFormComponent } from './admin-class-instance-form.component';

describe('AdminClassInstanceFormComponent', () => {
  let component: AdminClassInstanceFormComponent;
  let fixture: ComponentFixture<AdminClassInstanceFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminClassInstanceFormComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminClassInstanceFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
