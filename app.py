from flask import Flask, render_template, request

app = Flask(__name__)

project_types = {
        

}

def validate_form(form_response):
    return


@app.route('/')
def index():
    return render_template('index.html')