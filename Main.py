from Tkinter import *

class Display(Frame):
"""Displays to the user the numbers and operators user has entered. Current
state of user input represented as a string in self.output['text'].

"""

    def __init__(self, master=None):
    """Initializes the display.

    """
        Frame.__init__(self, master)
        self.output = Label(self, text='0', bg='white', bd=5, \
            relief=SUNKEN, width=25)
        self.output.pack()
        self.initial = True
        self.seen_op = False
        self.ready_equals = False

    def output_num(self, num):
    """Outputs the provided number NUM (which is represented as a string) to
    the display. Determines whether NUM should replace or simply be
    be appended to the display's current contents.

    """
        if self.initial == True:
            self.output['text'] = num
            self.initial = False
        else:
            if self.seen_op == True:
                self.ready_equals = True
            self.output['text'] += num

    def output_op(self, op):
    """Outputs the provided operator OP (represented as a string) to
    the display.

    """
        self.output['text'] += ' ' + op + ' '  
        self.seen_op = True

    def get_text(self):
    """Returns a string corresponding to the display content.

    """
        return self.output['text']

    def set_text(self, new_text):
    """Sets the display content to NEW_TEXT.

    """
        self.output['text'] = new_text

    def set_initial(self, boolean):
    """Sets self.initial to BOOLEAN. The instance variable self.initial
    is used to indicate whether the calculator is in its initial state 
    (i.e. the user will begin a new computation.

    """
        self.initial = boolean
 
    def get_seen_op(self):
    """Returns whether the user has already entered an operator into the
    calculator.

    """
        return self.seen_op

    def set_seen_op(self, boolean):
    """Sets self.seen_op to BOOLEAN.

    """
        self.seen_op = boolean


class Application(Frame):
"""Displays the calculator buttons (numbers, operators, clear).

"""

    def __init__(self, display, master=None):
    """Initializes the Application.
    
    """
        Frame.__init__(self, master)
        self.display = display
        self.createWidgets()
 
    def createWidgets(self):
    """Creates the 16 buttons that will appear on the calculator, along
    with their underlying values/functions.

    """
        num_positions = [   (3,0), (2,0), (2,1), (2,2), (1,0), \
                            (1,1), (1,2), (0,0), (0,1), (0,2)   ]  

        op_info = { '+': (3, 3), '-': (2, 3), '*': (1, 3), '/': (0, 3) }
        self.operators = {}

        #Creates the 10 number buttons.
        for i in range(10):
            button = Button(self, text=str(i), height=2, width=5)
            button['command'] = lambda i=i: self.handle_num_general(str(i))
            r, c = num_positions[i][0], num_positions[i][1]
            button.grid(row=r, column=c)

        #Creates the 4 operator buttons.
        for op,position in op_info.iteritems():
            button = Button(self, text=str(op), height=2, width=5)
            button['command'] = lambda op=op: self.handle_op_general(op)
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

    def handle_num_general(self, num):
    """Called when the user clicks one of the number buttons.

    """
        if not self.display.get_seen_op():
            self.change_ops_state(ACTIVE)
        else:
            self.change_equals_state(ACTIVE)
        self.display.output_num(num) 

    def handle_op_general(self, op):
    """Called when the user clicks one of the operator buttons.

    """
        self.change_ops_state(DISABLED)
        self.display.output_op(op)

    def perform_op(self):
    """Called when the user clicks the equals button. Does the actual
    calculation and returns the result.

    """
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
            result = float(arg1) / float(arg2)
            result = '%.0f' % (result) if round(result) == result \
                else '%f' % (result)

        self.reset(result)

    def reset(self, new_text):
    """Returns the calculator to its initial state. Called after the clear
    or equal button has been clicked.

    """
        self.display.set_text(new_text)
        self.display.set_initial(True)
        self.display.set_seen_op(False)
        self.change_ops_state(DISABLED)
        self.change_equals_state(DISABLED)

    def change_ops_state(self, state):
    """Changes the four operator buttons to an either ACTIVE (the buttons
    can be clicked, signifying that they are valid options) or DISABLED
    (nonclickable, and thus invalid options) state.

    """
        for op_button in self.operators.values():
            op_button['state'] = state

    def change_equals_state(self, state):
    """Like the CHANGE_OPS_STATE method, sets the equals button to STATE,
    which take on the value ACTIVE or DISABLED. 

    """
        self.equals['state'] = state


root = Tk()
root.title('Calculator')
top_frame = Display(master=root)
top_frame.pack(side=TOP)
app = Application(top_frame, master=root)
app.pack(side=BOTTOM)
app.mainloop()
