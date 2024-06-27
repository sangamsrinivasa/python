import argsparse


if __name__ == "__main__":
    parser = argsparse.ArgumentParser()
    parser.addArgument("--salaries", required=True, default=[100, 200, 300])
    parser.addArgument("--employee_grades", required=True, default=['A11', 'A12', 'A13'])
    tc = test_Class(salaries, employee_grades)
    tc.print_employee_grades()
    tc.print_grade_salaries()

class test_Class():
    def __init__(self, salary, employee_grade):
        self.salary = salary
        self.employee_grade = employee_grade

    def print_employee_grades(self):
        for grade in self.employee_grade:
            print(grade)
    
    def print_grade_salaries(self):
        for sal in self.salary:
            print(sal)
