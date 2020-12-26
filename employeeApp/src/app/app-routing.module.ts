import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CreateEmployeeComponent } from './components/create-employee/create-employee.component';
import { DeleteEmployeeComponent } from './components/delete-employee/delete-employee.component';
import { EmpListComponent } from './components/emp-list/emp-list.component';

const routes: Routes = [
  {path: '', component: EmpListComponent},
  {path: 'create', component: CreateEmployeeComponent},
  {path: 'delete', component: DeleteEmployeeComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
