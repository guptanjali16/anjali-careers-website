from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_anjali():
    return render_template('home.html')

print(__name__)

if __name__ == '__main__':
   print('im inside main')
   app.run(host='0.0.0.0', debug=True)
