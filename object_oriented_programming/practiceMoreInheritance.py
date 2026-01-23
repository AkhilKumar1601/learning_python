class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector2D({self.x}, {self.y})"

v2 = Vector2D(2, 3)
print(v2)

Vector2D(2, 3)

class Vector3D(Vector2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)   # initialize x and y from Vector2D
        self.z = z

    def __str__(self):
        return f"Vector3D({self.x}, {self.y}, {self.z})"

v3 = Vector3D(2, 3, 4)
print(v3)

