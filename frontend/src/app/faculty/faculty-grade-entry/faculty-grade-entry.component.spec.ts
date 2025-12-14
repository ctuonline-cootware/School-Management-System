import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FacultyGradeEntryComponent } from './faculty-grade-entry.component';

describe('FacultyGradeEntryComponent', () => {
  let component: FacultyGradeEntryComponent;
  let fixture: ComponentFixture<FacultyGradeEntryComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FacultyGradeEntryComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FacultyGradeEntryComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
