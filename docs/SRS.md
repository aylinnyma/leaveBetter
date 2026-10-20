# LeaveBetter - Software Requirements Specification

## Table of contents
- [Table of contents](#table-of-contents)
- [1. Introduction](#1-introduction)
    - [1.1 Purpose](#11-purpose)
    - [1.2 Scope](#12-scope)
    - [1.3 Definitions, Acronyms and Abbreviations](#13-definitions-acronyms-and-abbreviations)
    - [1.4 References](#14-references)
    - [1.5 Overview](#15-overview)
- [2. Overall Description](#2-overall-description)
    - [2.1 Vision](#21-vision)
    - [2.2 Use Case Diagram](#22-use-case-diagram)
    - [2.3 Technology Stack](#23-technology-stack)
- [3. Specific Requirements](#3-specific-requirements)
    - [3.1 Functionality](#31-functionality)
    - [3.2 Usability](#32-usability)
    - [3.3 Reliability](#33-reliability)
    - [3.4 Performance](#34-performance)
    - [3.5 Supportability](#35-supportability)
    - [3.6 Design Constraints](#36-design-constraints)
    - [3.7 Online User Documentation and Help System Requirements](#37-online-user-documentation-and-help-system-requirements)
    - [3.8 Purchased Components](#38-purchased-components)
    - [3.9 Interfaces](#39-interfaces)
    - [3.10 Licensing Requirements](#310-licensing-requirements)
    - [3.11 Legal, Copyright and Other Notices](#311-legal-copyright-and-other-notices)
    - [3.12 Applicable Standards](#312-applicable-standards)
- [4. Supporting Information](#4-supporting-information)

---

## 1. Introduction

### 1.1 Purpose
This Software Requirements Specification (SRS) describes all software requirements for the web platform **LeaveBetter**. It outlines the vision of the project, detailed functionality, architectural choices, and the boundary conditions for development during the RUP Inception phase.

### 1.2 Scope
LeaveBetter is developed as a responsive, phone-friendly web application. The platform connects travelers and locals with communities in need, allowing users to report local aid needs and volunteers to find and fulfill them.

The system consists of the following subsystems:
- **Reporting System:** Users can report local shortages (such as clean water, school supplies, or medicine) using a structured form and location tags.
- **Verification & Moderation System:** Community moderators review incoming reports to prevent scams, duplicates, and fake requests before they appear publicly.
- **Interactive Map & Discovery System:** An interactive map powered by external map services displays verified need locations with visual pins categorized by urgency.
- **Fulfillment & Matching System:** Volunteers can choose a need, pledge support or items, and update the status of the request until it is solved.
- **Account & Profile System:** Manages user identities for reporters, volunteers, and moderators.

### 1.3 Definitions, Acronyms and Abbreviations
| Abbreviation | Explanation |
| :--- | :--- |
| **SRS** | Software Requirements Specification |
| **RUP** | Rational Unified Process |
| **UC** | Use Case |
| **MVC** | Model-View-Controller |
| **API** | Application Programming Interface |
| **SPA** | Single Page Application |
| **n/a** | Not applicable |
| **tbd** | To be determined |

### 1.4 References
| Title | Date | Publishing Organization |
| :--- | :---: | :--- |
| [LeaveBetter Blog](https://leavebetter5.wordpress.com/) | 15.10.2026 | LeaveBetter Team |
| [GitHub Repository](https://github.com/aylinnyma/leaveBetter.git) | 15.10.2026 | LeaveBetter Team |

### 1.5 Overview
The next section provides an overview of the project vision, technology stack, and the overall Use Case Diagram. The third chapter details specific functional requirements (using the FURPS+ model) including usability, reliability, performance, and interfaces. The final section contains team and supporting project information.

---

## 2. Overall Description

### 2.1 Vision
Inspired by mutual-aid networks and responsible travel ideas, LeaveBetter connects travelers with local communities that need support. Often, tourists want to give back to the places they visit, but they do not know what is truly needed or where to deliver help. LeaveBetter provides a community map where local needs (like books for a rural school or medical kits) are posted and verified. Volunteers can view nearby requests, commit aid, and help directly without middlemen.

### 2.2 Use Case Diagram

![Overall Use Case Diagram](./assets/)

- **Planned until December (MVP / Core Deliverables):**
  - UC1: Submit Aid Need
  - UC2: Upload Photo Evidence
  - UC3: Geotag Location on Map
  - UC4: Review Pending Reports
  - UC5: Validate Need
  - UC7: Browse Needs on Map
- **Planned until June (Extended Features):**
  - UC6: Flag Scam / Inappropriate Content
  - UC8: Filter by Category and Urgency
  - UC9: Offer Aid Commitment
  - UC10: Update Fulfillment Status

### 2.3 Technology Stack
The platform uses the following technologies:

**Backend:**
- Python 3.11+
- Django and Django REST Framework
- SQLite Database (Development phase)

**Frontend:**
- React (Single Page Application)
- HTML5, CSS3, JavaScript (ES6+)

**External Services & APIs:**
- Google Maps JavaScript API & Geocoding API

**IDE & Version Control:**
- Visual Studio Code
- Git & GitHub 

**Testing:**
- Django TestCase / Pytest for backend logic
- Jest and React Testing Library for frontend components

---

## 3. Specific Requirements

### 3.1 Functionality
This section describes the use cases shown in the Use Case Diagram.

#### Planned until December:

##### 3.1.1 Submit Aid Need (UC1)
This is the core feature of the platform. A traveler or local reporter can submit an aid request. The user chooses a category (such as Water, Education, or Health), sets the urgency level, enters a description, and sets the location.

##### 3.1.2 Upload Verification Photo (UC2)
When submitting an aid request, the reporter can optionally attach an image as proof. This helps moderators verify that the request is genuine.

##### 3.1.3 Geotag Location on Map (UC3)
When creating a report, the location must be specified. The system uses map coordinates (latitude and longitude) to place a pin accurately on the map.

##### 3.1.4 Review Pending Reports (UC4)
To prevent scams and inaccurate information, all newly submitted reports enter a review queue. Moderators can access this list to inspect details before public display.

##### 3.1.5 Validate Need (UC5)
A moderator checks the report description and photo. If valid, the moderator marks the request as verified, making it visible to volunteers on the public map.

##### 3.1.6 Browse Needs on Map (UC7)
Volunteers and travelers can open an interactive map to see active needs pinned across different regions. Clicking a pin opens a summary card with details.

#### Planned until June:

##### 3.1.7 Flag Inappropriate Content or Scams (UC6)
Moderators can flag, reject, or remove posts that violate platform guidelines or appear to be fraudulent.

##### 3.1.8 Filter by Urgency and Category (UC8)
Volunteers can filter map markers by category (e.g., only "Clean Water") or urgency (e.g., "Critical") to find relevant requests quickly.

##### 3.1.9 Offer Aid Commitment (UC9)
A volunteer can click an "Offer Aid" button on a verified request to state what supplies or time they can provide, notifying the original poster.

##### 3.1.10 Update Fulfillment Status (UC10)
Once aid is delivered, the status of the ticket can be updated from "In Progress" to "Resolved" to keep the map clean and up to date.

---

### 3.2 Usability

#### 3.2.1 Intuitive Mobile-First Design
The user interface is designed to work smoothly on mobile web browsers so travelers can easily use it on the go.

#### 3.2.2 Fast Submission Flow
Submitting an aid report takes under 3 minutes and requires no technical training or complex forms.

#### 3.2.3 Clear Visual Indicators
Map markers use simple, standard colors based on urgency:
- Red: Critical / Immediate
- Yellow: Medium urgency
- Green: In progress or resolved

---

### 3.3 Reliability

#### 3.3.1 High Availability
The web platform aims for 95% availability during normal development cycles.

#### 3.3.2 Data Integrity
No need report can be created without valid geographical coordinates and a valid category.

---

### 3.4 Performance

#### 3.4.1 Map Load Speed
The interactive map should load and display up to 100 markers within 2 seconds on a regular mobile connection.

#### 3.4.2 API Response Time
Backend REST API endpoints should return JSON responses within 300 ms for common database queries.

---

### 3.5 Supportability

#### 3.5.1 Clean Code and MVC Architecture
The system strictly separates concerns:
- **Model:** Django ORM handles database models.
- **View:** React renders the user interface.
- **Controller:** Django REST APIs route requests and connect data to views.

#### 3.5.2 AI Tool Usage Guidelines
All team members adhere to established AI policies: prompt requests must be clear, and every piece of AI-generated code or text must be reviewed and tested by a human.

---

### 3.6 Design Constraints
- **Architecture:** Decoupled frontend (React) and backend (Django) communicating via RESTful JSON APIs.
- **Repository Structure:** Documentation files must stay strictly under `/docs` and runtime code under `/src`.
- **Supported Browsers:** Chrome, Firefox, Safari, and Edge (both mobile and desktop).

---

### 3.7 Online User Documentation and Help System Requirements
The interface is self-explanatory. An "About & Safety" page explains how the verification process works, along with a simple contact link for user support.

### 3.8 Purchased Components
No commercial components are purchased. The system uses open-source libraries and the free development tier of Google Maps Platform.

---

### 3.9 Interfaces

#### 3.9.1 User Interfaces
- **Map Discovery View:** The main screen showing the interactive map, pins, and filters.
- **Report Submission Form:** Form to enter details, upload photos, and pick a location.
- **Moderator Dashboard:** Queue interface for moderators to review, approve, or reject submissions.
- **Need Detail Card:** Pop-up card showing full details, items needed, and the status button.

#### 3.9.2 Hardware Interfaces
*(n/a)*

#### 3.9.3 Software Interfaces
- Integration with **Google Maps JavaScript API** for rendering map tiles.
- Integration with **Google Geocoding API** for location conversion.

#### 3.9.4 Communication Interfaces
- HTTPS protocol for secure communication between client and server.
- JSON format for data exchange across REST endpoints.

---

### 3.10 Licensing Requirements
The project is licensed under the open-source MIT License.

### 3.11 Legal, Copyright and Other Notices
User privacy is respected; personal contact details are kept private and are not displayed on public map endpoints.

### 3.12 Applicable Standards
Development follows clean code principles, PEP 8 standards for Python, and standard Git branch naming conventions.

---

## 4. Supporting Information
For more details, visit our blog or contact the team:
- **Project Blog:** [LeaveBetter Blog](https://leavebetter5.wordpress.com/)
- **Team Members:**
  - Dina  (UI Designer & Frontend Developer)
  - Aylin (System Analyst & Documentation)
  - Jochen (Project Manager & Requirements)
  - Mourad (Software Architect & Backend Developer)