Loan_amount = 100000
Month_Rate =2
percent =100
Months =12
Extra_days =0

Tol_Int = Month_Rate/percent


def Intrest():
    Total_Intrest =(Loan_amount * Tol_Int *Months) + (Loan_amount* Tol_Int/30 *Extra_days)
    print("your intrest is:" ,Total_Intrest)

    def Payable():
        print("your total payables :",Total_Intrest+Loan_amount)
    Payable()

Intrest()