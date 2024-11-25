class SBI:
    ROI = 0.07  

    def __init__(self, Name, Mobno, Aadhar, Gender, Bal, Pin):
        self.Name = Name
        self.Mobno =Mobno  
        self.Aadhar = Aadhar
        self.Gender = Gender
        self.Bal = Bal
        self.Pin = Pin

    def Details(self):
        print(f'Name   : {self.Name}')
        print(f'Mobno  : {self.Mobno}')
        print(f'Aadhar : {self.Aadhar}')
        print(f'Gender : {self.Gender}')
        print(f'Bal    : {self.Bal}')
        print(f'Pin    : {self.Pin}')

    def withdraw(self):
        if self.Checkpin() == self.Pin:
            amount = int(input('Enter the amount to withdraw: '))
            if self.Bal >= amount:
                self.Bal -= amount
                print('Amount debited successfully.')
                print(f'The available balance is {self.Bal}')
            else:
                print('Insufficient balance.')
        else:
            print('Invalid pin.')

    @staticmethod
    def Checkpin():
        return int(input('Enter the 4-digit pin: '))

    def deposit(self):
        amount = int(input('Enter the amount to deposit: '))
        self.Bal += amount
        print('Amount credited successfully.')
        print(f'The available balance is {self.Bal}')

    @classmethod
    def changeROI(cls):
        var = float(input('Enter the new Rate of Interest (ROI): '))
        cls.ROI = var
        print(f'Rate of Interest changed to {cls.ROI}')


cust1 = SBI('Sudheer', '7095644965', '98349203928', 'male', 5000, 1234)
cust2 = SBI('Naveen', '8500023115', '859392829926', 'male', 7000, 5678)
cust1.withdraw()
