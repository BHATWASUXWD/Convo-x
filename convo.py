import requests
import json

# Facebook Page Access Token
PAGE_ACCESS_TOKEN = 'your_page_access_token'

# Recipient ID - the ID of the user you're sending the message to
RECIPIENT_ID = 'recipient_user_id'

# Path to the message file
message_file_path = 'path_to_message_file.txt'

# Sender's "hatername" (the custom sender name)
hatername = 'YourHaterName'

# Function to read message from a file
def read_message_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"Error: File not found: {file_path}")
        return None

# Read the message from the file
message_text = read_message_from_file(message_file_path)

if message_text:
    # Add the hatername to the message
    message_with_name = f"{hatername} says: {message_text}"

    # Prepare the message payload
    message_data = {
        'recipient': {'id': RECIPIENT_ID},
        'message': {'text': message_with_name}
    }

    # Facebook Graph API URL for sending messages
    url = f'https://graph.facebook.com/v16.0/me/messages?access_token={PAGE_ACCESS_TOKEN}'

    # Sending the POST request to the API
    response = requests.post(url, json=message_data)

    # Print the response from Facebook
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print(f"Failed to send message: {response.status_code}")
        print(response.text)
else:
    print("No message to send.")
