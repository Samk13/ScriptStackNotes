class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __repr__(self):
        return "Employee('{}', '{}')".format(self.first, self.last)

    @property
    def employee_details(self):
        return {
            "full name": f"{self.first} {self.last}",
            "email": self.email,
        }

    @property
    def email(self):
        return "{}.{}@company.com".format(self.first, self.last)

    @property
    def fullname(self):
        return "{} {}".format(self.first, self.last)

    @fullname.setter
    def fullname(self, name):
        if name is None or name.split()[1] == None:
            raise ValueError("Name cannot be None")
        splitted_name = name.split(" ")
        if len(splitted_name) > 2 and splitted_name[0] is None:
            raise ValueError("Name cannot be None")
        else:
            self.first = splitted_name[0]
            self.last = splitted_name[-1]

    @fullname.deleter
    def fullname(self):
        print("Delete Name!")
        self.first = None
        self.last = None


emp_1 = Employee("John", "Smith")
emp_1.fullname = "sam kamal arbid"
print(emp_1.first)
print(emp_1.email)
print(emp_1.employee_details)
print("test")
