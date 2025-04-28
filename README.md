# Case Study - Python Developer (Odoo Assignment)

## Table of Contents

- [Installation](#installation)
- [Running Odoo](#running-odoo)
- [Features Implemented](#features-implemented)
- [Customizations Overview](#customizations-overview)
- [Usage](#usage)
- [Development Helpers](#development-helpers)
- [Notes](#notes)

---

## Installation

You will need:

- [Docker](https://docs.docker.com/engine/install/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- (Optional but recommended) [Task](https://taskfile.dev/) — a small tool for automating common commands

---

## Setup

1. Clone this repository.

2. Create a `.env` file by copying the provided example:

   ```bash
   cp .env.example .env
   ```

3. Start the Odoo environment:

   ```bash
   go-task up
   ```

   (or manually run `docker-compose up -d`)

4. Odoo will be available at [`http://localhost:8069/web`](http://localhost:8069/web)

5. Default Odoo admin user:  
   (user and password as defined in your `.env` file)

---

## Features Implemented

✅ Custom module called **assignment** extending Odoo functionality.  
✅ Recruitment enhancements including validation, email sending, and custom API.  
✅ Full Dockerized setup.  
✅ REST API to create applicants from external systems.

---

## Customizations Overview

### 1. Employee Number Constraint

- A new required field `employee_number` was added to both:
  - `hr.employee`
  - `hr.applicant`
- The value must be **unique across employees and applicants** (even archived ones).
- Automatic generation for `employee_number` if not provided.

### 2. Recruitment Website Form Validation

- Improved validation for required fields like Name, Email, Phone.
- User-friendly error messages next to the problematic fields.
- Custom CSS/JS for validation styling.

### 3. Email Sending Wizard

- A wizard that allows uploading an Excel (.xlsx) file.
- Reads emails and random texts from the Excel.
- Sends welcome emails where:
  - Email target = first column
  - Subject = second column
- If no file is uploaded, generates a random one automatically.

### 4. REST API Endpoint

- POST JSON payload to:

  ```
  POST http://localhost:8069/case_study/applicant/get
  ```

- Expected JSON structure:

  ```json
  {
    "candidates": [
      {
        "id": 12345,
        "title": "Ing",
        "firstname": "John",
        "surname": "Doe",
        "phone": "123456789",
        "email": "applicant@odoo.com",
        "isActive": 1,
        "gender": "male",
        "job": {
          "id": 4249974,
          "title": "Job title",
          "addDate": "2021-05-11",
          "stateId": 1
        }
      }
    ]
  }
  ```

- It will:
  - Create a new Applicant (hr.applicant).
  - Link to the Job Position by `api_id`.

---

## Usage

**Testing the REST API manually:**

Example (you may need to update the `id` field in the `test_payload.json`):

```bash
go-task curl
```

Or manually:

```bash
curl -X POST http://localhost:8069/case_study/applicant/get \
  -H "Content-Type: application/json" \
  -d @your_test_payload.json
```

**Administer Jobs and Applicants:**

- Jobs must have `API ID` field populated.
- Applicants can now have and manage `employee_number` and `gender`.

---

## Development Helpers

`Taskfile.yml` automates common commands:

| Task | Command |
|:-----|:--------|
| Start containers | `go-task up` |
| Stop containers | `go-task down` |
| Restart containers | `go-task reup` |
| Format Python code | `go-task fmt` |
| Test API call | `go-task curl` |

---

## Notes

- Developer mode should be enabled inside Odoo for advanced technical settings.
- If no outgoing email server is configured, Odoo stores outgoing messages in `Settings > Technical > Emails > Emails`.
- Failed emails can be inspected and manually retried if needed.
- The Website module must be installed to properly view the Recruitment frontend page (`/careers`).

---

# Final words

This case study provides a realistic simulation of extending Odoo with backend, frontend (JS), and API integrations while maintaining a clean modular structure.  

The entire project is Dockerized for easy setup and testing.
