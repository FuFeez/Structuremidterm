#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
import tkinter.ttk as ttk
from collections import deque
import numpy as np
import time
import csv
from tkinter import *
import itertools
from numpy import genfromtxt
np.set_printoptions(threshold=np.inf)
m = tk.Tk()
m.title('Test Performance')
m.geometry('1280x400')
m.maxsize(1280,720)


# In[2]:


i = 0
listinput = []
position = []
x = []
a = int(0)
searchbox = []
somebox = []
arrayinput = np.array([])
F = []
root = []
text = []


# In[3]:


text1=tk.StringVar()
text2=tk.StringVar()
text3=tk.StringVar()
textlistpush=tk.StringVar()
textlistsort=tk.StringVar()
textlistinsert=tk.StringVar()
textlistremove=tk.StringVar()
textlistsearch=tk.StringVar()
textlistshow=tk.StringVar()
textlistfix=tk.StringVar()
textarrpush=tk.StringVar()
textarrsort=tk.StringVar()
textarrinsert=tk.StringVar()
textarrremove=tk.StringVar()
textarrsearch=tk.StringVar()
textarrshow=tk.StringVar()
textarrfix=tk.StringVar()
texttreepush=tk.StringVar()
texttreeinorder=tk.StringVar()
texttreeinsert=tk.StringVar()
texttreeremove=tk.StringVar()
texttreesearch=tk.StringVar()
texttreepostorder=tk.StringVar()


# In[4]:


T = Text(m, height = 10, width = 140)
T.place (x = 10, y=30)
box2=tk.Entry(m,textvariable=text2 ,width = 186)
box2.place(x=10,y=200)
time1=tk.Entry(m,textvariable=textlistpush,width=20)
time1.place(x=310, y=249)
time2=tk.Entry(m,textvariable=textlistsort,width=20)
time2.place(x=440, y=249)
time3=tk.Entry(m,textvariable=textlistinsert,width=20)
time3.place(x=570, y=249)
time4=tk.Entry(m,textvariable=textlistremove,width=20)
time4.place(x=700, y=249)
time5=tk.Entry(m,textvariable=textlistsearch,width=20)
time5.place(x=830, y=249)
time6=tk.Entry(m,textvariable=textlistshow,width=20)
time6.place(x=960, y=249)
time7=tk.Entry(m,textvariable=textlistfix,width=20)
time7.place(x=1090, y=249)


# In[5]:


boxlabel1=Label(m,text = "text box")
boxlabel1.place(x=1158,y=60)
boxlabel2=Label(m,text = "position")
boxlabel2.place(x=1158,y=110)
box1=tk.Entry(m,textvariable=text1,width=15)
box1.place(x=1160, y=80)
box3=tk.Entry(m,textvariable=text3,width=3)
box3.place(x=1160, y=130)


# In[6]:


