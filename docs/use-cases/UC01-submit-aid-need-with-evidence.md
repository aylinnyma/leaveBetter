# UC1: Submit aid need with evidence

**Type:** CRUD – **Create**
**Primary actor:** Reporter
**Supporting systems:** none directly (geolocation is handled in UC3)
**Includes:** [UC3: Geotag location on map](UC03-geotag-location-on-map.md)

## Revision History

| Version | Date       | Description   | Author |
|---------|------------|---------------|--------|
| 0.1     | 2026-10-27 | Initial draft | <name> |

## 1. Use-Case Name

Submit aid need with evidence

### 1.1 Brief Description

_To be added together with the .feature files._

## 2. Flow of Events

### 2.1 Wireframe

![UC1 wireframe – report form](img/uc01-wireframe.png)

### 2.2 Activity Diagram

![UC1 activity diagram](img/uc01-activity.png)

### 2.3 Basic Flow

1. The Reporter selects "Report a need".
2. The system shows the report form.
3. The Reporter enters the description of the need and its category.
4. The Reporter attaches evidence (photos or documents).
5. The Reporter submits the form.
6. The system validates the input.
7. The system geotags the location of the need (include [UC3](UC03-geotag-location-on-map.md)).
8. The system saves the need with the status "Pending Review".
9. The system notifies the Reporter that the need was received and is waiting for moderation.
10. The use case ends.

### 2.4 Alternative Flows

**A1: Required fields missing or invalid** (at step 6)
1. The system shows an error next to each missing or invalid field.
2. The Reporter corrects the data.
3. The flow continues at step 5.

**A2: Evidence file not accepted** (at step 4)
1. The system rejects the file and explains why (file type or size).
2. The Reporter removes it or selects another file.
3. The flow continues at step 4.

**A3: Location could not be determined** (at step 7)
1. The system informs the Reporter (see the alternative flows of UC3).
2. No need is saved.
3. The Reporter can retry or submit later. The use case ends.

**A4: Reporter cancels** (at any step before step 8)
1. The Reporter cancels the form.
2. Nothing is saved. The use case ends.

## 3. Special Requirements

_(Proposed – adjust to your SRS)_
- Allowed file types and maximum file size for evidence must be defined.
- Evidence is stored securely and is not visible to volunteers before the need is verified.

## 4. Preconditions

- The Reporter is registered and logged in.

## 5. Postconditions

- **Success:** The need is saved with the status "Pending Review". It is not yet visible on the public map. The Reporter has been notified.
- **Failure:** No need is saved.

## 6. Extension Points

None.