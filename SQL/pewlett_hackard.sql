--Data Engineering
--Use the information you have to create a table schema for each of the six CSV files. Remember to specify data types, primary keys, foreign keys, and other constraints.

CREATE TABLE departments (
	dept_no varchar NOT NULL,
	dept_name varchar NOT NULL,
	CONSTRAINT pk_Departments PRIMARY KEY (dept_no)
);

CREATE TABLE dept_emp (
	emp_no int NOT NULL,
	dept_no varchar NOT NULL,
	from_date date NOT NULL,
	to_date date NOT NULL
);

CREATE TABLE dept_manager (
	dept_no varchar NOT NULL,
	emp_no int NOT NULL,
	from_date date NOT NULL,
	to_date date NOT NULL
);

CREATE TABLE employees (
	emp_no int NOT NULL,
	birth_date date NOT NULL,
	first_name varchar NOT NULL,
	last_name varchar NOT NULL,
	gender varchar NOT NULL,
	hire_date date NOT NULL,
	CONSTRAINT pk_Employees PRIMARY KEY (emp_no)
);

CREATE TABLE salaries (
	emp_no int NOT NULL,
	salary int NOT NULL,
	from_date date NOT NULL,
	to_date date NOT NULL
);

CREATE TABLE titles (
	emp_no int NOT NULL,
	title varchar NOT NULL,
	from_date date NOT NULL,
	to_date date NOT NULL
);

ALTER TABLE dept_emp
	ADD CONSTRAINT fk_Dept_emp_emp_no FOREIGN KEY (emp_no) REFERENCES employees (emp_no);

ALTER TABLE dept_manager
	ADD CONSTRAINT fk_Dept_manager_dept_no FOREIGN KEY (dept_no) REFERENCES departments (dept_no);

ALTER TABLE salaries
	ADD CONSTRAINT fk_Salaries_emp_no FOREIGN KEY (emp_no) REFERENCES employees (emp_no);

ALTER TABLE titles
	ADD CONSTRAINT fk_Titles_emp_no FOREIGN KEY (emp_no) REFERENCES employees (emp_no);

--List the following details of each employee: employee number, last name, first name, gender, and salary.
SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	e.gender,
	s.salary
FROM
	Employees e
	FULL JOIN salaries s ON e.emp_no = s.emp_no;

--List employees who were hired in 1986.
SELECT
	*
FROM
	employees
WHERE
	EXTRACT(year FROM hire_date) = 1986;

--List the manager of each department with the following information: department number, department name, the manager's employee number, last name, first name, and start and end employment dates.
SELECT
	d.dept_no,
	d.dept_name,
	dm.emp_no,
	e.last_name,
	e.first_name,
	dm.from_date,
	dm.to_date
FROM
	departments d,
	employees e,
	dept_manager dm
WHERE
	d.dept_no = dm.dept_no
	AND dm.emp_no = e.emp_no;

--List the department of each employee with the following information: employee number, last name, first name, and department name.
SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM
	employees e,
	departments d,
	dept_emp de
WHERE
	e.emp_no = de.emp_no
	AND de.dept_no = d.dept_no;

--List all employees whose first name is "Hercules" and last names begin with "B."
SELECT
	*
FROM
	employees
WHERE
	first_name LIKE 'B%';

--List all employees in the Sales department, including their employee number, last name, first name, and department name.
SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM
	employees e,
	departments d,
	dept_emp de
WHERE
	e.emp_no = de.emp_no
	AND de.dept_no = d.dept_no
	AND dept_name = 'Sales';

--List all employees in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT
	e.emp_no,
	e.last_name,
	e.first_name,
	d.dept_name
FROM
	employees e
	JOIN dept_emp de ON e.emp_no = de.emp_no
	JOIN departments d ON de.dept_no = d.dept_no
WHERE
	dept_name = 'Sales'
	OR dept_name = 'Development';

--In descending order, list the frequency count of employee last names, i.e., how many employees share each last name.
SELECT
	last_name,
	count(last_name) AS total
FROM
	employees
GROUP BY
	last_name
ORDER BY
	total DESC;