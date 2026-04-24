import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tradingeconomics as te
te.login('')

#Please subscribe to a plan at https://tradingeconomics.com/api/pricing.aspx to get an API key.

#getting data to plot a bar chart
mydata = te.fetchMarkets(symbol = 'aapl:us')
 
y_pos = np.arange(len(list(mydata)))

#Values from the Open, High, Low, Close got from fetchMarkets(symbol = 'aapl:us', for 2017-01-03 ) 
performance = [0,1158000,1163300,1147600,1161500]

plt.bar(y_pos, performance, align='center', alpha=0.3)
plt.xticks(y_pos, mydata)
plt.xlabel('AAPL:US - 2017-01-03 ')
plt.title('Historical Markets')
plt.grid(True)
plt.show()


