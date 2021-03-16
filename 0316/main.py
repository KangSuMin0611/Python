import requests
from bs4 import BeautifulSoup as bs

MEMBER_DATA = {
    'merberID' : 'wkdghtn1218',
    'memberPassword' : 'wkdghtn7897'
}

with requests.Session() as s: 
    request = s.post('http://dowellcomputer.com/member/memberLoginAction.jsp', 
                     data = MEMBER_DATA)
    
print(request.text)