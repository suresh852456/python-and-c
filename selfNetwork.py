#!/usr/bin/python
""" 
Author : Suresh Nagulavancha
Created : 29 April 2016
Version : 1.0
All copyrights reserved
"""

"""
This program is used to create self learning Network to avoid 
Faults in the network 
"""

class Node:
	""" this class is used to create the node """
	connections={}
	def __init__(self,name,ports=12,interfaces={"eth0":False,"wlan0":False},IPaddr="0.0.0.0",MacAddr="00:00:00:00:00:00",xpos=50,ypos=50,clockSpeed= 1.8,QueueSize=100,heat=30):
		self.name=name
		self.ports=ports
		self.interfaces=interfaces
		self.IPaddr=Ipaddr
		self.MacAddr=MacAddr
		self.xpos=xpos
		self.ypos=ypos
		self.clockSpeed=clockspeed
		self.QueueSize=QueueSize
		self.heat=heat
	def __generateAlarm(self,name,priority,timestamp,*args,**kwargs):
		#create alarm object with name,priority and timestamp
		for arg in args:
			pass
		for key,value in kwargs.iteritems():
			pass
	def __receiveAlarm(self,Alarm,priority,time):
		pass
	def __getHeat(self):
		return self.heat
	def __setHeat(self,value):
		self.heat=value
	def __changePosition(self,x,y):
		self.xpos=x
		self.ypos=y
	def __modifyPropoerties(self,name,ports=12,interfaces=["etho","wlan0"],IPaddr="0.0.0.0",MacAddr="00:00:00:00:00:00",xpos=50,ypos=50,clockSpeed= 1.8,QueueSize=100,heat=30):
		self.name=name
		self.ports=ports
		self.interfaces=interfaces
		self.IPaddr=Ipaddr
		self.MacAddr=MacAddr
		self.xpos=xpos
		self.ypos=ypos
		self.clockSpeed=clockspeed
		self.QueueSize=QueueSize
		self.heat=heat
	def __connect(self,iface,node):
		if iface in self.interfaces.keys():
			if self.interfaces[iface]==False:
				self.interfaces[iface]=True
				Node.connections.update({iface:node})
			else:
				print "Unable to connect to "+node+" at "+iface+"interface , interface already connected"
		else:
			print "Unable to connect to "+node+" at "+iface+"interface, interface not available" 	
	def __disconnect(self,iface,node):
		if iface in self.interfaces.keys():
			if self.interfaces[iface]==True:
				self.interfaces[iface]==False
				del Node.connections[iface]
			else:
				print "Interface was not used unable to disconnect"
		else:
			print "Unable to disconnect no such interface"


class connection:
	""" this is used to create the connection object"""
	def __init__(self,name,length,typeofconn="fe",medium="UTP"):
		self.name=name
		self.length=length
		self.typeofconn=typeofconn
		self.medium=medium
	def __connect(node1,node2,node1if,node2if):
		node1._Node__connect(node1if,node2)
		node2._Node__connect(node2if,node1)
	def __disconnect(node1,node2):
		node1._Node__disconnect(node1if,node2)
		node2._Node__disconnect(node2if,node1)
	def __breakit(node1,node2):
		pass
def Topology():
	"""used to display the topology connections between all the nodes"""
	pass
def main():
	pass
if __name__=="__main__":
	main()

	
