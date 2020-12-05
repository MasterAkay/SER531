import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { MainDisplayPaneComponent } from './main-display-pane/main-display-pane.component';
import {FormsModule} from '@angular/forms';
import { NavbarComponent } from './navbar/navbar.component';
import { GlueComponent } from './glue/glue.component';



@NgModule({
  declarations: [
    AppComponent,
    MainDisplayPaneComponent,
    NavbarComponent,
    GlueComponent
  ],
    imports: [
        BrowserModule,
        HttpClientModule,
        FormsModule
    ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
