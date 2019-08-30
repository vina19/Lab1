class_name = []
classes_number = input('How many classes are you taking this semester? ')
while True:
    name = input('Enter the name of the class: ')
    length = len(classes_number)
    class_name.append(classes_number)
    class_name += [name]
print('The classes you are taking are: ')
print(class_name)

for n in class_name:
    print(n)
