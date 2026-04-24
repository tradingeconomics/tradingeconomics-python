import tradingeconomics as te
import json

te.login('')


def on_message(ws, message):
    print(json.loads(message))


te.subscribe('EURUSD:CUR')
te.run(on_message)
