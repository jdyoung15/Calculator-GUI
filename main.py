from Tkinter import *

class Display(Frame):

    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createWidget()
        self.initial = True
        self.seen_op = False

    def createWidget(self):
        self.output = Label(self, text="0", bg="white", bd=5, \
            relief=SUNKEN, width=25)
        self.output.pack()

    def append_num(self, num):
        if self.initial == True:
            self.output["text"] = num
            self.initial = False
        else:
            if self.seen_op == True:
                self.ready_equals = True
            self.output["text"] += num

    def append_op(self, op):
        if self.initial == True:
            self.output["text"] = "0"
        elif self.seen_op == False \
            or ("=" in op and self.ready_equals == True):
            self.output["text"] += " " + op + " "
            self.seen_op = True
 
    def get_str(self):
        return self.output["text"]

    def set_str(self, value):
        self.output["text"] = value

    def clear(self):
        self.output["text"] = "0"
        self.set_initial()

    def set_initial(self):
        self.initial = True
    
    def set_seen_op(self):
        self.seen_op = False 
       

class Application(Frame):

    def __init__(self, display, master=None):
        Frame.__init__(self, master)
        self.display = display
        self.createWidgets()
 

    def createWidgets(self):

        self.one = Button(self, text="1", height=2, width=5)
        self.one["command"] = self.append_one
        self.one.grid(row=2)

        self.two = Button(self, text="2", height=2, width=5)
        self.two["command"] = self.append_two
        self.two.grid(row=2, column=1)

        self.three = Button(self, text="3", height=2, width=5)
        self.three["command"] = self.append_three
        self.three.grid(row=2, column=2)

        self.four = Button(self, text="4", height=2, width=5)
        self.four["command"] = self.append_four
        self.four.grid(row=1)

        self.five = Button(self, text="5", height=2, width=5)
        self.five["command"] = self.append_five
        self.five.grid(row=1, column=1)

        self.six = Button(self, text="6", height=2, width=5)
        self.six["command"] = self.append_six
        self.six.grid(row=1, column=2)

        self.seven = Button(self, text="7", height=2, width=5)
        self.seven ["command"] = self.append_seven
        self.seven.grid(row=0, column=0)

        self.eight = Button(self, text="8", height=2, width=5)
        self.eight ["command"] = self.append_eight
        self.eight.grid(row=0, column=1)

        self.nine = Button(self, text="9", height=2, width=5)
        self.nine["command"] = self.append_nine
        self.nine.grid(row=0, column=2)

        self.zero = Button(self, text="0", height=2, width=5)
        self.zero["command"] = self.append_zero
        self.zero.grid(row=3, column=0)

        self.clear = Button(self, text="C", height=2, width=5)
        self.clear["command"] = self.handle_clear
        self.clear.grid(row=3, column=1)

        self.plus = Button(self, text="+", height=2, width=5)
        self.plus["command"] = self.append_plus
        self.plus.grid(row=3, column=3)

        self.minus = Button(self, text="-", height=2, width=5)
        self.minus["command"] = self.append_minus
        self.minus.grid(row=2, column=3)

        self.multiply = Button(self, text="*", height=2, width=5)
        self.multiply["command"] = self.append_multiply
        self.multiply.grid(row=1, column=3)

        self.divide = Button(self, text="/", height=2, width=5)
        self.divide["command"] = self.append_divide
        self.divide.grid(row=0, column=3)

        self.equals = Button(self, text="=", height=2, width=5, \
            state=DISABLED)
        self.equals["command"] = self.perform_op
        self.equals.grid(row=3, column=2)

        self.deactivate_ops()

    def append_one(self):
        self.append_num_general("1")

    def append_two(self):
        self.append_num_general("2")

    def append_three(self):
        self.append_num_general("3")

    def append_four(self):
        self.append_num_general("4")

    def append_five(self):
        self.append_num_general("5")

    def append_six(self):
        self.append_num_general("6")

    def append_seven(self):
        self.append_num_general("7")

    def append_eight(self):
        self.append_num_general("8")

    def append_nine(self):
        self.append_num_general("9")

    def append_zero(self):
        self.append_num_general("0")

    def append_num_general(self, num):
        if self.display.seen_op == False:
            self.activate_ops()
        else:
            self.activate_equals()
        self.display.append_num(num) 

    def append_plus(self):
        self.append_op_general("+")

    def append_minus(self):
        self.append_op_general("-")

    def append_multiply(self):
        self.append_op_general("*")

    def append_divide(self):
        self.append_op_general("/")

    def handle_clear(self):
        self.display.clear()
        self.display.set_seen_op()
        self.deactivate_ops()
        self.deactivate_equals()

    def append_op_general(self, op):
        self.deactivate_ops()
        self.display.append_op(op)

    def activate_ops(self):
        self.plus["state"] = ACTIVE
        self.minus["state"] = ACTIVE
        self.multiply["state"] = ACTIVE
        self.divide["state"] = ACTIVE

    def deactivate_ops(self):
        self.plus["state"] = DISABLED 
        self.minus["state"] = DISABLED
        self.multiply["state"] = DISABLED
        self.divide["state"] = DISABLED

    def activate_equals(self):
        self.equals["state"] = ACTIVE

    def deactivate_equals(self):
        self.equals["state"] = DISABLED

    def perform_op(self):
        args = self.display.get_str().split(" ") 
        arg1 = args[0]
        arg2 = args[2]
        op = args[1]
        result = ""

        if op == "+":
            result = str(int(arg1) + int(arg2))
        elif op == "-":
            result = str(int(arg1) - int(arg2))
        elif op == "*":
            result = str(int(arg1) * int(arg2))
        else:
            result = str((int(arg1) + 0.0) / int(arg2))

        self.display.set_str(result)
        self.display.set_initial()
        self.display.set_seen_op()
        self.deactivate_ops()
        self.deactivate_equals()



root = Tk()
root.title('Calculator')
top_frame = Display(master=root)
top_frame.pack(side=TOP)
app = Application(top_frame, master=root)
app.pack(side=BOTTOM)
app.mainloop()
root.destroy()
