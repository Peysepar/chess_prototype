import datetime
import time
from flask import Flask
from flask_socketio import SocketIO

# # Break html
# break_screen = '''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>My Pomodoro</title>
#     </head>
#     <body>
#         <h1 style="color:red">STOP WORKING!</h1>
#         <p>Good job!</p>
#     </body>
#     </html>
#     '''
#
# # Back to work html
# work_screen = '''
#     <!DOCTYPE html>
#     <html>
#     <head>
#         <title>My Pomodoro</title>
#     </head>
#     <body>
#         <h1 style="color:red">BREAK IS OVER, GO BACK TO WORK!</h1>
#     </body>
#     </html>
#     '''

# # Write the HTML code to a file
# with open('break.html', 'w') as b, open('work.html', 'w') as w:
#     b.write(break_screen)
#     w.write(work_screen)
#

app = Flask(__name__)

socketio_app = SocketIO(app)


def pomodoro():
    work_time = 25 * 60
    rest_time = 5 * 60

    start_time = datetime.datetime.now()

    # work time
    while True:
        socketio_app.emit('timer_update', {'time_left': work_time}, namespace='/main')
        time.sleep(work_time)  # work time begins
        socketio_app.emit('break_start', namespace='/main')
        time.sleep(rest_time)  # break time begins
        socketio_app.emit('work_start', namespace='/main')


#         work_topic = input("What did you work on?\n")
#         end_time = datetime.datetime.now()
#         with open(f"work_log_{datetime.date.today().strftime('%m-%d')}.txt", 'a') as f2:
#             f2.write(
#                 f"Worked on {work_topic}, started at {start_time.strftime('%Y-%m-%d %H:%M:%S')} \
# for {str(end_time - start_time).split('.')[0]} long (H:MM:SS).\n")
#         print(f"Your break started at {datetime.datetime.now().strftime('%H:%M:%S')}.")
#         time.sleep(rest_time)
#
#         # Open the BACK TO WORK screen a web browser
#         webbrowser.open('file:///Users/kasperpeysepar/PycharmProjects/chess_prototype/work.html')

        ready = input("Whenever ready type y.\n")
        if ready.lower() == 'y':
            start_time = datetime.datetime.now()
            continue


if __name__ == '__main__':
    pomodoro()
