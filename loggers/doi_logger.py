# -*- coding: utf-8 -*-
from logger_base import *
from bs4 import BeautifulSoup
import requests
import threading

'''
Support:
        ACS
        Elsevier
        Wiley
        Springer
        Nature
        RSC
'''


class DoiLogger(Logger):
    def __init__(self, need_data_file=False):
        url = 'http://dx.doi.org/'
        Logger.__init__(self, url=url, need_data_file=False)
        self.log_file = 'doi.log'

        self.database_dict = {

            'ACS'      : self.get_ACS_pdf_url,
            'Elsevier' : self.get_Elsevier_pdf_url,
            'Wiley'    : self.get_Wiley_pdf_url,
            'Springer' : self.get_Springer_pdf_url,
            'Nature'   : self.get_Nature_pdf_url,
            'RSC'      : self.get_RSC_pdf_url,

        }

    #Elsevier
    @staticmethod
    def get_Elsevier_pdf_url(page_content):
        #create BS object
        soup = BeautifulSoup(page_content)
        #get pdf link
        url_list = soup.find_all(id='pdfLink')
        if not url_list:
            return
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
        if not url_list:
            return
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
        if not url_list:
            return
        pdf_url = url_list[0].attrs['src']

        return pdf_url

    #Springer
    @staticmethod
    def get_Springer_pdf_url(page_content):
        pdf_url_head = 'http://link.springer.com'
        #create BS object
        soup = BeautifulSoup(page_content)
        #get pdf link
        url_list = soup.find_all(
            'a', id='action-bar-download-article-pdf-link')
        if not url_list:
            return
        partial_pdf_url = url_list[0].attrs['href']
        quasi_url = pdf_url_head + partial_pdf_url

        return quasi_url  # please use download_pdf_by_urllib()

    #Nature
    @staticmethod
    def get_Nature_pdf_url(page_content):
        home_url = 'http://www.nature.com'
        #create BS object
        soup = BeautifulSoup(page_content)
        #get pdf link
        url_list = soup.find_all('a', id='download-pdf')
        if not url_list:
            return
        partial_pdf_url = url_list[0].attrs['href']
        pdf_url = home_url + partial_pdf_url

        return pdf_url

    #RSC
    @staticmethod
    def get_RSC_pdf_url(page_content):
        home_url = 'http://pubs.rsc.org'
        #create BS object
        soup = BeautifulSoup(page_content)
        #get pdf link
        url_list = soup.find_all(
            'a', class_='gray_bg_normal_txt', title='PDF')
        if not url_list:
            return
        partial_pdf_url = url_list[0].attrs['href']
        pdf_url = home_url + partial_pdf_url

        return pdf_url

    @staticmethod
    def download_pdf_by_requests(pdf_url, target_path, save_name):
        req = requests.get(pdf_url)
        content = req.content

        fullname = target_path + save_name
        with open(fullname, 'wb') as f:
            f.write(content)

        return

    @staticmethod
    def download_pdf_by_urllib(pdf_url, target_path, save_name):
        '''
        Use this method to download pdf from quasi_url
        returned from get_Springer_pdf_url.
        '''
        response = urllib2.urlopen(pdf_url, timeout=100)
        content = response.read()

        fullname = target_path + save_name
        with open(fullname, 'wb') as f:
            f.write(content)

        return
