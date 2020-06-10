import turtle
def line(t,length):
    k=float(length)

    if k>3:
        line(t,k/3)
        t.lt(60)
        line(t,k/3)
        t.rt(120)
        line(t,k/3)
        t.lt(60)
        line(t,k/3)

    else:
        t.fd(k)

bob=turtle.Turtle()
bob.pu()
bob.bk(300)
bob.lt(90)
bob.fd(200)
bob.rt(90)
bob.pd()
line(bob,300)
bob.rt(90)
line(bob,300)
bob.rt(90)
line(bob,300)
bob.rt(90)
line(bob,300)

turtle.mainloop()
