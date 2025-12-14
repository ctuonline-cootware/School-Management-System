import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminFacultyListComponent } from './admin-faculty-list.component';

describe('AdminFacultyListComponent', () => {
  let component: AdminFacultyListComponent;
  let fixture: ComponentFixture<AdminFacultyListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminFacultyListComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminFacultyListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
