import random as rand
import turtle as trtl
import math
import time


##################
### Game setup ###
##################

wn = trtl.Screen()

wn.setup(580,449)
wn.addshape("taco.gif")
wn.addshape("menu.gif")
wn.addshape("burrito.gif")
wn.addshape("buttonunpressed.gif")
wn.addshape("buttonpressed.gif")
wn.addshape("fork.gif")
wn.addshape("background.gif")
rectCors = ((-10,20),(10,20),(10,-20),(-10,-20))
wn.register_shape('rectangle',rectCors)
score = 0

# math problems and answers for burrito lootbox
math_problems = ["1 + 1 = ?","84 / 4 = ?","5 * 25 = ?","3^4 = ?","9 ^ 1/2 = ?","6 * 2 = ?", "50 / 10 = ?","Solve for x. 9((3x+6)/3) = 0"]
math_anwers = ["2", "21", "125","81","3", "12", "5", "-2"]

# Score Writer
score_writer = trtl.Turtle()
score_writer.speed(0)
score_writer.penup()
score_writer.hideturtle()
score_writer.setposition(-200, -180)
score_writer.pendown()
# Font
font_setup = ("Arial", "15", "normal")


# Taco per click upgrade Button
button = trtl.Turtle()
button.speed(0)
button.penup()
button.setposition(-200, 120)

# Burrito math loot box
burrito = trtl.Turtle()
burrito.speed(0)
burrito.shape("burrito.gif")
burrito.penup()
burrito.hideturtle()
burrito.setposition(200, 120)

  




# Score rate
score_rate = 1
upgrade_cost = (score_rate*2)**2

rate = trtl.Turtle()
rate.speed(0)
rate.penup()
rate.hideturtle()
rate.setposition(-200, -160)
rate.pendown()

# Score rate upgrade text
next = trtl.Turtle()
next.color("moccasin")
next.speed(0)
next.penup()
next.hideturtle()
next.setposition(-245, 180)
next.pendown()

# Taco
taco = trtl.Turtle()
score = 0
taco.shape("taco.gif")

taco.speed(0)
taco.penup() 

font_setup = ("Arial", "15", "normal")

# Point Text
p = trtl.Turtle()
p.hideturtle()
p.speed(3)


#-----game start-----
wn.bgpic("menu.gif")
game_start = False
settings = trtl.Turtle()
settings.shape("rectangle")
start_button = trtl.Turtle()
start_button.color("lemonchiffon")
start_button.shape("fork.gif")

start_button.shapesize(4)




######################
### Game functions ###
######################


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
tabasco_autoclick()
  

def buy_sauce():
  global tabasco_click, tabasco_bought
  if tabasco_bought == True:
    tabasco_click += 1
    tabasco_bought = False





def start_game(x, y):
  global game_start
  wn.setup(612,410)
  wn.bgpic("background.gif")
  game_start = True
  start_button.hideturtle()
  taco.showturtle()
  score_writer.write(str(score) + " tacos", font = font_setup)
  score_writer.write(str(score) + " tacos", font = font_setup)
  


  taco.shape("taco.gif")
  button.shape("buttonunpressed.gif")
  next.write("Next upgrade: " + str(upgrade_cost) + " tacos",font = ("Arial", "7", "italic"))
  rate.write("tacos per click: " + str(score_rate))




start_button.onclick(start_game)


while game_start != True:
  taco.hideturtle()
  button.hideturtle()



def countdown():
  burrito.showturtle()
  wn.ontimer(countdown, rand.randint(30000,120000))

wn.ontimer(countdown,rand.randint(30000,120000))


#When the taco is clicked increase the score
def taco_click(x, y):
  update_score()

#When the burrito is clicked ask a random math question
def burrito_click(x, y):
  lootbox()

#Asking the random math question
def lootbox():
  number = rand.randint(0,len(math_problems)-1)  
  answer = wn.textinput("Problem","What is " + str(math_problems[number]))
  while answer != math_anwers[number]:
    answer = wn.textinput("Problem","Try again what is " + (math_problems[number]))
  else:
    score_writer.clear()
    global score
    score = score + score_rate*rand.randint(50,150) 
    print(score)
    score_writer.write(str(score) + " tacos", font = font_setup)
    burrito.hideturtle()
    burrito.hideturtle()

#update the amount of tacos
def update_score():
  score_writer.clear()
  taco.speed(2)
  taco.setposition(rand.randint(-100,100),rand.randint(-100,100))
  taco.speed(0)
  global score
  score += score_rate
  print(score)
  score_writer.write(str(score) + " tacos", font = font_setup)
  

#When the button is clicked upgrade
def button_click(x, y):
  upgrade() 

#Upgrade the rate of tacos per click
def upgrade():
  global score_rate
  global score
  global upgrade_cost
  if score >= upgrade_cost:
    button.shape("buttonpressed.gif")
    score_rate += 1
    rate.clear()
    rate.write("Tacos per click: " + str(score_rate))
    score -= upgrade_cost
    score_writer.clear()
    score_writer.write(str(score) + " tacos", font = font_setup)
    upgrade_cost = (score_rate*2)**3

    next.clear()
    next.write("Next upgrade: " + str(upgrade_cost) + " tacos")
    button.shape("buttonunpressed.gif")




#detecting the clicks
wn.onkeypress(buy_tabasco, "1")
burrito.onclick(burrito_click)
button.onclick(button_click)
taco.onclick(taco_click)
button.showturtle()


wn.mainloop()