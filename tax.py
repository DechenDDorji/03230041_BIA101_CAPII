# it represents the attributes of employee that are name,income,position,number of chidern and expense per child
class Employee:
    def __init__(self, name, income, position, num_childern,expenses_per_child):
        self.name = name
        self.income = income
        self.position = position
        self.num_children = num_childern
        self.expenses_per_child=expenses_per_child

class DeductionsCalculator: # code use to deductions from the income
    def __init__(self,income, position,num_childern,expenses_per_child):
        self.income=income
        self.position = position
        self.num_childern=num_childern 
        self.expenses_per_child=expenses_per_child

    def calculate_deductions(self):
        total_deduction=0
        if self.position=='regular': # Deduction based on position 
            total_deduction += self.income * 0.10 # Deduction based on income
            total_deduction += min (350000 * self.num_childern,self.expenses_per_child * self.num_childern)  # Deduction for children expenses
            total_deduction += 200
        
        else:
             total_deduction += self.income * 0.10
             total_deduction += min (350000 * self.num_childern,self.expenses_per_child * self.num_childern)
             total_deduction += 200
        return total_deduction
        

class TaxCalculator:  # Calculate taxes based on income, position, and dependent information.
    def __init__(self, income,position,num_childern,expenses_per_child):
        self.income = income
        self.position=position
        self.num_childern=num_childern
        self.expenses_per_child=expenses_per_child

    def calculate_taxable_income(self):  # Calculate the taxable income after deducting applicable deductions.
        deductions_calc = DeductionsCalculator(self.income,self.position,self.num_childern,self.expenses_per_child)
        total_deductions = deductions_calc.calculate_deductions()
        taxable_income = self.income - total_deductions
        return taxable_income

    def calculate_tax(self,taxable_income): # calculation of the tax payable with the given tax classes or Calculate tax based on the taxable income using progressive tax rates.
        if taxable_income <=300000:
            return 0
        elif  300001 <  taxable_income <400000:
            return taxable_income * 0.1
        elif  400001 <  taxable_income <650000:
            return taxable_income * 0.15
        elif  650001 <  taxable_income <1000000:
            return taxable_income * 0.2
        elif  1000001 <  taxable_income <1500000:
            return taxable_income * 0.25
        else:
            return taxable_income *0.30
        
        
     

   


try: # Get employee information from user input
    name = input("Enter employee name: ")
    income = float(input("Enter employee income: "))
    position = input("Enter employee position (Contract/Regular): ").lower()
    num_children = int(input("Enter number of children: "))
    expense=int(input('Enter expenses per child :'))

    employee = Employee(name, income, position, num_children,expense)
    deduction=DeductionsCalculator(income,position,num_children,expense)
    cal_deduction=deduction.calculate_deductions()
    print('deductable amount is ',cal_deduction)

    tax_calculator = TaxCalculator(income,position,num_children,expense)
    taxable_income = tax_calculator.calculate_taxable_income()
    print('Taxable income is ', taxable_income)

    if income < 300000:
        print("Income is below taxable threshold. No tax is payable.")
    else:
        tax_calculator = TaxCalculator(income,position,num_children,expense)
        taxable_income = tax_calculator.calculate_taxable_income()
        tax_amount = tax_calculator.calculate_tax(taxable_income)
        print(name,'you have to pay tax of Nu.',  tax_amount)

except ValueError:
    print("Invalid input for income, number of children, or insurance premium.")
