"""Main script, uses other modules to generate sentences."""
from flask import Flask, request
from histogram import generate_word, frequency, word_count

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.


@app.route("/", methods=('GET', 'POST'))
def home():
    """Route that returns a web page containing the generated text."""
    # if request.method == 'GET':
    #     return f'"{word}" appears {word_frequency} times'
    generated_word = generate_word()
    word_frequency = frequency(generated_word, word_count)

    return f'"{generated_word}" appears {word_frequency} times'


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
