import serial

ser = serial.Serial('COM6', 115200, timeout=1)
print("Leyendo datos desde GPS...\n")

while True:
    line = ser.readline().decode('ascii', errors='replace').strip()
    if line.startswith('$GPRMC'):
        print(line)