# Leave Better
Project for Software Engineering

## 📁 Project Structure

To maintain clean engineering practices and comply with RUP guidelines, this repository strictly separates project documentation from runtime source code:

```text
LeaveBetter/
│
├── docs/                               # Project documentation & engineering artifacts
│   └── SRS.md                          # Complete 
│
├── src/                                # Application source code
│   ├── backend/                        # Django & Python server logic, models, and REST APIs
│   └── frontend/                       # React client components, pages, and interactive maps
│
├── .gitignore                          # Git ignore rules for virtual environments & build files
└── README.md                           # Repository overview, setup instructions, and architecture