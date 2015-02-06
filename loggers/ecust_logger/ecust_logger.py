from logger_base import *
class EcustCampusLogger(Logger):
	def __init__(self, url):
		Logger.__init__(self, url)
		#self.add_form_data(self.load_form_data())
		self.log_file = './ecust.log'
		self._log_str = {
			'update_form_data'  : ('there has been \'${form_name} = ${old_value}\','
								  'update to \'${form_name} = ${new_value}\''),
			'connect2none'      : ('Cannot connect to internet.\nScript stopping...\n'
								   'Please check your internet connection '
								   'and run it again.'),
			'connect2all'       : 'status : connected',
			'no_log2campus'     : 'Campus connection lost, relogging in...',
			'connect_done'      : 'done.',
			'log_info'			: 'Warning:${log_info}'
			}

	def chk_connection(self):
		#check connection to network
		fnull = open(os.devnull, 'w')
		connect2campus = not subprocess.call('ping 172.20.13.100', shell = True, 
										stdout = fnull, stderr = fnull)
		connect2baidu = not subprocess.call('ping www.baidu.com', shell = True, 
										stdout = fnull, stderr = fnull)
		connect2weibo = not subprocess.call('ping www.weibo.com', shell = True, 
										stdout = fnull, stderr = fnull)
		if not (connect2campus or connect2baidu or connect2weibo):
			#print "Can not connected to Internet.\nPlease check your connection."
			return 'connect2none'
		if not (connect2baidu or connect2weibo) and connect2campus:
			return 'connect2campus'
		if connect2campus and connect2baidu and connect2weibo:
			baidu_title = self.get_page_title('http://www.baidu.com/')
			weibo_title = self.get_page_title('http://www.weibo.com/')
			ecust_title = self.get_page_title('http://172.20.13.100/')
			if baidu_title == weibo_title == ecust_title: #can not connected to CN
				return 'connect2campus'
			else:
				return 'connect2all'
		if (connect2baidu or connect2weibo) and connect2campus:
			return 'connect2all'

	def login_campus(self):
		counter = 0
		while True:
			try:
				chk_result = self.chk_connection()
			except:
				continue
			if chk_result == 'connect2all':
	#			print "status:connected"
				if counter % 100 == 0:
					self.log('connect2all')
				else:
					pass
			if chk_result == 'connect2none':
	#			print "Cannot connect to internet.\nScript stopping..."
	#			print "Please check your internet connection and run it again."
				self.log('connect2none')
			if chk_result == 'connect2campus':  #cannot connet to campus network
	#			print "Connection lost, relogging in..."
				self.log('no_log2campus')
				login_info = self.do_login()
				if login_info:
					if 'action=login_ok' in login_info:
	#					print "Done."
						self.log('connect_done')
					else:
	#					print login_info
						self.log('log_info',log_info=login_info)
			counter += 1
			time.sleep(5)