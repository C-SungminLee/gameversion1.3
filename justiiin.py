import random as rand
import turtle as trtl
import math
import time

##################
### Game setup ###
##################

wn = trtl.Screen()
wn.addshape("taco.gif")
wn.addshape("burrito.gif")
#wn.addshape("tabasco.gif")
wn.addshape("fork.gif")

# Taco
taco = trtl.Turtle()
score = 0

taco.speed(0)
taco.penup() 

#-----game start-----
game_start = False
start_button = trtl.Turtle()
start_button.shapesize(4)

def start_game(x, y):
  global game_start
  game_start = True
  start_button.hideturtle()
  taco.showturtle()
  taco.shape("taco.gif")
start_button.onclick(start_game)

while game_start != True:
  taco.hideturtle()

# Score Writer
score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.hideturtle()
score_writer.setposition(-200, -180)
score_writer.pendown()
# Font
font_setup = ("Arial", "15", "normal")

score_writer.write(str(score) + " tacos", font = font_setup)

# Taco per click upgrade Button
tpc = trtl.Turtle()
tpc.speed(0)
tpc.shape("fork.gif")
tpc.penup()
tpc.setposition(-170, 180)

# Score rate
score_rate = 1
upgrade_cost = (score_rate*2)**2

rate = trtl.Turtle()
rate.speed(0)
rate.penup()
rate.hideturtle()
rate.setposition(-200, -220)
rate.pendown()
rate.write("tacos per click: " + str(score_rate))

next = trtl.Turtle()
next.speed(0)
next.penup()
next.hideturtle()
next.setposition(-220, 200)
next.pendown()
next.write("Next upgrade: " + str(upgrade_cost) + " tacos")

# Point Text
p = trtl.Turtle()
p.hideturtle()
p.speed(3)

#-----autoclickers-----

# tabasco
tabasco = trtl.Turtle()

sauce_list = [tabasco]
tabasco_delay = 1000
wait = False
for sauces in sauce_list:
  sauces.penup()
  sauces.speed(0)
tabasco.setposition(0, -200)
#tabasco.shape("tabasco.gif")
######################
### Game functions ###
######################
def taco_click(x, y):
  update_score()
  

def update_score():
  score_writer.clear()
  global score
  score += score_rate
  print(score)
  score_writer.write(str(score) + " tacos", font = font_setup)
  

def tpc_click(x, y):
  upgrade(tpc) 


def upgrade(upgrade):
  global score_rate, score, upgrade_cost
  if score >= upgrade_cost:
    score_rate += 1
    rate.clear()
    rate.write("Tacos per click: " + str(score_rate))
    score -= upgrade_cost
    score_writer.clear()
    score_writer.write(str(score) + " tacos", font = font_setup)
    upgrade_cost = (score_rate*2)**2

    next.clear()
    next.write("Next upgrade: " + str(upgrade_cost) + " tacos")

tpc.onclick(tpc_click)
taco.onclick(taco_click)

#-----autoclickers------

# tabasco
tabasco_click = 0

def tabasco_clickk():
  global score, wait
  score += tabasco_click
  wait = False

def tabasco_autoclick():
  global wait
  if wait == False:
    wait = True
    wn.ontimer(tabasco_clickk, tabasco_delay)

wn.ontimer(tabasco_clickk, tabasco_delay)

tabasco_bought = False
def buy_tabasco(x, y):
  global tabasco_bought
  tabasco_bought = True
  buy_sauce()

# all clickers
while game_start == True:
  tabasco_autoclick()
  

def buy_sauce():
  global tabasco_click, tabasco_bought
  if tabasco_bought == True:
    tabasco_click += 1
    tabasco_bought = False
tabasco.onclick(buy_tabasco, "1")
wn.listen()
wn.mainloop()
