from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import silly_story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def show_form():
    """Show form to input madlib words"""
    input_prompts = silly_story.prompts

    return render_template("questions.html", prompts=input_prompts)

@app.get("/results")
def show_results():
    """Show results of madlib inputs"""
    answers = {}
    for prompt in silly_story.prompts:
        answers[prompt] = request.args[prompt]

    result = silly_story.get_result_text(answers)

    return render_template("results.html", story_result = result)



