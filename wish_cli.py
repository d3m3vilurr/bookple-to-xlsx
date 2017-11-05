# -*- coding: utf8 -*-
import requests
import time
from datetime import datetime, timedelta
import lxml.html

ALADIN = 'https://www.aladin.co.kr'
ALADIN_LOGIN = ALADIN + '/login/wlogin_popup.aspx'
BOOKPLE = 'https://bookple.aladin.co.kr'
BOOKPLE_UPDATE_ITEM = BOOKPLE + '/api/reading.aspx'

def login_aladin(config):
    session = requests.Session()
    data = dict(Email=config['bookple']['id'],
                Password=config['bookple']['password'],
                Action=1,
                ReturnUrl=None,
                ReturnUrl_pop=None,
                SecureLogin=False,
                snsUserId=0,
                snsType=0,
                snsAppId=1)
    res = session.post(ALADIN_LOGIN, data=data)
    return session

if __name__ == '__main__':
    import yaml

    config = yaml.load(file('config.yml'))
    aladin_session = login_aladin(config)

    while True:
        book_id = raw_input('add wish> ')

        print book_id
        timestamp = str(int(round(time.time() * 1000)))
        params = dict(callback='jsonp' + timestamp,
                      method='UpdateReadStatus',
                      itemid=book_id,
                      output='jsonp',
                      ReadYear='1',
                      ReadMonth='1',
                      ReadStatus='4')
        #print params
        res = aladin_session.get(BOOKPLE_UPDATE_ITEM, params=params, verify=False)
        print res.text
