# LeaveBetter – Software Requirements Specification

Oct 20, 2026 · @Aylin

## 1. Introduction

### 1.1 Purpose

This Software Requirements Specification (SRS) describes the application "LeaveBetter". It gives an overview of the project and its vision, the planned features, and the boundary conditions of the development process.

### 1.2 Scope

LeaveBetter is a geolocation-based app that shows on a map where people need help (food, water, education, supplies, construction help, childcare, etc.). Tourists who want to give something back to the place that hosts them, and locals who want to help their own community, can see the map, contact the person in need and agree on the help together.

The target platform is tbd (to be decided by the team, together with the technology stack in section 2.3).

Actors:

- **Requester:** a person or group who posts a need for help.
- **Helper:** a tourist or a local who offers help.
- **Moderator / admin:** reviews and removes content and users (later phase).

Planned subsystems:

- **Help Map:** the central part of the user interface. Requests appear as pins on a map with category, short description and location.
- **Account System:** users register and log in so requests, offers and messages can be linked to a person.
- **Request Management:** requesters create, edit and close help requests using a standardized form (category, description, location, urgency) with a free-text field for specifics.
- **Connecting People:** a helper can contact the requester to agree on the details of the help; the requester is notified. This can be done through an in-app messaging system or automated emails.
- **Search and Filter:** users find requests by category, distance and date.
- **Data Storage:** accounts, requests and messages are stored; this is the foundation for the map, the account system and the search.
- **Verification and Anti-Fraud (later):** checks that requests and donations are genuine. Details follow in a later phase.

### 1.3 Definitions, Acronyms and Abbreviations

| Abbreviation | Explanation |
| --- | --- |
| SRS | Software Requirements Specification |
| UC | Use Case |
| UCD | Overall Use Case Diagram |
| API | Application Programming Interface |
| FAQ | Frequently Asked Questions |
| n/a | not applicable |
| tbd | to be determined |

### 1.4 References

| Title | Date | Publishing organization |
| --- | --- | --- |
| LeaveBetter project blog (WordPress) | tbd | LeaveBetter Team |
| Code repository | tbd | LeaveBetter Team |

### 1.5 Overview

Chapter 2 gives an overview of the project with the vision, the Overall Use Case Diagram and the technology stack. Chapter 3 describes the specific requirements: functionality, usability, reliability, performance and design constraints. Chapter 4 contains supporting information.

## 2. Overall Description

### 2.1 Vision

LeaveBetter connects people who need help with people who want to give it. Travelers often want to leave a place better than they found it, and locals often want to help their own community, but neither group knows where help is needed. LeaveBetter closes that gap with a map of real needs: a helper opens the map, picks a request nearby, contacts the person, and they agree on the help together.

### 2.2 Use Case Overview

The table lists the planned use cases. "Core" means part of the first working version; "Later" means a later phase. The priorities are a proposal until the team confirms them.

| ID | Use case | Actor | Phase |
| --- | --- | --- | --- |
| UC1 | Create an account | Requester, Helper | Core |
| UC2 | Log in | Requester, Helper, Moderator | Core |
| UC3 | Log out | Requester, Helper, Moderator | Core |
| UC4 | View the help map | Helper | Core |
| UC5 | Post a help request | Requester | Core |
| UC6 | View request details | Helper | Core |
| UC7 | Offer help and get in touch | Helper | Core |
| UC8 | Exchange messages | Requester, Helper | Core |
| UC9 | Manage own requests (edit, close) | Requester | Core |
| UC10 | Search and filter requests | Helper | Later |
| UC11 | Present yourself (profile) | Requester, Helper | Later |
| UC12 | Report a user or request | Requester, Helper | Later |
| UC13 | Ban users and delete requests | Moderator | Later |
| UC14 | Verify that a request is genuine | Moderator | Later |

### 2.3 Technology Stack

The stack is not final. The team is still deciding, and the choice must fit the tasks that follow in the course. Open choices:

| Area | Decision |
| --- | --- |
| Platform (Android, web, cross-platform) | tbd |
| Backend language and framework | tbd (JavaScript has been suggested; team wants to check fit with later course tasks) |
| Database | tbd |
| Map and geolocation service | tbd |
| Project management and version control | tbd |
| Testing | tbd |
| Deployment | tbd |

## 3. Specific Requirements

### 3.1 Functionality

**Core features**

