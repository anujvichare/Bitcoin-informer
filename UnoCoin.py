import datetime
import time
import urllib2
import xml.etree.ElementTree as ET
import ctypes  # An included library with Python install.
#from plyer import notification
#import balloonNotification

upperbound = ("00","00")
lowerbound = ("00","00")
displayStr = ""
flag = True


while 1:

   
	headers = { 'User-Agent' : 'Mozilla/5.0' };
	req = urllib2.Request('https://www.unocoin.com/', None, headers);
	flag = True;
	fileFlag = True;
	try:
		htmlResponse = urllib2.urlopen(req).read();
		curTime = datetime.datetime.fromtimestamp(time.time()).strftime('%d-%m-%y %H:%M:%S');
		#values = htmlResponse.xpath('//*[@id="menubarbuyprice"]')[0].extract()
	except urllib2.URLError as err:
		print "No Network..."
		flag = False
	
	if(flag == True):	
		BuyValue = htmlResponse[htmlResponse.find('menubarbuyprice')+17:htmlResponse.find('menubarbuyprice')+24];
		SellValue =  htmlResponse[htmlResponse.find('menubarsellprice')+18:htmlResponse.find('menubarsellprice')+25];
	
		BuyValue = BuyValue.replace(',','')
		SellValue = SellValue.replace(',','')
		
		if(upperbound[0] == "00" and lowerbound[0]=="00"):
			
			try:
				objFile = open('D:\ANUJ\Python\LastDayValues.txt','r');
			except IOError as err:
				fileFlag = False;
			
				
			if(fileFlag == True):
				
				try:
					ValuesFromFile = objFile.read(40);
					tempTuple = tuple(item for item in ValuesFromFile.split(';') if item.strip())
					lastUpperBound = tuple(item for item in tempTuple[0].split(',') if item.strip())
					lastLowerBound = tuple(item for item in tempTuple[1].split(',') if item.strip())
					print lastUpperBound
					print lastLowerBound
					objFile.close();
			
					if(int(lastUpperBound[0]) < int(BuyValue)):
						displayStr =  "buy value: "+ BuyValue + "\n sell value is " + SellValue +"\n  at: "+ curTime+ "\n\n Raising than yesterday";
						ctypes.windll.user32.MessageBoxA(0, displayStr, "UnoCoin", 0)
					elif(int(lastLowerBound[0])> int(BuyValue)):
						displayStr =  "buy value: "+ BuyValue + "\n sell value is " + SellValue +"\n  at: "+ curTime+ "\n\n Reducing than yesterday";
						ctypes.windll.user32.MessageBoxA(0, displayStr, "UnoCoin", 0)
					else: 
						displayStr =  "buy value: "+ BuyValue + "\n sell value is " + SellValue +"\n  at: "+ curTime+ "\n\n In Range with yesterday";
						ctypes.windll.user32.MessageBoxA(0, displayStr, "UnoCoin", 0)
						
				except IndexError as err:
					print "error while reading values.."
				
 			upperbound = (BuyValue,SellValue)
			lowerbound = (BuyValue,SellValue)
		
		
		elif(int(upperbound[1])< int(SellValue)):
			
			upperbound = (BuyValue,SellValue)
			displayStr =  "buy value: "+ BuyValue + "\n sell value is " + SellValue +"\n  at: "+ curTime+ "\n\n Market is Raising"
			ctypes.windll.user32.MessageBoxA(0, displayStr, "UnoCoin", 0)
			
			objFile = open('D:\ANUJ\Python\LastDayValues.txt','w+')
			objFile.write(upperbound[0] + ',' + upperbound[1]);
			objFile.write(';');
			objFile.write(lowerbound[0] + ',' + lowerbound[1]);
			objFile.close();
			
		elif(int(lowerbound[1])> int(SellValue)):	
			
			lowerbound = (BuyValue,SellValue)
			displayStr =  "buy value: "+ BuyValue + "\n sell value is " + SellValue + "\n at: "+ curTime + "\n\n Market is Reducing"
			ctypes.windll.user32.MessageBoxA(0, displayStr, "UnoCoin", 0)
			
			objFile = open('D:\ANUJ\Python\LastDayValues.txt','w+')
			objFile.write(upperbound[0] + ',' + upperbound[1]);
			objFile.write(';');
			objFile.write(lowerbound[0] + ',' + lowerbound[1]);
			objFile.close();
		
		print '+--------'+curTime+'---------+'	
		print upperbound 
		print lowerbound 	
		print '--['+ BuyValue+", "+SellValue+ ']--'
		print '+----------------------------------+'
		
		#balloon_tip("UnoCoin","temprary message")
	time.sleep(120);
	
	
