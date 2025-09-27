# kenyan_flag_turtle.py
import turtle
import math

# --- Configuration ---
FLAG_W = 600      # flag width in pixels
FLAG_H = 400      # flag height in pixels (3:2 ratio -> 600x400)
CENTER = (0, 0)
STRIPE_H = FLAG_H / 3

# Colors
BLACK = "#000000"
RED = "#FF0000"
GREEN = "#006600"
WHITE = "#FFFFFF"
SPEAR_COLOR = "#444444"
SHIELD_RED = "#C8102E"

# Setup screen
screen = turtle.Screen()
screen.setup(width=FLAG_W + 50, height=FLAG_H + 50)
screen.title("Kenyan Flag - Turtle")
screen.tracer(0)   # turn off animation for faster drawing

t = turtle.Turtle()
t.hideturtle()
t.speed("fastest")
t.pensize(1)

# Helper: draw filled rectangle with center-based coordinates
def draw_rect_center(cx, cy, w, h, color):
    t.up()
    t.goto(cx - w/2, cy - h/2)
    t.setheading(0)
    t.down()
    t.fillcolor(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
    t.end_fill()
    t.up()

# Helper: draw ellipse (parametric)
def draw_ellipse(cx, cy, a, b, color, pen_width=1):
    t.up()
    points = []
    steps = 120
    for i in range(steps + 1):
        theta = 2 * math.pi * i / steps
        x = cx + a * math.cos(theta)
        y = cy + b * math.sin(theta)
        points.append((x, y))
    t.goto(points[0])
    t.down()
    t.pensize(pen_width)
    t.fillcolor(color)
    t.begin_fill()
    for (x, y) in points:
        t.goto(x, y)
    t.end_fill()
    t.up()

# Draw the flag background stripes (black, red, green)
# The Kenyan flag actually has 5 stripes with thin white fimbriations:
# top: black (1/3), middle: red (1/3), bottom: green (1/3)
# White thin stripes separate the red from black and green.
# We'll draw black, then a thin white, then red, then thin white, then green.

# Entire flag centered at CENTER
cx, cy = CENTER

# Draw black stripe (top third)
draw_rect_center(cx, cy + STRIPE_H, FLAG_W, STRIPE_H, BLACK)

# thin white fimbriation (between black and red)
fimb = 6  # thickness for the white separators
draw_rect_center(cx, cy + fimb/2, FLAG_W, fimb, WHITE)  # between top and middle (positioned)

# Draw red stripe (middle third)
draw_rect_center(cx, cy, FLAG_W, STRIPE_H, RED)

# second thin white fimbriation (between red and green)
draw_rect_center(cx, cy - STRIPE_H + fimb/2, FLAG_W, fimb, WHITE)

# Draw green stripe (bottom third)
draw_rect_center(cx, cy - STRIPE_H, FLAG_W, STRIPE_H, GREEN)

# Draw the shield and spears roughly centered
# Shield dimensions relative to flag
shield_cx, shield_cy = cx, cy
shield_a = 60   # horizontal radius (half-width)
shield_b = 110  # vertical radius (half-height)

# Draw spears (behind the shield)
def draw_spear(x1, y1, x2, y2):
    # draw shaft
    t.up()
    t.goto(x1, y1)
    t.down()
    t.pensize(6)
    t.pencolor(SPEAR_COLOR)
    t.setheading(t.towards(x2, y2))
    t.goto(x2, y2)

    # spear head (triangle)
    head_len = 25
    angle = math.radians(15)
    heading = t.heading()
    # position at tip
    tx, ty = x2, y2
    # compute two base points of triangle
    left_x = tx - head_len * math.cos(math.radians(heading) - angle)
    left_y = ty - head_len * math.sin(math.radians(heading) - angle)
    right_x = tx - head_len * math.cos(math.radians(heading) + angle)
    right_y = ty - head_len * math.sin(math.radians(heading) + angle)
    t.up()
    t.goto(tx, ty)
    t.down()
    t.fillcolor(SPEAR_COLOR)
    t.begin_fill()
    t.goto(left_x, left_y)
    t.goto(right_x, right_y)
    t.goto(tx, ty)
    t.end_fill()
    t.up()
    t.pensize(1)

# draw two crossed spears (behind shield)
# left-to-right spear
draw_spear(shield_cx - 160, shield_cy + 120, shield_cx + 40, shield_cy - 140)
# right-to-left spear
draw_spear(shield_cx + 160, shield_cy + 120, shield_cx - 40, shield_cy - 140)

# Draw shield: layered ellipses to approximate the Kenyan Maasai shield
# Outer white border (slightly larger)
draw_ellipse(shield_cx, shield_cy, shield_a + 18, shield_b + 18, WHITE, pen_width=1)
# Outer red field (main)
draw_ellipse(shield_cx, shield_cy, shield_a + 10, shield_b + 10, SHIELD_RED, pen_width=1)
# white stripe vertical (thin)
draw_ellipse(shield_cx, shield_cy, shield_a + 4, shield_b + 4, WHITE, pen_width=1)
# inner black vertical field (central panel)
draw_ellipse(shield_cx, shield_cy, shield_a - 6, shield_b - 6, BLACK, pen_width=1)
# thin white central vertical stripe (draw a narrow vertical rectangle)
t.up()
t.goto(shield_cx - 8, shield_cy + shield_b - 20)
t.down()
t.fillcolor(WHITE)
t.begin_fill()
t.setheading(270)
t.forward((shield_b - 20) * 2)
t.right(90)
t.forward(16)
t.right(90)
t.forward((shield_b - 20) * 2)
t.end_fill()
t.up()

# Add small white dots/lamps to mimic the shield markings (simple approximation)
t.goto(shield_cx - 30, shield_cy + 20)
t.down()
t.fillcolor(WHITE)
t.begin_fill()
t.circle(6)
t.end_fill()
t.up()

t.goto(shield_cx + 30, shield_cy - 20)
t.down()
t.begin_fill()
t.circle(6)
t.end_fill()
t.up()

# Final touches: center black vertical narrow shape (to echo real shield)
t.up()
t.goto(shield_cx - 4, shield_cy + shield_b - 12)
t.down()
t.fillcolor(BLACK)
t.begin_fill()
t.setheading(270)
t.forward((shield_b - 12) * 2)
t.right(90)
t.forward(8)
t.right(90)
t.forward((shield_b - 12) * 2)
t.end_fill()
t.up()

# Redraw thin white fimbriations (to ensure crispness on boundaries)
draw_rect_center(cx, cy + fimb/2, FLAG_W, fimb, WHITE)
draw_rect_center(cx, cy - STRIPE_H + fimb/2, FLAG_W, fimb, WHITE)

screen.update()
turtle.done()
