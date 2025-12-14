import { ComponentFixture, TestBed } from '@angular/core/testing';

import { FacultyClassRosterComponent } from './faculty-class-roster.component';

describe('FacultyClassRosterComponent', () => {
  let component: FacultyClassRosterComponent;
  let fixture: ComponentFixture<FacultyClassRosterComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [FacultyClassRosterComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(FacultyClassRosterComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
