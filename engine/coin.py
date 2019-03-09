import twder


def now_currency(coin):
	if coin == '美金':
		coin = 'USD'
	elif coin == '日币':
		coin = 'JPY'
	currency = twder.now(coin)[4]
	return currency
