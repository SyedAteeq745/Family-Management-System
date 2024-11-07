# Define the Person class
class Person:	
    def __init__(self, name):
        self.name = name

# Define the Child class inheriting from Person
class Child(Person):
    def __init__(self, name, biological_parent):
        super().__init__(name)
        self.biological_parent = biological_parent

    # Method to check if the child is a stepchild
    def is_step_child(self, parent):
        return self.biological_parent != parent

# Define the Couple class
class Couple:
    def __init__(self, partner1, partner2):
        self.partner1 = partner1
        self.partner2 = partner2
        self.children = []  # List to store children

    # Method to check if the couple has kids
    def has_kids(self):
        return len(self.children) > 0

    # Method to adopt a child if they don't have any
    def adopt_kid(self, child):
        if not self.has_kids():
            self.children.append(child)
            print(f"{self.partner1.name} and {self.partner2.name} have adopted {child.name}.")

    # Method to display parents of a child
    def parents(self, child):
        return f"Parents of {child.name}: {self.partner1.name} and {self.partner2.name}"

# Example usage

# Create two partners for the couple
partner1 = Person("Alice")
partner2 = Person("Bob")

# Initialize the Couple
couple = Couple(partner1, partner2)

# Create a biological child for Alice
biological_child = Child("Charlie", partner1)

# Check if the couple has kids; if not, adopt one
if not couple.has_kids():
    couple.adopt_kid(biological_child)

# Create another child who is a stepchild
step_child = Child("Daisy", partner2)  # This child is a biological child of partner2

# Add the stepchild to the children list
couple.children.append(step_child)

# Check if Daisy is a stepchild for Alice
print(f"Is {step_child.name} a stepchild of {partner1.name}? {step_child.is_step_child(partner1)}")

# Show the parents of Charlie and Daisy
print(couple.parents(biological_child))
print(couple.parents(step_child))
