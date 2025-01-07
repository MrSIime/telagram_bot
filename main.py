import subprocess
import logging
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import threading
from archiver import LogArchiver
import os
import time

with open("off.txt", "w") as data:
    data.write("")

def background_task():
    global bot_process
    while not stop_event.is_set():
        try:
            logging.info("Running bot.pyw script...")
            bot_process = subprocess.Popen(["pythonw", "bot.pyw"])
            bot_process.wait()
            logging.info(f"Script executed successfully with return code {bot_process.returncode}")
        except subprocess.CalledProcessError as e:
            logging.error(f"Error occurred during script execution: {e}")
            logging.exception(e)
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
            logging.exception(e)

        try:
            with open("off.txt", "r") as data:
                command = data.read().strip()
                logging.info(f"Command from off.txt: {command}")

            if command == "off":
                logging.info("Stop command received. Exiting...")
                stop_event.set()
                on_exit()
            else:
                logging.info(f"Continuing execution. Command: {command}")
        except Exception as e:
            logging.error(f"Error reading off.txt: {e}")
            logging.exception(e)

        time.sleap(3)


def on_exit(icon=None, item=None):
    logging.info("Stopping application...")
    stop_event.set()
    if bot_process is not None:
        logging.info("Terminating bot.py process...")
        bot_process.terminate()
        bot_process.wait()
    if icon:
        icon.stop()
    logging.info("Application stopped.")
    os._exit(0)


def create_icon():
    try:
        return Image.open("icon.png")
    except FileNotFoundError:
        logging.info("Icon file not found. Creating a default icon.")
        size = 64
        image = Image.new("RGB", (size, size), (255, 255, 255))
        draw = ImageDraw.Draw(image)
        draw.rectangle((size // 4, size // 4, 3 * size // 4, 3 * size // 4), fill=(0, 128, 255))
        return image


def setup_tray():
    icon_image = create_icon()
    icon = Icon("My App", icon_image, menu=menu)
    icon.run()


def run_background_thread():
    thread = threading.Thread(target=background_task, daemon=True)
    thread.start()


def run_application():
    run_background_thread()
    setup_tray()


if __name__ == "__main__":
    archiver = LogArchiver(archive_name="logs\\logs_main.zip", log_file="logs\\main.log")
    archiver.save_to_zip()
    archiver.setup_logging()
    stop_event = threading.Event()
    bot_process = None
    menu = Menu(MenuItem("Вихід", on_exit))
    run_application()
