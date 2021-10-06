class Car:
    def __init__(self, name, color, owner_name,model_name):
        self.car_name = name
        self.car_color = color
        self.car_owner_name = owner_name
        self.car_model_number = model_name

    def create(self, c_color, c_model):
        self.car_color = c_color
        self.car_model_number = c_model

    def start(self):
        print("Car started")
    
    def stop(self):
        print("Car stoped")

class BMW(Car):
    price = 10000

object = Car('volvo','Red','nahid',123)

# object2 = BMW
# obj = BMW
# obj.start()