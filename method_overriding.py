class parent():
    def study(self):
        print("Keep Studying")

class child(parent):
    def study(self):
        print('Take a break')

c=child()
c.study()

# child.study()


