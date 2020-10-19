from flask import Flask, render_template
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()
sense.clear()
app = Flask(__name__)


@app.route('/')

def senseData():
    
    temp = sense.get_temperature()
    humidity = sense.get_humidity()

    temp = round(temp, 1)
    humidity = round(humidity, 1)

    Data = {'temp': temp, 'humidity': humidity}
    return render_template('senseData.html', **Data)

@app.route('/hello/<name>')
def hello(name):
    return render_template('page.html', name=name)
    

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
