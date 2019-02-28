
import random

class Pound:

    # constructor in order to create methods in the class
    # when we make an object "coin1", then "self" gets replaced by "coin1"
    # when we make an object "coin2", then "self" gets replaced by "coin2"
    def __init__(self, rare = False): 
        
        self.rare = rare

        if self.rare:
            self.value = 1.25
        else:
            self.value = 1.00
        
        self.color = "gold"
        self.num_edges = 1
        self.diameter = 22.5     # in mm
        self.thickness = 3.15    # in mm
        self.heads = True

    def __del__(self):
        print("Coin Spent!")

    def rust(self):
        self.color = "greenish"

    def clean(self):
        self.color = "gold"

    def flip(self):
        heads_options = [True, False]
        choice = random.choice(heads_options)
        self.heads = choice
    
    
# object is an instance of a class
coin1 = Pound(rare = True)
coin2 = Pound()

print(coin1.rare)
print(coin2.rare)
print(coin1.value)
print(coin2.value)

print(coin1.color)
coin1.rust()
print(coin1.color)
coin1.clean()
print(coin1.color)

coin1.flip()
print(coin1.heads)
coin1.flip()
print(coin1.heads)

del coin1

# if we uncomment the below, then coin1 will not be defined anymore
# coin1.value()



 

