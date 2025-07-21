from flask import Flask, render_template, request
import datetime

app = Flask(__name__)

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I'm a simple chatbot created by Mridul."
    elif "who made you" in user_input:
        return "I was created by Mridul Yadav during an internship project."
    elif "time" in user_input:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")
    elif "date" in user_input:
        return "Today's date is " + datetime.datetime.now().strftime("%Y-%m-%d")
    elif "python" in user_input:
        return "Python is a powerful, easy-to-learn programming language."
    elif "bye" in user_input or "exit" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "Sorry, I don't understand that."

@app.route("/", methods=["GET", "POST"])
def index():
    user_input = ""
    bot_response = ""
    if request.method == "POST":
        user_input = request.form["message"]
        bot_response = get_response(user_input)
    return render_template("index.html", user_input=user_input, bot_response=bot_response)

if __name__ == "__main__":
    app.run(debug=True)
