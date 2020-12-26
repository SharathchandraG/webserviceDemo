import { Component, OnInit } from '@angular/core';
import { AbstractControl, FormControl } from '@angular/forms';
import { Employee } from './employee-model';
import { MOCK_EMPLOYEES } from './mock-employees';

@Component({
  selector: 'app-edit-employee',
  templateUrl: './edit-employee.component.html',
  styleUrls: ['./edit-employee.component.scss']
})
export class EditEmployeeComponent implements OnInit {
  empId: AbstractControl;
  employeeDetails: Employee[] = [];
  employee: Employee;

  constructor() { }

  ngOnInit(): void {
    this.empId = new FormControl('');
    this.employeeDetails = MOCK_EMPLOYEES;
  }

  getDetails() {
    this.employee = this.employeeDetails[this.employeeDetails.findIndex(item => item.Emp_ID === parseInt(this.empId.value))];
  }

}
