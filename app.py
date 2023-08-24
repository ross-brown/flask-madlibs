from flask import Flask, render_template, request
from flask_debugtoolbar import DebugToolbarExtension

from stories import stories

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolbarExtension(app)


@app.get("/")
def show_dropdown():
    """Show dropdown of stories."""
    return render_template("dropdown.html", stories=stories.values())


@app.get("/questions")
def show_form():
    """Show form to input madlib words"""
    story_code = request.args['story_code']
    input_prompts = stories[story_code].prompts

    return render_template("questions.html",
                           story_code=story_code,
                           prompts=input_prompts)

@app.get("/<story_code>/results")
def show_results(story_code):
    """Show results of madlib inputs"""
    current_story = stories[story_code]

    result = current_story.get_result_text(request.args)

    return render_template("results.html", story_result=result)
