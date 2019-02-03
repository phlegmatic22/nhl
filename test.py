
from requests import get
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
import datetime

def simple_get(url):
    """
    Attempts to get the content at `url` by making an HTTP GET request.
    If the content-type of response is some kind of HTML/XML, return the
    text content, otherwise return None.
    """
    try:
        with closing(get(url, stream=True)) as resp:
            if is_good_response(resp):
                return resp.content
            else:
                return None

    except RequestException as e:
        log_error('Error during requests to {0} : {1}'.format(url, str(e)))
        return None


def is_good_response(resp):
    """
    Returns True if the response seems to be HTML, False otherwise.
    """
    content_type = resp.headers['Content-Type'].lower()
    return (resp.status_code == 200 
            and content_type is not None 
            and content_type.find('html') > -1)


def log_error(e):
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    print(e)

def return_month(mo):
    mo_mo = mo.split(' ')[0]
    mo_day = int(mo.split(' ')[1])
    """
    It is always a good idea to log errors. 
    This function just prints them, but you can
    make it do anything.
    """
    if mo_mo == 'JAN':
        return datetime.date(datetime.date.today().year,1,mo_day)
    if mo_mo =='FEB':
        return datetime.date(datetime.date.today().year,2,mo_day)
    if mo_mo =='MAR':
        return datetime.date(datetime.date.today().year,3,mo_day)
    if mo_mo =='APR':
        return datetime.date(datetime.date.today().year,4,mo_day)
    if mo_mo =='MAY':
        return datetime.date(datetime.date.today().year,5,mo_day)
    if mo_mo =='JUN':
        return datetime.date(datetime.date.today().year,6,mo_day)
    if mo_mo =='JUL':
        return datetime.date(datetime.date.today().year,7,mo_day)
    if mo_mo =='AUG':
        return datetime.date(datetime.date.today().year,8,mo_day)
    if mo_mo =='SEP':
        return datetime.date(datetime.date.today().year,9,mo_day)
    if mo_mo =='OCT':
        return datetime.date(datetime.date.today().year,10,mo_day)
    if mo_mo =='NOV':
        return datetime.date(datetime.date.today().year,11,mo_day)
    if mo_mo =='DEC':
        return datetime.date(datetime.date.today().year,12,mo_day)

    return -1


raw_html = simple_get('https://www.nhl.com/player/sebastian-aho-8478427')
html = BeautifulSoup(raw_html, 'html.parser')
for i, td in enumerate(html.select('tbody')):
        #for x in td.contents :
        if i == 4:
            print(td.contents[1].contents)
            sb_pvm = td.contents[1].contents[3].contents[1].text
            sb_maalit = td.contents[1].contents[5].contents[1].text
            sb_syotot = td.contents[1].contents[7].contents[1].text

raw_html = simple_get('https://www.nhl.com/player/patrik-laine-8479339')
html = BeautifulSoup(raw_html, 'html.parser')

for i, td in enumerate(html.select('tbody')):
        #for x in td.contents :
        if i == 4:
            print(td.contents[1].contents)
            pl_pvm = td.contents[1].contents[3].contents[1].text
            pl_maalit = td.contents[1].contents[5].contents[1].text
            pl_syotot = td.contents[1].contents[7].contents[1].text

raw_html = simple_get('https://www.nhl.com/player/mikko-rantanen-8478420')
html = BeautifulSoup(raw_html, 'html.parser')

for i, td in enumerate(html.select('tbody')):
        #for x in td.contents :
        if i == 4:
            print(td.contents[1].contents)
            mr_pvm = td.contents[1].contents[3].contents[1].text
            mr_maalit = td.contents[1].contents[5].contents[1].text
            mr_syotot = td.contents[1].contents[7].contents[1].text

sb_pvm_d = return_month(pl_pvm)
pl_pvm_d = return_month(pl_pvm)
mr_pvm_d = return_month(mr_pvm)
pvm_today = datetime.date.today()
sb_log =''
pl_log =''
mr_log =''
logs = ['NHL ... ']
if sb_pvm_d != pvm_today:
    sb_log = 'SB:' + sb_maalit + '+' + sb_syotot + ' '
    logs.append(sb_log)
if pl_pvm_d != pvm_today:
    pl_log = 'PL:' + pl_maalit + '+' + pl_syotot + ' '
    logs.append(pl_log)
if mr_pvm_d != pvm_today:
    mr_log = 'MR:' + mr_maalit + '+' + mr_syotot + ' '
    logs.append(mr_log)

print(logs)

