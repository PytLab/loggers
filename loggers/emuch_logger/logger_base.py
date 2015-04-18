# -*- coding: utf-8 -*-
import urllib, urllib2, cookielib
import subprocess
import time
import os
from string import Template
import re


class Logger(object):
    """
    This is a parent class to be inherited by other logger class.
    """
    def __init__(self, url):
    	self.form_data_dict = {}
    	self.url_login = url 
    	self.add_form_data(self.load_form_data())
    	self._log_format = '%-70s%-20s\n'
    	self._log_str = {
            'match_file_fail' : 'No file link in \'${url}\'',
            'suffix_unmatch:' : ('Warning: unmatched suffix : \'${suffix_1}\' and '
                                 '\'${suffix_2}\',force to change to \'${suffix_2}\''),
            'illegal_path'    : 'illegal_path : ${illegal_path}',
            'download_fail'   : '${filename} download overtime',
            'download_times'  : '${filename} download time:${times} ',
            'download_time'   : '${filename} download time used : ${time_pass}s '
        }
        self.log_file = ''

    def log(self, event, **kwargs):
        "append log info into log file"
        file_obj = open(self.log_file, 'a')
        #append new log infomation
        message_template = Template(self._log_str[event])
        message = message_template.substitute(kwargs)
        append_ctnt = self._log_format % (message, '['+time.ctime()+']')
        file_obj.write(append_ctnt)
        file_obj.close()

    def get_page_title(self, url):
        page_ctnt = urllib2.urlopen(url).read()
        match = re.search(r'(<title>)(.*)(</title>)', page_ctnt)
        return match.group(2)  # title

    def load_form_data(self, filename='formdata.txt'):
        "parse in form data from form file"
        form_data_dict = {}
        file_obj = open(filename, 'rU')
        for line_str in file_obj:
            name, value = line_str.split('=')
            form_data_dict[name.strip()] = value.strip()
        file_obj.close()
        return form_data_dict

    def add_form_data(self, form_data_dict):
        "update form data attr with log info appended"
        for tag_name in form_data_dict.keys():
            if tag_name in self.form_data_dict:
#               print "there has been '%s = %s', update to '%s = %s'" % \
#                   (tag_name, self.form_data_dict[tag_name],
#               tag_name, form_data_dict[tag_name])
                self.log('update_form_data', form_name=tag_name,
                         old_value=self.form_data_dict[tag_name],
                         new_value=form_data_dict[tag_name])
            else:
                self.form_data_dict[tag_name] = form_data_dict[tag_name]
        #return Ture

    def do_login(self):
    #set cookie
        cj = cookielib.CookieJar()
        url_login = self.url_login
        form_data = self.form_data_dict
        try:
            opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
            urllib2.install_opener(opener)
            req = urllib2.Request(url_login, urllib.urlencode(form_data))
            u = urllib2.urlopen(req)
            return u.read().decode('utf-8').encode('gbk')
        except:
            print "Ooops! Failed to log in !>_< there may be a problem."
            return

    @staticmethod
    def send_post(url, form_data_dict):
        "pass value by POST method, return response string"
        #url_login = self.url_login
        #form_data = self.form_data_dict
        req = urllib2.Request(url, urllib.urlencode(form_data_dict))
        #return response page content
        return urllib2.urlopen(req).read()

    def login_check(self):
        result = self.do_login()
        if result:
            print result

#	def extract_file_url(self, url):
#		"match file urls in page, return a list"
#		response = urllib2.urlopen(url).read()
#		regex = r'<a href="http://.+\..+" style="color:green;font-size:'+\
#				r'12px;font-weight:bold;" target="_blank">'
#		m = re.findall(regex, response)
#		if m:
#			return [i[9:-71] for i in m]
#		else:
##			raise ValueError('No '+file_type+' file is found')
#			self.log('match_file_fail', url=url)
#			return

    def download_file(self, file_url, target_path, save_name):
        "download file to path with custom name"
        #check consistency of url and file type
        url_suffix = file_url.rsplit('.')[-1]
        if '.' in save_name:
            file_suffix = save_name.rsplit('.')[-1]
            if file_suffix != url_suffix:
                save_name = save_name.rsplit('.')[0] + '.' +\
                    file_url.rsplit('.')[-1]
                #log
                self.log('suffix_unmatch', suffix_1=file_suffix,
                         suffix_2=url_suffix)
        else:
            #no suffix in file name
            save_name += url_suffix

        if not target_path.endswith('\\') and not target_path.endswith('/'):
            #judge windows path or *nix path
            if target_path.split('\\'):  # windows path
                target_path += '\\'
            elif target_path.split('/'):  # *nix path
                target_path += '/'
            else:
                self.log('illegal_path', illegal_path=target_path)

        file_fullname = target_path + save_name

        #begin downloading
        start = time.clock()
        retrieve = urllib.urlretrieve(file_url, file_fullname)
        end = time.clock()
        #downloading time
        pass_time = end - start
        #check file size
        file_size = os.path.getsize(file_fullname)

        down_max = 25
        i = 1
        #print 'loop->'
        while pass_time < 2.0 or file_size < 3000:
            if i > down_max:
                self.log('download_fail', filename=file_fullname)
                print "Overtime! download failed."
                break
            #print i
            time.sleep(60)
            start = time.clock()
            retrieve = urllib.urlretrieve(file_url, file_fullname)
            end = time.clock()
            pass_time = end - start
            file_size = os.path.getsize(file_fullname)
            i += 1
            #print 'loop->'
#		retrieve = urllib.urlretrieve(file_url, file_fullname)

        self.log('download_times', filename=file_fullname, times=i)
        self.log('download_time', filename=file_fullname, time_pass=pass_time)
        print "download %s -> stopped.\nTime used : %fs\n" % (save_name, pass_time)
