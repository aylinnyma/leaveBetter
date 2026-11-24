# LeaveBetter — Class Diagram

Covers all use cases from the SRS (UC1–UC14).
Will be used for the development process of the Django backend .
Rendered with [Mermaid](https://mermaid.live) — paste the block below into mermaid.live to view it.

```mermaid
classDiagram

    %% ── Enumerations ────────────────────────────────────────────────

    class StatusEnum {
        <<enumeration>>
        Pending Review
        Verified
        In Progress
        Resolved
        Rejected
    }

    class CategoryEnum {
        <<enumeration>>
        Water
        Food
        Education
        Health
        Construction
        Other
    }

    class UrgencyEnum {
        <<enumeration>>
        Critical
        High
        Medium
        Low
    }

    class DecisionEnum {
        <<enumeration>>
        approved
        rejected
    }

    %% ── Core classes ────────────────────────────────────────────────

    class User {
        +int id
        +String username
        +String email
        +String password
        +bool is_active
        +bool is_blocked
        +DateTime created_at
        +register()
        +login()
    }

    class Profile {
        +int id
        +User user
        +bool is_moderator
        +String phone_number
    }

    class AidNeed {
        +int id
        +User reporter
        +String title
        +String description
        +CategoryEnum category
        +UrgencyEnum urgency
        +StatusEnum status
        +float latitude
        +float longitude
        +File evidence
        +bool is_flagged
        +DateTime created_at
        +DateTime updated_at
        +submit()
        +cancel()
    }

    class ModerationLog {
        +int id
        +AidNeed need
        +User moderator
        +DecisionEnum decision
        +String reason
        +DateTime logged_at
    }

    class Flag {
        +int id
        +AidNeed need
        +User reporter
        +String reason
        +DateTime created_at
    }

    class AidCommitment {
        +int id
        +AidNeed need
        +User volunteer
        +String message
        +DateTime created_at
        +offerAid()
        +updateStatus()
    }

    class BlockedUser {
        +int id
        +String email_hash
        +String phone_hash
        +User blocked_by
        +DateTime blocked_at
        +String reason
    }

    %% ── Relationships ───────────────────────────────────────────────

    User "1" --> "0..1" Profile : has
    User "1" --> "0..*" AidNeed : reports
    User "1" --> "0..*" ModerationLog : logs as moderator
    User "1" --> "0..*" Flag : raises
    User "1" --> "0..*" AidCommitment : commits as volunteer
    User "1" --> "0..*" BlockedUser : blocks

    AidNeed "1" --> "0..*" ModerationLog : reviewed in
    AidNeed "1" --> "0..*" Flag : flagged by
    AidNeed "1" --> "0..*" AidCommitment : fulfilled by

    AidNeed --> StatusEnum : status
    AidNeed --> CategoryEnum : category
    AidNeed --> UrgencyEnum : urgency
    ModerationLog --> DecisionEnum : decision
```

## Actor roles

| Actor | Definition |
|-------|-----------|
| **Reporter** | A `User` who submits an `AidNeed` |
| **Volunteer** | A `User` who creates an `AidCommitment` on another user's need |
| **Moderator** | A `User` whose `Profile.is_moderator == True` |

## Use case coverage

| UC | Name | Classes involved |
|----|------|-----------------|
| UC1 | Submit aid need | `User`, `AidNeed` |
| UC2 | Upload photo evidence | `AidNeed.evidence` |
| UC3 | Geotag location | `AidNeed.latitude`, `AidNeed.longitude` |
| UC4 | Review pending/flagged reports | `AidNeed`, `ModerationLog`, `Profile` |
| UC5 | Validate need | `AidNeed`, `ModerationLog` |
| UC6 | Flag a report | `Flag`, `AidNeed` |
| UC7 | Browse needs on map | `AidNeed` (status = Verified / In Progress) |
| UC8 | Filter by category and urgency | `AidNeed.category`, `AidNeed.urgency` |
| UC9 | Offer aid commitment | `AidCommitment` |
| UC10 | Update fulfillment status | `AidNeed.status`, `AidCommitment` |
| UC11 | Reject report | `AidNeed`, `ModerationLog` |
| UC12 | Register an account | `User` |
| UC13 | Log in | `User` |
| UC14 | Block user | `BlockedUser`, `Profile` |
