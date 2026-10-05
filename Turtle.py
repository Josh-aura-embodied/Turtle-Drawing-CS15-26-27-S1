from turtle import *

speed(4)
pensize(3)

penup()
goto(-120, -80)
pendown()
color("brown")

goto(120, -80)
goto(120, 80)
goto(-120, 80)
goto(-120, -80)

penup()
goto(-140, 80)
pendown()

goto(140, 80)
goto(0, 220)
goto(-140, 80)

penup()
goto(-25, -80)
pendown()
color("darkred")

goto(-25, 0)
goto(25, 0)
goto(25, -80)

penup()
goto(-95, -20)
pendown()
color("blue")

goto(-55, -20)
goto(-55, 20)
goto(-95, 20)
goto(-95, -20)

penup()
goto(55, -20)
pendown()

goto(95, -20)
goto(95, 20)
goto(55, 20)
goto(55, -20)

penup()
goto(15, -45)
pendown()
color("black")

goto(20, -45)
goto(20, -40)
goto(15, -40)
goto(15, -45)

done()