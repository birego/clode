from flask import Flask, request, render_template, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import joblib

app = Flask(__name__)

# Charger le modèle
model = joblib.load('model.joblib')
vectorizer = model['vectorizer']
question_vectors = model['question_vectors']
questions = model['questions']
réponses = model['réponses']

def calculate(expression):
    try:
        return str(eval(expression))
    except Exception as e:
        return "Désolé, je n'ai pas pu évaluer cette expression : " + str(e)

def get_most_probable_response(new_question, questions, réponses, vectorizer):
    if not new_question.strip():
        raise ValueError("La question ne peut pas être vide.")

    if any(char.isdigit() for char in new_question) and any(op in new_question for op in ['+', '-', '*', '/']):
        return calculate(new_question)

    new_question_vector = vectorizer.transform([new_question])
    similarités = cosine_similarity(new_question_vector, question_vectors)

    meilleur_index_similaire = similarités.argmax()
    probabilité_max = similarités[0, meilleur_index_similaire]

    if probabilité_max < 0.5:
        with open('amelioration.txt', 'a') as f:
            f.write(f'{new_question},{probabilité_max}\n')
        return "Je suis en phase d'entraînement et votre question est complexe pour mon niveau."

    if meilleur_index_similaire < 0 or meilleur_index_similaire >= len(questions):
        raise ValueError("Index de question invalide.")

    meilleure_réponse_probable = réponses[meilleur_index_similaire]

    if not meilleure_réponse_probable.strip():
        raise ValueError("La réponse à la question donnée est vide.")

    return meilleure_réponse_probable

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/ask', methods=['POST'])
def ask_question():
    data = request.get_json()
    question = data.get('question')
    response = get_most_probable_response(question, questions, réponses, vectorizer)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
