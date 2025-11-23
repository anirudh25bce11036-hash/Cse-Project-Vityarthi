**README.md** 

# 📈 Brokerage & Profit/Loss Calculator

A simple Python script that helps traders calculate **buy value, sell value, brokerage, turnover, and net profit/loss** for stock trades.

This tool is useful for beginners who want to understand how brokerage and charges affect their overall profit.


## 🚀 Features

* Accepts **buy quantity & price**
* Accepts **sell quantity & price**
* Calculates:

  * Total Buy Value
  * Total Sell Value
  * Gross Profit/Loss
  * Turnover
  * Brokerage (0.02% of turnover by default)
  * Other Charges (₹10 fixed)
  * Net Profit/Loss after charges
* Easy to run and modify


## 📥 How to Use

1. Make sure you have **Python 3** installed.
2. Save the script as `brokerage_calculator.py`.
3. Run it in your terminal:

```bash
python brokerage_calculator.py
```

4. Enter the values when prompted:

   * Number of shares bought
   * Buy price
   * Number of shares sold
   * Sell price

The program will display a detailed breakdown of your trade results.



## 📊 Example Output

```
------ Brokerage & Profit/Loss Calculator ------

Enter number of shares bought: 100
Enter buy price per share: 150
Enter number of shares sold: 100
Enter sell price per share: 160

----------- Results -----------
Total Buy Value : ₹15000.00
Total Sell Value : ₹16000.00
Gross Profit/Loss : ₹1000.00
Turnover : ₹31000.00
Brokerage (0.02%) : ₹6.20
Other Charges : ₹10.00
Net Profit/Loss : ₹983.80
--------------------------------




You can change:

* **Brokerage rate**


brokerage = 0.0002 * turnover


* **Other Charges**


other_charges = 10


Modify as needed for different brokers.

## 📄 License

This project is free to use and modify.
