#list of classes
list_of_classes = []

#asking the classes that the user take this semester
number_of_class = int(input('How many classes are you taking this semester? '))

#loop of asking the user to enter the name of the class
for n in range(number_of_class):
    class_name = input('Enter the name of the class: ')
    list_of_classes.append(class_name)
    
print('The classes you are taking are: ')

for name in list_of_classes:
    print('\n'.join(list_of_classes))

