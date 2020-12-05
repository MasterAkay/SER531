import { ComponentFixture, TestBed } from '@angular/core/testing';

import { MainDisplayPaneComponent } from './main-display-pane.component';

describe('MainDisplayPaneComponent', () => {
  let component: MainDisplayPaneComponent;
  let fixture: ComponentFixture<MainDisplayPaneComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ MainDisplayPaneComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(MainDisplayPaneComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
