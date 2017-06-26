# Note - this code must run in Python 2.7.6 and you must download
# this code must be run in command line interface 
# Implemented on Windows OS 
# By : Abinethri Santhanam (student id: 008634782)

print "Compute your profit !" 
x = 1
while(x<10):
    
    symbol = raw_input('Enter a stock symbol(as alphabets): ')
    
    try:
      allotment = int(raw_input('Enter allotment(number of shares): '))
    except:
      print "Invalid Input"
      print "Enter valid positive integer"
      continue
    try:   
      f_price = float(raw_input('Enter final share price(in dollars): '))
    except:
      print "Invalid Input"
      print "Enter valid positive integer"
      continue
   
    try:
      s_commission = float(raw_input('Enter sell commission(in dollars): '))     
    except:
      print "Invalid Input"
      print "Enter valid positive integer"
      continue

    try:   
      i_price = float(raw_input('Enter initial share price(in dollars): '))
    except:
      print "Invalid Input"
      print "Enter valid positive integer"
      continue

    try:   
      b_commission = float(raw_input('Enter buy commission(in dollars): '))
    except:
      print "Invalid Input"
      print "Enter valid postivie integer"
      continue
   
    try:
      cg_txrate = float(raw_input('Enter capital gain tax rate(in %): '))
      x = 11   
      break 
    except:
      print "Invalid Input"
      print "Enter valid postivie integer"
      continue
     
print '\n'
print "Ticker symbol: ", symbol
print "Allotment: ", allotment
print "Final Share Price: ", f_price
print "Sell Commission: ", s_commission
print "Initial Share Price: ", i_price
print "Buy commission: ", b_commission
print "Capital Gain Tax Rate(%)", cg_txrate

proceeds = allotment * f_price
total_bprice = allotment * i_price
c_gain = (allotment*f_price)-(allotment*i_price)-b_commission-s_commission

tax_amount = (cg_txrate/100) * c_gain
cost = (allotment * i_price) + b_commission + s_commission + tax_amount
 
net_profit = c_gain - tax_amount
roi = (net_profit/cost)*100
break_evn_price = ((i_price*100)+ b_commission + s_commission )/ 100

print '\n'
print "PROFILE REPORT: "
print "STOCK SYMBOL", symbol
print "PROCEEDS: ", '$',proceeds
print "COST: ", '$',cost
print "TOTAL PURCHASE PRICE: ", '$',total_bprice
print "BUY COMMISSION: ", '$',b_commission
print "SELL COMMISSION: ", '$',s_commission
print "TAX ON CAPITAL GAIN: ", '$',tax_amount
print "NET PROFIT: ", '$',net_profit
print "RETURN ON INVESTMENT: ",roi,'%'
print "FINAL SHARE PRICE TO BREAK EVEN: ", '$',break_evn_price

