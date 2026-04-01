"""
This program is a simple version of a store inventory management.
It allows a user to:
1. View the store's inventory
2. Add new products to the inventory
3. remove products from the inventory
"""
############################################################################
#Section 1 - Import Modules and Global Variables
###########################################################################
import random  # used to generate random PID

store_inventory = [ # sample store inventory
  {'product_id': 4327, 'type': 'Shoes', 'price': 100.0, 'total': 20},
  {'product_id': 3915, 'type': 'Tshirts', 'price': 43.5, 'total': 32},
  {'product_id': 2119, 'type': 'Pants', 'price': 34.0, 'total': 19},
  {'product_id': 1194, 'type': 'Jumpers', 'price': 250.0, 'total': 5},  
  {'product_id': 1300, 'type': 'Blouse', 'price': 24.76, 'total': 3},
  {'product_id': 1118, 'type': 'Dress', 'price': 50.0, 'total': 10}, 
  {'product_id': 1664, 'type': 'Suits', 'price': 250, 'total': 5}
] 

program_loop = True # used to check on program status: True means running and False means stop running

##############################################################################
#Section 2 - Functions Definition
#############################################################################

#Displays the main menu
def display_menu():
  print("\n **GenZ STORE INVENTORY SYSTEM**")  
  print("1. View Store Inventory ") 
  print("2. Add A New Product")   
  print("3. Remove Products")  
  print("4. Exit\n")  

  #used to capture and process user selections
def user_selection():
    in_use =True
    user_choice = int(input("Enter a number between 1-4: "))
    if user_choice == 1:  #Go to Store Inventory.
        display_inventory()  #print('show inventory')
    elif user_choice == 2:  #Initiate New Product Process.
        add_new_product()  #print('add a new product')   
    elif user_choice == 3:  #Initiate Removing a Product.
        remove_product()  #print('remove a product')
    elif user_choice == 4:  #Exit the program
        print("Thank you for using the program!"
              )  # adds thank you message before exiting the program
        in_use = False  #print("program ends.")  # changes the value of isUsed to False
    else:
        print("\nSorry, Not a Valid Choice. Please try again!")
    return in_use

# this function displays story inventory
def display_inventory():
    print("\n **GEN-Z STORE INVENTORY**")
    for product in store_inventory:
        print("----------------------------")
        for key, value in product.items():            
          print(f"{key}:{value}")          
    print("___________________________")

# add a new product function
def add_new_product():    
    print("\n **Adding A New Product To The Inventory**")
    print("------------------------------------")
    type = input("Enter a type(Shoes, Jacket,...): ").capitalize()
    #simple validation technique
    try:
        price = float(input("Enter a price: "))
    except ValueError:
        price = 0.0  # assigned a default number
    try:
        total = int(input("Enter a total: "))  #needs validation
    except ValueError:
        total = 0  # assigned a default number

    # only add a product to the inventory if price and total greater than zero
    if price > 0 and total > 0:
        #create a new product instance based on the attributes provided
        new_product = Product(type, price, total)      
        store_inventory.append(new_product.features()) # added product to inventory
        display_inventory() #  used for testing

    else:
        print(
            "Invalid Price or/and Total. Product not Added to the Inventory ")




#Remove a product
def remove_product():  
    to_delete_index = -1
    display_inventory()
    print("\n **Removing A Product From The Inventory**")
    print("------------------------------------")
    try:
        PID = int(input("Enter Product ID Number to Remove: "))
    except ValueError:
        PID = 0
    for i, product in enumerate(store_inventory):           
        if store_inventory[i]["product_id"] == PID:
            to_delete_index = i  #index of the product to delete
            break # ends the search and loop

    #outside of the loop
    if to_delete_index == -1:  #no product found based on the PID
        print("This is not in the inventory. Try again.")
    else:       
        store_inventory.pop(to_delete_index)  # delete the product from the inventory
        print("Product was successfully removed from the store inventory.")

#####################################################################################
#Section 3 - Class Definition
######################################################################################

class Product:
    #constructor method used to instantiate any new class
    def __init__(self, type, price, total):
        self.product_id = random.randint(1000,5000)  # new attribute added
        self.type = type        
        self.price = price        
        self.total = total

    def features(self):
      return {"product_id":self.product_id,
              "type":self.type,
              "price":self.price,
              "total":self.total
             }

##################################################################################
#Section 4 - Running Section
##################################################################################

while program_loop:
  display_menu()
  program_loop =user_selection() 
