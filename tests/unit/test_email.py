def test_verify_email():
    '''
    GIVEN a user is prompted to verify their email
    WHEN an email address is given
    THEN send mail to the given email address
    '''

    # Define the sender and recipient email addresses
    sender_email = "uvicanon.emailverify@gmail.com"
    recipient_email = "test-email@gmail.com"


    # Send the email
    error_dict = {}
    error_dict = smtp_connection.sendmail(sender_email, recipient_email, message)

    assert error_dict == {}