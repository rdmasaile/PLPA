class Car:
    def move(self,):
       print("Driving the car")

class Plane:
    def move(self,):
       print("Flying the plane")

class Cat:
    def move(self,):
       print("Cat is walking") 

objects = [Car(),Plane(),Cat()]

for obj in objects:
    obj.move()