from emuch_logger import *
import time

url = 'http://emuch.net/bbs/logging.php?action=login'
emuch_logger = EmuchLogger(url)
emuch_logger.log_in()
#parse in urls
f = open('download_list.txt', 'rU')
url_list = f.readlines()
f.close()

#check time
current_time = int(time.ctime().split()[3].split(':')[0])
while 7 <= current_time <= 23:
	print 'Current_time : %s' % (time.ctime().split()[3])
	print "Waiting for 12 o'clock coming...(-_-zZ"
	print "Don't close the window!\n"
	time.sleep(600)
	current_time = int(time.ctime().split()[3].split(':')[0])
print "(>o<)Oh, it's time to make a move!\n"
#loop to download files in each url
i = 0
for download_url in url_list:
	i += 1
	print "url[%d] -> %s\n" % (i, download_url)
	try:
		download_url = download_url.strip('\n')
		emuch_logger.download_from_1st_url(download_url)
	except:
		pass
	finally:
		time.sleep(60)
raw_input('Press Enter to exit...')