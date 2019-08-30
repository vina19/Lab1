from dataclasses import dataclass

@dataclass
class Student:
    name: str
    college_id: int
    gpa: float

vina = Student('Vina', 12345, 3.5)
print(vina)