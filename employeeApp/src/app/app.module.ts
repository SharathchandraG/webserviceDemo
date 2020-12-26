import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { CreateEmployeeComponent } from './components/create-employee/create-employee.component';
import { DeleteEmployeeComponent } from './components/delete-employee/delete-employee.component';
import { EmpListComponent } from './components/emp-list/emp-list.component';

@NgModule({
  declarations: [
    AppComponent,
    CreateEmployeeComponent,
    DeleteEmployeeComponent,
    EmpListComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
