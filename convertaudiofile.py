from pydub import AudioSegment
import os

# Variablen für die Konfiguration
input_file_path = "D:\Downloads\Sprache zu Text test.m4a"  # Pfad zur Eingabedatei
output_file_path = "D:\Downloads\Sprache zu Text test.wav"  # Pfad zur Ausgabedatei mit Dateiname und Erweiterung
input_format = "m4a"  # Eingangsformat (z.B. "m4a", "mp3", "wav", "ogg", "flv")
output_format = "wav"  # Ausgangsformat (z.B. "m4a", "mp3", "wav", "ogg", "flv")

# Unterstützte Formate für Eingabe und Ausgabe
supported_formats = ["mp3", "wav", "ogg", "flv", "m4a", "aac"]

# Überprüfen, ob das Eingangs- und Ausgangsformat unterstützt werden
if input_format not in supported_formats:
    raise ValueError(f"Eingangsformat '{input_format}' wird nicht unterstützt. Unterstützte Formate sind: {supported_formats}")

if output_format not in supported_formats:
    raise ValueError(f"Ausgangsformat '{output_format}' wird nicht unterstützt. Unterstützte Formate sind: {supported_formats}")

# Überprüfen, ob die Eingabedatei vorhanden sind, wenn nicht, wird eine Fehlermeldung ausgegeben und das Programm beendet, ansonsten wird die Datei geladen
if not os.path.exists(input_file_path):
    raise FileNotFoundError(f"Eingabedatei '{input_file_path}' nicht gefunden.")

# Überprüfen, ob die Ausgabedatei bereits vorhanden ist und fragen, ob sie überschrieben werden soll
if os.path.exists(output_file_path):
    user_input = input(f"Ausgabedatei '{output_file_path}' existiert bereits. Möchten Sie sie überschreiben? (j/n): ")
    if user_input.lower() != "j":
        print("Vorgang abgebrochen.")
        exit()

# Laden Sie die Audiodatei im angegebenen Eingangsformat
audio = AudioSegment.from_file(input_file_path, format=input_format)

# Exportieren Sie die Datei im angegebenen Ausgangsformat
audio.export(output_file_path, format=output_format)

print(f"Datei erfolgreich konvertiert und gespeichert unter: {output_file_path}")
