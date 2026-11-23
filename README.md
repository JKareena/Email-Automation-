# Email Automation System

A Python-based automated email system that reads recipient details from an Excel spreadsheet and sends personalized emails using AI-generated content.

## Features

- Reads recipient information from an Excel file using OpenPyXL.
- Generates personalized email content using Ollama (Llama 3.2).
- Sends emails through Gmail SMTP.
- Checks recipient dates and email status before sending.
- Updates Excel status after successful or failed attempts.
- Implements exception handling and retry mechanisms.
- Maintains logs for tracking email activity.
- Supports scheduled execution using Windows Task Scheduler.

## Technologies Used

- Python
- OpenPyXL
- Ollama (Llama 3.2)
- Requests
- Python-dotenv
- Gmail SMTP
- Windows Task Scheduler

## Project Structure

```text
Email-Automation/
│
├── main.py
├── email_list.xlsx
├── requirements.txt
├── .env
├── .gitignore
└── email_automation.log
```

## Setup Instructions

1. Clone this repository.
2. Create a Python virtual environment.
3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Install Ollama and download the model:

```bash
ollama pull llama3.2:1b
```

5. Create a `.env` file and configure your Gmail credentials:

```env
EMAIL_ADDRESS=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

6. Start Ollama.
7. Run the automation:

```bash
python main.py
```

## Excel Format

The Excel file contains the following columns:

| Name | Email | Date | Status |
|---|---|---|---|
| Sample User | sample@gmail.com | 2026-11-30 | pending |

## Error Handling and Logging

The system includes exception handling, retry attempts for AI content generation, and logging to track successful and failed operations.

## Scheduling

Windows Task Scheduler is used to execute the Python script automatically at the configured time.

## Security

- Email credentials are stored in environment variables.
- The `.env` file is excluded using `.gitignore`.
- Use dummy recipient details when sharing the project publicly.

## Author

Joanna Kareena
