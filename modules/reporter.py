import json
import os
from datetime import datetime


REPORT_FOLDER = "reports"


def ensure_report_folder():
    os.makedirs(REPORT_FOLDER, exist_ok=True)


def save_text_report(data):

    ensure_report_folder()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = os.path.join(
        REPORT_FOLDER,
        f"report_{timestamp}.txt"
    )

    with open(filename, "w", encoding="utf-8") as file:

        file.write("=" * 60 + "\n")
        file.write("PASSWORD HASH CRACKER REPORT\n")
        file.write("=" * 60 + "\n\n")

        file.write(f"Date      : {datetime.now()}\n")
        file.write(f"Algorithm : {data['algorithm']}\n")
        file.write(f"Hash      : {data['hash']}\n")
        file.write(f"Status    : {'FOUND' if data['found'] else 'NOT FOUND'}\n")
        file.write(f"Password  : {data['password']}\n")
        file.write(f"Attempts  : {data['attempts']}\n")
        file.write(f"Time      : {data['time']:.3f} sec\n")
        file.write(f"Speed     : {data['speed']:.0f} H/s\n")

    return filename


def save_json_report(data):

    ensure_report_folder()

    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    filename = os.path.join(
        REPORT_FOLDER,
        f"report_{timestamp}.json"
    )

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    return filename