import speech_recognition as sr

# Pfad zur Audiodatei
audio_file_path = "d:\Downloads\Sprache zu Text test.m4a"

# Initialisieren des Recognizer
recognizer = sr.Recognizer()

# Audiodatei in Audio-Daten konvertieren
with sr.AudioFile(audio_file_path) as source:
    audio_data = recognizer.record(source)

# Transkription der Audiodatei
text = recognizer.recognize_google(audio_data, language="de-DE")
print(text)
