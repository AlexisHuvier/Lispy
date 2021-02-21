import turtle
from lispy.error import lispy_function

@lispy_function("turtle:forward", ["int|float"], "Make turtle move forward")
def turtle_forward(args):
    turtle.forward(args[0])

@lispy_function("turtle:back", ["int|float"], "Make turtle move back")
def turtle_back(args):
    turtle.back(args[0])

@lispy_function("turtle:right", ["int|float"], "Make turtle turn right")
def turtle_right(args):
    turtle.right(args[0])

@lispy_function("turtle:left", ["int|float"], "Make turtle turn left")
def turtle_left(args):
    turtle.left(args[0])

@lispy_function("turtle:setpos", ["list"], "Set position of turtle")
def turtle_setpos(args):
    turtle.setpos(args[0])

@lispy_function("turtle:setx", ["int|float"], "Set x position of turtle")
def turtle_setx(args):
    turtle.setx(args[0])

@lispy_function("turtle:sety", ["int|float"], "Set y position of turtle")
def turtle_sety(args):
    turtle.sety(args[0])

@lispy_function("turtle:setangle", ["int|float"], "Set angle of turtle")
def turtle_setangle(args):
    turtle.setheading(args[0])

@lispy_function("turtle:home", [], "Teleport turtle to home")
def turtle_home(args):
    turtle.home()

@lispy_function("turtle:circle", ["int|float"], "Make circle from turtle")
def turtle_circle(args):
    turtle.circle(args[0])

@lispy_function("turtle:dot", ["int", "int", "int", "int"], "Make colored dot from turtle")
def turtle_dot(args):
    turtle.dot(args[0], args[1:3])

@lispy_function("turtle:undo", [], "Undo action")
def turtle_undo(args):
    turtle.undo()

@lispy_function("turtle:setspeed", ["int|float"], "Setting turtle speed")
def turtle_setspeed(args):
    turtle.speed(args[0])

@lispy_function("turtle:speed", [], "Getting turtle speed")
def turtle_speed(args):
    return turtle.speed()

@lispy_function("turtle:pos", [], "Getting turtle position")
def turtle_pos(args):
    return turtle.pos()

@lispy_function("turtle:towards", ["int|float", "int|float"], "Getting angle to go to argument position")
def turtle_towards(args):
    return turtle.towards(args[0:2])

@lispy_function("turtle:x", [], "Getting turtle x position")
def turtle_x(args):
    return turtle.xcor()

@lispy_function("turtle:y", [], "Getting turtle y position")
def turtle_y(args):
    return turtle.ycor()

@lispy_function("turtle:angle", [], "Getting turtle angle")
def turtle_angle(args):
    return turtle.heading()

@lispy_function("turtle:down", [], "Start drawing when move")
def turtle_down(args):
    turtle.pendown()

@lispy_function("turtle:up", [], "Stop drawing when move")
def turtle_up(args):
    turtle.penup()

@lispy_function("turtle:setwidth", ["int"], "Setting line width to turtle")
def turtle_setwidth(args):
    turtle.width(args[0])

@lispy_function("turtle:width", [], "Getting line width of turtle")
def turtle_width(args):
    return turtle.width()

@lispy_function("turtle:isdown", [], "Return if turtle is drawing")
def turtle_isdown(args):
    return turtle.isdown()

@lispy_function("turtle:setpencolor", ["int|float", "int|float", "int|float"], "Setting turtle color pen")
def turtle_setpencolor(args):
    turtle.pencolor(args[0:3])

@lispy_function("turtle:pencolor", [], "Getting turtle color pen")
def turtle_pencolor(args):
    return turtle.pencolor()

@lispy_function("turtle:setfillcolor", ["int|float", "int|float", "int|float"], "Setting turtle color fill")
def turtle_setfillcolor(args):
    turtle.fillcolor(args[0:3])

@lispy_function("turtle:fillcolor", [], "Getting turtle color fill")
def turtle_fillcolor(args):
    return turtle.fillcolor()

@lispy_function("turtle:isfilling", [], "Return if turtle is filling")
def turtle_isfilling(args):
    return turtle.filling()

@lispy_function("turtle:beginfill", [], "Start filling with turtle")
def turtle_beginfill(args):
    turtle.begin_fill()

@lispy_function("turtle:endfill", [], "Stop filling with turtle")
def turtle_endfill(args):
    turtle.end_fill()

@lispy_function("turtle:reset", [], "Reset turtle")
def turtle_reset(args):
    turtle.reset()

@lispy_function("turtle:clear", [], "Clear turtle")
def turtle_clear(args):
    turtle.clear()

@lispy_function("turtle:hide", [], "Hide turtle")
def turtle_hide(args):
    turtle.hideturtle()

@lispy_function("turtle:show", [], "Show turtle")
def turtle_show(args):
    turtle.showturtle()

@lispy_function("turtle:isshowed", [], "Return if turtle is showed")
def turtle_isshowed(args):
    return turtle.isvisible()

@lispy_function("turtle:end", [], "Stop turtle")
def turtle_end(args):
    turtle.Screen().bye()