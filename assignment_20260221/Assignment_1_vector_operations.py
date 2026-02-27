class vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def multiply(self, scalar):
        return vector(self.x * scalar, self.y * scalar)
    
    def norm(self):
        return (self.x**2 + self.y**2)**0.5
    
    def turn(self, angle):
        import math
        radians = math.radians(angle)
        cos_angle = math.cos(radians)
        sin_angle = math.sin(radians)
        new_x = self.x * cos_angle - self.y * sin_angle
        new_y = self.x * sin_angle + self.y * cos_angle
        return vector(new_x, new_y)
    
    def dot_product(self, other):
        return self.x * other.x + self.y * other.y

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y)

    def __mul__(self, scalar):
        return vector(self.x * scalar, self.y * scalar)

    def __truediv__(self, scalar):
        return vector(self.x / scalar, self.y / scalar)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
def main():
    print("\n*** Vector Dot Product ***")
    v1 = vector(2, 3)
    v2 = vector(4, 5)

    print("Input vector v1:", v1)
    print("Input vector v2:", v2)
    print(f"Dot product of v1 and v2: {v1.dot_product(v2)}")

if __name__ == "__main__":
    main()
