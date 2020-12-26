import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { EditEmployeeComponent } from './components/edit-employee/edit-employee.component';
import { EmpListComponent } from './components/emp-list/emp-list.component';

const routes: Routes = [
  {path : '', component : EditEmployeeComponent},
  {path : 'emplList', component : EmpListComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
