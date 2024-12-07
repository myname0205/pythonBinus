#class PaymentMehod:
#    nomorRekTujuan = ""
#    nominalBayar = 0
#    transactionCode = ""
#
#    def __init__(self, noRek, nominalBayar, transCode):
#        self.nomorRekTujuan = noRek
#        self.nominalBayar = nominalBayar
#        self.transactionCode = transCode
#
#    def Bayar(self):
#        print("Halo!")
#
#    def CheckTransactionCode(self):
#        print("Checking...")
#
#    def Print(self):
#        print("No. Rekening Anda:", self.nomorRekTujuan)
#        print("Nominal Pembayaran:", self.nominalBayar)
#        print("Kode Transaksi:", self.transactionCode)
#
#class KartuKredit:
#    userNumber = ""
#
#    def __init__(self, noRek, nominalBayar, transCode, userNumber):
#        PaymentMehod.__init__(self, noRek, nominalBayar, transCode)
#        self.userNumber = userNumber
#
#    def Bayar(self):
#        PaymentMehod.Bayar(self)
#        print("Ini menggunakan metode kartu kredit")
#    
#    def CheckTransactionCode(self):
#        PaymentMehod.CheckTransactionCode(self)
#        print("Please wait...")
#
#    def Print(self):
#        PaymentMehod.Print(self)
#        print("This is an extra requirement for your credit number:", self.userNumber)
#
#def main():
#    creditCardPayment = KartuKredit("0235103232", "113124441", "TRX1112487", "#223")
#    print("###Payment Method###")
#    creditCardPayment.Bayar()
#    creditCardPayment.CheckTransactionCode()
#    print("##Personal Information###")
#    creditCardPayment.Print()
#
#main()

#5.1
#class Employee:
#    
#    name = ""
#    idNumber = 0
#    deparment = ""
#    salary = ""
#
#    def __init__(self, name, idNumber, deparment, salary):
#        self.name = name
#        self.idNumber = idNumber
#        self.deparment = deparment
#        self.salary = salary
#
#    def Display(self):
#        print("Name:", self.name)
#        print("ID Number:", self.idNumber)
#        print("Department:", self.deparment)
#        print("Salary:", self.salary)
#
#class Manager:
#
#    teamSize = 0
#
#    def __init__(self, name, idNumber, deparment, salary, teamSize):
#        Employee.__init__(self, name, idNumber, deparment, salary)
#        self.teamSize = teamSize
#
#    def Display(self):
#        Employee.Display(self)
#        print("Team Size (Manager):", self.teamSize)
#        
#class Engineer:
#
#    programmingLanguages = []
#
#    def __init__(self, name, idNumber, deparment, salary, programmingLanguages):
#        Employee.__init__(self, name, idNumber, deparment, salary)
#        self.programmingLanguages = programmingLanguages
#
#    def Display(self):
#        Employee.Display(self)
#        print("Programming Lanuages (Engineer):", self.programmingLanguages)
#
#def main():
#    employeeOne = Employee("Budi", 100, "Supply", "$1000")
#    employeeTwo = Manager("Ray", 1, "Supply", "$10000", 10)
#    employeeThree = Engineer("John", 87, "Supply", "$5000", ["Python", "C++", "C#"])
#
#    print("\033[1mEMPLOYEE ONE\033[0m")
#    employeeOne.Display()
#    print("\033[1mEMPLOYEE TWO\033[0m")
#    employeeTwo.Display()
#    print("\033[1mEMPLOYEE THREE\033[0m")
#    employeeThree.Display()
#
#main()

#FIBONACCI SEQ
#def CalculateFibonnaciSequeunce(n):
#    if n <= 0:
#        return 0
#    elif n == 1:
#        return 1
#    elif n > 1:
#        return CalculateFibonnaciSequeunce(n - 1) + CalculateFibonnaciSequeunce(n - 2)
#        
#def main():
#    n = int(input("Insert n: "))
#    for i in range(n):
#        print(CalculateFibonnaciSequeunce(i), end=" ")
#
#main()

#HW
class PaymentMethod:

    paymentMethodname = ""
    total = 0
    totalDiscount = 0
    
    def __init__(self, paymentMethodName):
        self.paymentMethodName = paymentMethodName

    def Pay(self):
        self.total = self.total - self.totalDiscount
        return self.total
        
class CreditCard(PaymentMethod):

    paymentMethodname = "Credit Card"
    total = 0
    totalDiscount = 0
    paymentType = ""
    bank = ""
    totalTagihan = 0
    installment = 0

    def __init__(self, paymentType, bank, totalTagihan, installment):
        PaymentMethod.__init__(self, self.paymentMethodName)
        self.paymentType = paymentType
        self.bank = bank
        self.totalTagihan = totalTagihan
        self.installment = installment

    def getTotalInstallment(self):
        return self.installment

    def getTotalDiscount(self):
        return self.totalDiscount
    
    def Pay(self):
         discountPercent = 9
         adminFee = 25000
         
         if self.paymentType == "full_payment":
             if self.bank == "BCA":
                 discountPercent = 10
             elif(self.bank == "MANDIRI"):
                 discountPercent = 12
             elif(self.bank == "UOB"):
                 discountPercent = 13
         else:
             self.totalTagihan = self.totalTagihan/self.installment
             discountPercent = 0
         
         self.totalDiscount = self.totalTagihan * discountPercent/100
         self.total = self.totalTagihan - self.totalDiscount + adminFee
         return self.total

        
        