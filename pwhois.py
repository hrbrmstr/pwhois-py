#!/usr/bin/env python
#
# (C) 2017, W. Dean Freeman
#
# Python interface to Prefix Whois.  Will query public server if
# 0 is passed as ther server. Otherwise, pass string of hostname
# for your own server
#
# see https://www.pwhois.org for further details regarding Prefix Whois itself
#
import socket, sys

class PwhoisData:
	def __init__(self):
		ip 		= ""
		origin_as 	= 0
		prefix		= ""
		as_path		= ""
		as_org_name	= ""
		org_name	= ""
		net_name	= ""
		cache_date	= 0
		lat		= 0.0
		lon		= 0.0
		city		= ""
		region		= ""
		country		= ""
		country_code	= ""
	def __str__(self):
		info	= 	"IP: "			+ self.ip + "\n" \
			+	"Origin-AS: "		+ str(self.origin_as) + "\n" \
			+	"Prefix: "		+ self.prefix + "\n" \
			+	"AS-Path: "		+ self.as_path + "\n" \
			+	"AS-Org-Name: " 	+ self.as_org_name + "\n" \
			+	"Org-Name: "		+ self.org_name + "\n" \
			+	"Net-Name: "		+ self.net_name + "\n" \
			+	"Cache-Date: "		+ str(self.cache_date) + "\n" \
			+	"Latitude: "		+ str(self.lat) + "\n" \
			+	"Longitude: "		+ str(self.lon) + "\n" \
			+	"City: "		+ self.city + "\n" \
			+	"Region: "		+ self.region + "\n" \
			+	"Country: "		+ self.country + "\n" \
			+	"Country-Code: " 	+ self.country_code 

		return info

# TODO: learn Python better and make this less... verbose
def parse_resp(text):
	""" 
	parse_resp_single: parses a single record into its constituent parts and
	populates the class members with the data
	"""
	p = PwhoisData()
	for line in text.splitlines():
		ent = line.split(": ")
		if (ent[0] == "IP"):
			p.ip = ent[1]
		elif (ent[0] == "Origin-AS"):
			p.origin_as = int(ent[1])
		elif (ent[0] == "Prefix"):
			p.prefix = ent[1]
		elif (ent[0] == "AS-Path"):
			p.as_path = ent[1]
		elif (ent[0] == "AS-Org-Name"):
			p.as_org_name = ent[1]
		elif (ent[0] == "Org-Name"):
			p.org_name = ent[1]
		elif (ent[0] == "Net-Name"):
			p.net_name = ent[1]
		elif (ent[0] == "Cache-Date"):
			p.cache_date = int(ent[1])
		elif (ent[0] == "Latitude"):
			p.lat = float(ent[1])
		elif (ent[0] == "Longitude"):
			p.lon = float(ent[1])
		elif (ent[0] == "City"): 
			p.city = ent[1]
		elif (ent[0] == "Region"):
			p.region = ent[1]
		elif (ent[0] == "Country"):
			p.country = ent[1]
		elif (ent[0] == "Country-Code"):
			p.country_code = ent[1] 
	return p



def lookup_pwhois_single(server,target):
	"""
	perform a single whois query and fetch a single response
	assumes pwhois native format with this call
	"""
	if server == 0:
		server = "whois.pwhois.org"
	s = socket.socket()
	s.connect((server, 43))
	s.send(target + "\r\n")
	resp = s.recv(512)
	s.close
	return parse_resp(resp) 

def lookup_pwhois_bulk(server, targets):
	"""
	perform a bulk lookup of more than one target IP address
	return an array of PwhoisData objects
	"""
	if server == 0:
		server = "whois.pwhois.org"
	info_list = [] 
	s = socket.socket()
	s.connect((server, 43))
	s.send("begin\r\n")
	for target in targets:
		s.send(target + "\r\n")
		resp = s.recv(512)
		bgp_info = parse_resp(resp)
		info_list.append(bgp_info)
	s.send("end\r\n")
	s.close
	return info_list
		

if __name__ == "__main__":
	a = lookup_pwhois_bulk(0, ["4.2.2.1", "8.8.8.8"])
	for i in a:
		print i
		print