T = Text(m, height = 10, width = 140)
T.place (x = 10, y=30)
box2=tk.Entry(m,textvariable=text2 ,width = 186)
box2.place(x=10,y=200)
time1=tk.Entry(m,textvariable=textlistpush,width=20)
time1.place(x=310, y=249)
time2=tk.Entry(m,textvariable=textlistsort,width=20)
time2.place(x=440, y=249)
time3=tk.Entry(m,textvariable=textlistinsert,width=20)
time3.place(x=570, y=249)
time4=tk.Entry(m,textvariable=textlistremove,width=20)
time4.place(x=700, y=249)
time5=tk.Entry(m,textvariable=textlistsearch,width=20)
time5.place(x=830, y=249)
time6=tk.Entry(m,textvariable=textlistshow,width=20)
time6.place(x=960, y=249)
time7=tk.Entry(m,textvariable=textlistfix,width=20)
time7.place(x=1090, y=249)
arrtime1=tk.Entry(m,textvariable=textarrpush,width=20)
arrtime1.place(x=310, y=304)
arrtime2=tk.Entry(m,textvariable=textarrsort,width=20)
arrtime2.place(x=440, y=304)
arrtime3=tk.Entry(m,textvariable=textarrinsert,width=20)
arrtime3.place(x=570, y=304)
arrtime4=tk.Entry(m,textvariable=textarrremove,width=20)
arrtime4.place(x=700, y=304)
arrtime5=tk.Entry(m,textvariable=textarrsearch,width=20)
arrtime5.place(x=830, y=304)
arrtime6=tk.Entry(m,textvariable=textarrshow,width=20)
arrtime6.place(x=960, y=304)
arrtime7=tk.Entry(m,textvariable=textarrfix,width=20)
arrtime7.place(x=1090, y=304)
labelarr=Label(m,text = "Array function")
labelarr.place(x=10,y=277)
labellist=Label(m,text = "List function")
labellist.place(x=10,y=222)
labeltree=Label(m,text = "Binary tree function")
labeltree.place(x=10,y=332)
label2=Label(m,text = "display channel")
label2.place(x=10,y=5)
label3=Label(m,text = "time of listpush")
label3.place(x=308,y=224)
label4=Label(m,text = "time of listsort")
label4.place(x=438,y=224)
label5=Label(m,text = "time of listinsert")
label5.place(x=568,y=224)
label6=Label(m,text = "time of listremove")
label6.place(x=698,y=224)
label7=Label(m,text = "time of listsearch")
label7.place(x=828,y=224)
label7=Label(m,text = "time of listshow")
label7.place(x=958,y=224)
label7=Label(m,text = "time of listfix")
label7.place(x=1088,y=224)
arrlabel3=Label(m,text = "time of arraypush")
arrlabel3.place(x=308,y=279)
arrlabel4=Label(m,text = "time of arraysort")
arrlabel4.place(x=438,y=279)
arrlabel5=Label(m,text = "time of arrayinsert")
arrlabel5.place(x=568,y=279)
arrlabel6=Label(m,text = "time of arrayremove")
arrlabel6.place(x=698,y=279)
arrlabel7=Label(m,text = "time of arraysearch")
arrlabel7.place(x=828,y=279)
arrlabel7=Label(m,text = "time of arrayshow")
arrlabel7.place(x=958,y=279)
arrlabel7=Label(m,text = "time of arrayfix")
arrlabel7.place(x=1088,y=279)
treetime1=tk.Entry(m,textvariable=texttreepush,width=20)
treetime1.place(x=323, y=359)
treetime2=tk.Entry(m,textvariable=texttreeinorder,width=20)
treetime2.place(x=453, y=359)
treetime3=tk.Entry(m,textvariable=texttreepostorder,width=20)
treetime3.place(x=583, y=359)
treetime4=tk.Entry(m,textvariable=texttreeinsert,width=20)
treetime4.place(x=713, y=359)
treetime5=tk.Entry(m,textvariable=texttreeremove,width=20)
treetime5.place(x=843, y=359)
treetime6=tk.Entry(m,textvariable=texttreesearch,width=20)
treetime6.place(x=973, y=359)
treelabel3=Label(m,text = "time of create BST")
treelabel3.place(x=321,y=334)
treelabel4=Label(m,text = "time of inorder")
treelabel4.place(x=451,y=334)
treelabel5=Label(m,text = "time of postorder")
treelabel5.place(x=581,y=334)
treelabel6=Label(m,text = "time of treeinsert")
treelabel6.place(x=711,y=334)
treelabel7=Label(m,text = "time of treeremove")
treelabel7.place(x=841,y=334)
treelabel7=Label(m,text = "time of treesearch")
treelabel7.place(x=971,y=334)


# In[7]:


