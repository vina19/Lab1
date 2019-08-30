list_of_classes = []
number_of_class = input("How many classes are you taking this semester? ")
while True:
    class_name = ('Enter the name of the class: ')
    list_of_classes.append(class_name)
    
print("The classes you are taking are: ")

for name in list_of_classes:
    print(list_of_classes + '\n')