- **3.1.1 Creating an account:** A user registers as a requester or helper. Accounts link requests, offers and messages to a person.
- **3.1.2 Logging in and out:** Users log in to post, offer help or message, and can log out manually, for example on a shared phone.
- **3.1.3 Viewing the help map:** The map shows open requests as pins by category near the user's location. Tapping a pin shows a short summary.
- **3.1.4 Posting a help request:** A requester fills in a form with category (food, water, education, supplies, construction help, childcare, other), description, location and urgency, plus a free-text field for specifics.
- **3.1.5 Viewing request details:** A helper opens a request to see all its details and the requester's public information.
- **3.1.6 Offering help and getting in touch:** A helper contacts the requester from the request page. The requester is notified.
- **3.1.7 Exchanging messages:** Requester and helper exchange messages to agree on the details (in-app messaging or automated emails, tbd).
- **3.1.8 Managing own requests:** A requester sees their requests, edits them and marks them as fulfilled or closed.

**Later features**

- **3.1.9 Searching and filtering:** Users filter requests by category, distance and date.
- **3.1.10 Profiles:** Users describe themselves; they choose what to show, in line with European privacy rules.
- **3.1.11 Reporting:** Users can report a request or user that seems abusive or fake.
- **3.1.12 Moderation:** Moderators can ban users and delete requests.
- **3.1.13 Verification and anti-fraud:** Checks that requests and donations are genuine. Fraud scenarios and the concept are worked out in a later phase and may affect the architecture (open question, see chapter 4).

### 3.2 Usability

The interface should be intuitive and understandable without training. Tourists may not speak the local language, so the app must be easy to use for people with different backgrounds and languages. Multi-language support is tbd. The design follows familiar map-app conventions.

### 3.3 Reliability

- **Availability:** target tbd. Downtime should not affect helpers who are already in contact with a requester.
- **Defect rate:** no loss of requests, accounts or messages, even after a server outage.

### 3.4 Performance

- **Capacity:** the system handles many simultaneous users and requests; exact numbers tbd.
- **Response time:** the map and request pages load quickly; target tbd.
- **Storage:** the app keeps local storage small, and the map loads only requests near the user.

### 3.5 Supportability

- **Coding standards:** the team follows common clean code conventions, with names that describe functionality.
- **Testing strategy:** important functions and edge cases are covered by automated tests.

### 3.6 Design Constraints

The application is modular and follows the MVC architecture, which keeps the front end and back end separate. Front end and back end communicate through a RESTful API with data in JSON format. Supported platforms and minimum versions are tbd with the technology stack. Location data is sensitive: precise addresses should only be shared once requester and helper are in contact (proposal, to be confirmed). Security and anti-fraud requirements will be added in a later phase.

### 3.7 Online User Documentation and Help System Requirements

The app should be self-explanatory. A help section with an FAQ and a contact form for the development team is planned.

### 3.8 Purchased Components

None yet. Purchased components, such as a map service with paid usage limits, will be listed here if they are used.

### 3.9 Interfaces

**3.9.1 User interfaces**

- Map: shows requests near the user and lets users filter them
- Request page: shows the details of a request and the contact option
- New request: the form to post a request
- Login and registration
- My requests and offers: an overview of the user's own activity
- Messages: conversation between requester and helper
- Profile and settings

**3.9.2 Hardware interfaces:** device location (GPS). Further hardware interfaces: n/a.

**3.9.3 Software interfaces:** a map and geolocation service (tbd). Supported operating systems are tbd.

**3.9.4 Communication interfaces:** client and server communicate over HTTP(S) using a REST API.

### 3.10 Licensing Requirements

Tbd, depending on the libraries and map services used.

### 3.11 Legal, Copyright and Other Notices

The team takes no responsibility for incorrect data in the app. Handling of personal and location data must follow applicable data protection law (GDPR); details tbd.

### 3.12 Applicable Standards

The development follows common clean code standards and naming conventions. A definition of done will be added here when it is complete.

## 4. Supporting Information

For further information, contact the LeaveBetter Team or read the project blog.

**Team members:** four members, names and roles tbd.

**Open points**

| Topic | Question | Where it affects the SRS |
| --- | --- | --- |
| Fraud and verification | How do we check that a request or donation is real, and does this change the architecture early? | 3.1.13, 3.6 |
| Technology stack | Which platform and backend fit the course tasks that follow? | 2.3, 3.6, 3.9.3 |
| Messaging | In-app messages or automated emails? | 3.1.7 |
| AI usage | Which rules for the use of AI does the team follow? | 3.12 |
| Data protection | How is location data stored and shown? | 3.6, 3.11 |
