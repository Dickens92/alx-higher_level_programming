0. All your files, classes and methods must be unit tested and be PEP 8 validated.
1. Writing the first class Base
2. the class Rectangle that inherits from Base
3. he class Rectangle by adding validation of all setter methods and instantiation (id excluded)
4. the class Rectangle by adding the public method def area(self): that returns the area value of the Rectangle instance.
5. the class Rectangle by adding the public method def display(self): that prints in stdout the Rectangle instance with the character # - you don’t need to handle x and y her
6. the class Rectangle by overriding the __str__ method so that it returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
7.  the class Rectangle by improving the public method def display(self): to print in stdout the Rectangle instance with the character # by taking care of x and y
8.  the class Rectangle by adding the public method def update(self, *args): that assigns an argument to each attribute
9. the class Rectangle by updating the public method def update(self, *args): by changing the prototype to update(self, *args, **kwargs) that assigns a key/value argument to attributes
10. he class Square that inherits from Rectangle
11. he class Square by adding the public getter and setter size
12. the class Square by adding the public method def update(self, *args, **kwargs) that assigns attributes
13. the class Rectangle by adding the public method def to_dictionary(self): that returns the dictionary representation of a Rectangle
14. the class Square by adding the public method def to_dictionary(self): that returns the dictionary representation of a Square
15. JSON is one of the standard formats for sharing data representation
16. he class Base by adding the class method def save_to_file(cls, list_objs): that writes the JSON string representation of list_objs to a file
17. the class Base by adding the static method def from_json_string(json_string): that returns the list of the JSON string representation json_string
