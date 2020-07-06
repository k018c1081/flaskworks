from flask import Flask
import datetime
app = Flask(__name__)

@app.route('/')
def top():
    current_time = datetime.datetime.now()
    return current_time.strftime('%m/%d %H:%M')

if __name__ == "__main__":
    app.run(debug=True)