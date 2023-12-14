#your code goes here
class Shape:
    @staticmethod
    def area(width, height):
        return width * height

w = int(input())
h = int(input())

print(Shape.area(w, h))