from flask import Flask, request
from flask_restful import Api, Resource
import json

app = Flask(__name__)
api = Api(app)

@app.route("/")
def home():
    return {
        "message": "Welcome to Who Wants to Be a Millionaire API!"
    }


# Загружаем вопросы из JSON
with open("questions.json", "r") as file:
    questions = json.load(file)


class Questions(Resource):
    def get(self):
        result = []

        for q in questions:
            result.append({
                "id": q["id"],
                "question": q["question"],
                "options": q["options"]
            })

        return result, 200


class Answer(Resource):
    def post(self):
        data = request.get_json()

        question_id = data.get("id")
        user_answer = data.get("answer")

        for q in questions:

            if q["id"] == question_id:

                if q["answer"].lower() == user_answer.lower():

                    return {
                        "correct": True,
                        "message": "Correct answer!"
                    }, 200

                else:

                    return {
                        "correct": False,
                        "message": "Wrong answer!"
                    }, 200

        return {
            "message": "Question not found"
        }, 404


api.add_resource(Questions, "/questions")
api.add_resource(Answer, "/answer")

if __name__ == "__main__":
    app.run(debug=True)