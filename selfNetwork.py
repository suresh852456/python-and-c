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
globals().keys()[globals().values().index(node)]
"""

class Node:
	""" this class is used to create the node """
	def __init__(self,name,ports=12,interfaces=["eth0","wlan0"],IPaddr="0.0.0.0",MacAddr="00:00:00:00:00:00",xpos=50,ypos=50,clockSpeed= 1.8,QueueSize=100,heat=30):
		self.connections={}
		self.name=name
		self.ports=ports
		self.interfaces=interfaces
		self.IPaddr=IPaddr
		self.MacAddr=MacAddr
		self.xpos=xpos
		self.ypos=ypos
		self.clockSpeed=clockSpeed
		self.QueueSize=QueueSize
		self.heat=heat
		for i in interfaces:
			self.connections.update({i:False})
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
	def __connect(self,iface,node):
		if iface in self.connections.keys():
			if self.connections[iface]==False:
				self.connections[iface]=True
				self.connections.update({iface:node})
			else:
				print "Unable to connect to interface , interface already connected"
		else:
			print "Unable to connect to interface, interface not available" 	
	def __disconnect(self,iface,node):
		if iface in self.connections.keys():
			if self.connections[iface]==True:
				self.connections[iface]==False
			else:
				print "Interface was not used unable to disconnect"
		else:
			print "Unable to disconnect no such interface"


class connection:
	""" this is used to create the connection object"""
	def __init__(self,name,length=50,typeofconn="fe",medium="UTP"):
		self.name=name
		self.length=length
		self.typeofconn=typeofconn
		self.medium=medium
	def __connect(self,node1,node2,node1if,node2if):
		node1._Node__connect(node1if,node2)
		node2._Node__connect(node2if,node1)
	def __disconnect(self,node1,node2):
		node1._Node__disconnect(node1if,node2)
		node2._Node__disconnect(node2if,node1)
	def __breakit(self,node1,node2):
		pass
"""
def Topology():
	#used to display the topology connections between all the nodes
	pass
def main():
	pass
if __name__=="__main__":
	main()
"""
