from parking import Car
from parking import ParkingLot
import sys
sys.stdout=open("output.txt","w")
class Parking:
    
    def __init__(self):
        self.parking = None
        self.command = []
    def functions(self, command):
        self.command = command.split()
        if self.command[0] == "Create_parking_lot":
            lotcount = int(self.command[1])
            self.parking = ParkingLot(lotcount)
            print("Created parking of " + str(lotcount) + " slots")
        elif self.command[0] == "Park":
            regno = self.command[1].strip()
            age = int(self.command[3].strip())
            response = self.parking.park(regno, age)
            print(response[1])
        elif self.command[0] == "Slot_numbers_for_driver_of_age":
            age = int(self.command[1].strip())
            response = self.parking.getSlotNumbersFromAge(age)
            print(response[1])
        elif self.command[0] == "Slot_number_for_car_with_number":
            regno = self.command[1].strip()
            response = self.parking.getSlotNumberFromRegNo(regno)
            print(response[1])
        elif self.command[0] == "Leave":
            slot = int(self.command[1])
            response = self.parking.leave(slot)
            print(response[1])
        elif self.command[0] == "Vehicle_registration_number_for_driver_of_age":
            slot = self.command[1]
            response = self.parking.getRegistrationNumbersFromAge(slot)
            print(response[1])
if __name__ == '__main__':
    with open('input.txt') as f:
        commands= [line.rstrip() for line in f]
    parking= Parking()
    L=commands[0].split(" ")
    if(L[0]!='Create_parking_lot'):
        print("ERROR")
        exit(0)
    for command in commands:
        parking.functions(command)
