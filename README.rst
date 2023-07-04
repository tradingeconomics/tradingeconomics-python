=====================
Trading Economics API
=====================

The Trading Economics Python package provides direct access to over 300,000 economic indicators, exchange rates, stock market indexes, government bond yields, and commodity prices. This package offers various request methods to query the Trading Economics databases and supports exporting data in XML, CSV, or JSON format. The API can be used to feed custom-developed applications, public websites, or off-the-shelf software.


Installation
----------------------------------------

You can install the package using pip:

    - pip install tradingeconomics


Authentication
----------------------------------------

To use the Trading Economics API, you need to authenticate by providing your API key and secret:

    - import tradingeconomics as te
    - te.login('key:secret')


Sample Usage
----------------------------------------

Here are some examples of how to use the Trading Economics Python package:

    - te.getCalendarData()
    - te.getIndicatorData(country=['mexico', 'sweden'], output_type='df')
    - te.getMarketsData(marketsField='commodities')
    - te.getMarketsBySymbol(symbols='aapl:us')
    - te.getFinancialsData(symbol='aapl:us', output_type='df')


GitHub Examples
----------------------------------------

You can find additional examples and usage instructions in the GitHub repository:
 - https://github.com/tradingeconomics/tradingeconomics-python/tree/main/examples


Documentation
----------------------------------------

For detailed documentation and API reference, please visit the Trading Economics API documentation:
 - https://docs.tradingeconomics.com