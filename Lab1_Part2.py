#list of classes
list_of_classes = []

#asking the classes that the user take this semester
number_of_class = input("How many classes are you taking this semester? ")

#loop of asking the user to enter the name of the class
while True:
    class_name = ('Enter the name of the class: ')
    list_of_classes.append(class_name)
    
print("The classes you are taking are: ")

for name in list_of_classes:
    print(list_of_classes + '\n')

