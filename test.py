import firebase_admin
from firebase_admin import credentials, db, auth

# Initialize Firebase Admin SDK
cred = credentials.Certificate("C:\\Users\\marek\\OneDrive - MUNI\\Lenovo\\Desktop\\Programy_2.0\\my_icq\\first-4b2ba-firebase-adminsdk-aph4j-f5db4b419b.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://first-4b2ba-default-rtdb.firebaseio.com/"
})

# Function to authenticate user and send a message to the Realtime Database
def send_message_as_authenticated_user(uid, message):
    try:
        # Send the message to the database
        ref = db.reference('/first-4b2ba/Message')  # Reference to the 'Message' node in your database
        ref.push().set({
            'uid': uid,
            'message': message
        })

        print("Message sent successfully to the database as authenticated user.")
    except Exception as e:
        print(f"Error sending message to the database: {e}")

# Example usage
if __name__ == "__main__":
    uid = "UID_OF_AUTHENTICATED_USER"
    message = "Hello, Firebase!"
    send_message_as_authenticated_user(uid, message)
