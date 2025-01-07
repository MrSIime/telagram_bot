import logging
import os
import zipfile


class LogArchiver:
    def __init__(self, archive_name="all_logs.zip", log_file="log.log"):
        self.archive_name = archive_name
        self.log_file = log_file

    def save_to_zip(self):
        if not os.path.exists(self.log_file):
            return

        with open(self.log_file, 'r') as log_file:
            lines = log_file.readlines()

        if not lines:
            return

        try:
            time = lines[0].split(" ")
            day = time[0]
            seconds = time[1].split(",")[0]
            first_date = f"[{day}_{seconds}]"
            time = lines[-1].split(" ")
            day = time[0]
            seconds = time[1].split(",")[0]
            last_date = f"[{day}_{seconds}]"
        except ValueError:
            first_date = "unknown"
            last_date = "unknown"

        log_archive_name = f"{first_date}{last_date}.log"

        with zipfile.ZipFile(self.archive_name, 'a') as archive:
            archive.write(self.log_file, log_archive_name)
            
        os.remove(self.log_file)

    def setup_logging(self):
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
