from django.core.mail import send_mail
from django.shortcuts import render
import csv
# Create your views here.
def send_emails(request):
    # Specify the path to your CSV file
    csv_file_path = r"C:\Users\yvlku\PycharmProjects\pythonProject\django project\TTM\static\email.csv"

    # Open the CSV file
    with open(csv_file_path, 'r') as csvfile:
        reader = csv.DictReader(csvfile)

        # Iterate over each row in the CSV file
        for row in reader:
            recipient_email = row['email']  # Get the email address from the 'email' column
            subject = 'Hello KLUian'  # Set your subject here
            message_body = 'Hey, Welcome to PFSD Class, Hope u have a great time with python'  # Set your email content here

            # Send the email
            send_mail(
                subject,
                message_body,
                '',  # Add your sender email address here if required
                [recipient_email],
                fail_silently=False,
            )

            # Print a message indicating that the email was sent successfully
            print(f'Sent email to {recipient_email}')

    # Assuming you have a template named 'Emails_sent_successfully.html' for rendering
    return render(request, 'Emails_sent_successfully.html')
