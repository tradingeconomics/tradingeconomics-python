
# Trading Economics - Python

[![PyPI version](https://img.shields.io/pypi/v/tradingeconomics.svg)](https://pypi.org/project/tradingeconomics/)

The Trading Economics Application Python package provides direct access to millions of time series with economic data, financial markets quotes, commodity prices, crypto currencies data and much more. It also allows you to query Trading Economics  real-time economic calendar and to subscribe to updates. 

#

## Installation


```bash
pip install tradingeconomics
```

Install the latest version directly from GitHub 

```bash
git clone https://github.com/tradingeconomics/tradingeconomics-python.git
cd tradingeconomics-python
python setup.py install
```

#

## Authentication - the secure way

Protect your credentials! Please set your keys as environment variables before you launch your application. This lets you share your code without disclosing your credentials.

```bash
# windows command line
set apikey='guest:guest'
# linux / mac bash
export apikey='guest:guest'
```

```python
# python
import tradingeconomics as te
te.login()
```

## Authentication - the easy way

```python
import tradingeconomics as te
te.login('guest:guest')
```
Please replace guest:guest with your API key or we will be returning sample data.

#

## Sample Usage

```python
te.getCalendarData()
te.getIndicatorData(country=['mexico', 'sweden'], output_type='df')
te.getMarketsData(marketsField = 'commodities')
te.getMarketsBySymbol(symbols='aapl:us')
te.getFinancialsData(symbol = 'aapl:us', output_type = 'df')
```

## More examples

https://github.com/tradingeconomics/tradingeconomics-python/tree/main/examples

#

## Docker

Try our python interface in a container without installing anything

```bash
docker run -it --name te-python tradingeconomics-python:latest
```
#

## Documentation

https://docs.tradingeconomics.com


#

## Learn More

https://tradingeconomics.com/analytics/api.aspx

