CHAPTER 4: INHERITANCE

===================
Learning Objectives
===================
- Understanding inheritance and its role in OOP
- Learning parent-child class relationships
- Implementing inheritance hierarchies in Python
- Using super() for parent class method access
- Managing private properties across inheritance chains
- Creating clean and logical class hierarchies

=====
Notes
=====
- Inheritance allows child classes to inherit properties and methods from parent classes
- Child classes can extend and override parent functionality
- super() enables access to parent class methods
- Private properties require getters even in child classes
- Good inheritance follows "is-a" relationships
- Multiple children can inherit from the same parent
- Inheritance trees should be logical and well-structured
- Child classes should be strict subsets of parent classes
- Over-nesting inheritance hierarchies should be avoided
- Code reuse through inheritance promotes DRY principles

====================
Lessons & Challenges
====================
[x] Lesson 1: Basic Inheritance
  - Introduced fundamental inheritance concepts
  - Created Animal and Cow class relationship example
  - Implemented Archer class inheriting from Human
  - Added private property management
  - Created getter methods for encapsulation
  - Demonstrated basic inheritance syntax

[x] Lesson 2: Inheritance Hierarchy
  - Explored deeper inheritance structures
  - Built Wall and Castle class hierarchy
  - Implemented private property access patterns
  - Extended Archer with Crossbowman class
  - Added resource management system
  - Created clean inheritance interfaces

[x] Lesson 3: Multiple Children (Part 1)
  - Created Hero base class for game units
  - Implemented Archer as first child class
  - Added arrow resource management
  - Created damage system mechanics
  - Implemented private variable protection
  - Added getter method interfaces

[x] Lesson 4: Multiple Children (Part 2)
  - Added Wizard class alongside Archer
  - Implemented distinct resource systems
  - Created specialized combat mechanics
  - Maintained consistent class interfaces
  - Demonstrated branching inheritance
  - Added mana management system

[x] Lesson 5 & 6: Dragons System
  - Built Unit base class for game entities
  - Created Dragon specialized class
  - Implemented position tracking system
  - Added area effect calculations
  - Created unit targeting mechanics
  - Demonstrated complex inheritance patterns

[x] Challenge 1: Rectangles and Squares
  - Implemented Rectangle base class
  - Created Square child class
  - Added area calculations
  - Implemented perimeter methods
  - Demonstrated "is-a" relationship
  - Maintained geometric accuracy

[x] Challenge 2: Caravan and Siege Weapons
  - Created base Siege class
  - Implemented BatteringRam specialization
  - Added Catapult variation
  - Created movement cost calculations
  - Implemented cargo volume system
  - Added efficiency calculations

========================
Code Documentation Style
========================
In this project, we follow professional commenting practices that focus on clarity and purpose:

1. Comments explain "why" decisions were made, not "what" the code does
2. We document:
   - Design decisions and trade-offs
   - Non-obvious technical choices
   - Important implementation rationale
3. We avoid:
   - Comments that merely describe the code
   - Redundant class/method documentation when names are self-explanatory
   - Over-commenting obvious operations 