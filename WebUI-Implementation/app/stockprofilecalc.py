# Note - this code must run in Python 2.7.6 and you must download
# implemented in windows 8
# requires a browser preferred Chrome 
# By : Abinethri Santhanam (student id: 008634782)

from app import app

from flask import Flask, render_template, request

@app.route('/')
def profit():
    return render_template("StockProfit.html")
@app.route('/post', methods=['POST'])
def test_func():    
    symbol = (request.form['usym'])
    a= int(request.form['uallot'])
    fsp = float(request.form['ufsp'])
    sc= float(request.form['usc'])
    isp= float(request.form['uisp'])
    bc= float(request.form['ubc'])
    r= float(request.form['utrate'])
    
    result = calculate(symbol,a,fsp,sc,isp,bc,r)
    
    return render_template("response1.html", uticksym = result['Symbol'],uproceeds= result['Proceeds'], ucost= result['Cost'], upp= result['Tpp'], ubc= result['Bc'], usc= result['Sc'], txamount= result['TxCapitalGain'], unp= result['NetProfit'], uroi= result['Roi'], ubreak= result['Breakevn'])
        
def calculate(symbol,a,fsp,sc,isp,bc,r):
    prcds = a *fsp
    total_bprice = a*isp
    c_gain = (a*fsp)-(a*isp)-bc-sc
    tax_amount = (r/100)* c_gain
    cost = (a*isp) + bc + sc + tax_amount
    net_profit = c_gain - tax_amount
    roi = (net_profit/cost) * 100
    break_evnprice = ((isp*100)+ bc + sc)/100
    dict = {'Symbol': symbol,'Proceeds': prcds, 'Cost': cost, 'Tpp': total_bprice, 'Bc': bc, 'Sc': sc, 'TxCapitalGain': tax_amount, 'NetProfit': net_profit, 'Roi': roi, 'Breakevn': break_evnprice} 
    return dict  
          
        
        