class ListFei:
    def listshow():
        t0 = time.time()
        listinputtext = ' '.join([str(elem) for elem in listinput])
        T.delete('1.0', END)
        T.insert(1.0,listinput)
        t1 = time.time()
        tlshow = t1-t0
        textlistshow.set(tlshow)
    
    def listsort():
        t0 = time.time()
        global listinput
        listinput = sorted(listinput)
        listinputtext = ' '.join([str(elem) for elem in listinput])
        T.delete('1.0', END)
        T.insert(1.0,listinputtext)
        t1 = time.time()
        tlsort = t1-t0
        textlistsort.set(tlsort)
    
    def listinsert():
        t0 = time.time()
        global listinput
        position.append(box3.get())
        if position[0] != '' :
            listinput.insert(int(position[0]),box1.get())
            position.clear()
        else :
            position.clear()
        listinputtext = ' '.join([str(elem) for elem in listinput])
        T.delete('1.0', END)
        T.insert(1.0,listinputtext)
        t1 = time.time()
        tlinsert = t1-t0
        textlistinsert.set(tlinsert)
        
    def listremove():
        t0 = time.time()
        global listinput
        position.append(box3.get())
        if position[0] != '' :
            del listinput[int(position[0])]
        else :
            position.clear()
        position.clear()
        listinputtext = ' '.join([str(elem) for elem in listinput])
        T.delete('1.0', END)
        T.insert(1.0,listinputtext)
        t1 = time.time()
        tlremove = t1-t0
        textlistremove.set(tlremove)
    def listsearch():
        t0 = time.time()
        global listinput
        global i
        global somebox
        searchbox.append(box1.get())
        if searchbox[0] != '' :
            x = searchbox[0]            
            for i in range(0, len(listinput))  :
                if x == listinput[i] :
                    somebox.append(i)
                    searchbox.clear()
            if len(somebox) ==0 :
                text2.set ("not found")
            if len(somebox) !=0 :
                somebox = ' '.join([str(elem) for elem in somebox])
                text2.set ("found ตำแหน่งที่ " + somebox)
            searchbox.clear()
        else :
            searchbox.clear()
        somebox = []
        t1 = time.time()
        tlsearch = t1-t0
        textlistsearch.set(tlsearch)
    def listfix():
        t0 = time.time()
        global listinput
        position.append(box3.get())
        if position[0] != '' :
            listinput[int(position[0])] = box1.get()
            position.clear()
        else :
            position.clear()
        listinputtext = ' '.join([str(elem) for elem in listinput])
        T.delete('1.0', END)
        T.insert(1.0,listinputtext)
        t1 = time.time()
        tlfix = t1-t0
        textlistfix.set(tlfix)
    def listpush():
        t0 = time.time()
        global listinput
        filepath = ('2500dataframe.csv')
        file = open(filepath,encoding="utf8")
        Reader = csv.reader(file)
        listinput = list(itertools.chain(*Reader))
        listinputtext = ' '.join([str(elem) for elem in listinput])
        T.delete('1.0', END)
        T.insert(1.0,listinputtext)
        t1 = time.time()
        tlpush = t1-t0
        textlistpush.set(tlpush)
    listbutton1=tk.Button(text='push',command=listpush)
    listbutton1.place(x=10, y=245)
    listbutton2=tk.Button(text='sort',command=listsort)
    listbutton2.place(x=50, y=245)
    listbutton3=tk.Button(text='insert',command=listinsert)
    listbutton3.place(x=85, y=245)
    listbutton4=tk.Button(text='remove',command=listremove)
    listbutton4.place(x=130, y=245)
    listbutton5=tk.Button(text='search',command=listsearch)
    listbutton5.place(x=185, y=245)
    listbutton6=tk.Button(text='show',command=listshow)
    listbutton6.place(x=235, y=245)
    listbutton7=tk.Button(text='fix',command=listfix)
    listbutton7.place(x=280, y=245)
    listbutton8=tk.Button(text='fix',command=listfix)
    listbutton8.place(x=280, y=245)



# In[8]:


