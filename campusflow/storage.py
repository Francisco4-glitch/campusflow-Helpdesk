import json
from pathlib import Path

DATA_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "tickets.json"
)


def load_tickets():
    """Load saved tickets from the JSON file."""
    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)

    if not DATA_FILE.exists():
        return []

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            tickets = json.load(file)
    except json.JSONDecodeError as error:
        raise ValueError("Ticket storage contains invalid JSON.") from error

    if not isinstance(tickets, list):
        raise ValueError("Ticket storage must contain a list.")

    if not all(isinstance(ticket, dict) for ticket in tickets):
        raise ValueError("Every ticket must be a dictionary.")

    return tickets


def save_tickets(tickets):
    """Save tickets to the JSON file."""
    if not isinstance(tickets, list):
        raise ValueError("Tickets must be stored in a list.")

    DATA_FILE.parent.mkdir(parents=True, exist_ok=True)
    temporary_file = DATA_FILE.with_suffix(".tmp")

    with temporary_file.open("w", encoding="utf-8") as file:
        json.dump(tickets, file, indent=4)
        file.write("\n")

    temporary_file.replace(DATA_FILE)