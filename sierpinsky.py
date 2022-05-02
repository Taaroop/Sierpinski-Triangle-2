import turtle as t

t.speed(0)

angle = 60
distance = 2
iterations = 10

x_cor = -30
y_cor = 0

li_ins = ["x"]

t.penup()
t.goto(x_cor, y_cor)
t.pendown()

for i in range(iterations):
    length = len(li_ins)
    last_ins = li_ins[length-1]
    ins_now = ""
    
    for letter in last_ins:
        if letter == "x":
            ins_now += "y+x+y"
        elif letter == "y":
            ins_now += "x-y-x"
        else:
            ins_now += letter
    
    li_ins.append(ins_now)

    
for ins in li_ins:
    for char in ins:
        if char == "+":
            t.right(angle)
        if char == "-":
            t.left(angle)
        t.forward(distance)

t.mainloop()