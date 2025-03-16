import os
from openai import OpenAI
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

client = OpenAI(
    api_key='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')

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/chat', methods=['POST'])
def ask():
    try:
        data = request.get_json()
        user_input = data["user_input"]
        prompt1 = (
            f'a user said:"{user_input}" '
            f'you are a compassionate mental health therapist that helps veterans and veterans only with mental health'
            f'Respond in a conversational manner, offering empathetic support and listen actively'
            f'keep your tone warm and understanding, non judgemental'
        )

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "you are a helpful and empathetic mental health assisstant helping veterans"},
                {"role": "user", "content": prompt1}
            ]
        )

        answer = response.choices[0].message.content.strip()
        return jsonify({"response": answer})
    except Exception as e:
        print(e)
        return jsonify({"response": "sorry something went wrong"})
    
@app.route("/breathing_exercise")
def breathing_exercise():
    return render_template("breathing_exercise.html")

@app.route("/funny_cat_videos") # This is the new route!
def funny_cat_videos():
    return render_template("funnycatvid.html") # This renders the funny cat video page
@app.route("/funny_dog_videos") # This is the new route!
def funny_dog_videos():
    return render_template("funnydogvid.html") # This renders the funny dog video page

if __name__ == "__main__":
    app.run(debug=True)
