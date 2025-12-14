import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FacultyClassesListComponent } from './faculty-classes-list.component';

describe('FacultyClassesListComponent', () => {
  let component: FacultyClassesListComponent;
  let fixture: ComponentFixture<FacultyClassesListComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FacultyClassesListComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FacultyClassesListComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
