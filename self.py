class Student:
    def __init__(self, name, college_id, gpa):
        self.name = name
        self.college_id = college_id
        self.gpa = gpa
    
    def __str__(self):
        return f'Name: {self.name}, id: {self.college_id}, gpa: {self.gpa}'

def main():
    alice = Student('Alice', 'aa123', 4.0)
    bob = Student('Bob', 'bb123', 3.5)
    vina = Student('Vina', 'cc123', 3.5)

    print(vina.name)
    print(vina.gpa)

    print(vina)

main()

class Author:
    def __init__(self, name, books):
        self.name = name
        self.books = []
    
    def publish(self, title):
        self.books.append(title)

    def __str__(self):
        titles = ', '.join(self.books) or 'No published books'
        return f'{self.name}. Books: {self.books}'

def main():
    author1 = Author('Mayazaki')
    author2 = Author('Marie', 'Miiko')

    author.publish('In the Corner of the World')
    


