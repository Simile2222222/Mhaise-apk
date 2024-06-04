from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# In-memory storage for requests (for simplicity)
driver_requests = []
vip_requests = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/request_driver', methods=['GET', 'POST'])
def request_driver():
    if request.method == 'POST':
        details = {
            'name': request.form['name'],
            'pickup_location': request.form['pickup_location'],
            'destination': request.form['destination']
        }
        driver_requests.append(details)
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/request_vip', methods=['GET', 'POST'])
def request_vip():
    if request.method == 'POST'):
        details = {
            'name': request.form['name'],
            'pickup_location': request.form['pickup_location'],
            'destination': request.form['destination']
        }
        vip_requests.append(details)
        return redirect(url_for('index'))
    return render_template('index.html')

@app.route('/driver_requests')
def show_driver_requests():
    return render_template('driver_requests.html', requests=driver_requests)

@app.route('/vip_requests')
def show_vip_requests():
    return render_template('vip_requests.html', requests=vip_requests)

if __name__ == '__main__':
    app.run(debug=True)
