# -*- coding: utf-8 -*-
from logger_base import *
from bs4 import BeautifulSoup
import requests


class DoiLogger(Logger):
    def __init__(self, need_data_file=False):
        url = 'http://dx.doi.org/'
        Logger.__init__(self, url=url, need_data_file=False)
        self.log_file = 'doi.log'

    #Elsevier
    @staticmethod
    def get_ScienceDirect_pdf_url(page_content):
        #create BS object
        soup = BeautifulSoup(page_content)
        #get pdf link
        url_list = soup.find_all(id='pdfLink')
        pdf_url = url_list[0].attrs['href']

        return pdf_url

    #ACS
    @staticmethod
    def get_ACS_pdf_url(page_content, doi_number):
        home_url = 'http://pubs.acs.org'
        #create BS object
        soup = BeautifulSoup(page_content)
        #get pdf link
        href_pattern = re.compile(str(doi_number))
        url_list = soup.find_all('a', text='PDF', href=href_pattern)
        partial_pdf_url = url_list[0].attrs['href']
        pdf_url = home_url + partial_pdf_url

        return pdf_url

    #Wiley
    @staticmethod
    def get_Wiley_pdf_url(doi_number):
        quasi_url = 'http://onlinelibrary.wiley.com/doi/' +\
            str(doi_number) + '/pdf'
        page_content = urllib.urlopen(quasi_url)
        #create BS object
        soup = BeautifulSoup(page_content)
        #get pdf link
        url_list = soup.find_all('iframe', id='pdfDocument')
        pdf_url = url_list[0].attrs['src']

        return pdf_url

    @staticmethod
    def download_pdf(pdf_url, target_path, save_name):
        req = requests.get(pdf_url)
        content = req.content

        fullname = target_path + save_name
        with open(fullname, 'wb') as f:
            f.write(content)

        return

    def download_doi(self, doi_number, save_name, target_path='./'):
        #get journal official page content
        print "Getting page content..."
        form_data_dict = {'hdl': str(doi_number)}
        page_content = self.send_post(self.url_login, form_data_dict)
        if page_content:
            print "Ok."
        else:
            raise ValueError('No Content.')
        #get pdf link
        print "Extract file url..."
        pdf_url = self.get_pdf_url(page_content)
        print 'url: ' + str(pdf_url)
        print 'Ok.'
        #download pdf
        print "Downloading..."
        self.download_pdf(pdf_url, target_path, save_name)
        print "Download complete!"

        return
