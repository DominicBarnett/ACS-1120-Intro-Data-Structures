"""Main script, uses other modules to generate sentences."""
from flask import Flask
from cleanup import source_text
from markov import markov_chain

app = Flask(__name__)

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.


@app.route("/", methods=('GET', 'POST'))
def home():
    """Route that returns a web page containing the generated text."""
    # generated_word = generate_word()
    # word_frequency = frequency(generated_word, histogram_test)

    # return f'"{generated_word}" appears {word_frequency} times'
    mc = markov_chain()
    mc.create_chain_from_text(corpus=source_text)  # Change this to your text file's path
    generated_text = mc.walk(length=10)
    return f" The generated sentence is--------:  {generated_text}"


if __name__ == "__main__":
    """To run the Flask server, execute `python app.py` in your terminal.
       To learn more about Flask's DEBUG mode, visit
       https://flask.palletsprojects.com/en/2.0.x/server/#in-code"""
    app.run(debug=True)
