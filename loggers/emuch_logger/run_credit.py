from emuch_logger import *
import time

url = 'http://emuch.net/bbs/logging.php?action=login'
emuch_logger = EmuchLogger(url)
def emuch(emuch_logger):
	url = emuch_logger.url_login
	#chk internet connection
	try:
		resp = urllib2.urlopen(url)
	except:
		return 'no_internet'

	title_1 = emuch_logger.get_page_title(url)
	try:
	    title_2 = emuch_logger.get_page_title('http://www.weibo.com/')
	except:
		title_2 = None
	try:
	    title_3 = emuch_logger.get_page_title('http://www.baidu.com/')
	except:
		title_3 = None
		
	if title_1 == title_2 or title_1 == title_3:
		return 'need_login'
	else:
		cookies = emuch_logger.log_in()
		if cookies:
		    #get credit
		    response = emuch_logger.get_credit()
		    #check if there is a formhash tag
		    if 'have_got' in response:
			    print 'You\'ve got today\'s coin~'
			    print 'Current credit number : %s' % str(response[1])
			    return 
		    else:
			    credit_num = emuch_logger.get_credit_number(response)
			    print "Today's credit -> get!"
			    print 'Current credit number : %s' % str(credit_num)
			    return
		else:
			print "Failed to set cookies."

signal = emuch(emuch_logger)
#if signal == 'no_internet':
#	print 'Failed, check your internet connection'
#if signal == 'need_login':
#	print 'Please log in your wlan account'
while signal == 'no_internet' or signal == 'need_login':
	if signal == 'no_internet':
		print 'Failed, please connect to internet.'
		print 'Dont\' close the window!\n'
	if signal == 'need_login':
		print 'Failed, please log in your wlan account'
		print 'Dont\' close the window!\n'
	time.sleep(5)
	signal = emuch(emuch_logger)


raw_input('Press Enter to exit...')