
#1. Let the user input a string.
user_input = input("Please input a string: ")

num_words = len(user_input.split())

isEven = 'even' if (num_words%2 == 0) else 'odd'

#2. Display how many words the user inputs. 3. display number of words is either odd or even.
print(f"Number of words: {num_words}\nIt is an {isEven} number")