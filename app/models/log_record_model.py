"""
Log Model Module
------------------------
Responsible to define our ORM Object to handle with the database

Author: Álef Ádonis dos Santos Carlos
Date: 10/01/2024
"""
from ..extensions import db


class Log(db.Model):
    """
    Represents a log record entity stored in the 'log_records' table.

    Attributes:
        - id (int): Primary key and unique identifier for the log record.
        - ip_address (str): The IP address associated with the event.
        - date (str): The date when the event occurred (format: dd-Mon-yyyy).
        - hour (str): The time when the event occurred (format: hh:mm:ss.xxx).
        - software_name (str): The name of the software or application related to the event.
        - version (str): The version of the software or application.
        - log_id (str): A unique identifier for the log entry.
        - title (str): A concise title or label describing the nature of the logged event.
        - description (str): A detailed description of the event, potentially containing additional information.
        - origin_file (str): The file from which the log record originated.

    Methods:
        - __init__: Initializes a Log object with the specified attributes.
        - serialize: Serializes the object attributes into a dictionary.

    """
    __tablename__ = "log_records"

    id = db.Column(db.Integer, primary_key=True, unique=True)
    ip_address = db.Column(db.String(40), nullable=False)
    date = db.Column(db.String(12), nullable=False)
    hour = db.Column(db.String(15), nullable=False)
    software_name = db.Column(db.String(80), nullable=False)
    version = db.Column(db.String(8), nullable=False)
    log_id = db.Column(db.String(15), nullable=False)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(400), nullable=False)
    origin_file = db.Column(db.String(80), nullable=False)

    def __init__(
        self,
        ip_address: str,
        date: str,
        hour: str,
        software_name: str,
        version: str,
        log_id: str,
        title: str,
        description: str,
        origin_file: str,
    ) -> None:
        """
        Initializes a Log object with the specified attributes.

        Parameters:
            - ip_address (str): The IP address associated with the event.
            - date (str): The date when the event occurred (format: dd-Mon-yyyy).
            - hour (str): The time when the event occurred (format: hh:mm:ss.xxx).
            - software_name (str): The name of the software or application related to the event.
            - version (str): The version of the software or application.
            - log_id (str): A unique identifier for the log entry.
            - title (str): A concise title or label describing the nature of the logged event.
            - description (str): A detailed description of the event, potentially containing additional information.

        Returns:
            None
        """

        self.ip_address = ip_address
        self.date = date
        self.hour = hour
        self.software_name = software_name
        self.version = version
        self.log_id = log_id
        self.title = title
        self.description = description
        self.origin_file = origin_file

    def serialize(self) -> dict:
        """
        Serialize the object attributes values into a dictionary.

        Returns:
           dict: a dictionary containing the attributes values
        """
        data = {
            "id": str(self.id),
            "ip_address": self.ip_address,
            "date": self.date,
            "hour": self.hour,
            "software_name": self.software_name,
            "version": self.version,
            "log_id": self.log_id,
            "title": self.title,
            "description": self.description,
            "origin_file": self.origin_file,
        }

        return data
