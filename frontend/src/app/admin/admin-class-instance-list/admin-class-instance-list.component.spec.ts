import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminClassInstanceListComponent } from './admin-class-instance-list.component';

describe('AdminClassInstanceListComponent', () => {
  let component: AdminClassInstanceListComponent;
  let fixture: ComponentFixture<AdminClassInstanceListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminClassInstanceListComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminClassInstanceListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
