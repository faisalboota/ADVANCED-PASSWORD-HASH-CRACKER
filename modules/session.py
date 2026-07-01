import os
from datetime import datetime

SESSION_FOLDER = "sessions"
SESSION_FILE = os.path.join(SESSION_FOLDER, "history.log")


def initialize_session():

    os.makedirs(SESSION_FOLDER, exist_ok=True)


def save_session(data):

    initialize_session()

    with open(SESSION_FILE, "a", encoding="utf-8") as file:

        file.write("-" * 60 + "\n")
        file.write(f"Date       : {datetime.now()}\n")
        file.write(f"Algorithm  : {data['algorithm']}\n")
        file.write(f"Target Hash: {data['hash']}\n")
        file.write(f"Result     : {'FOUND' if data['found'] else 'NOT FOUND'}\n")
        file.write(f"Password   : {data['password']}\n")
        file.write(f"Attempts   : {data['attempts']}\n")
        file.write(f"Time       : {data['time']:.3f} sec\n")
        file.write(f"Speed      : {data['speed']:.0f} H/s\n")
        file.write("-" * 60 + "\n\n")