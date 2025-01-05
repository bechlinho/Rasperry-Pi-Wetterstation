import adafruit_dht
import board
import time
import csv
from datetime import datetime

# DHT11-Sensor auf GPIO 4 PIN initialisieren
dht_device = adafruit_dht.DHT11(board.D4)

# CSV-Datei zum Speichern der Daten
file_name = "wetterdaten.csv"

# Kopfzeile nur beim ersten Mal schreiben
with open(file_name, mode='a', newline='') as file:
    writer = csv.writer(file)
    if file.tell() == 0:  # Datei ist leer
        writer.writerow(["Zeit", "Temperatur (°C)", "Luftfeuchtigkeit (%)"])

try:
    while True:
        # Werte vom Sensor lesen
        temperature = dht_device.temperature
        humidity = dht_device.humidity

        # Aktuelle Zeit erfassen
        current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # Daten ausgeben
        print(f"{current_time} - Temperatur: {temperature:.1f}°C, Luftfeuchtigkeit: {humidity:.1f}%")

        # Daten in CSV speichern (wetterdaten.csv)
        with open(file_name, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([current_time, temperature, humidity])

        # Warte 20 Sekunden vor der nächsten Messung
        time.sleep(20)

except KeyboardInterrupt:
    print("Messung beendet.")
except RuntimeError as error:
    print(f"Fehler: {error}")
finally:
    dht_device.exit()
