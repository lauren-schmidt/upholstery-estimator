from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for session management

project_types = {
    # Fill this with your project types, e.g.
    'drc': 'Dining Room Chair',
    'drc-a': 'Dining Room Chair with Arms',
    'drc-b': 'Dining Room Chair with Back',
    'drc-ab': 'Dining Room Chair with Arms and Back',
    'o' : 'Ottoman',
    'o-o' : 'Ottoman - Oversized',
    'fs' : 'Foot Stool',
    'bc' : 'Box Cushion',
    'tp' : 'Throw Pillow'
}

seat_types = {
    'a' : 'Attached',
    'd' : 'Drop-In'
}

def validate_form(form_response):
    # Check if all required fields are filled
    
    
    # Additional validation can be added here

    return True

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
       
        if validate_form(request.form):
            
            return redirect(url_for('index'))  # Redirect to avoid resubmission on refresh

    return render_template('index.html', project_types=project_types, seat_types=seat_types)

if __name__ == '__main__':
    app.run(debug=True)
