import speech_recognition as sr
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
    engine.say(text)
    engine.runAndWait()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        query = recognizer.recognize_google(audio)
        print(f"You said: {query}")
        return query
    except sr.UnknownValueError:
        print("Sorry, I didn't get that.")
        return ""
    except sr.RequestError as e:
        print(f"Sorry, an error occurred: {e}")
        return ""


if __name__ == "__main__":
    speak("Hello, I'm your voice assistant. How can I help you?")

    while True:
        query = listen().lower()

        if "Hello" in query:
            speak("Hi there! How can I assist you today?")
        elif "How is the weather today?" in query:
            speak("It is sunny here today")
        elif "How far is it from Guntur to Tirupati ?" in query:
            speak("yes, for sure. It is 370 kilometers.")
        elif "Can you tell me how to book tickets for darshan ?" in query:
            speak("you can book your tickets in TTD official website based on the slots provided amongst the given dates.")
        elif "What is the best time for darshan ?" in query:
            speak("you can allot your darshan in early hours and get to hear suprabhatam that morning.")
        elif "Are there any other transport for travelling to Tirupati ?" in query:
            speak("Yes, you can.")
        elif "How?" in query:
            speak("You can book a bus or a train to Tirupati. Or you can travel to Tirupati through flight as well.")
        elif "Can you play Telugu devotional songs on Spotify ?" in query:
            speak("Yes, of course ")
        elif "Can you increase the volume for me, please ?" in query:
            speak("Of course.")
        elif "goodbye" in query or "bye" in query:
            speak("Goodbye! Have a great day!")
            break
        else:
            speak("Sorry, I'm not sure how to help with that.")
