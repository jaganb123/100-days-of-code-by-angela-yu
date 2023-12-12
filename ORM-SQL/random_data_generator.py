import random

first_name = ['uma', 'gokul', 'tony', 'thor', 'bruce', 'mouli', 'periyasami', 'hari', 'prasanna', 'jaya', 'kavi', 'jessica', 'monica', 'adhirsta', 'lakshmi']
last_name = ['sureshkumar', 'kannan', 'krishna', 'guptha', 'stark', 'banner', 'gosh', 'lakshmi', 'thendral', 'babu', 'grist', 'andrew', 'lakshmi']

class RandomData:
    def __init__(self, count = 1) -> None:
        self.count: int = count
        if self.count == 1:
            self.data = self.generate_data()
        elif self.count > 1:
            self.data = []
            for i in range(self.count):
                self.data.append(self.generate_data())
    
    # def age(self):
    #     rand_age = random.randint(18, 56)
    #     return rand_age
    
    # def f_name(self):
    #     rand_f_name = random.choice(first_name).lower()
    #     print(rand_f_name)
    #     return rand_f_name
    
    # def l_name(self):
    #     rand_l_name = random.choice(last_name).lower()
    #     return rand_l_name
    
    def full_name(self, f_name: str, l_name: str):
        f_name1: str = f_name
        l_name1: str = l_name
        return f"{f_name1.capitalize()} {l_name1.capitalize()}"
    
    def generate_data(self):
        rand_age = random.randint(18, 56)        
        rand_f_name = random.choice(first_name).lower()
        rand_l_name = random.choice(last_name).lower()        
        full_name = self.full_name(rand_f_name, rand_l_name)
        return {"age": rand_age, "f_name": rand_f_name, "l_name": rand_l_name, "full_name": full_name}