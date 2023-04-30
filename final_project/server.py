from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/english_to_french")
def english_to_french_req():
    text_to_translate = request.args.get('Text To Translate')
    french_text = translator.english_to_french(text_to_translate)
    return french_text

@app.route("/french_to_english")
def french_to_english_req():
    text_to_translate = request.args.get('Text To Translate')
    english_text = translator.french_to_english(text_to_translate)
    return english_text

@app.route("/")
def render_index_page():
    # Write the code to render template
    render_template('index.page')

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8080)
