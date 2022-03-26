class parent():
    def _init__(self):
        print("This is the Parent Class")
    
    def menu(dish):
        if dish == "burger":
            print("You can add the following toppings")
            print("\n Add More Cheese | Add Jalepeno | Add More Onions")
        elif dish == "Ice Cream":
            print("You can have the following flavours")
            print("\n Chocolate | Vanilla | ButterScotch | StrawBerry")
        else:
            print("Please Enter A Valid Dish From The Menu")
        
    
    def final_amount(dish, add_on):
        if dish == "burger" and add_on == "Cheese":
            print("\n You need to pay 100 Rupees")
        if dish == "burger" and add_on == "Jalepeno":
            print("\n You need to pay 110 Rupees")
        if dish == "burger" and add_on == "Onions":
            print("\n You need to pay 150 Rupees")
        if dish == "Ice Cream" and add_on == "Chocolate":
            print("\n You need to pay 90 Rupees")
        if dish == "Ice Cream" and add_on == "Vanilla":
            print("\n You need to pay 90 Rupees")
        if dish == "Ice Cream" and add_on == "ButterScotch":
             print("\n You need to pay 90 Rupees")
        if dish == "Ice Cream" and add_on == "StrawBerry":
             print("\n You need to pay 200 Rupees")
        
class child1(parent):
    
    def __init__(self, dish):
        self.new_dish = dish 
    def get_menu(self):
        parent.menu(self.new_dish)

class child2(parent):
    def __init__(self, dish, add_on):
        self.new_dish = dish 
        self.new_add_on = add_on
    def Order(self):
        parent.final_amount(self.new_dish, self.new_add_on)
        
child1_object = child1("Ice Cream")    

child2_object = child2("Ice Cream", "Chocolate")
child2_object.Order()
