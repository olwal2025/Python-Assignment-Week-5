# OOP Assignment

## Description
This assignment demonstrates the principles of Object-Oriented Programming (OOP) in Python. It consists of two activities that explore class design, inheritance, encapsulation and polymorphism.

---

### **Assignment 1: Design Your Own Class! **
- **Objective**: Create a class representing a superhero.
- **Tasks**:
  1. Define a `Superhero` class with attributes and methods to bring the class to life.
  2. Use constructors (`__init__`) to initialize each object with unique values.
  3. Add an inheritance layer to explore polymorphism or encapsulation.
  4. Demonstrate the functionality of the class and its methods.

#### Implementation
The `superhero.py` file implements this activity:
- A `Superhero` base class is defined with attributes like `name`, `alias`, `origin` and `powers`.
- Methods include:
  - `show_powers()`: Displays the superhero's powers.
  - `activate_power()`: Activates a specific power.
  - `teleport()`: Teleports the superhero to a specified location.
  - `pause_time()`: Pauses time if the superhero has the "Chrono Pause" power.
- A `TechSuperhero` subclass is created to demonstrate inheritance and adds a unique method:
  - `hack_digital_world()`: Allows the superhero to phase into the digital world.

---

### **Activity 2: Polymorphism Challenge! **
- **Objective**: Create a program that demonstrates polymorphism.
- **Tasks**:
  1. Create a program that includes animals or vehicles with the same action (like `move()`).
  2. Make each class define `move()` differently (e.g. `Car.move()` prints "Driving" , while `Plane.move()` prints "Flying" ).

#### Implementation
The `polymorphism.py` file implements this activity:
- A base class `Animal` is defined with a `move()` method.
- Subclasses like `Lion`, `Eagle`, `Elephant` and `Snake` override the `move()` method to provide unique implementations.
- The program demonstrates polymorphism by iterating through a list of animals and calling their `move()` methods.

---

### **How to Run**
1. Clone the repository or download the files.
2. Run `superhero.py` to see the implementation of the Superhero class and its functionality.
3. Run `polymorphism.py` to see the polymorphism challenge in action.

---

### **Example Outputs**

#### **Assignment 1: Superhero Class**
```
Welcome to the World of Astria!
Real Name: Ahenda Olwal
Alias: Astria
Origin: Mombasa, Kenya

Astria's Powers:
 Teleportation
 Telepathy
 Digital Phasing
 Invisibility Cloak
 Chrono Pause
 Kinetic Recall

Astria activates Telepathy 
Astria teleports to Greece 
Astria activates Chrono Pause ... Time stands still.
Astria enters the digital world through Digital Phasing 
```

#### **Activity 2: Polymorphism Challenge**
```
Wild Animal Movements:
 The lion prowls stealthily across the savannah.
 The eagle soars high above the mountains and valleys.
 The elephant walks slowly through the jungle.
 The snake slithers silently along the forest paths.
```
