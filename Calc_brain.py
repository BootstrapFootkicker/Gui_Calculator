class Calculator:
    def choose_operation(self, operation,x,y):
        if operation == '+':
            return x + y
        elif operation == '-':
             return x - y
        elif operation == '/':
            return x/y
        elif operation=='X':
            return x * y
        else:
            print("no")


