#!/usr/bin/env python3
import socket
import sys

class WhoisEntry:
    def __init__(self):
        self.ip = ""
        self.origin_as = 0
        self.prefix = ""
        self.as_path = ""
        self.as_org_name = ""
        self.org_name = ""
        self.net_name = ""
        self.cache_date = 0
        self.lat = 0.0
        self.lon = 0.0
        self.city = ""
        self.region = ""
        self.country = ""
        self.country_code = ""

    def __str__(self):
        info = "IP: " + self.ip + "\n" \
               + "Origin-AS: " + str(self.origin_as) + "\n" \
               + "Prefix: " + self.prefix + "\n" \
               + "AS-Path: " + self.as_path + "\n" \
               + "AS-Org-Name: " + self.as_org_name + "\n" \
               + "Org-Name: " + self.org_name + "\n" \
               + "Net-Name: " + self.net_name + "\n" \
               + "Cache-Date: " + str(self.cache_date) + "\n" \
               + "Latitude: " + str(self.lat) + "\n" \
               + "Longitude: " + str(self.lon) + "\n" \
               + "City: " + self.city + "\n" \
               + "Region: " + self.region + "\n" \
               + "Country: " + self.country + "\n" \
               + "Country-Code: " + self.country_code

        return info


class PyWhois:
    def __init__(self, **kwargs):
        self.server = "whois.pwhois.org"
        if 'server' in kwargs.keys():
            self.server = kwargs['server']

    def lookup(self, *args):
        targets = []
        s = socket.socket()
        s.connect((self.server, 43))
        if len(args) == 1:
            s.send(bytes(args[0], 'ascii') + b"\r\n")
            resp = s.recv(512)
            targets.append(self.parse_response(resp))
        elif len(args) > 1:
            s.send(b"begin\r\n")
            for target in args:
                s.send(bytes(target, 'ascii') + b"\r\n")
                resp = s.recv(512)
                targets.append(self.parse_response(resp))
            s.send(b"end\r\n")
        s.close()
        return targets

    def parse_response(self, item):
        p = WhoisEntry()
        for line in item.decode('ascii').splitlines():
            fields = line.split(": ")
            if fields[0] == "IP":
                p.ip = fields[1]
            elif fields[0] == "Origin-AS":
                p.origin_as = fields[1]
            elif fields[0] == "Prefix":
                p.prefix = fields[1]
            elif fields[0] == "AS-Path":
                p.as_path = fields[1]
            elif fields[0] == "AS-Org-Name":
                p.as_org_name = fields[1]
            elif fields[0] == "Org-Name":
                p.org_name = fields[1]
            elif fields[0] == "Net-Name":
                p.net_name = fields[1]
            elif fields[0] == "Cache-Data":
                p.cache_date = int(fields[1])
            elif fields[0] == "Latitude":
                p.lat = float(fields[1])
            elif fields[0] == "Longitude":
                p.lon = float(fields[1])
            elif fields[0] == "City":
                p.city = fields[1]
            elif fields[0] == "Region":
                p.region = fields[1]
            elif fields[0] == "Country":
                p.country = fields[1]
            elif fields[0] == "Country-Code":
                p.country_code = fields[1]
        return p


if __name__ == '__main__':
    p = PyWhois()
    ans = p.lookup("4.2.2.1")
    for a in ans:
        print(a)
    ans = p.lookup("4.2.2.1", "8.8.8.8")
    for a in ans:
        print(a)