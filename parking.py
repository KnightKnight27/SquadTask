from collections import defaultdict

class Car:

    def __init__(self, reg_no, age):
        self.reg_no = reg_no
        self.age = age


class ParkingLot:

    def __init__(self, max_size):

        self.max_size = max_size

        self.current_cars = 0

        self.slots = [None for i in range(self.max_size)]

        self.slot_regno = defaultdict(str)
        self.reg_age = defaultdict(int)
        self.regno_slot = defaultdict(int)
        self.age_reg = defaultdict(list)
        self.age_slot = defaultdict(list)

    def __isFull(self):
        if self.current_cars == self.max_size:
            return True
        return False

    def __isEmpty(self):
        if self.current_cars == 0 and self.max_size > 0:
            return True
        return False

    def __getNearestSlot(self):
        for idx, slot in enumerate(self.slots):
            if not slot:
                return idx
        return -1

    def park(self, reg_no, age):
        car = Car(reg_no, age)
        slot = self.__getNearestSlot()
        if self.__isFull():
            return [False,"Parking Lot is Full"]
        elif slot != -1:
            self.slots[slot] = car
            self.current_cars += 1
            self.slot_regno[slot] = reg_no
            self.regno_slot[reg_no] = slot
            self.age_reg[age].append(reg_no)
            self.age_slot[age].append(slot)
            self.reg_age[reg_no] = age
            return [True,'Car with vehicle registration number "{}" has been parked at slot number {}'.format(reg_no ,slot+1)]

    def leave(self, slot):
        slot-=1
        if not self.max_size:
            return [False, "Sorry Parking Slot is empty"]
        elif self.slots[slot] is not None:
            car = self.slots[slot]
            
            age = car.age

            reg_no = car.reg_no
            self.slots[slot] = None
            self.current_cars -= 1
            del self.slot_regno[slot]

            del self.regno_slot[reg_no]

            self.age_reg[age].pop(self.age_reg[age].index(reg_no))

            self.age_slot[age].pop(self.age_slot[age].index(slot))

            del self.reg_age[reg_no]

            return [True,'Slot number {} vacated, the car with vehicle registration number "{}" left the space, the driver of the car was of age {}'.format(slot+1,reg_no,age)]
        return [False, "Slot already Vacant"]

    def getRegistrationNumbersFromAge(self, age):
        age=int(age)
        if not self.max_size:
            return [False, "Sorry, parking lot is not created"]
        elif self.age_reg[age]:
            reg_nos = ", ".join(self.age_reg[age])
            return [True, "The following are the registration number of cars with driver of age {} are ".format(age) + reg_nos]
        else:
            return [False, "Not found"]

    def getSlotNumbersFromAge(self, age):
        if not self.max_size:
            return [False, "Sorry, parking lot is not created"]
        elif len(self.age_slot[age]):
            slot1 = [i+1 for i in self.age_slot[age]]
            slot1.sort()
            slots = ",".join(map(str, slot1 ) )
            return [True,(slots)]
        else:
            return [False, "Not found"]

    def getSlotNumberFromRegNo(self, regNo):
        if not self.max_size:
            return [False, "Sorry, parking lot is not created"]
        elif self.regno_slot[regNo]:
            return [True, self.regno_slot[regNo]+1]
        return [False, "Not Found"]
