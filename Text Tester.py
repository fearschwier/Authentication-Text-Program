from twilio.rest import Client #Imports Twilio, the service used to send the text messages.
from random import randint #Imports random to generate a random integer for authentication

accountSID = "" #The account SID of my twilio account, censored for privacy sake
authToken = "" #The accountToken given to me by Twilio, censored for privacy sake
TwilioNumber = '+19259400688' #The number given to me by Twilio to text from
myNumber = '+16812617130' #The number I wish to text
twilioCli = Client(accountSID, authToken)

def get_message() -> None:
    """
    Generates the message texted to the user, which is a random integer of length 4,
    and sends this to be texted to the end user, and prompts verification
    """
    message = randint(1000, 9999)
    text_message(message)
    verify_user(message)

def text_message(message_input: int) -> None:
    """
    Texts the message to the end user

    Arugment: message_input
        the 4 digit random int to be sent to the user
    """
    message = twilioCli.messages.create(body = message_input, from_=TwilioNumber, to=myNumber)

def verify_user(number_texted):
    """
    Prompts verification to end user in inputs.
    If the input matches the text, send a welcome message
    If the number doesn't match, send an Error, and prompt again.
    """
    while True:
        verify = input("Enter the verification code sent to your phone number\n")
        if verify == str(number_texted):
            print("You are now verified... Welcome")
            break
        else:
            print("Error! Wrong passcode Entered.")
            continue


if __name__ == "__main__":
    get_message()




