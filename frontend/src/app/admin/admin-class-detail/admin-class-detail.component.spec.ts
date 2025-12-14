import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AdminClassDetailComponent } from './admin-class-detail.component';

describe('AdminClassDetailComponent', () => {
  let component: AdminClassDetailComponent;
  let fixture: ComponentFixture<AdminClassDetailComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [AdminClassDetailComponent]
    })
    .compileComponents();
    
    fixture = TestBed.createComponent(AdminClassDetailComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
