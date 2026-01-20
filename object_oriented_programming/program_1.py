class Programmer:
    company = "Google";

    def __init__(self,name,age,working_id):
        self.name = name;
        self.age = age;
        self.working_id = working_id;
        print("Constructor called");

    def print_attributes(self):
        print(f"Programmer name is {self.name}. \n");
        print(f"Programmer age is {self.age}. \n");
        print(f"Programmer working id is {self.working_id} \n");
        print(f"Programmer is working in {self.company}.");

first_programmer = Programmer("Akhil",22,"akh123@google.com");
first_programmer.print_attributes();
