def run_quiz(questions):
    score = 0
    print("🧪 Welcome to the Python Quiz Game!\n")
    
    for i, q in enumerate(questions, start=1):
        print(f"Question {i}: {q['question']}")
        print(f"a) {q['options']['a']}")
        print(f"b) {q['options']['b']}")
        print(f"c) {q['options']['c']}")
        print(f"d) {q['options']['d']}")
        
        answer = input("Your answer (a/b/c/d): ").lower()
        if answer == q['answer']:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer is '{q['answer']}'\n")
    
    print(f"🎯 Your Final Score: {score}/{len(questions)}")
    if score == len(questions):
        print("🎉 Perfect score! Well done!")
    elif score >= len(questions) * 0.7:
        print("🎉 Great job! Keep practicing!")
    else:
        print("📘 Keep learning and try again!")

# Define quiz questions
quiz_questions = [
    {
        "question": "What will be the output of the following?\nx = 5\ny = x\nx = x + 2\nprint(y)",
        "options": {"a": "7", "b": "5", "c": "2", "d": "Error"},
        "answer": "b"
    },
    {
        "question": "Which keyword is used to define a function in Python?",
        "options": {"a": "define", "b": "def", "c": "function", "d": "fun"},
        "answer": "b"
    },
    {
        "question": "What is the output of this code?\nprint(\"2\" + \"5\")",
        "options": {"a": "7", "b": "25", "c": "Error", "d": "\"2 5\""},
        "answer": "b"
    },
    {
        "question": "Which of these is a valid Python variable name?",
        "options": {"a": "1value", "b": "value#1", "c": "value_1", "d": "value-1"},
        "answer": "c"
    },
    {
        "question": "What is the output?\na = [1, 2, 3]\nprint(len(a))",
        "options": {"a": "1", "b": "3", "c": "0", "d": "Error"},
        "answer": "b"
    },
    {
        "question": "Which data type is immutable in Python?",
        "options": {"a": "List", "b": "Set", "c": "Dictionary", "d": "Tuple"},
        "answer": "d"
    },
    {
        "question": "What will this return?\ntype(3.0)",
        "options": {"a": "<class 'int'>", "b": "<class 'float'>", "c": "<class 'str'>", "d": "<class 'double'>"},
        "answer": "b"
    },
    {
        "question": "What does this print?\nprint(bool(0))",
        "options": {"a": "True", "b": "False", "c": "0", "d": "Error"},
        "answer": "b"
    },
    {
        "question": "Which of the following is used to import a module in Python?",
        "options": {"a": "include", "b": "require", "c": "import", "d": "using"},
        "answer": "c"
    },
    {
        "question": "Which loop is used when we don't know how many times to repeat?",
        "options": {"a": "for loop", "b": "if loop", "c": "while loop", "d": "repeat loop"},
        "answer": "c"
    }
]

# Start quiz
run_quiz(quiz_questions)
