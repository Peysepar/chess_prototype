from flask import Flask

# Flask instance
app = Flask(__name__)


def file_reader(file_path):
    with open(file_path) as file:
        full_file = file.read()
    return full_file


html_file = file_reader('pomodoro_main.html')


# Pomodoro home page
@app.route('/')
def html_page():
    return html_file


if __name__ == '__main__':
    app.run(debug=True)
    # print(html_file)
