from flask import Flask, request, jsonify
import openai
import os

app = Flask(__name__)

openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data['message']
    response = openai.Completion.create(
        engine="davinci",
        prompt=f"Conversation with a chatbot:\nUser: {message}\nBot:",
        temperature=0.5,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return jsonify({'response': response.choices[0].text.strip()}), 200

if __name__ == '__main__':
    app.run(debug=True, port=5000, host='0.0.0.0')


"""
I apologize for the continued errors. It seems that the API key is still not being properly authenticated. Here's a modified version of the code that should resolve the issue:


"""
