





import random




questions = {
"What is Python?" : "A high-level programming language",
"What is a variable?" : "A container for storing data values",
"What is a list?" : "A collection of ordered items",
"What is a dictionary?" : "A collection of key-value pairs",
"What is a function?" : "A block of reusable code",
"What is a loop?" : "A way to repeat code multiple times",
"What is an if statement?" : "A condition-based decision structure",
"What is a class?" : "A blueprint for creating objects",
"What is an object?" : "An instance of a class",
"What is indentation in Python?" : "Spacing used to define code blocks",
}



def python_trivia_game():
    question_list = list(questions.keys())
    total_questions = 10;
    score = 0;
    
    selected_questions = random.sample(question_list, total_questions );
    for idx , question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("your answer: ").lower()
        correct_answer = questions[question]
        
        if user_answer == correct_answer.lower():
            print("CORRECT!\n")
            score += 1
            
        else:
            print(f"Wrong. The correct answer is :{correct_answer}.\n  ")
        
    
    
python_trivia_game()


 