#!/usr/bin/python
import sys
#from itertools import product
#import ipaddress
from netaddr import IPNetwork,IPAddress
rule_file=open("rules.txt","r")
rule_file_attr=rule_file.readline()[:-1].split(",")
#rule_file_attr[len(rule_file_attr)-1]=rule_file_attr[len(rule_file_attr)-1][:len(rule_file_attr[len(rule_file_attr)-1])-1]
#rule1=rule_file.readline()[:-1]
#rule2=rule_file.readline()[:-1]
#rule3=rule_file.readline()[:-1]
#rule4=rule_file.readline()[:-1]
#rule5=rule_file.readline()[:-1]
#rule6=rule_file.readline()[:-1]
#print rule_file_attr[len(rule_file_attr)-1]
rules=[]
[rules.append(line[:-1]) for line in rule_file.readlines()]
#print rule_file_attr
#print rule1
#print rule2
#print rule3
#print rule4
#print rule5
#print rule6
#print rules
in_rules=[]
out_rules=[]
anyif_rules=[]
for rule in rules:
	#print rule.split(",")[0]
	if rule.split(",")[0]=='1':
		in_rules.append(",".join(rule.split(",")[1:]))
	elif rule.split(",")[0]=='0':
		out_rules.append(",".join(rule.split(",")[1:]))
	else:
		anyif_rules.append(",".join(rule.split(",")[1:]))
tcpin_rules=[]
udpin_rules=[]
anyprotoin_rules=[]
for protorule in in_rules:
	if protorule.split(",")[2]=='tcp':
		tcpin_rules.append(protorule.split(",")[0]+","+protorule.split(",")[1]+","+protorule.split(",")[3]+","+protorule.split(",")[4]+","+protorule.split(",")[5]+","+protorule.split(",")[6])
	elif protorule.split(",")[2]=='udp':
		udpin_rules.append(protorule.split(",")[0]+","+protorule.split(",")[1]+","+protorule.split(",")[3]+","+protorule.split(",")[4]+","+protorule.split(",")[5]+","+protorule.split(",")[6])
	else:
		anyprotoin_rules.append(protorule.split(",")[0]+","+protorule.split(",")[1]+","+protorule.split(",")[3]+","+protorule.split(",")[4]+","+protorule.split(",")[5]+","+protorule.split(",")[6])
tcpout_rules=[]
udpout_rules=[]
anyprotoout_rules=[]
for protorule in out_rules:
	if protorule.split(",")[2]=='tcp':
		tcpout_rules.append(protorule.split(",")[0]+","+protorule.split(",")[1]+","+protorule.split(",")[3]+","+protorule.split(",")[4]+","+protorule.split(",")[5]+","+protorule.split(",")[6])
	elif protorule.split(",")[2]=='udp':
		udpout_rules.append(protorule.split(",")[0]+","+protorule.split(",")[1]+","+protorule.split(",")[3]+","+protorule.split(",")[4]+","+protorule.split(",")[5]+","+protorule.split(",")[6])
	else:
		anyprotoout_rules.append(protorule.split(",")[0]+","+protorule.split(",")[1]+","+protorule.split(",")[3]+","+protorule.split(",")[4]+","+protorule.split(",")[5]+","+protorule.split(",")[6])
tcpany_rules=[]
udpany_rules=[]
anyprotoany_rules=[]
for protorule in anyif_rules:
	if protorule.split(",")[2]=='tcp':
		tcpany_rules.append(protorule.split(",")[0]+","+protorule.split(",")[1]+","+protorule.split(",")[3]+","+protorule.split(",")[4]+","+protorule.split(",")[5]+","+protorule.split(",")[6])
	elif protorule.split(",")[2]=='udp':
		udpany_rules.append(protorule.split(",")[0]+","+protorule.split(",")[1]+","+protorule.split(",")[3]+","+protorule.split(",")[4]+","+protorule.split(",")[5]+","+protorule.split(",")[6])
	else:
		anyprotoany_rules.append(protorule.split(",")[0]+","+protorule.split(",")[1]+","+protorule.split(",")[3]+","+protorule.split(",")[4]+","+protorule.split(",")[5]+","+protorule.split(",")[6])
for rul in tcpin_rules:
	count=0
	for i in range(len(tcpin_rules)):
		if rul.split(",")[1]==tcpin_rules[i].split(",")[1]:
			count+=1
	if count>1:
		print "double time"
	if count==1:
		print "single"

print "inbound rules"
print in_rules
print "out_bound rules"
print out_rules
print "tcp in bound rules"
print tcpin_rules
print "udp in bound rules"
print udpin_rules
print "any proto in bound rules"
print anyprotoin_rules
print "tcp out rules"
print tcpout_rules
print "udp out rules"
print udpout_rules
print "any proto out rules"
print anyprotoout_rules
print "any proto any rules"
print anyprotoany_rules
rule_file.close()
sys.exit()
