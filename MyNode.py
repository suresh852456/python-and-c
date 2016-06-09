# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 23:18:54 2016

@author: seeker
"""
class Node:
    def __init__(self,tag,value,data=None):
        self.tag=tag
        self.value=value
        self.data=data
        self.parent=None
        self.root=False
        self.child=[]
    def add_child(self,children,*args):
        self.child.append(children)
        if len(args)>0:
            for i in args:
                self.child.append(i)
    def remove_child(self,children):
        if children in self.child:
            self.child.remove(children)
    def move_child(self,children,index):
        if children in self.child:
            self.child.remove(children)
            self.child.insert(index,children)
    def set_parent(self,parentnode):
        self.parent=parentnode
    def get_parent(self):
        return self.parent
    def is_leaf(self):
        if len(self.child)==0:
            return True
        else:
            return False
    def is_root(self):
        if self.parent==None:
            return True
        else:
            return False
    def getData(self):
        return self.data
    def getTag(self):
        return self.tag
    def getValue(self):
        return self.value
    def getAll(self):
        return self.tag,self.value,self.parent,self.child,self.data