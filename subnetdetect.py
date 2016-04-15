#!/usr/bin/python
import ipaddress
from netaddr import IPNetwork,IPAddress
print ipaddress.ip_network(unicode('192.168.0.0'))
print IPNetwork('192.168.43.34')
if IPAddress("192.168.43.34") in IPNetwork('192.168.43.34'):
	print True
else:
	print False