class ArrayFei:
    def arraypush() :
        global arrayinput
        t0 = time.time()
        arrayinput = genfromtxt('2500dataframe.csv', delimiter=',',dtype = str,encoding='utf8')
        arrayinputtext = ' '.join([str(elem) for elem in arrayinput])
        T.delete('1.0', END)
        T.insert(1.0,arrayinputtext)
        t1 = time.time()
        tapush = t1-t0
        textarrpush.set(tapush)
    def arraysort() :
        t0 = time.time()
        global i
        global arrayinput
        i = np.argsort(arrayinput)
        arrayinput = arrayinput[i]
        arrayinputtext = ' '.join([str(elem) for elem in arrayinput])
        T.delete('1.0', END)
        T.insert(1.0,arrayinputtext)
        t1 = time.time()
        tasort = t1-t0
        textarrsort.set(tasort)
    def arrayinsert():
        t0 = time.time()
        global arrayinput
        position.append(box3.get())
        if position[0] != '' :
            arrayinput = np.insert(arrayinput,int(position[0]),str(box1.get()))
            position.clear()
        else :
            position.clear()
        arrayinputtext = ' '.join([str(elem) for elem in arrayinput])
        T.delete('1.0', END)
        T.insert(1.0,arrayinputtext)
        t1 = time.time()
        tainsert = t1-t0
        textarrinsert.set(tainsert)
    def arrayremove():
        t0 = time.time()
        global arrayinput
        position.append(box3.get())
        if position[0] != '' :
            arrayinput = np.delete(arrayinput , int(position[0]))
            position.clear()
        else :
            position.clear()
        arrayinputtext = ' '.join([str(elem) for elem in arrayinput])
        T.delete('1.0', END)
        T.insert(1.0,arrayinputtext)
        t1 = time.time()
        taremove = t1-t0
        textarrremove.set(taremove)
    def arraysearch():
        t0 = time.time()
        global arrayinput
        global i
        global somebox
        searchbox.append(box1.get())
        if searchbox[0] != '' :
            x = searchbox[0]            
            for i in range(0, len(arrayinput))  :
                if x == arrayinput[i] :
                    somebox.append(i)
                    searchbox.clear()
            if len(somebox) ==0 :
                text2.set ("not found")
            if len(somebox) !=0 :
                somebox = ' '.join([str(elem) for elem in somebox])
                text2.set ("found ตำแหน่งที่ " + somebox)
            searchbox.clear()

        else :
            searchbox.clear()
        somebox = []
        t1 = time.time()
        tasearch = t1-t0
        textarrsearch.set(tasearch)
    def arrayfix():
        t0 = time.time()
        global arrayinput
        position.append(box3.get())
        if position[0] != '' :
            arrayinput[int(position[0])] = box1.get()
            position.clear()
        else :
            position.clear()
        listinputtext = ' '.join([str(elem) for elem in arrayinput])
        T.delete('1.0', END)
        T.insert(1.0,listinputtext)
        t1 = time.time()
        tafix = t1-t0
        textarrfix.set(tafix)

    def arrayshow():
        t0 = time.time()
        arrayinputtext = ' '.join([str(elem) for elem in arrayinput])
        T.delete('1.0', END)
        T.insert(1.0,arrayinput)
        t1 = time.time()
        tashow = t1-t0
        textarrshow.set(tashow)
        

        
    arrbutton1=tk.Button(text='push',command=arraypush)
    arrbutton1.place(x=10, y=300)
    arrbutton2=tk.Button(text='sort',command=arraysort)
    arrbutton2.place(x=50, y=300)
    arrbutton3=tk.Button(text='insert',command=arrayinsert)
    arrbutton3.place(x=85, y=300)
    arrbutton4=tk.Button(text='remove',command=arrayremove)
    arrbutton4.place(x=130, y=300)
    arrbutton5=tk.Button(text='search',command=arraysearch)
    arrbutton5.place(x=185, y=300)
    arrbutton7=tk.Button(text='fix',command=arrayfix)
    arrbutton7.place(x=280, y=300)
    arrbutton6=tk.Button(text='show',command=arrayshow)
    arrbutton6.place(x=235, y=300)


# In[9]:


class newNode:
    def __init__(self,data) :
        self.key = str(data)
        self.count = 1
        self.left = None
        self.right = None
def insert(node,key):
    if node == None:
        k = newNode(key)
        return k
    if key == node.key:
        (node.count) += 1
        return node
    if key < node.key:
        node.left = insert(node.left,key)
    else:
        node.right = insert(node.right,key)
    return node
def minValueNode(node):
    current = node
    while current.left != None:
        current = current.left
    return current
