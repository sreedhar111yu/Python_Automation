airtel_recharge =50
data =1

if airtel_recharge >= 400 or data>=1.5:
    print("discount applied")
    dicount_amt= airtel_recharge *(15/100)
    final_price =airtel_recharge-dicount_amt
    print("Discount price:",dicount_amt)
    print("Final price:",final_price)

else:
    print("Discount above 400$ or 1.5GB data")