## 🧱 1. What is a Class?

A class is like a blueprint for creating objects.

### Example analogy:
A class is like a car blueprint — it defines how a car should look and behave.
But each car you make from it (like a Toyota, BMW, etc.) is an object.

## Syntax:
```
class ClassName:
    # class body
    # define attributes and methods here
```

**Example:**

```
class Car:
    pass
```

This defines a class named Car, but it doesn’t do anything yet.

## 🚗 2. What is an Object?

An object is an instance of a class — created from that class.

**Example:**
```
car1 = Car()   # creating an object
car2 = Car()   # another object
```

Now car1 and car2 are two separate objects of the Car class.

## 🧍‍♀️ 3. What is __init__()?

 __init__ is a constructor method — automatically called when you create a new object.

It’s used to initialize (set up) the object’s data (attributes).

**Example:**
```
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color
```

When you create an object:
```
car1 = Car("Tesla", "Red")
car2 = Car("BMW", "Blue")
```

👉 Internally, Python does this:
```
Car.__init__(car1, "Tesla", "Red")
```

That’s why we need self 👇

## 🤔 4. What is self?

**self** refers to the current object being created or used.

It allows you to access attributes and methods of that specific object.

**Example:**
```
class Car:
    def __init__(self, brand, color):
        self.brand = brand   # 'self.brand' means "this car's brand"
        self.color = color

    def show_info(self):
        print(f"Brand: {self.brand}, Color: {self.color}")
```

**Usage:**
```
car1 = Car("Tesla", "Red")
car1.show_info()   # Output: Brand: Tesla, Color: Red

car2 = Car("BMW", "Blue")
car2.show_info()   # Output: Brand: BMW, Color: Blue
```

👉 Each object remembers its own data, because of self.

## 🧩 5. Example with everything combined
```
class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def display(self):
        print(f"Name: {self.name}, Roll: {self.roll}")

# create objects
s1 = Student("Amirtha", 101)
s2 = Student("Kavi", 102)

# call method
s1.display()   # Name: Amirtha, Roll: 101
s2.display()   # Name: Kavi, Roll: 102

```

## 🧠 6. Quick summary
|Concept	|Meaning|	Example|
|----      | ----  |-----|    
|Class	|Blueprint or template	|class Car:|
|Object	|Instance of class	|car1 = Car()|
|self|	Refers to current object|	self.name = name|
|init()|	Constructor to initialize attributes	|def __init__(self, name):|

## ⚙️ 7. Behind the scenes (important to know)

When you write:

```car1 = Car("Tesla", "Red")```


Python internally does:

Create a new empty object.

Call ```Car.__init__(car1, "Tesla", "Red")```

Store data (self.brand, self.color) inside car1.
