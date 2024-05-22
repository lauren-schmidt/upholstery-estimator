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

project_type_prices = {
    'drc': (65.00, 40.00),
    'drc-a': (75.00, 50.00),
    'drc-b': (150.00, 125.00),
    'drc-ab': (150.00, 125.00),
    'o': (200.00, 200.00),
    'o-o': (300.00, 300.00),
    'fs': (75.00, 50.00),
    'bc': (0.00, 0.00),
    'tp': (0.00, 0.00)
}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Calculate the price 
        project_type = request.form['projecttype']
        seat_type = request.form['seattype']
        price = 10.00  # Initializing price variable

        # Check if the project type is in the project_type_prices dictionary
        if project_type in project_type_prices:
            price = project_type_prices[project_type][0] if seat_type == 'a' else project_type_prices[project_type][1]
        
        #Check for upholstery vs foam 
        if request.form['upholsteryradio'] == 'upholstery_foam':
            price = price + 30.00
        
        #Check for checked add-ons 
        if request.form['addons1'] == 'piping':
            price = price + 5.00
        if request.form['addons2'] == 'seaming':
            price = price + 40.00
        if request.form['addons3'] == 'pattmatch':
            price = price + 5.00
        
        #Check for number of buttons 
        numBtn = request.form['numbtn']
        price = price + (10.00 * int(numBtn))

        #Check for feet of decorative tacks 
        numTacks = request.form['numtacks']
        price = price + (20.00 * int(numTacks))

        #Convert price to string
        price = str(price)
        return render_template('index.html', project_types=project_types, seat_types=seat_types, estimate = price) 
    
    return render_template('index.html', project_types=project_types, seat_types=seat_types, estimate = '0.00')

if __name__ == '__main__':
    app.run(debug=True)
