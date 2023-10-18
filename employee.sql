CREATE TABLE employee_management.employees (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    department VARCHAR(255),
    salary DECIMAL(10, 2)
);
select *from  employee_management.employees;
