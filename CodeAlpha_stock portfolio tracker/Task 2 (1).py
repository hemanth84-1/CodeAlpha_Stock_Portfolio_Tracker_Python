from datetime import datetime
Technology={
    "Name": ['Microsoft Corp.', 'NVIDIA Corp.', 'Apple Inc.'],
    "MSFT": 378.12,
    "NVDA": 210.69,
    "AAPL": 298.01,
    "Average Price": 295.61}
Financial={
    "Name": ['JPMorgan Chase & Co.', 'Visa Inc.', 'Bershire Hathaway Inc.'],
    "JPM": 325.22,
    "V": 327.24,
    "BRK.B": 489.46,
    "Average Price":380.64}
Healthcare={
    "Name": ['Eli Lilly and Co.', 'Johnson & Johnson', 'Intuitive Surgical Inc.'],
    "LLY": 1098.57,
    "JNJ": 154.5,
    "ISRG": 406.78,
    "Average Price": 553.28}
Consumer_Discretionary= {
    "Name": ['Amazon.com Inc.', 'Tesla Inc.','Costco Wholesale Corp.'],
    "AMZN": 188.1,
    "TSLA": 175.4,
    "COST": 845.55,
    "Average Price": 403.02}
Communication={
    "Name": ['Alphabet Inc.','Meta Platforms Inc.','Netflix Inc.'],
    "GOOGL":178.2,
    "META": 505.35,
    "NFLX": 654.12,
    "Average Price": 445.89}
stock_type= {
    "1": Technology,
    "2": Financial,
    "3": Healthcare,
    "4": Consumer_Discretionary,
    "5": Communication}

stock_weight={}
profit=[]
loss=[]
total=0.0
net_return=0.0

def cal(n,m):
    global stock_weight,profit,loss
    avg_price=n
    stock=m
    try:
        num=int(input("Enter quantity: "))
        live_price= float(input("Enter live market price: "))
    except ValueError:
        print("\nInvalid input")
        return True
    print("\n--- Stock Portfolio Dashboard ---\n")
    avg_value=avg_price*num
    print(f"Cost Basis= ${avg_value:.2f}")
    current_value=live_price*num
    print(f"Current Market Value= ${current_value:.2f}")
    if stock not in stock_weight:
        stock_weight.update({stock:current_value})
    else:
        stock_weight.update({stock: stock_weight[stock]+current_value})
    diff=current_value-avg_value
    if diff>0:
        print(f"Unrealized Gain/Profit= +${diff:.2f}")
        profit.append(diff)
    elif diff<0:
        print(f"Unrealized Loss= -${-diff:.2f}")
        loss.append(diff)
    else:
        print("No either gain or loss")
    return_per=(diff/(avg_price*num))*100
    print(f"Total Return Percentage= {return_per:.2f}\n")
    try:
        return bool(int(input("Enter 0 if you want to continue or 1 to return main menu: ")))
    except ValueError:
        print("\nInvalid format input. Returning to main menu by default.\n")
        return True

schoice= True
while schoice:    
    print(":-:-: Welcome to Stock Portfolio Tracker :-:-:\n")
    print("1. Technology\n2. Financial\n3. Healthcare\n4. Consumer_Discretionary\n5. Communication\n6. Exit Tracker")
    print()
    sector=input("Enter sector number: ")
    fchoice=False
    if sector=='6':
        break
    if sector in stock_type:
        selected=stock_type[sector]
        stock_name=selected["Name"].copy()
        while True:
            print()
            for x,y in enumerate(stock_name, start=1):
                print(x,".",y)
            print(f"Average market price of this sector= ${selected['Average Price']}")
            print()
            name=input("Enter stock ticker symbol: ").upper().strip()
            if name not in selected:
                print("\nInvalid stock ticker\n")
                try:
                    fchoice=bool(int(input("Enter 0 if you want to retry ticker symbol or 1 to return main menu: ")))
                    if fchoice:
                        break
                except ValueError:
                    print("\nInvalid format input. Breaking loop to menu.\n")
                    break
            else:
                fchoice= cal(selected[name],name)
                if fchoice:
                    break
    else:
        print("\nInvalid sector")
    try:
        schoice=bool(int(input("\nEnter 0 if you want to exit or 1 to continue: ")))
    except ValueError:
        print("\nInvalid format of input. Closing program execution\n")
        schoice= False
        
else:
    total=sum(stock_weight.values())
    if total!=0:
        print(f"\n<--Summary-->\n\nTotal Investment Value= ${total}")
        print("\n--- Stock Weight Allocation ---\n")
        for x,y in stock_weight.items():
            per=(y/total)*100
            print(f"{x}= {per:.2f}%")
    print(f"\nTotal profit= ${sum(profit):.2f}")
    print(f"Total loss= ${-sum(loss):.2f}")
    net_return=sum(profit)+sum(loss)
    if net_return>=0:
        print(f"Net Portfolio Return= +${net_return:.2f}")
    else:
        print(f"Net Portfolio Return= -${-net_return:.2f}")
    print("\nThank you for using this tracker. Have a nice day!")
    
time=datetime.now()
now=time.strftime("%Y-%m-%d %I:%M %p")
with open("Stock_Report.txt","a") as file:
    file.write("=========================================\n")
    file.write(f"Report generated on: {now}\n")
    file.write(f"Total Investment Value= ${total:.2f}\n")
    if net_return<0:
        file.write(f"Net Portfolio Return= -${-net_return:.2f}\n")
    else:
        file.write(f"Net Portfolio Return= +${net_return:.2f}\n")
    if total!=0:
        file.write("--- Position Structure Allocations ---\n")
        for x,y in stock_weight.items():
            per=(y/total)*100
            file.write(f"{x}= {per:.2f}%\n")
    file.write("\n")
print("\nProgress successfully logged to 'Stock_Report.txt'!")
 