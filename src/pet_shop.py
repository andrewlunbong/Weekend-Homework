# 1 
def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

#2
def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]
#3
def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount
#4
def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]
#5
def increase_pets_sold(pet_shop, amount_sold):
    pet_shop["admin"]["pets_sold"] += amount_sold 
#6
def get_stock_count(pet_shop):
    return len(pet_shop["pets"])   
#7
def get_pets_by_breed(pet_shop, pet_breed):
    breed_of_pets = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == pet_breed:
            breed_of_pets.append(pet)
    return breed_of_pets
#8
def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"]== pet_name:
            return pet 
#9        
def remove_pet_by_name(pet_shop, name):
   pet_to_remove = find_pet_by_name(pet_shop, name)
   pet_shop["pets"].remove(pet_to_remove)
#10

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

#11

def get_customer_cash(customer_cash):
    return customer_cash["cash"]

#12 

def remove_customer_cash(customer_cash, amount):
    customer_cash["cash"] -= amount 

#13

def get_customer_pet_count(customer_index):
    return len(customer_index["pets"])


#14
def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


