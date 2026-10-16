# CampusFlow Design Decisions

## 1. Ticket Data Structure

Each ticket will be represented as a Python dictionary.

Every ticket will contain:
- id
- title
- category
- urgency
- affected_users
- priority
- status
- assigned_to

## 2. Ticket Categories

Allowed categories:
- Network
- Hardware
- Software
- Other

Category input will be case-insensitive and stored in normalized form.

## 3. Urgency Levels

Allowed urgency levels:
- low
- medium
- high

Urgency input will be normalized to lowercase.

## 4. Priority Rules

1. High urgency and at least 10 affected users: critical.
2. High urgency or at least 10 affected users: high.
3. Medium urgency or at least 3 affected users: medium.
4. Otherwise: low.

Rules will be checked in this order.

## 5. Validation

- Titles cannot be blank.
- Categories must be allowed values.
- Urgency must be low, medium, or high.
- Affected users must be a positive whole number.
- Invalid input must not add a ticket to the ticket collection.

## 6. Ticket IDs

Ticket IDs will follow the format T001, T002, T003, and so on.

The ID generator will check existing ticket IDs before selecting the next ID.

## 7. Initial Ticket State

New tickets will have:
- status: open
- assigned_to: None

## 8. Function Interface

Engineer A provides these functions in campusflow/tickets.py:
- validate_title(title)
- validate_category(category)
- validate_urgency(urgency)
- validate_affected_users(affected_users)
- calculate_priority(urgency, affected_users)
- generate_ticket_id(tickets)
- create_ticket(title, category, urgency, affected_users, tickets)

The create_ticket function returns the new ticket and appends it to the supplied list.

## 9. Integration and Storage

Engineer B and Engineer A will agree on how the ticket list is shared with the workflow and JSON storage modules.

The storage implementation must preserve existing tickets and IDs when saving and loading.

## 10. Testing

Python unittest will be used to test validation, priority rules, ID generation, and ticket creation.

## 11. Team Approval

Engineer A: ____________________

Engineer B: ____________________

Date: ____________________