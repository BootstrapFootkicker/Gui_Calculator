from tkinter import *
from Calc_brain import Calculator

calculator = Calculator()
FONT = ('Montserrat', 12, 'bold')
operations = ['+', '-', 'X', '/']




class CalcGui:
    def clear(self):
        self.values = []
        self.x = []
        self.y = []
        self.operation = ''
        self.display_input()

    def display_input(self):
        self.display.config(text=self.values)
        # print(self.values)  # tester

    def append_value(self, mybutton):
        self.values.append(mybutton)
        self.display_input()
        print(self.values)

    def input_parser(self, input_values):
        pre_pop=False
        for count, num in enumerate(input_values):

            if num not in operations:
                self.x.append(num)
            else:
                self.operation = num
                break

        for num2 in input_values[count + 1::]:
            if num2 not in operations:
                self.y.append(num2)
            else:
                break
        temp_x = int(''.join(self.x))
        temp_y = int(''.join(self.y))

        self.result = calculator.choose_operation(self.operation, temp_x, temp_y)
        self.values = []
        print(self.result, 'result')
        # self.y = [num for num in input_values[count + 1:: ] if num in operations    ]
        self.display.config(text=self.result)
        self.x=[]
        self.values = []
        self.x = []
        self.y = []
        self.operation = ''

        # print(self.y, 'y_value')
        # print(self.x, 'x value')
        # print(self.operation, 'operation')

    def __init__(self):
        self.values = []
        self.x = []
        self.y = []
        self.operation = ''
        self.result = 0
        self.window = Tk()
        self.window.title('Calculator')
        self.window.minsize(width=250, height=450)
        self.window.config(padx=20, pady=20)
        self.display = Label(text='0', anchor='e', height=4, font=FONT)
        self.display.grid(column=0, row=0, columnspan=4)

        # Buttons

        # row 1
        self.clear_button = Button(text='AC', height=4, width=8, font=FONT, command=self.clear)
        self.plus_minus_button = Button(text='+/-', height=4, width=8, font=FONT)
        self.percentage_button = Button(text='%', height=4, width=8,
                                        font=FONT)  # no idea figure out what this actually does, Decimal???
        self.div_button = Button(text='/', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.div_button.cget('text')))

        self.clear_button.grid(column=0, row=1)
        self.plus_minus_button.grid(column=1, row=1)
        self.percentage_button.grid(column=2, row=1)
        self.div_button.grid(column=3, row=1)

        # row 2
        self.num7_button = Button(text='7', height=4, width=8, font=FONT,
                                  command=lambda: self.append_value(
                                      mybutton=self.num7_button.cget('text')))

        self.num8_button = Button(text='8', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.num8_button.cget('text')))

        self.num9_button = Button(text='9', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.num9_button.cget('text')))

        self.multiply_button = Button(text='X', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.multiply_button.cget('text')))

        self.num7_button.grid(column=0, row=2)
        self.num8_button.grid(column=1, row=2)
        self.num9_button.grid(column=2, row=2)
        self.multiply_button.grid(column=3, row=2)

        # row 3
        self.num4_button = Button(text='4', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.num4_button.cget('text')))
        self.num5_button = Button(text='5', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.num5_button.cget('text')))
        self.num6_button = Button(text='6', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.num6_button.cget('text')))
        self.subtract_button = Button(text='-', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.subtract_button.cget('text')))

        self.num4_button.grid(column=0, row=3)
        self.num5_button.grid(column=1, row=3)
        self.num6_button.grid(column=2, row=3)
        self.subtract_button.grid(column=3, row=3)

        # row 4
        self.num1_button = Button(text='1', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.num1_button.cget('text')))
        self.num2_button = Button(text='2', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.num2_button.cget('text')))
        self.num3_button = Button(text='3', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.num3_button.cget('text')))
        self.add_button = Button(text='+', height=4, width=8, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.add_button.cget('text')))

        self.num1_button.grid(column=0, row=4)
        self.num2_button.grid(column=1, row=4)
        self.num3_button.grid(column=2, row=4)
        self.add_button.grid(column=3, row=4)

        # row 5
        self.num0_button = Button(text='0', height=4, width=20, font=FONT,
                                      command=lambda: self.append_value(
                                          mybutton=self.num0_button.cget('text')))
        self.equal_button = Button(text='=', height=4, width=8, font=FONT,
                                   command=lambda: self.input_parser(input_values=self.values))
        self.decimal_button = Button(text='.', height=4, width=8, font=FONT)

        self.num0_button.grid(column=0, row=6, columnspan=2)
        self.decimal_button.grid(column=2, row=6)
        self.equal_button.grid(column=3, row=6)

        self.window.mainloop()

    # TODO create display updater/concat for digits
