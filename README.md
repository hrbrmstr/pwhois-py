**PyPWhois**

PyPWhois is a Python3 client library for interacting with [Prefix Whois(pwhois)](https://www.pwhois.org). It enables the calling application
to issue a one-off or bulk lookup of information related to an IP address.

**Usage**
```python
>>> from pypwhois import *
>>> p = PyWhois()
>>> print(p.lookup('2.2.2.2'))
IP: 2.2.2.2
Origin-AS: 3215
Prefix: 2.2.0.0/16
AS-Path: 24441 3491 5511 3215
AS-Org-Name: AS3215
Org-Name: FR-TELECOM-20100712
Net-Name: FR-TELECOM-20100712
Cache-Date: 0
Latitude: 22.28552
Longitude: 114.15769
City: Hong Kong
Region: Hong Kong
Country: Hong Kong
Country-Code: HK
>>>
```

The ``lookup`` method takes a variable length of arguments. If on a single target is given, then a single WhoisEntry object will be returned. If multiple IPs are queried,
then a list of WhoisEntry objects will be returned:

```python
>>> for elm in p.lookup('8.8.8.8', '4.2.2.1'):
...     print(elm)
...
IP: 8.8.8.8
Origin-AS: 15169
Prefix: 8.8.8.0/24
AS-Path: 24441 15169
AS-Org-Name: Google LLC
Org-Name: Google LLC
Net-Name: LVLT-GOGL-8-8-8
Cache-Date: 0
Latitude: 37.405992
Longitude: -122.078515
City: Mountain View
Region: California
Country: United States
Country-Code: US
IP: 4.2.2.1
Origin-AS: 3356
Prefix: 4.0.0.0/9
AS-Path: 24441 1299 3356
AS-Org-Name: Level 3 Parent, LLC
Org-Name: Level 3 Parent, LLC
Net-Name: LVLT-ORG-4-8
Cache-Date: 0
Latitude: 32.78306
Longitude: -96.80667
City: Dallas
Region: Texas
Country: United States
Country-Code: US
```