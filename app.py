from flask import Flask, render_template
from flask_socketio import SocketIO

# Flask instance
app = Flask(__name__)
# app.config['SECRET_KEY'] = ''


socketio = SocketIO(app)


def file_reader(file_path):
    with open(file_path) as file:
        full_file = file.read()
    return full_file


html_file = file_reader('pomodoro_main.html')


# Pomodoro home page
@app.route('/')
def html_page():
    return html_file


@socketio.on('connect', namespace='/main')
def handle_connect():
    print('Client connected')


if __name__ == '__main__':
    # Run Flask app with SocketIO
    socketio.run(app, debug=True, allow_unsafe_werkzeug=True)
