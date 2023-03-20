import smtplib
import random
import string

def test_verify_email():
    '''
    GIVEN a user is prompted to verify their email
    WHEN an email address is given
    THEN send mail to the given email address
    '''

    # Define the sender and recipient email addresses
    sender_email = "uvicanon.emailverify@gmail.com"
    recipient_email = "test-email@gmail.com"

    ## GENERATE VERIFICATION KEY ##
    characters = string.ascii_letters + string.digits
    verification_code = ''.join(random.choice(characters) for i in range(8))

    # Define the message content
    message = f"""\
    Subject: Verify your email address
    Hi there,
    Thank you for signing up for Uvic Anon!
    Your verification code is 
    {verification_code}
    Best regards,
    UvicAnon
    """

    # Create an SMTP connection to a mail server
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    smtp_username = "uvicanon.emailverify@gmail.com"
    smtp_password = "gojlhivcujkidmax"
    smtp_connection = smtplib.SMTP(smtp_server, smtp_port)
    smtp_connection.starttls()
    smtp_connection.login(smtp_username, smtp_password)

    # Send the email
    error_dict = {}
    error_dict = smtp_connection.sendmail(sender_email, recipient_email, message)

    assert error_dict == {}


    # Close the SMTP connection
    smtp_connection.quit()