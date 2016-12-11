# -*- coding: utf-8 -*-
def IphoneSerial(serial):
    OEM_Factory = serial[0:3]
    manufacturing_date=serial[3:5].lower()
    Factory_Code={'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'c':10,'d':11,'f':12,'g':13,'h':14,'j':15,'k':16,'l':17,'m':18,'n':19,'p':20,'q':21,'r':22,'t':23,'v':24,'w':25,'x':26,'y':27}
    for x in Factory_Code:
        print ("Factory_Code[%s] = " % x,dict[x])
