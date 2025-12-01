import turtle


def draw_koch_snowflake (order, size= 300 ):
    window = turtle. Screen ()
    window. bgcolor ( "white" )

    t=turtle. Turtle ()
    t. speed ( 0 )  
    t. penup ()
    t. goto (-size / 2 , 0 )
    t. pendown ()

    koch_snowflake(t, order, size)

    window. mainloop ()


def koch_snowflake (t: turtle.Turtle, order, size= 300, side = 3):
    if side == 1:
        koch_curve (t, order, size, side)
    else:
        koch_curve (t, order, size, side)
        t. left (-120)
        koch_snowflake (t, order, size, side - 1 )


def koch_curve (t: turtle.Turtle, order, size, side):
    print('FLAKE ', 'order - ', order, 'side - ', side)
    if order == 0:
        t. forward (size)
    else:
        for angle in [ 60 , - 120 , 60 , 0 ]:
            koch_curve (t, order - 1 , size / 3, side )
            t. left (angle)


draw_koch_snowflake ( 3 )