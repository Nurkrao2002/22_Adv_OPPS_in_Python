from abc import ABC,abstractmethod
class Payment():
    def printslip(self,amount):
        print("Purchase Amount is ",amount)

    def payment(self,amount):
        print('ok')

class cardpayment(Payment): pass
    # def payment(self,amount):
    #     print("Credit card Payment of",amount)
class walletpayment(cardpayment):
    def payment(self,amount):
        print("Wallet Payment of",amount)


c=cardpayment()
# c.payment(200)
# c.printslip(200)
# print(isinstance(c,Payment))
# c=walletpayment()
# c.payment(300)
# c.printslip(300)

