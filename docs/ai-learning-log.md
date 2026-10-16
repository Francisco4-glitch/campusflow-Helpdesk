# CampusFlow AI Learning Log

## Interaction 1: Understanding Ticket Priority

**Prompt used:** I asked AI to explain how to implement the CampusFlow prrriority rules.

**What AI suggested:** Check the critical rule before the high, medium, and low rules.

**What I learned:** The order of conditional statements matters because a ticket may satisfy more than one condition.

**My verification:** I will run the priority unit tests and compare the results with the assessment rules.

## Interaction 2: Input Validation

**Prompt used:** I asked AI how to validate ticket titles, categories, urgency, and affected-user counts.

**What AI suggested:** Use separate validation functions and raise ValueError when input is invalid.

**What I learned:** Separating validation makes each rule easier to understand and test.

**My verification:** I will run tests for blank titles, invalid categories, invalid urgency, and invalid user counts.

## Interaction 3: Independent Review

**Prompt used:** I asked AI to help implement ticket creation and generate unique ticket IDs.

**What AI suggested:** Validate inputs before adding a ticket to the collection.

**My independent review:** I will inspect the ID-generation logic, test repeated ticket creation, and check that invalid tickets do not change the list.

**What I changed, improved, or rejected:** Record the actual issue you found and the correction you made, or explain why you accepted the implementation after testing.

**Evidence:** Record the commands you ran and the actual test results.