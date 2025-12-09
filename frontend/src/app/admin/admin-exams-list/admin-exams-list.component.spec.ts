import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminExamsListComponent } from './admin-exams-list.component';

describe('AdminExamsListComponent', () => {
  let component: AdminExamsListComponent;
  let fixture: ComponentFixture<AdminExamsListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminExamsListComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminExamsListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
