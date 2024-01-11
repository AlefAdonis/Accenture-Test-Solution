"""
Service Module
------------------------
Responsible to process the data and deal with the database.

Author: Álef Ádonis dos Santos Carlos
Date: 10/01/2024
"""

from ..extensions import db
from ..models.log_record_model import Log
import concurrent.futures
import os


DIR_PATH = os.environ.get("LOG_PATH")
extracted_logs = []


def transform_log_records_to_object(filepath: str) -> None:
    """
    Transform log records from a file into Log objects and append them to the extracted_logs list.

    Parameters:
        filepath (str): The path to the log file.

    Returns:
        None
    """
    global extracted_logs

    with open(filepath, "r", encoding="utf-8") as file:
        for line in file:
            record = line.rstrip("\n").split(";")

            log_record = Log(
                ip_address=record[0],
                date=record[1],
                hour=record[2],
                software_name=record[3],
                version=record[4],
                log_id=record[5],
                title=record[6],
                description=record[7],
                origin_file=filepath.split("/")[-1],
            )

            extracted_logs.append(log_record)


def extract_log_records_from_files() -> bool:
    """
    Extract log records from multiple files in parallel and store them in the extracted_logs list.

    Returns:
        bool: True if log records were successfully extracted, False otherwise.
    """
    filepath_list = []
    for file_ in os.listdir(DIR_PATH):
        filepath = os.path.join(DIR_PATH, file_)
        filepath_list.append(filepath)

    if not filepath_list:
        return False

    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [
            executor.submit(transform_log_records_to_object, log_path)
            for log_path in filepath_list
        ]

        results = [
            future.result() for future in concurrent.futures.as_completed(futures)
        ]

    return True


def save_records_in_database():
    """
    Save log records in batches to the database.

    Returns:
        List[dict]: Serialized log records of the last batch saved.
    """
    global extracted_logs

    for index in range(0, len(extracted_logs), 200):
        batch_logs = extracted_logs[index : min(index + 200, len(extracted_logs))]

        db.session.add_all(batch_logs)
        db.session.commit()

    saved_logs = [log.serialize() for log in extracted_logs[:6]]
    extracted_logs = []
    return saved_logs


def get_log_by_id(id: str):
    """
    Retrieve a log record from the database by ID.

    Parameters:
        id (str): The ID of the log record to retrieve.

    Returns:
        dict or None: Serialized log record if found, None otherwise.
    """
    log_record = Log.query.filter_by(id=id).first()

    if log_record is not None:
        return log_record.serialize()
    else:
        return None


def get_all_logs_from_database():
    """
    Retrieve all log records from the database.

    Returns:
        List[dict]: Serialized list of all log records in the database.
    """
    return [log.serialize() for log in Log.query.all()]


def delete_log_record_by_id(id: str):
    """
    Delete a log record from the database by ID.

    Parameters:
        id (str): The ID of the log record to delete.

    Returns:
        None
    """
    try:
        db.session.query(Log).filter(Log.id == id).delete()
        db.session.commit()

    except:
        db.session.rollback()
        raise Exception


def delete_all_log_records_from_database() -> int:
    """
    Delete all log records from the database.

    Returns:
        int: Number of rows deleted.

    Raises:
        Exception: If an error occurs during deletion.
    """
    try:
        num_rows_deleted = db.session.query(Log).delete()
        db.session.commit()
        return num_rows_deleted
    except:
        db.session.rollback()
        raise Exception
