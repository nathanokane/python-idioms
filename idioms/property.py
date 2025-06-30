#This program was created by Nathan O'Kane on 26/06/25
#Last edited by Nathan O'Kane on 26/06/25

#The below code is an example of the "property" idiom for OOP in python
#It also uses python's setter syntax as well to define values


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def height(self):
        return self._height
    
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value < 0:
            print("Invalid value of width")
        else:
            print(f"Setting value of width to {value}")
            self._width = value

    @height.setter
    def height(self, value):
        if value < 0:
            print("Invalid value of height")
        else:
            print(f"Value of height was set to {value}")
            self._height = value

    @property
    def area(self):
        return self._height * self._width
    
    @property
    def perimeter(self):
        return (2 * self._height) + (2 * self._width)
    
    @property
    def aspect_ratio(self):
        return self._width / self._height
    
    #This property is read only and can't be modified outside of the class
    #This returns a boolean value
    @property
    def is_square(self):
        return self._width == self._height
    
    @property
    def shape_name(self):
        return "Square" if self.is_square else "rectangle"
    

new_rec = Rectangle(5,6)
print(new_rec.area)
print(new_rec.is_square)
#The below line would fail as the property is read only by design
#new_rec.is_square = False