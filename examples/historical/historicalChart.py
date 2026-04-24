import matplotlib.pyplot as plt
import numpy as np
import tradingeconomics as te

#Please subscribe to a plan at https://tradingeconomics.com/api/pricing.aspx to get an API key.
te.login('')


#plot a simple chart
mydata = te.getHistoricalData(country = 'United states', indicator = 'Imports')

plt.title("United states - Imports")
plt.grid(True)
plt.ylabel("Indicator - Imports")
plt.xlabel("Historical")

plt.plot(mydata)
plt.show()
