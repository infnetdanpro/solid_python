# The Interface segregation principle: "Clients should not be forced to
# depend upon interfaces that they do not use."

# BAD:
class Shape:
    def draw_circle(self):
        raise NotImplemented

    def draw_square(self):
        raise NotImplemented


class Circle(Shape):
    def draw_circle(self):
        pass

    # WTF?:)
    def draw_square(self):
        pass


# Good
class Shape:
    def draw(self):
        raise NotImplemented

class Circle(Shape):
    def draw(self):
        pass

class Square(Shape):
    def draw(self):
        pass
