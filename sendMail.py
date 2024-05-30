import os
import requests
import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText
from link_list import Links
from dotenv import load_dotenv

load_dotenv()
# constants
SENDER = os.getenv('SENDER_MAIL')
PASSWD = os.getenv('PASSWD')
RECEIVER= os.getenv('RECEIVER_MAIL')
TIME_INTERVAL = 10 #Delay in seconds

# Directory to save downloaded PDFs
download_dir = 'pdf_downloads'
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# Split the string into a list of URLs, removing any empty lines
url_list = Links.strip().split('\n')
# print(url_list)

# Email configuration
sender_email = SENDER
receiver_email = RECEIVER
password = PASSWD  # Use the App Password generated

# Email content
subject = "Test Email from Python"
body = "This is a test email sent from Python."

# Function to download a file from a URL
def download_pdf(url, dest_folder):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful
        filename = os.path.join(dest_folder, url.split('/')[-1])
        with open(filename, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)
        return filename
    except requests.exceptions.RequestException as e:
        print(f"Failed to download {url}: {e}")
        return None

# Function to send an email with attachment
def send_email_with_attachment(sender_email, receiver_email, password, subject, body, attachment_path):
    if not attachment_path:
        print("No attachment to send.")
        return

    # Create a MIMEText object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Attach the PDF
    try:
        with open(attachment_path, 'rb') as attachment_file:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment_file.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(attachment_path)}"')
            msg.attach(part)
    except Exception as e:
        print(f"Failed to attach the file {attachment_path}: {e}")
        return

    # Send the email
    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the connection
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print(f"Email sent successfully with attachment {os.path.basename(attachment_path)}!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Main script to download PDFs and send them via email
email_count = 0

for url in url_list:
    if url.strip():  # Check if URL is not empty
        try:
            pdf_path = download_pdf(url, download_dir)
            send_email_with_attachment(sender_email, receiver_email, password, subject, body, pdf_path)
            email_count += 1
            print(f"Total emails sent: {email_count}")
            # Delete the PDF file after sending
            os.remove(pdf_path)
            print(f"Deleted {pdf_path}")
            time.sleep(TIME_INTERVAL)  # Delay 
        except Exception as e:
            print(f"Failed to process URL {url}: {e}")

print(f"Finished sending {email_count} emails.")


# # Delete PDF files after sending all emails
# for pdf_path in pdf_paths:
#     try:
#         os.remove(pdf_path)
#         print(f"Deleted {pdf_path}")
#     except Exception as e:
#         print(f"Failed to delete {pdf_path}: {e}")