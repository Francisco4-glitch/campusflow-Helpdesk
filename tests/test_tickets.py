import unittest

from campusflow.tickets import (
    validate_title,
    validate_category,
    validate_urgency,
    validate_affected_users,
    calculate_priority,
    generate_ticket_id,
    create_ticket,
)


class TestTicketValidation(unittest.TestCase):

    def test_valid_title(self):
        self.assertEqual(
            validate_title(" Campus Wi-Fi "), "Campus Wi-Fi"
        )

    def test_blank_title_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_title("   ")

    def test_valid_category_is_normalized(self):
        self.assertEqual(validate_category("network"), "Network")

    def test_invalid_category_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_category("Food")

    def test_valid_urgency_is_normalized(self):
        self.assertEqual(validate_urgency("HIGH"), "high")

    def test_invalid_urgency_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_urgency("urgent")

    def test_positive_affected_users(self):
        self.assertEqual(validate_affected_users("5"), 5)

    def test_zero_affected_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_affected_users(0)

    def test_negative_affected_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_affected_users(-3)

    def test_decimal_affected_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_affected_users(2.5)

    def test_text_affected_users_is_rejected(self):
        with self.assertRaises(ValueError):
            validate_affected_users("many")


class TestTicketPriority(unittest.TestCase):

    def test_high_urgency_and_many_users_is_critical(self):
        self.assertEqual(calculate_priority("high", 12), "critical")

    def test_high_urgency_and_few_users_is_high(self):
        self.assertEqual(calculate_priority("high", 2), "high")

    def test_many_users_with_low_urgency_is_high(self):
        self.assertEqual(calculate_priority("low", 10), "high")

    def test_medium_urgency_is_medium(self):
        self.assertEqual(calculate_priority("medium", 1), "medium")

    def test_three_or_more_users_is_at_least_medium(self):
        self.assertEqual(calculate_priority("low", 4), "medium")

    def test_low_urgency_and_one_user_is_low(self):
        self.assertEqual(calculate_priority("low", 1), "low")


class TestTicketCreation(unittest.TestCase):

    def setUp(self):
        self.tickets = []

    def test_create_valid_ticket(self):
        ticket = create_ticket(
            "Wi-Fi is down",
            "Network",
            "high",
            12,
            self.tickets,
        )

        self.assertEqual(ticket["id"], "T001")
        self.assertEqual(ticket["priority"], "critical")
        self.assertEqual(ticket["status"], "open")
        self.assertIsNone(ticket["assigned_to"])
        self.assertEqual(len(self.tickets), 1)

    def test_two_tickets_have_unique_ids(self):
        first = create_ticket(
            "Wi-Fi problem", "Network", "high", 12, self.tickets
        )
        second = create_ticket(
            "Broken computer", "Hardware", "low", 1, self.tickets
        )

        self.assertEqual(first["id"], "T001")
        self.assertEqual(second["id"], "T002")

    def test_invalid_ticket_does_not_change_list(self):
        with self.assertRaises(ValueError):
            create_ticket(
                "",
                "Network",
                "high",
                12,
                self.tickets,
            )

        self.assertEqual(self.tickets, [])

    def test_invalid_ticket_does_not_consume_id(self):
        with self.assertRaises(ValueError):
            create_ticket(
                "Wi-Fi problem",
                "Invalid category",
                "high",
                12,
                self.tickets,
            )

        ticket = create_ticket(
            "Valid ticket",
            "Network",
            "low",
            1,
            self.tickets,
        )

        self.assertEqual(ticket["id"], "T001")

    def test_next_id_uses_existing_tickets(self):
        self.tickets.append({"id": "T001"})
        self.tickets.append({"id": "T003"})

        self.assertEqual(generate_ticket_id(self.tickets), "T004")


if __name__ == "__main__":
    unittest.main()