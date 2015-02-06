from ecust_logger import *
url = 'http://172.20.13.100/cgi-bin/srun_portal'
ecust_logger = EcustCampusLogger(url)
if os.path.exists('./ecust.log'):
	os.remove('./ecust.log')
#while True:
#	ecust_logger.login_campus()
#	time.sleep(15)
ecust_logger.login_campus()