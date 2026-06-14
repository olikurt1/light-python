class Vector2D:
    def __init__(self, x ,y):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return f"Vector2D({self.x}, {self.y})"
    
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y -  other.y)
    
    def __mul__(self, other):
        return Vector2D(self.x * other, self.y * other)
    
    def __eq__(self, other):
        return Vector2D(self, other)

a = Vector2D(1, 2)
b = Vector2D(3, 4)

c = a + b
d = b - a
e = a * 3

print(c)
print(d)
print(e)