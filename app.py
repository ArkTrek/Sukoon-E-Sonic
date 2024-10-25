from flask import Flask, session, render_template, request, redirect, url_for
import time
import openai
import json
import os
import pygame  # Import Pygame

app = Flask(__name__)
app.secret_key = 'SukoonIsHere'  # Change this to a random secret key

openai.api_key = 'api-key'  # Set up your API key here

# Initialize Pygame mixer for audio playback
pygame.mixer.init()

def generate_questions():
    with open('questions.json', encoding='utf-8') as f:
        return json.load(f)

@app.route('/', methods=['GET', 'POST'])
def index():
    # Load and play intro music
    pygame.mixer.music.load('static/audio/sonic-theme.mp3') 
    pygame.mixer.music.play(-1)

    if request.method == 'POST':
        session.clear()
        session['name'] = request.form['name']
        session['question_number'] = 0
        session['user_answers'] = []
        session['session_status'] = 1
        session['start_time'] = time.time()
        pygame.mixer.music.stop()  # Stop music before redirect
        return redirect(url_for('quiz'))
    
    return render_template('index.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    # Load and play quiz theme music
    pygame.mixer.music.load('static/audio/sonic-race.mp3') 
    pygame.mixer.music.play(-1)
    questions = generate_questions()

    if 'question_number' not in session:
        session['question_number'] = 0
        session['user_answers'] = []

    question_number = session['question_number']

    if 'start_time' in session and time.time() - session['start_time'] > 240:
        pygame.mixer.music.stop()  # Stop music before redirect
        return redirect(url_for('result'))

    if request.method == 'POST':
        answer = request.form.get('answer')
        if answer:
            session['user_answers'].append(answer)
            session['question_number'] += 1

        if session['question_number'] >= len(questions):
            pygame.mixer.music.stop()  # Stop music before redirect
            return redirect(url_for('result'))

    current_question = questions[question_number] if question_number < len(questions) else None
    return render_template('quiz.html', question=current_question, question_number=question_number + 1)

@app.route('/result')
def result():
    # Load and play victory music
    pygame.mixer.music.load('static/audio/sonic-victory.mp3') 
    pygame.mixer.music.play(-1)
    user_answers = session.get('user_answers', [])
    questions = generate_questions()
    score, category = calculate_score(user_answers, questions)
    session.clear()
    return render_template('result.html', answers=user_answers, score=score, category=category)
    
def calculate_score(user_answers, questions):
    score = 0
    # Calculate score based on answers
    for answer in user_answers:
        if answer == 'A':
            score += 1
        elif answer == 'B':
            score += 2
        elif answer == 'C':
            score += 3

    # Determine category based on score
    if score <= 10:
        score = 3
        category = "Needs More Emotional Care!"
    elif score <= 20:
        score = 7.5
        category = "Just Fine I Guess..."
    else:
        score = 10
        category = "Is Emotionally Strong!"

    return score, category

if __name__ == '__main__':
    app.run(debug=True)
