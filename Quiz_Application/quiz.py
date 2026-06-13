# Build A Simple Quiz Application : 

quiz_questions = [
    {
        "question": "Which of the following is a valid Python variable name?",
        "options": ["2name", "user_name", "user-name", "class"],
        "answer": "user_name"
    },
    {
        "question": "What data type is the value 25?",
        "options": ["float", "str", "int", "bool"],
        "answer": "int"
    },
    {
        "question": "What data type is the value 3.14?",
        "options": ["int", "float", "str", "list"],
        "answer": "float"
    },
    {
        "question": "Which data type represents True or False values?",
        "options": ["str", "bool", "int", "float"],
        "answer": "bool"
    },
    {
        "question": "What is the output of type('Hello')?",
        "options": ["int", "str", "list", "bool"],
        "answer": "str"
    },
    {
        "question": "Which symbol is used to assign a value to a variable?",
        "options": ["==", "=", ":", "+"],
        "answer": "="
    },
    {
        "question": "What data type is created by [1, 2, 3]?",
        "options": ["tuple", "set", "list", "dict"],
        "answer": "list"
    },
    {
        "question": "Which of the following creates a tuple?",
        "options": ["[1, 2, 3]", "{1, 2, 3}", "(1, 2, 3)", '{"a": 1}'],
        "answer": "(1, 2, 3)"
    },
    {
        "question": "What will be the value of x after x = 10?",
        "options": ["10", "'10'", "int", "None"],
        "answer": "10"
    },
    {
        "question": "Which function is used to check the data type of a variable?",
        "options": ["check()", "typeof()", "datatype()", "type()"],
        "answer": "type()"
    }
]

print("=========================")
print("Welcome To Quiz!!!")
print("=========================")
score = 0
while True:
    choice = int(input("***ENTER YOUR CHOICE*** "\
                       "\n 1.START QUIZ "\
                       "\n 2.SHOW SCORE "\
                       "\n 3.EXIT :- "))
    if(choice == 1):
        for quiz in quiz_questions:
            print("=========================")
            for key,value in quiz.items():
                if(key != "answer"):
                    print(f"{key} : {value}")
                else:
                    user_select = input("Enter your answer :- ")
                    if(user_select == value):
                        print("Correct Answer!!")
                        score += 1
                    else:
                        print("Wrong Answer!!")
                    print(f"Current Score :- {score}")
    elif(choice == 2):
        print("=========================")
        print(f"Total Question : 10.")
        print(f"Correct Answer : {score}.")
        print(f"Score : {score}/10.")
        print("=========================")
    elif(choice == 3):
        print("=========================")
        print("Thank You For Playing A Quiz!!")
        print("=========================")
        break
    else:
        print("=========================")
        print("Incorrect Choice!!")
        print("=========================")
