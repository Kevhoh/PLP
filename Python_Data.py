#Write a program that accepts user input to create a list of integers.
integers = [] #Create an empty list to store the user input

num = input("Enter an integer (to finish type 'done'): ") #prompt the user to enter data
while num != 'done': # while enables  user to continue entering data until they enter 'done'
    integers.append(int(num)) #append helps add user inputs into the list
    num = input("Enter another integer (to finish type 'done'): ")
#Then, compute the sum of all the integers in the list.
total = sum(integers)#comes after the loop

print("The sum of the listed integers is:", total)

#Create a tuple containing the names of five of your favorite books. 
favorite_books = ("Catching Fire", "Harry Potter", "The Hitchhiker's Guide to the Galaxy", "Good Omens", "Catch 22")
#Then, use a for loop to print each book name on a separate line.
for book in favorite_books:
    print(book)
    
#Write a program that uses a dictionary to store information about a person, such as their name, age, and favorite color.     
person = {} #Create an empty dictionary to store the user inputs
#Ask the user for input and store the information in the dictionary. 
name = input("What is Your name?")
age =int(input("What is your Age?"))#int converts age into an integer
color =input("What is your favorite Color?")
hobby = input("What is your Hobby?")
person["Name"] = name
person["Age"] = age
person["Favorite Color"] = color
person["Hobby"] =hobby
#Then, print the dictionary to the console.
print(person)

#Write a program that accepts user input to create two sets of integers.
set1 = set()
set2 = set() 

num = input("Enter an integer for set 1 (to finish type 'done'): ")
while num != 'done':
    set1.add(int(num))  
    num = input("Enter another integer for set 1 (to finish type 'done'): ")

num = input("Enter an integer for set 2 (to finish type 'done'): ")  
while num != 'done':
    set2.add(int(num))
    num = input("Enter another integer for set 2 (to finish type 'done'): ")
    
#Then, create a new set that contains only the elements that are common to both sets.
common_set = set1.intersection(set2)

print(" The common number(s) in the two sets are:", common_set)

#Create a program that can ask users for new words. lets use names of people
names = []
print("Write The names of all your Friends(Type 'end' to finish):")
name = input("")
while name != 'end':
    names.append(name)
    name = input("")
odd_names = [n for n in names if len(n) % 2 != 0]#add n to the list if the odd length s satisfied
print("Your friends With their names with odd number of characters are:")
print(odd_names)
    




#Create a program that stores a list of words. Then, use list comprehension to create a new list that contains only the words that have an odd number of characters.