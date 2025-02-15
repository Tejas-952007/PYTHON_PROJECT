# This is a program for a quiz show.
# The feature of the program is that if the user gives the correct answer, the reward is added to the reward variable.
# The program features 5 questions and the reward is added to the reward variable.
# Author: Tejas Ingle
# Date: 10/10/2021

# Print the welcome message for the quiz show
print("""
      +++++++++++++++++++++++++++++++++++
      +                                 +
      + <<<---Tejas new quiz show--->>> +
      +                                 +
      +++++++++++++++++++++++++++++++++++
      """ )
print("\n")
print("\t\t-:- Welcome to the quiz show\n")

# Initialize counters for incorrect answers and reward
else_count = 0
reword = 0

# Function for the first quiz question
def quiz_example():
    global else_count
    global reword
    print(f"Question 1: What is 2+2?")
    if(input() == '4'):
        print("Correct!")
        reword += 1000  # Add reward for correct answer
    else:
        print("Incorrect!")
        else_count += 1  # Increment else_count for incorrect answer
    return reword

# Function for the second quiz question
def quiz_example2():
    global else_count
    global reword
    print(f"Question 2: What is 2+3?")
    if(input() == '5'):
        print("Correct!")
        reword += 2000  # Add reward for correct answer
    else:
        print("Incorrect!")
        else_count += 1  # Increment else_count for incorrect answer
    return reword

# Function for the third quiz question
def quiz_example3():
    global else_count
    global reword
    print(f"Question 3: What is 16-90?")
    if(input() == '-74'):
        print("Correct!")
        reword += 4000  # Add reward for correct answer
    else:
        print("Incorrect!")
        else_count += 1  # Increment else_count for incorrect answer
    return reword

# Function for the fourth quiz question
def quiz_example4():
    global else_count
    global reword
    print(f"Question 4: What is 1738/356?")
    if(input() == '4.875'):
        print("Correct!")
        reword += 8000  # Add reward for correct answer
    else:
        print("Incorrect!")
        else_count += 1  # Increment else_count for incorrect answer
    return reword

# Function for the fifth quiz question
def quiz_example5():
    global else_count
    global reword
    print(f"Question 5: What is 8994+8803?")
    if(input() == '17797'):
        print("Correct!")
        reword += 16000  # Add reward for correct answer
    else:
        print("Incorrect!")
        else_count += 1  # Increment else_count for incorrect answer
    return reword

# Call the quiz functions to ask all questions
quiz_example()
quiz_example2()
quiz_example3()
quiz_example4()
quiz_example5()

# Print the number of incorrect answers
print(f"The else condition was executed {else_count} times")

# Print the total reward
print(f"Total reward: {reword}")

# Check the number of incorrect answers and print the final reward message
if else_count == 0:
    print(f"\t\t\t\t\t--Your reward is {reword}--")
if else_count == 5:
    print(f"\t\t\t\t\t--Your reward is -{reword}--")
    print("\n\t\t\t\t\t--give the reward equal money to quiz show--")

# Print the thank you message
print("\n\t\t\t\t----->Thank you for participating in the quiz show<-----")