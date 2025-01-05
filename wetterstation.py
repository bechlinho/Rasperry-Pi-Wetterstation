import adafruit_dht
import board
import time

# DHT11-Sensor auf GPIO-PIN 4 initialisieren
dht_device = adafruit_dht.DHT11(board.D4)

try:
    while True:
        # Liest die Temperatur vom DHT-Sensor
        temperature = dht_device.temperature
        # Liest die Luftfeuchtigkeit vom DHT-Sensor
        humidity = dht_device.humidity
        # Gibt die gemessene Temperatur auf .1 genau an
        print(f"Temperatur: {temperature:.1f}°C")
        # Gibt die gemessene Luftfeuchtigkeit auf .1 genau an
        print(f"Luftfeuchtigkeit: {humidity:.1f}%")
        
        # Wartet 20 Sekunden vor der nächsten Messung, um den Sensor nicht zu überlasten
        time.sleep(20)
except KeyboardInterrupt:
    # Beendet die Schleife, wenn der Nutzer `Strg+C` drückt
    print("Messung beendet.")
except RuntimeError as error:
    # Fängt Laufzeitfehler des Sensors ab, z. B. wenn der Sensor kurzzeitig nicht erreichbar ist
    print(f"Fehler: {error}")
finally:
    # Stellt sicher, dass die Ressourcen des DHT-Sensors freigegeben werden
    dht_device.exit()
