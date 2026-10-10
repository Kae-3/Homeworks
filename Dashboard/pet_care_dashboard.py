class Pet:
    """Parent Pet class demonstrating Encapsulation."""
    def __init__(self, name: str, age: int, health_score: int):
        self.name = name
        self.age = age
        # Encapsulation: Private attribute denoted by double underscore
        self.__health_score = max(0, min(100, health_score))

    # Getter method to safely access private health score
    def get_health_score(self) -> int:
        return self.__health_score

    # Setter method to safely update private health score with validation
    def set_health_score(self, score: int) -> None:
        if 0 <= score <= 100:
            self.__health_score = score
            print(f"Updated {self.name}'s health score to {self.__health_score}%.")
        else:
            print(f"Invalid health score ({score}). Must be between 0 and 100.")

    def make_sound(self) -> str:
        """Base method to be overridden by child classes."""
        return "Some generic pet sound"

    def describe_care_routine(self) -> str:
        """Polymorphic method for daily pet care requirements."""
        return "Provide food, clean water, and shelter."


class Dog(Pet):
    """Child class representing a Dog."""
    def make_sound(self) -> str:
        return "Woof! Woof!"

    def describe_care_routine(self) -> str:
        return "Needs 45 minutes of walking and high-protein kibble."


class Cat(Pet):
    """Child class representing a Cat."""
    def make_sound(self) -> str:
        return "Meow!"

    def describe_care_routine(self) -> str:
        return "Needs litter box cleaning, daily grooming, and wet food."


class Bird(Pet):
    """Child class representing a Bird."""
    def make_sound(self) -> str:
        return "Chirpy chirp!"

    def describe_care_routine(self) -> str:
        return "Needs cage cleaning, seed mix, and daily flight exercise."


# Main Dashboard Execution
if __name__ == "__main__":
    print("=== PET CARE DASHBOARD ===\n")

    # Creating pet instances
    dog = Dog(name="Buddy", age=3, health_score=85)
    cat = Cat(name="Luna", age=2, health_score=90)
    bird = Bird(name="Rio", age=1, health_score=95)

    # List of pet objects to demonstrate Polymorphism in action
    pets: list[Pet] = [dog, cat, bird]

    print("--- 1. Polymorphism in Action (Looping through Pet objects) ---")
    for pet in pets:
        print(f"Pet Name : {pet.name} ({pet.__class__.__name__})")
        print(f"  Sound  : {pet.make_sound()}")
        print(f"  Care   : {pet.describe_care_routine()}")
        print(f"  Health : {pet.get_health_score()}%\n")

    print("--- 2. Encapsulation & Safe Updates (Getters & Setters) ---")
    # Attempting to modify private attribute safely via setter
    dog.set_health_score(92)

    # Attempting an invalid health update
    cat.set_health_score(150)

    print(f"\nFinal Health Check - {dog.name}: {dog.get_health_score()}%")