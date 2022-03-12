import time, sys, os

def write(string): # spells the letters one by one
  for ch in string:
    sys.stdout.write(ch)
    sys.stdout.flush()
    time.sleep(0.035) # controls the time between each letter spelled
  print()

def clear(): # function that clears the screen
  os.system('clear') 

class EdwardsCafe:
  def __init__(self):
    self.specials = ["[1] - xiaolongbao (soup dumplings)", "[2] - chicken soup", "[3] - mild golden curry"]
    self.fast_foods = ["[1] - cheeseburger", "[2] - pizza", "[3] - fries"]
    self.asian_foods = ["[1] - dumplings", "[2] - Beijing duck", "[3] - steamed buns"]
    self.finspecials = ["xiaolongbao (soup dumplings)", "chicken soup", "mild golden curry"]
    self.finfast_foods = ["cheeseburger", "pizza", "fries"]
    self.finasian_foods = ["dumplings", "Beijing duck", "steamed buns"]
    self.drinks = ["[1] - soda", "[2] - juice", "[3] - tea", "[4] - coffee"]
    self.findrinks = ["soda", "juice", "tea", "coffee"]
    customer = input("Hi! What is your name?\n")
    self.customer = customer
    write(f"Welcome to Edward's PythonCafe, {self.customer}!")
    write("Please wait while we find you a seat.\n")
    time.sleep(3)
    write("Thank you for dining with Edward's PythonCafe today!")
    write(f"What can I get for you, {self.customer}?")
    write("We have: [1] - our specials, [2] - fast_foods, [3] - asian_foods")
    want = int(input())
    self.want = want
    if self.want == 1:
      write(f"We have: {', '.join(self.specials)}")
      special = int(input())
      self.special = special
      food = self.specials_choice(self.special)
      self.food = food
    elif self.want == 2:
      write(f"We have: {', '.join(self.fast_foods)}")
      fast_food = int(input())
      self.fast_food = fast_food
      self.food = self.fast_foods_choice(self.fast_food)
    elif self.want == 3:
      write(f"We have: {', '.join(self.asian_foods)}")
      asian_food = int(input())
      self.asian_food = asian_food
      self.food = self.asian_foods_choice(self.asian_food)
    write("Would you like some drinks? [yes/no]")
    choose = input()
    self.choose = choose
    if self.choose == "no":
      self.checkout(self.food)
    elif self.choose == "yes":
      write(f"We have: {', '.join(self.drinks)}")
      option = int(input()) 
      self.option = option
      drink = self.drinks_choice(self.option)
      self.drink = drink
      self.checkout(self.food, drink=self.drink)
  def specials_choice(self, special):
    self.special = special
    if self.special == 1:
      self.special = self.finspecials[0]
    elif self.special == 2:
      self.special = self.finspecials[1]
    elif self.special == 3:
      self.special = self.finspecials[2]
    return self.special
  def fast_foods_choice(self, fast_food):
    self.fast_food = fast_food
    if self.fast_food == 1:
      self.fast_food = self.finfast_foods[0]
    elif self.fast_food == 2:
      self.fast_food = self.finfast_foods[1]
    elif self.fast_food == 3:
      self.fast_food = self.finfast_foods[2]
    return self.fast_food
  def asian_foods_choice(self, asian_food):
    self.asian_food = asian_food
    if self.asian_food == 1:
      self.food = self.finasian_foods[0]
    elif self.asian_food == 2:
      self.asian_food = self.finasian_foods[1]
    elif self.asian_food == 3:
      self.asian_food = self.finasian_foods[2]
    return self.asian_food
  def drinks_choice(self, drink):
    self.drink = drink
    if self.drink == 1:
      self.drink = self.findrinks[0]
    elif self.drink == 2:
      self.drink = self.findrinks[1]
    elif self.drink == 3:
      self.drink = self.findrinks[2]
    elif self.drink == 4:
      self.drink = self.findrinks[3]
    return self.drink
  def checkout(self, food, drink=None):
    self.drink = drink
    self.food = food
    if self.drink:
      write(f"You have ordered a {self.food} and a {self.drink}")
      time.sleep(1)
      write("Thank you for ordering today! See you again!")
    else:
      write(f"You have ordered a {self.food}")
      time.sleep(1)
      write("Thank you for ordering today! See you again!")
    
EdwardsCafe()
