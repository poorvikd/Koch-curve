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

line(bob,500)
turtle.mainloop()
