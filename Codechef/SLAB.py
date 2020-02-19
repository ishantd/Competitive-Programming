try:
    T = input().split(" ")

    tax_slabs = []
    tax_percent = []
    money = 0
    percent = 5
    count = 0

    for i in range (6):
        money = money + 250000
        
        tax_slabs.append(money)
        
        tax_percent.append(percent)
        percent = percent + 5
        
    def find_tax(cash):
        global count
        if cash<=tax_slabs[0]:
            return 0
        else:
            for i in range(6):
                if cash>=tax_slabs[i]:
                    count=count+1
            tax = ((tax_slabs[count-1])*(tax_percent[count-2]/100)) - 12500 
            tax = tax + (cash-tax_slabs[count-1])*(tax_percent[count-1]/100)
                    
            return int(tax)                                            

    for i in range(int(T)):
        cash = input()
        print(int(cash)-find_tax(int(cash)))

except:
    print("error")