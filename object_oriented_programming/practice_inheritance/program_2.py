class Employee:
    def __init__(self,salary,increment):
        self._salary = salary;
        self._increment = increment;


    @property
    def salary(self):
        return self._salary;

    @salary.setter
    def salary(self,value):
        self._salary = value;


    @property
    def increment(self):
        return self._increment;

    @property
    def incremented_salary(self):
        return self._salary + (self._salary * self._increment / 100);


e = Employee(150000, 5)

print(e.salary)              # 150000
print(e.increment)           # 5
print(e.incremented_salary)    # 157500

   
