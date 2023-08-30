import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Key phrase to listen for
key_phrase = "Hello"

def listen_and_print():
    print("Function triggered! Listening...")
    while True:
        with sr.Microphone() as source:
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print("You said:", text)
            except sr.UnknownValueError:
                print("Sorry, could not understand audio")
            except sr.RequestError as e:
                print("Error requesting results; {0}".format(e))

while True:
    retries = 3  # Maximum number of retries
    success = False

    while retries > 0 and not success:
        with sr.Microphone() as source:
            print("Listening for key phrase...")
            audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print("You said:", text)
                
                if(text.lower() == "hello"):
                    print("Key word detected")
                    listen_and_print()  # Start listening and printing continuously
                    success = True
            except sr.RequestError as e:
                print("Error requesting results; {0}".format(e))
                break
            except Exception as e:
                print("Error:", e)
                retries -= 1
                print(f"Retries remaining: {retries}")

        if not success:
            print("Retrying...")
