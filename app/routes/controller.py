"""
Controller Module
------------------------
Responsible to handle the request, his attributes and error handling.

Author: Álef Ádonis dos Santos Carlos
Date: 10/01/2024
"""
from flask import Blueprint, jsonify, make_response
from ..service.log_service import (
    extract_log_records_from_files,
    save_records_in_database,
    get_log_by_id,
    get_all_logs_from_database,
    delete_all_log_records_from_database,
    delete_log_record_by_id,
)


controller = Blueprint("controller", __name__)


@controller.route("/logs/extract", methods=["POST"])
def extract_log():
    """
    Extract and save log files

    Extract the log files from their directory and save them in the database.
    ---
    tags:
    - Log Record
    responses:
      200:
        description: List of all log records retrieved successfully
        schema:
          type: object
          properties:
            data:
              type: array
              items:
                type: object
                properties:
                  date:
                    type: string
                  description:
                    type: string
                  hour:
                    type: string
                  id:
                    type: string
                  ip_address:
                    type: string
                  log_id:
                    type: string
                  software_name:
                    type: string
                  title:
                    type: string
                  version:
                    type: string
        examples:
          application/json:
            data:
              - date: "01-Apr-2022"
                description: "eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor"
                hour: "2:50:07.000"
                id: "78331"
                ip_address: "224.191.78.71"
                log_id: "871783207-1"
                software_name: "Konklab"
                title: "Customer-focused responsive installation"
                version: "4.42"
      404:
        description: No logs to extract
        schema:
          type: object
          properties:
            message:
              type: string
        examples:
          application/json:
            message: "There was no logs to extract"
      500:
        description: Error retrieving log records
        schema:
          type: object
          properties:
            message:
              type: string
        examples:
          application/json:
            message: "It was not possible to retrieve log records from the database {error}"
    """

    try:
        log_extracted = extract_log_records_from_files()

        if not log_extracted:
            return make_response(
                jsonify({"message": "There was no logs to extract"}), 404
            )
    except Exception as error:
        print(error)
        return make_response(
            jsonify(
                {"message": "It was not possible to extract log records from file."}
            ),
            500,
        )

    try:
        response = save_records_in_database()
        return make_response(jsonify({"data": response}), 200)

    except Exception:
        return make_response(
            jsonify(
                {"message": "It was not possible to save log records in the database"}
            ),
            500,
        )


@controller.route("/log/<id>", methods=["GET"])
def get_log(id: str):
    """
    Retrieve a log record by ID

    Retrieve a log record from the database based on its ID.
    ---
    tags:
      - Log Record
    parameters:
      - name: id
        in: path
        description: ID of the log record to retrieve
        required: true
        type: string
    responses:
      200:
        description: List of all log records retrieved successfully
        schema:
          type: object
          properties:
            data:
              type: object
              properties:
                date:
                  type: string
                description:
                  type: string
                hour:
                  type: string
                id:
                  type: string
                ip_address:
                  type: string
                log_id:
                  type: string
                software_name:
                  type: string
                title:
                  type: string
                version:
                  type: string
        examples:
          application/json:
            data:
              date: "01-Apr-2022"
              description: "eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor"
              hour: "2:50:07.000"
              id: "78331"
              ip_address: "224.191.78.71"
              log_id: "871783207-1"
              software_name: "Konklab"
              title: "Customer-focused responsive installation"
              version: "4.42"
      404:
        description: No logs found
        schema:
          type: object
          properties:
            message:
              type: string
        examples:
          application/json:
            message: "Log record not found"
      500:
        description: Error retrieving log records
        schema:
          type: object
          properties:
            message:
              type: string
        examples:
          application/json:
            message: "It was not possible to retrieve log records from the database {error}"

    """
    try:
        log_record = get_log_by_id(id)

        if log_record is None:
            return make_response(jsonify({"message": "Log record not found"}), 404)

        return make_response(jsonify({"data": log_record}), 200)
    except Exception as error:
        return make_response(
            jsonify(
                {
                    "message": f"It was not possible to retrieve log record from the database {error}"
                }
            ),
            500,
        )


@controller.route("/logs", methods=["GET"])
def get_all_logs():
    """
    Retrieve all log records

    Retrieve all log records from the database.
    ---
    tags:
      - Log Record
    responses:
      200:
        description: List of all log records retrieved successfully
        schema:
          type: object
          properties:
            data:
              type: array
              items:
                type: object
                properties:
                  date:
                    type: string
                  description:
                    type: string
                  hour:
                    type: string
                  id:
                    type: string
                  ip_address:
                    type: string
                  log_id:
                    type: string
                  software_name:
                    type: string
                  title:
                    type: string
                  version:
                    type: string
        examples:
          application/json:
            data:
              - date: "01-Apr-2022"
                description: "eget tempus vel pede morbi porttitor lorem id ligula suspendisse ornare consequat lectus in est risus auctor"
                hour: "2:50:07.000"
                id: "78331"
                ip_address: "224.191.78.71"
                log_id: "871783207-1"
                software_name: "Konklab"
                title: "Customer-focused responsive installation"
                version: "4.42"

      500:
        description: Error retrieving log records
        schema:
          type: object
          properties:
            message:
              type: string
        examples:
          application/json:
            message: "It was not possible to retrieve log records from the database {error}"
    """

    try:
        logs = get_all_logs_from_database()
        return make_response(jsonify({"data": logs}), 200)
    except Exception as error:
        return make_response(
            jsonify(
                {
                    "message": f"It was not possible to retrieve log record from the database {error}"
                }
            ),
            500,
        )


@controller.route("/logs", methods=["DELETE"])
def delete_all_logs():
    """
    Delete all log records

    Delete all log records from the database.
    ---
    tags:
      - Log Record
    responses:
      200:
        description: Number of rows deleted from database
        schema:
          type: object
          properties:
            data:
              type: string
        examples:
          application/json:
            message: 101010
      500:
        description: Error deleting log records
        schema:
          type: object
          properties:
            message:
              type: string
        examples:
          application/json:
            message: "It was not possible to delete all log records from the database {error}"
    """

    try:
        number_of_logs_deleted = delete_all_log_records_from_database()
        return make_response(jsonify({"data": number_of_logs_deleted}), 200)
    except Exception as error:
        return make_response(
            jsonify(
                {
                    "message": f"It was not possible to delete all log records from the database {error}"
                }
            ),
            500,
        )


@controller.route("/log/<id>", methods=["DELETE"])
def delete_log_by_id(id: str):
    """
    Delete a log record by id

    Delete a log record by the given id from the database.
    ---
    tags:
      - Log Record
    parameters:
      - name: id
        in: path
        description: ID of the log record to delete
        required: true
        type: string
    responses:
      200:
        description: Id of the record deleted
        schema:
          type: object
          properties:
            data:
              type: string
        examples:
          application/json:
            message: 100100
      500:
        description: Error deleting log record
        schema:
          type: object
          properties:
            message:
              type: string
        examples:
          application/json:
            message: "It was not possible to delete log record from the database {error}"
    """
    try:
        delete_log_record_by_id(id)
        return make_response(jsonify({"data": id}), 200)
    except Exception as error:
        return make_response(
            jsonify(
                {
                    "message": f"It was not possible to delete log record from the database {error}"
                }
            ),
            500,
        )
