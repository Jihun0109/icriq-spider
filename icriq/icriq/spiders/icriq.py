# -*- coding: utf-8 -*-
from scrapy import Spider, Request
from urlparse import urlparse
from scrapy.utils.response import open_in_browser
from collections import OrderedDict
from shutil import copyfile

import json, re, sys, time, os, requests, urllib


class MySpider(Spider):

    name = "icriq"   
    start_urls = [
                    'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=IXJV3IH4TZ',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=27PSOF5085',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=QVNUBQ8K4E',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=MLDZEJB4HI',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=PABW22CZPU',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=EL98ENE2XH',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=VMYUJ3BL9G',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=PZQNW1FTBQ',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=ONA8ICC8CH',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=E35KLUVV9H',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=TXFMHQCS57',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=GWS5CIIR9M',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=KLLKOWHWLU',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=B4OPMKD61M',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=R1PZCBZSCW',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=IKF1MFH12E',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=5XPNFPPLQR',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=CKLZWI855I',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=RAUP5P67GA',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=L4Y6DJI0KX',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=O4OS5Y2NIP',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=TRMISLMXM9',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=RD19FAVQLH',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=D8IEBPI74S',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=LA397YU7NY',

'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=LFRLSCCCY8',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=6UPNXDTQWO',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=WV7PRGYAJL',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=N5K7ZL10I2',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=6M82T1WTB3',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=XT68Z1HB9J',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=9UDRHL131Z',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=2LMD0404WR',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=KH3XUG1MAG',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=DKTKELXRGA',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=BLG9Z481OL',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=NX1243NKBX',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=SJVEUR5KZ7',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=ZB05VTE8KB',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=OMXEQYVLDJ',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=YGYV8QV4M2',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=E9ZQ8D9EOO',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=GOJEMW2ER1',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=MWSKFAW6E6',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=WDADOJM06D',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=HSBN7RK12L',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=GGA1597EQ4',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=9P5TNEGXPD',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=625YJNRTU4',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=PMHESXIO4I',

'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=PNJIRETENU',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=SDVOTLGVIH',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=AOM6HCGNWK',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=02NWGW1KQ7',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=KSYXD166VW',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=ILQ2IQ5T8A',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=B1BTTZFUSK',
'http://www.icriq.com/pls/owa_rib/ribwaff1.afficher_profil?p_id_req=54868267&p_cle=4BHDBKZEDF',

                    ]

    def parse(self, response):
        
        item = OrderedDict()

        headers = response.xpath('//*[@colspan="2"]//text()').extract()

        item['Name'] = response.xpath('//*[@colspan="2"]//b/text()').extract_first()
        item['Address'] = headers[1]
        item['Phone'] = []
        item['Fax'] = []
        item['Region'] = ""
        
        for p in headers[2].split(","):
            if "Fax" in p:
                item['Fax'].append(p.split(":")[-1].strip())
            else:
                item['Phone'].append(p.strip())

        for i, h in enumerate(headers[2:]):
            if "Region:" in h:
                item['Region'] = h.split(":")[-1].strip()
            
        item['NEQ'] = ''.join(response.xpath('//*[text()="NEQ"]/parent::td[1]/following-sibling::td[text()]/text()').extract()).strip()
        item['Established'] = ''.join(response.xpath('//*[text()="Established"]/parent::td[1]/following-sibling::td[text()]/text()').extract()).strip()
        item['Business category'] = ''.join(response.xpath('//*[text()="Business category"]/parent::td[1]/following-sibling::td[text()]/text()').extract()).strip()
        yield item