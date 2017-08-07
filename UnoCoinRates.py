import datetime
import time
import urllib2
import xml.etree.ElementTree as ET

def GetBitCoinRates():    
	headers = { 'User-Agent' : 'Mozilla/5.0' }
	req = urllib2.Request('https://www.unocoin.com/', None, headers);

	htmlResponse = urllib2.urlopen(req).read();
	curTime = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%y %H:%M:%S');
	#values = htmlResponse.xpath('//*[@id="menubarbuyprice"]')[0].extract()

	BuyValue = htmlResponse[htmlResponse.find('menubarbuyprice')+17:htmlResponse.find('menubarbuyprice')+24];
	SellValue =  htmlResponse[htmlResponse.find('menubarsellprice')+18:htmlResponse.find('menubarsellprice')+25];

	BuyValue = BuyValue.replace(',','')
	SellValue = SellValue.replace(',','')

	#print curTime
	#print "buy value %s" %(BuyValue)
	#print "sell avlue is %s" %(SellValue)
	#print float(SellValue) * 0.00521715
	
	return [curTime,BuyValue,SellValue]

