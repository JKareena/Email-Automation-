import openpyxl
import datetime
import os 
from dotenv import load_dotenv
load_dotenv()
import smtplib
from email.message import EmailMessage
import requests
import time 

# Load credentials
sender_email = os.getenv("EMAIL_ADDRESS")
app_password = os.getenv("EMAIL_PASSWORD")
print(sender_email)
print(bool(app_password))

#excel loop 
workbook = openpyxl.load_workbook("email_list.xlsx")
worksheet = workbook["Sheet1"]
for row in worksheet.iter_rows(min_row=2):
    name = row[0].value
    email = row[1].value
    date = row[2].value
    status = row[3].value.strip()
    today = datetime.date.today()
    #print("Checking:", repr(name), repr(email), repr(date), repr(status))
    #print(date.date(),today.weekday())
    if date.date() == today and status == "pending" and (today.weekday() == 4 or today.weekday() == 5 or today.weekday() == 6):
        print("MATCH FOUND -", name,"-", status)
        
        #ollama api call to generate email content
        data = {
            "model": "llama3.2:1b",
            "prompt": f"""Write a short, professional and friendly invitation email addressed to {name}.

            The email is about an AI Technology Event taking place on 30 November 2026 at Taj Coromandel, Chennai.

            Invite the recipient to attend and express that we look forward to seeing them.

            Date: 30 November 2026
            Time: 10:00 AM to 1:00 PM
            Venue: Taj Coromandel, Chennai.

            Start directly with "Dear {name},".
            Do not include introductory phrases, a subject line, placeholders, or invented event details.

            End with "Best regards, Joanna".""",
            "stream": False
            }
        r = None
        for i in range(2):
            try:
                response = requests.post("http://localhost:11434/api/generate", json=data, timeout=120)
                response.raise_for_status()
                r = response.json()
                if not r.get("response"):
                    raise ValueError("Ollama returned an empty email.")    
                break
            except Exception as e:
                print(e)
                if i < 1:
                    print("Retrying...")
                    time.sleep(5)
        if r is None:
            print("Failed to generate email content after 2 attempts, Stopping the program.")
            exit()
            
        #create the email message
        msg = EmailMessage()
        msg["Subject"] = "Invitation: AI Technology Event - 30 November"
        msg["From"] = sender_email
        msg["To"] = email
        msg.set_content(r["response"])

        server = None
        #try/except block to handle errors
        try:
            # connect to gmail server 
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            
            #login to the email 
            server.login(sender_email, app_password)

            #sending the email
            server.send_message(msg)
            row[3].value = "sent"
            status = "sent"
            print("Email sent successfully!")

        except Exception as e:
            row[3].value = "failed"
            status = "failed"
            print(e)
            print("Email sending failed")
        
        finally:
            if server:
                server.close()
        print(f"Processed - name: {name} - email: {email} - date: {date} - status: {status}")
workbook.save("email_list.xlsx")

#to test the ollama api connection,uncomment the below lines to test the connection to the ollama api
#response = requests.get("http://localhost:11434")
#print(response.text)














'''for cell in row:
        print(cell.value, end = " ")
    print()
print(worksheet.max_row)
print(worksheet.max_column)'''

