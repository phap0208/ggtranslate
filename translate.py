from flask import Flask, request, render_template
import openai

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('translate.html')


@app.route('/translate', methods=['POST'])
def translate():
    source_text = request.form['source_text']
    source_lang = request.form['source_lang']
    target_lang = request.form['target_lang']

    openai.api_key = "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"
    model_engine = "text-davinci-002"

    response = openai.Completion.create(
        engine=model_engine,
        prompt="translate " + source_text + " from " + source_lang + " to " + target_lang,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    target_text = response['choices'][0]['text'].strip()

    return render_template('translate.html', source_text=source_text, target_text=target_text)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
