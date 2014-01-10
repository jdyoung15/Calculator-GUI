from Tkinter import *

class Display(Frame):


    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.output = Label(self, text='0', bg='white', bd=5, \
            relief=SUNKEN, width=25)
        self.output.pack()
        self.initial = True
        self.seen_op = False
        self.ready_equals = False


    def append_num(self, num):
        if self.initial == True:
            self.output['text'] = num
            self.initial = False
        else:
            if self.seen_op == True:
                self.ready_equals = True
            self.output['text'] += num


    def append_op(self, op):
        if self.initial == True:
            self.output['text'] = '0' 
        elif not self.seen_op or ('=' in op and self.ready_equals):
            self.output['text'] += ' ' + op + ' '  
            self.seen_op = True


    def get_text(self):
        return self.output['text']


    def set_text(self, new_text):
        self.output['text'] = new_text


    def set_initial(self, boolean):
        self.initial = boolean
 

    def get_seen_op(self):
        return self.seen_op


    def set_seen_op(self, boolean):
        self.seen_op = boolean



class Application(Frame):


    def __init__(self, display, master=None):
        Frame.__init__(self, master)
        self.display = display
        self.createWidgets()
 

    def createWidgets(self):

        #The position in the grid of the i'th number (e.g. the button
        #labelled '2' will be at position (2, 1)).
        num_positions = [   (3,0), (2,0), (2,1), (2,2), (1,0), \
                            (1,1), (1,2), (0,0), (0,1), (0,2)   ]  

        op_info = { '+': (3, 3), '-': (2, 3), '*': (1, 3), '/': (0, 3) }
        self.operators = {}

        #Creates the 10 number buttons.
        for i in range(10):
            button = Button(self, text=str(i), height=2, width=5)
            button['command'] = lambda i=i: self.append_num_general(str(i))
            r, c = num_positions[i][0], num_positions[i][1]
            button.grid(row=r, column=c)

        #Creates the 4 operator buttons.
        for op,position in op_info.iteritems():
            button = Button(self, text=str(op), height=2, width=5)
            button['command'] = lambda op=op: self.append_op_general(op)
            button.grid(row=position[0], column=position[1])
            self.operators[op] = button

        self.equals = Button(self, text='=', height=2, width=5)
        self.equals['command'] = self.perform_op
        self.equals.grid(row=3, column=2)

        self.clear = Button(self, text='C', height=2, width=5)
        self.clear['command'] = lambda: self.reset('0') 
        self.clear.grid(row=3, column=1)

        self.change_equals_state(DISABLED)
        self.change_ops_state(DISABLED)


    def append_num_general(self, num):
        if not self.display.get_seen_op():
            self.change_ops_state(ACTIVE)
        else:
            self.change_equals_state(ACTIVE)
        self.display.append_num(num) 


    def append_op_general(self, op):
        self.change_ops_state(DISABLED)
        self.display.append_op(op)


    def perform_op(self):
        args = self.display.get_text().split(' ') 
        arg1 = args[0]
        arg2 = args[2]
        op = args[1]
        result = ''

        if op == '+':
            result = str(int(arg1) + int(arg2))
        elif op == '-':
            result = str(int(arg1) - int(arg2))
        elif op == '*':
            result = str(int(arg1) * int(arg2))
        else:
            result = str((int(arg1) + 0.0) / int(arg2))

        self.reset(result)


    def reset(self, new_text):
        self.display.set_text(new_text)
        self.display.set_initial(True)
        self.display.set_seen_op(False)
        self.change_ops_state(DISABLED)
        self.change_equals_state(DISABLED)


    def change_ops_state(self, state):
        for op_button in self.operators.values():
            op_button['state'] = state


    def change_equals_state(self, state):
        self.equals['state'] = state


root = Tk()
root.title('Calculator')
top_frame = Display(master=root)
top_frame.pack(side=TOP)
app = Application(top_frame, master=root)
app.pack(side=BOTTOM)
app.mainloop()
