from flask import Flask, render_template, request
app = Flask(__name__)

<<<<<<< Updated upstream
kinoko_count = 3
takenoko_count = 5
messages = ['Kinoko is wonrderful!', 'Takenoko is awesome!']

=======
kitono_count = 3
takenoko_count = 5
messages = ["kinoko is wonderful","Takenoko is awesome"]
>>>>>>> Stashed changes
@app.route('/')
def top():
    return render_template('index.html', **vars())

@app.route('/vote', methods=['POST'])
def answer():
<<<<<<< Updated upstream
    kinoko_percent = kinoko_count / (kinoko_count + takenoko_count) * 100
    takenoko_percent = takenoko_count / (kinoko_count + takenoko_count) * 100
=======
    kitono_percent = kitono_count / (kitono_count + takenoko_count) *100
    takenoko_precent = takenoko_count / (takenoko_count + kitono_count) * 100

>>>>>>> Stashed changes
    return render_template('vote.html', **vars())

if __name__ == '__main__':
    app.run(debug=True)