def deleteNode(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = deleteNode(root.left, key)
        return root
    elif(key > root.key):
        root.right = deleteNode(root.right, key)
        return root
    if root.left is None and root.right is None:
          return None
    if root.left is None:
        temp = root.right
        root = None
        return temp
 
    elif root.right is None:
        temp = root.left
        root = None
        return temp
    succParent = root
    succ = root.right
 
    while succ.left != None:
        succParent = succ
        succ = succ.left
    if succParent != root:
        succParent.left = succ.right
    else:
        succParent.right = succ.right
    root.key = succ.key
 
    return root
def search(root,key):
    if root is None or root.key == key :
        return root
    if root.key < key:
        return search(root.right,key)
    
    return search(root.left,key)


# In[10]:


def post_traversing(root):
    global post
    post = []
    if root != None:
        post =  post_traversing(root.left)
        post = post + post_traversing(root.right)
        post.append(root.key)
    return post
def post_count(root):
    global postc
    postc = []
    if root != None:
        postc =  post_count(root.left)
        postc = postc + post_count(root.right)
        postc.append(root.count)
    return postc
def postordersum():
    global posts
    posts = []
    for i in range (0,len(post)) :
        posttext = str(post[i]) + "(" + str(postc[i]) + ")"
        posts.append(posttext)


# In[11]:


def inorder_traversing(root):
    global res
    res = []
    if root != None:
        res =  inorder_traversing(root.left)
        res.append(root.key)
        res = res + inorder_traversing(root.right)
    return res
def inorder_count(root):
    global cni
    cni = []
    if root != None:
        cni =  inorder_count(root.left)
        cni.append(root.count)
        cni = cni + inorder_count(root.right)
    return cni
def inordersum():
    global iod
    iod = []
    for i in range (0,len(res)) :
        iodt = str(res[i]) + "(" + str(cni[i]) + ")"
        iod.append(iodt)


# In[12]:


def createtree() :
    t0 = time.time()
    global root
    filepath = ('2500dataframe.csv')
    file = open(filepath,encoding="utf8")
    Reader = csv.reader(file)
    data = list(itertools.chain(*Reader))
    if __name__ == '__main__':
        root = None
        for i in range(0,len(data)) :
            root = insert(root, str(data[i]))
    inorder_traversing(root)
    inorder_count(root)
    inordersum()
    T.delete('1.0', END)
    T.insert(1.0,iod)    
    t1 = time.time()
    ttpush = t1-t0
    texttreepush.set(ttpush)


# In[13]:


def inorderbuttom() :
    t0 = time.time()
    global root
    inorder_traversing(root)
    inorder_count(root)
    inordersum()
    T.delete('1.0', END)
    T.insert(1.0,iod)
    t1 = time.time()
    ttinorder = t1-t0
    texttreeinorder.set(ttinorder)


# In[14]:


def postorderbuttom() :
    t0 = time.time()
    global root
    post_traversing(root)
    post_count(root)
    postordersum()
    T.delete('1.0', END)
    T.insert(1.0,posts)
    t1 = time.time()
    ttpostorder = t1-t0
    texttreepostorder.set(ttpostorder)


# In[15]:


def searchtree():
    t0 = time.time()
    searchtext = search(root,str(box1.get()))
    if searchtext != None :
        text2.set("found")
    else :
        text2.set('Not found')
    t1 = time.time()
    ttsearch = t1-t0
    texttreesearch.set(ttsearch)


# In[16]:


def inserttree():
    t0 = time.time()
    global root
    root = insert(root, str(box1.get()))
    inorder_traversing(root)
    inorder_count(root)
    inordersum()
    T.delete('1.0', END)
    T.insert(1.0,iod)
    t1 = time.time()
    ttinsert = t1-t0
    texttreeinsert.set(ttinsert)


# In[17]:


def deltree():
    t0 = time.time()
    global root
    textbox = box1.get()
    root = deleteNode(root,str(box1.get()))
    inorder_traversing(root)
    inorder_count(root)
    inordersum()
    T.delete('1.0', END)
    T.insert(1.0,iod)
    t1 = time.time()
    ttremove = t1-t0
    texttreeremove.set(ttremove)


# In[18]:


treebutton1=tk.Button(text='Create',command=createtree)
treebutton1.place(x=10, y=355)    
treebutton2=tk.Button(text='Postorder',command=postorderbuttom)
treebutton2.place(x=108, y=355)  
treebutton3=tk.Button(text='search',command=searchtree)
treebutton3.place(x=272, y=355)
#treebutton4=tk.Button(text='None',command=rootnone)
#treebutton4.place(x=500, y=395)
treebutton5=tk.Button(text='Insert',command=inserttree)
treebutton5.place(x=173, y=355)
treebutton6=tk.Button(text='Remove',command=deltree)
treebutton6.place(x=215, y=355)
treebutton7=tk.Button(text='Inorder',command=inorderbuttom)
treebutton7.place(x=57, y=355)  


# In[19]:


mainloop()

