import turtle
from lispy.error import lispy_function

@lispy_function("turtle:forward", ["int|float"])
def turtle_forward(args):
    turtle.forward(args[0])

@lispy_function("turtle:back", ["int|float"])
def turtle_back(args):
    turtle.back(args[0])

@lispy_function("turtle:right", ["int|float"])
def turtle_right(args):
    turtle.right(args[0])

@lispy_function("turtle:left", ["int|float"])
def turtle_left(args):
    turtle.left(args[0])

@lispy_function("turtle:setpos", ["list"])
def turtle_setpos(args):
    turtle.setpos(args[0])

@lispy_function("turtle:setx", ["int[float"])
def turtle_setx(args):
    turtle.setx(args[0])

@lispy_function("turtle:sety", ["int[float"])
def turtle_sety(args):
    turtle.sety(args[0])

@lispy_function("turtle:setangle", ["int[float"])
def turtle_setangle(args):
    turtle.setheading(args[0])

@lispy_function("turtle:home")
def turtle_home(args):
    turtle.home()

@lispy_function("turtle:circle", ["int|float"])
def turtle_circle(args):
    turtle.circle(args[0])

@lispy_function("turtle:dot", ["int", "int", "int", "int"])
def turtle_dot(args):
    turtle.dot(args[0], args[1:3])

@lispy_function("turtle:undo")
def turtle_undo(args):
    turtle.undo()

@lispy_function("turtle:setspeed", ["int|float"])
def turtle_setspeed(args):
    turtle.speed(args[0])

@lispy_function("turtle:speed")
def turtle_speed(args):
    return turtle.speed()

@lispy_function("turtle:pos")
def turtle_pos(args):
    return turtle.pos()

@lispy_function("turtle:towards", ["int|float", "int|float"])
def turtle_towards(args):
    return turtle.towards(args[0:2])

@lispy_function("turtle:x")
def turtle_x(args):
    return turtle.xcor()

@lispy_function("turtle:y")
def turtle_y(args):
    return turtle.ycor()

@lispy_function("turtle:angle")
def turtle_angle(args):
    return turtle.heading()

@lispy_function("turtle:down")
def turtle_down(args):
    turtle.pendown()

@lispy_function("turtle:up")
def turtle_up(args):
    turtle.penup()

@lispy_function("turtle:setwidth", ["int"])
def turtle_setwidth(args):
    turtle.width(args[0])

@lispy_function("turtle:width")
def turtle_width(args):
    return turtle.width()

@lispy_function("turtle:isdown")
def turtle_isdown(args):
    return turtle.isdown()

@lispy_function("turtle:setpencolor", ["int|float", "int|float", "int|float"])
def turtle_setpencolor(args):
    turtle.pencolor(args[0:3])

@lispy_function("turtle:pencolor")
def turtle_pencolor(args):
    return turtle.pencolor()

@lispy_function("turtle:setfillcolor", ["int|float", "int|float", "int|float"])
def turtle_setfillcolor(args):
    turtle.fillcolor(args[0:3])

@lispy_function("turtle:fillcolor")
def turtle_fillcolor(args):
    return turtle.fillcolor()

@lispy_function("turtle:isfilling")
def turtle_isfilling(args):
    return turtle.filling()

@lispy_function("turtle:beginfill")
def turtle_beginfill(args):
    turtle.begin_fill()

@lispy_function("turtle:endfill")
def turtle_endfill(args):
    turtle.end_fill()

@lispy_function("turtle:reset")
def turtle_reset(args):
    turtle.reset()

@lispy_function("turtle:clear")
def turtle_clear(args):
    turtle.clear()

@lispy_function("turtle:hide")
def turtle_hide(args):
    turtle.hideturtle()

@lispy_function("turtle:show")
def turtle_show(args):
    turtle.showturtle()

@lispy_function("turtle:isshowed")
def turtle_isshowed(args):
    return turtle.isvisible()

@lispy_function("turtle:end")
def turtle_end(args):
    turtle.Screen().bye()