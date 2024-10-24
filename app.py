from flask import Flask, session, render_template, request, redirect, url_for
import time
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

def generate_questions():
    # Load questions from your JSON file
    with open('questions.json') as f:
        return json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        session.clear()  # Clear previous session data
        session['name'] = request.form['name']
        session['question_number'] = 0  # Start from the first question
        session['user_answers'] = []  # Initialize the user_answers list
        session['start_time'] = time.time()  
        session['sonic_position'] = 0  # Initialize Sonic's position
        return redirect(url_for('quiz'))
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    questions = generate_questions()  # Load questions from the JSON file
    
    # Initialize question number if it doesn't exist
    if 'question_number' not in session:
        session['question_number'] = 0  # Reset to start
        session['user_answers'] = []  # Reset answers
        session['sonic_position'] = 0  # Initialize Sonic's position

    question_number = session['question_number']
    
    # Check if the time limit has been reached
    if 'start_time' in session and time.time() - session['start_time'] > 120:
        return redirect(url_for('result'))  # Redirect to result if time's up

    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer:
            session['user_answers'].append(answer)  # Store user's answer
            session['question_number'] += 1  # Move to the next question

            # Move Sonic to the right
            session['sonic_position'] += 2  # Increment Sonic's position for each question answered

        # Check if the last question has been answered
        if session['question_number'] >= len(questions):
            session['sonic_position'] = 1000  # Move Sonic to the rightmost part (adjust based on your layout)
            return redirect(url_for('result'))  # Redirect to result after all questions

    current_question = questions[question_number] if question_number < len(questions) else None
    sonic_position = session.get('sonic_position', 0)  # Sonic's position
    return render_template('quiz.html', question=current_question, question_number=question_number + 1, sonic_position=sonic_position)

def calculate_score(user_answers, questions):
    score = 0
    # Assuming the correct answers are stored in the questions list
    correct_answers = [
        "A",  # For question 1
        "B",  # For question 2
        "A",  # For question 3
        "C",  # For question 4
        "B",  # For question 5
        "A",  # For question 6
        "C",  # For question 7
        "A",  # For question 8
        "B",  # For question 9
        "C"   # For question 10
    ]

    # Loop through user answers and compare with correct answers
    for user_answer, correct_answer in zip(user_answers, correct_answers):
        if user_answer == correct_answer:
            score += 1  # Increment score for each correct answer

    # Determine category based on score
    if score <= 3:
        category = "Low"
    elif 4 <= score <= 7:
        category = "Neutral"
    else:
        category = "High"

    return score, category

@app.route('/result')
def result():
    user_answers = session.get('user_answers', [])
    questions = generate_questions()  # Load questions from JSON again
    score, category = calculate_score(user_answers, questions)  # Calculate the score and category

    session.clear()  # Clear session after finishing
    return render_template('result.html', answers=user_answers, score=score, category=category)

if __name__ == '__main__':
    app.run(debug=True)
