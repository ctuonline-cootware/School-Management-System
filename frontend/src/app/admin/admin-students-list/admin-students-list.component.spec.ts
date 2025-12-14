import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminStudentsListComponent } from './admin-students-list.component';

describe('AdminStudentsListComponent', () => {
  let component: AdminStudentsListComponent;
  let fixture: ComponentFixture<AdminStudentsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminStudentsListComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminStudentsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
