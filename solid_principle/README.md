Defining the SOLID principles in layman's terms (based on this video https://www.youtube.com/watch?v=0mcP8ZpUR38):

1. Single Responsibility
    Make things (classes, functions, etc.) responsible for fulfilling one type of role.
        e.g. Refactor code responsibilities into separate classes.

2. Open/Closed
    Open for extension but closed for modification.
    Be able to add new functionality to existing code easily without modifying existing code.
        e.g. Use abstract classes. These can define what subclasses will require and strengthen Principle 1. by separating code duties.

3. Liskov Substitution
    When a class inherits from another class, the program shouldn't break and you shouldn't need to hack anything to use the subclass.
        e.g. Define constructor arguments to keep inheritance flexible.

4. Interface Segregation
     Make interfaces (parent abstract classes) more specific, rather than generic.
        e.g. Create more interfaces (classes) if needed and/or provide objects to constructors.

5. Dependency Inversion
    Make classes depend on abstract classes rather than non-abstract classes.
        e.g. Make classes inherit from abstract classes.