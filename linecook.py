import serial

device = "/dev/ttyACM0"
scanner = serial.Serial(device)

while(1):
    product = scanner.readline()
    print product

scanner.close()
    
