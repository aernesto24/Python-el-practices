print("***THIS PROGRAM CALCULATE THE VOLUME OF A BOX***")
print("")

class VolumeCalc:
    
    def __init__(self, base, height, depth):
        self.base = base
        self.height = height
        self.depth = depth
        
    def volume_calculation(self):
        return self.base * self.height * self.depth


b = int(input("Enter the base of the box: "))
h = int(input("Enter the height of the box: "))
d = int(input("Enter the depth of the box: "))

volumebox1 = VolumeCalc(b, h, d)
print("The volume of the box is: ", volumebox1.volume_calculation(), "m3")