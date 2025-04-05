import requests
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText
import time

# CONFIGURATION
PRODUCT_URL = 'https://example.com/product-page'
CHECK_INTERVAL = 60 * 10  # check every 10 minutes
IN_STOCK_TEXT = 'In Stock'
HEADERS = {'User-Agent': 'Mozilla/5.0'}

# EMAIL/SMS SETTINGS
SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
EMAIL_ADDRESS = 'your_email@gmail.com'
EMAIL_PASSWORD = 'your_email_password'

EMAIL_RECIPIENTS = [
    'family1@example.com',
    'family2@example.com',
]

SMS_RECIPIENTS = [
    '5551234567@vtext.com',
    '5559876543@tmomail.net',
]


def check_availability():
    try:
        response = requests.get(PRODUCT_URL, headers=HEADERS)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()

        if IN_STOCK_TEXT.lower() in text.lower():
            print("Item is in stock!")
            return True
        else:
            print("Item is out of stock.")
            return False

    except Exception as e:
        print(f"Error checking availability: {e}")
        return False


def send_notification():
    subject = "🔔 Item Back in Stock!"
    body = f"The item is now available! Check here: {PRODUCT_URL}"
    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = EMAIL_ADDRESS

    all_recipients = EMAIL_RECIPIENTS + SMS_RECIPIENTS

    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            for recipient in all_recipients:
                message['To'] = recipient
                server.sendmail(EMAIL_ADDRESS, recipient, message.as_string())
                print(f"Notification sent to {recipient}")
    except Exception as e:
        print(f"Error sending notifications: {e}")


def main():
    print("Monitoring started...")
    while True:
        if check_availability():
            send_notification()
            break  # Stop after alert or remove to keep monitoring
        time.sleep(CHECK_INTERVAL)


if __name__ == '__main__':
    main()
