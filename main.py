#!/usr/bin/python

import time
import SendSms
import UnoCoinRates


lowerbound = [00,00]
upperbound = [00,00]
shortmessage = ""


while 1:
#	f = open('UnoCoin.log', 'w+')
	 
	values = UnoCoinRates.GetBitCoinRates()

	print values
	message = ' Buy Rate: ' + values[1] + '\n Sell Rate: '+ values[2] + '\n at : '+values[0]

	if (lowerbound == [00,00] and upperbound == [00,00]):
		lowerbound = values[1:2]
		upperbound = values[1:2]

	elif (long(lowerbound[0]) > long(values[1]) ):
	
		lowerbound = values[1:2]
		shortmessage = '\n\n Market is lowered '
		message = message + shortmessage
		SendSms.LoginAndSendSms('phone no','password','receivers no',message)
		print down

	elif (long(values[1]) > long(upperbound[0])):
	
		upperbound = values[1:2]
		shortmessage = '\n\n Market is raised '
		message = message + shortmessage
		SendSms.LoginAndSendSms('phone no','password','receivers no',message)
		print high

	shortmessage = ""
#	f.close()
	time.sleep(120)
