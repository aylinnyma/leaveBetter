# UC5: Validate need

**Type:** CRUD – **Update** (changes the status of a need)
**Primary actor:** Moderator
**Related use cases:** [UC1](UC01-submit-aid-need-with-evidence.md) (creates the pending need), UC7 (shows verified needs on the map)

## Revision History

| Version | Date       | Description   | Author |
|---------|------------|---------------|--------|
| 0.1     | 2026-10-27 | Initial draft | <name> |

## 1. Use-Case Name

Validate need

### 1.1 Brief Description

_To be added together with the .feature files._

## 2. Flow of Events

### 2.1 Wireframe

![UC5 wireframe – review screen](img/uc05-wireframe.png)

### 2.2 Activity Diagram

![UC5 activity diagram](img/uc05-activity.png)

### 2.3 Basic Flow

1. The Moderator opens the review queue.
2. The system lists all needs with the status "Pending Review".
3. The Moderator selects a need.
4. The system shows the details, the evidence and the location of the need.
5. The Moderator reviews the information and approves the need.
6. The system sets the status to "Verified".
7. The system publishes the need on the map.
8. The system notifies the Reporter that the need was approved.
9. The use case ends.

### 2.4 Alternative Flows

**A1: Moderator rejects the need** (at step 5)
1. The Moderator chooses "Reject" and enters a reason.
2. The system sets the status to "Rejected" and saves the reason.
3. The need is not published.
4. The system notifies the Reporter, including the reason.
5. The use case ends.

**A2: Rejection reason missing** (at A1, step 1)
1. The system asks for a reason and does not continue without one.
2. The flow continues at A1, step 1.

**A3: Need already handled by another Moderator** (at step 5 or A1)
1. The system informs the Moderator that the need has already been processed.
2. The system refreshes the review queue.
3. The flow continues at step 2.

## 3. Special Requirements

_(Proposed – adjust to your SRS)_
- Each decision is logged with Moderator, date/time and, if rejected, the reason.

## 4. Preconditions

- The Moderator is logged in and has the Moderator role.
- At least one need has the status "Pending Review".

## 5. Postconditions

- **Approved:** The need has the status "Verified" and is visible on the map. The Reporter is notified.
- **Rejected:** The need has the status "Rejected" and a saved reason. It is not visible on the map. The Reporter is notified.

## 6. Extension Points

None.