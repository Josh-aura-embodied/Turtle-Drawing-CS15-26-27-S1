from turtle import *

speed(4)
pensize(3)

# --- 1. MAIN BUILDING ---
penup()
goto(-120, -80)
pendown()
color("brown")

goto(120, -80)
goto(120, 80)
goto(-120, 80)
goto(-120, -80)

# --- 2. ROOF ---
penup()
goto(-140, 80)
pendown()
color("darkslategray")

goto(140, 80)
goto(0, 220)
goto(-140, 80)

# --- 3. FRONT DOOR ---
penup()
goto(-25, -80)
pendown()
color("darkred")

goto(-25, 0)
goto(25, 0)
goto(25, -80)

# --- 4. LEFT WINDOW ---
penup()
goto(-95, -20)
pendown()
color("blue")

goto(-55, -20)
goto(-55, 20)
goto(-95, 20)
goto(-95, -20)

# --- 5. RIGHT WINDOW ---
penup()
goto(55, -20)
pendown()

goto(95, -20)
goto(95, 20)
goto(55, 20)
goto(55, -20)

# --- 6. DOORKNOB ---
penup()
goto(15, -45)
pendown()
color("black")

goto(20, -45)
goto(20, -40)
goto(15, -40)
goto(15, -45)

done()