#David Lewis
import random
rotorlist=[]
rotorturn=0
bypass,bypass2,bypass3,bypass4=0,0,0,0
s1,s2,s3,s4,s5=-1,-1,-1,-1,-1
debug=0

#FEATURES:
    #5 ROTORS ◄
    #ABLE TO SET ROTORS ◄
    #LETTERS TO NUMBERS AND BACK ◄
    #PLUG BOARD ◄
    #ROTORS TURN AND WORK WHEN DOING SO ◄
    #OUTPUTS ENCODED ◄
    #DECODES MESSAGES ◄

def rotorimport():
    datafile=open("rotors.txt","r")
    data=datafile.read()
    datafile.close()
    data=data.replace("\n",',')
    datalist=data.split(",")
    for x in range(0,26):
        for i in range(0,26):
            rinput=datalist[i]
            routput=datalist[i+26]
            rinput2=datalist[i+26*2]
            routput2=datalist[i+26*3]
            rinput3=datalist[i+26*4]
            routput3=datalist[i+26*5]
            rinput4=datalist[i+26*6]
            routput4=datalist[i+26*7]
            rinput5=datalist[i+26*8]
            routput5=datalist[i+26*9]
            refinput=datalist[i+26*10]
            refoutput=datalist[i+26*11]
            r1=Rotor(rinput, routput, rinput2, routput2,rinput3,routput3,rinput4,routput4,rinput5,routput5,refinput,refoutput)
            rotorlist.append(r1)

class Rotor:
    def __init__(self, rinput, routput, rinput2, routput2,rinput3,routput3,rinput4,routput4,rinput5,routput5,refinput,refoutput):
        self.rinput=rinput
        self.routput=routput
        self.rinput2=rinput2
        self.routput2=routput2
        self.rinput3=rinput3
        self.routput3=routput3
        self.rinput4=rinput4
        self.routput4=routput4
        self.rinput5=rinput5
        self.routput5=routput5
        self.refinput=refinput
        self.refoutput=refoutput
    
def displayrotors():
    global dr1,dr2,dr3,dr4,dr5
    rotorlook="{:>18}{:>7}{:>7}{:>7}{:>7}{:>7}"
    print(rotorlook.format("R", rotorlist[dr5-1].rinput5,rotorlist[dr4-1].rinput4,rotorlist[dr3-1].rinput3,rotorlist[dr2-1].rinput2,rotorlist[dr1-1].rinput))

def setrotors():
    global dr1,dr2,dr3,dr4,dr5 
    global setting
    global bypass,bypass2,bypass3,bypass4
    rsetgo=input("Set rotors? (y/n) ")
    while rsetgo=="y":
        setting=1
        rset=int(input("Which rotor? (1,2,3,4,5) "))
        if rset==1:
            sp1=int(input("Choose position from 1 to 26: "))
            dr1=sp1
            while sp1!=0:
                rotateRotors()
                sp1-=1
            print("Rotor changed.")
        if rset==2:
            sp2=int(input("Choose position from 1 to 26: "))
            dr2=sp2
            bypass=1
            sp2=sp2
            while sp2!=0:
                rotateRotors()
                sp2-=1
            print("Rotor changed.")
        if rset==3:
            sp3=int(input("Choose position from 1 to 26: "))
            dr3=sp3
            bypass,bypass2=1,1
            sp3=sp3
            while sp3!=0:
                rotateRotors()
                sp3-=1
            print("Rotor changed.")
        if rset==4:
            sp4=int(input("Choose position from 1 to 26: "))
            dr4=sp4
            bypass,bypass2,bypass3=1,1,1
            sp4=sp4
            while sp4!=0:
                rotateRotors()
                sp4-=1
            print("Rotor changed.")
        if rset==5:
            sp5=int(input("Choose position from 1 to 26: "))
            dr5=sp5
            bypass,bypass2,bypass3,bypass4=1,1,1,1
            sp5=sp5
            while sp5!=0:
                rotateRotors()
                sp5-=1
            print("Rotor changed.")
        displayrotors()
        rsetgo=input("Change another rotor? (y/n) ")
        bypass,bypass2,bypass3,bypass4=0,0,0,0
    #displayrotors()
    
def inputmessage():
    global setting
    messagein=input("Input message: ")
    messagein=messagein.replace(" ","")
    messagein=messagein.lower()
    messagelist[:0]=messagein
    setting=0
    plugboard()
    for x in range(0,len(messagelist)):
        linput=ord(messagelist[x])-96
        #print(linput,"start")
        linput2=int(rotorlist[linput-1].routput)
        #print(linput2,"Li2")
        linput3=int(rotorlist[linput2-1].routput2)
        #print(linput3,"Li3")
        linput4=int(rotorlist[linput3-1].routput3)
        #print(linput4,"Li4")
        linput5=int(rotorlist[linput4-1].routput4)
        #print(linput5,"Li5")
        linput6=int(rotorlist[linput5-1].routput5)
        #print(linput6,"Li6")
        reflect=int(rotorlist[linput6-1].refoutput)
        #print(reflect,"R")
        for i in range(0,26):
            if int(reflect)==int(rotorlist[i].routput5):
                #print(i+1,"HEY DAVE")
                loc=i+1
        for j in range(0,26):
            if int(loc)==int(rotorlist[j].routput4):
                #print(j+1,"HEY AGAIN")
                loc2=j+1
        for k in range(0,26):
            if int(loc2)==int(rotorlist[k].routput3):
                #print(k+1,"AND AGAIN")
                loc3=k+1
        for l in range(0,26):
            if int(loc3)==int(rotorlist[l].routput2):
                #print(l+1,"IT GOES ON")
                loc4=l+1
        for m in range(0,26):
            if int(loc4)==int(rotorlist[m].routput):
                #print(m+1,"AND ON")
                loc5=m+1
        finoutput=chr(loc5+96)
        #print(finoutput)
        finmessage.append(finoutput)
        rotateRotors()
    
def rotateRotors():
    global dr1,dr2,dr3,dr4,dr5
    global rotorturn,rotorturn2,rotorturn3,rotorturn4,rotorturn5
    global s1list
    global rotorlist
    global setting
    global bypass,bypass2,bypass3,bypass4
    rotorturn+=1
    #print(rotorturn)
    for q in range(0,26):
        s1=rotorlist[q].routput
        s1list.append(s1)
    s1list=s1list[-1:]+s1list[:-1]
    for r in range(0,26):
        rotorlist[r].routput=s1list[r]
        #print(s1list)
        #print(rotorlist[r].routput)
    if setting!=1:
        dr1+=1
    if rotorturn==27 or bypass==1:
        for q in range(0,26):
            s1=rotorlist[q].routput2
            s1list.append(s1)
            s1list=s1list[-1:]+s1list[:-1]
        for r in range(0,26):
            rotorlist[r].routput2=s1list[r]
            #print(s1list)
            #print(rotorlist[r].routput2)
        rotorturn=1
        rotorturn2+=1
        if setting!=1:
            dr1=rotorturn
            dr2+=1
        #print(dr2)
        if rotorturn2==27 or bypass2==1:
            for q in range(0,26):
                s1=rotorlist[q].routput3
                s1list.append(s1)
                s1list=s1list[-1:]+s1list[:-1]
            for r in range(0,26):
                rotorlist[r].routput3=s1list[r]
                #print(s1list)
                #print(rotorlist[r].routput3)
            rotorturn2=1
            rotorturn3+=1
            if setting!=1:
                dr2=rotorturn2
                dr3+=1
            if rotorturn3==27 or bypass3==1:
                for q in range(0,26):
                    s1=rotorlist[q].routput4
                    s1list.append(s1)
                    s1list=s1list[-1:]+s1list[:-1]
                for r in range(0,26):
                    rotorlist[r].routput4=s1list[r]
                    #print(s1list)
                    #print(rotorlist[r].routput4)
                rotorturn3=1
                rotorturn4+=1
                if setting!=1:
                    dr3=rotorturn3
                    dr4+=1
                if rotorturn4==27 or bypass4==1:
                    for q in range(0,26):
                        s1=rotorlist[q].routput5
                        s1list.append(s1)
                        s1list=s1list[-1:]+s1list[:-1]
                    for r in range(0,26):
                        rotorlist[r].routput5=s1list[r]
                        #print(s1list)
                        #print(rotorlist[r].routput5)
                    rotorturn4=1
                    rotorturn5+=1
                    if setting!=1:
                        dr4=rotorturn4
                        dr5+=1
                    if rotorturn5==27:
                        rotorturn,rotorturn2,rotorturn3,rotorturn4,rotorturn5=0,0,0,0,0
                        dr1,dr2,dr3,dr4,dr5=1,1,1,1,1
    
def plugboardsetup():
    global wirenum
    global wire1,wire2,wire3,wire4,wire5,wire6,wire7,wire8,wire9,wire10
    wired=0
    wiring=input("Would you like to wire the plugboard? (y/n) ")
    while wiring=="y":
        wire=input("Which 2 letters to wire together? ")
        if len(wire)!=2:
            print("I said 2 letters. No more, no less.")
            wire=""
            wirenum=0
            rewireplugs()
        wirenum+=1
        if wirenum==1:
            wire1[:0]=wire
            wired+=1
            #print(wire1,'1')
            wiring=input("Add another wire? (y/n) ")
        if wirenum==2:
            wire2[:0]=wire
            wired+=1
            #print(wire2,'2')
            wiring=input("Add another wire? (y/n) ")
        if wirenum==3:
            wire3[:0]=wire
            wired+=1
            #print(wire3,'3')
            wiring=input("Add another wire? (y/n) ")
        if wirenum==4:
            wire4[:0]=wire
            wired+=1
            #print(wire4,'4')
            wiring=input("Add another wire? (y/n) ")
        if wirenum==5:
            wire5[:0]=wire
            wired+=1
            #print(wire5,'5')
            wiring=input("Add another wire? (y/n) ")
        if wirenum==6:
            wire6[:0]=wire
            wired+=1
            #print(wire6,'6')
            wiring=input("Add another wire? (y/n) ")
        if wirenum==7:
            wire7[:0]=wire
            wired+=1
            #print(wire7,'7')
            wiring=input("Add another wire? (y/n) ")
        if wirenum==8:
            wire8[:0]=wire
            wired+=1
            #print(wire8,'8')
            wiring=input("Add another wire? (y/n) ")
        if wirenum==9:
            wire9[:0]=wire
            wired+=1
            #print(wire9,'9')
            wiring=input("Add another wire? (y/n) ")
        if wirenum==10:
            wire10[:0]=wire
            wired+=1
            #print(wire10,'10')
            wiring=input("Add another wire? (y/n) ")
        if wired>=2:
            for e in range(0,2):
                #print(wire1[e],wire2[0],wire2[1])
                if wire1[e]==wire2[0] or wire1[e]==wire2[1]:
                    print("A letter is used more than once. Rewiring...")
                    rewireplugs()
            if wired>=3:
                for e in range(0,2):
                    #print(wire1[e],wire2[e],wire2[0],wire2[1],wire3[0],wire3[1])
                    if wire1[e]==wire2[0] or wire1[e]==wire2[1] or wire1[e]==wire3[0] or wire1[e]==wire3[1]:
                        print("A letter is used more than once. Rewiring...") 
                        rewireplugs()
                    if wire2[e]==wire3[0] or wire2[e]==wire3[1]:
                        print("A letter is used more than once. Rewiring...") 
                        rewireplugs()
                if wired>=4:
                    for e in range(0,2):
                        #print(wire1[e],wire2[e],wire2[0],wire2[1],wire3[0],wire3[1])
                        if wire1[e]==wire2[0] or wire1[e]==wire2[1] or wire1[e]==wire3[0] or wire1[e]==wire3[1] or wire1[e]==wire4[0] or wire1[e]==wire4[1]:
                            print("A letter is used more than once. Rewiring...") 
                            rewireplugs()
                        if wire2[e]==wire3[0] or wire2[e]==wire3[1] or wire2[e]==wire4[0] or wire2[e]==wire4[1]:
                            print("A letter is used more than once. Rewiring...") 
                            rewireplugs()
                        if wire3[e]==wire4[0] or wire3[e]==wire4[1]:
                            print("A letter is used more than once. Rewiring...") 
                            rewireplugs()
                    if wired>=5:
                        for e in range(0,2):
                            #print(wire1[e],wire2[e],wire2[0],wire2[1],wire3[0],wire3[1])
                            if wire1[e]==wire2[0] or wire1[e]==wire2[1] or wire1[e]==wire3[0] or wire1[e]==wire3[1] or wire1[e]==wire4[0] or wire1[e]==wire4[1] or wire1[e]==wire5[0] or wire1[e]==wire5[1]:
                                print("A letter is used more than once. Rewiring...") 
                                rewireplugs()
                            if wire2[e]==wire3[0] or wire2[e]==wire3[1] or wire2[e]==wire4[0] or wire2[e]==wire4[1] or wire2[e]==wire5[0] or wire2[e]==wire5[1]:
                                print("A letter is used more than once. Rewiring...") 
                                rewireplugs()
                            if wire3[e]==wire4[0] or wire3[e]==wire4[1] or wire3[e]==wire5[0] or wire3[e]==wire5[1]:
                                print("A letter is used more than once. Rewiring...") 
                                rewireplugs()
                            if wire4[e]==wire5[0] or wire4[e]==wire5[1]:
                                print("A letter is used more than once. Rewiring...") 
                                rewireplugs()
                        if wired>=6:
                            for e in range(0,2):
                                #print(wire1[e],wire2[e],wire2[0],wire2[1],wire3[0],wire3[1])
                                if wire1[e]==wire2[0] or wire1[e]==wire2[1] or wire1[e]==wire3[0] or wire1[e]==wire3[1] or wire1[e]==wire4[0] or wire1[e]==wire4[1] or wire1[e]==wire5[0] or wire1[e]==wire5[1] or wire1[e]==wire6[0] or wire1[e]==wire6[1]:
                                    print("A letter is used more than once. Rewiring...") 
                                    rewireplugs()
                                if wire2[e]==wire3[0] or wire2[e]==wire3[1] or wire2[e]==wire4[0] or wire2[e]==wire4[1] or wire2[e]==wire5[0] or wire2[e]==wire5[1] or wire2[e]==wire6[0] or wire2[e]==wire6[1]:
                                    print("A letter is used more than once. Rewiring...") 
                                    rewireplugs()
                                if wire3[e]==wire4[0] or wire3[e]==wire4[1] or wire3[e]==wire5[0] or wire3[e]==wire5[1] or wire3[e]==wire6[0] or wire3[e]==wire6[1]:
                                    print("A letter is used more than once. Rewiring...") 
                                    rewireplugs()
                                if wire4[e]==wire5[0] or wire4[e]==wire5[1] or wire4[e]==wire6[0] or wire4[e]==wire6[1]:
                                    print("A letter is used more than once. Rewiring...") 
                                    rewireplugs()
                                if wire5[e]==wire6[0] or wire5[e]==wire6[1]:
                                    print("A letter is used more than once. Rewiring...") 
                                    rewireplugs()
                            if wired>=7:
                                for e in range(0,2):
                                    #print(wire1[e],wire2[e],wire2[0],wire2[1],wire3[0],wire3[1])
                                    if wire1[e]==wire2[0] or wire1[e]==wire2[1] or wire1[e]==wire3[0] or wire1[e]==wire3[1] or wire1[e]==wire4[0] or wire1[e]==wire4[1] or wire1[e]==wire5[0] or wire1[e]==wire5[1] or wire1[e]==wire6[0] or wire1[e]==wire6[1] or wire1[e]==wire7[0] or wire1[e]==wire7[1]:
                                        print("A letter is used more than once. Rewiring...") 
                                        rewireplugs()
                                    if wire2[e]==wire3[0] or wire2[e]==wire3[1] or wire2[e]==wire4[0] or wire2[e]==wire4[1] or wire2[e]==wire5[0] or wire2[e]==wire5[1] or wire2[e]==wire6[0] or wire2[e]==wire6[1] or wire2[e]==wire7[0] or wire2[e]==wire7[1]:
                                        print("A letter is used more than once. Rewiring...") 
                                        rewireplugs()
                                    if wire3[e]==wire4[0] or wire3[e]==wire4[1] or wire3[e]==wire5[0] or wire3[e]==wire5[1] or wire3[e]==wire6[0] or wire3[e]==wire6[1] or wire3[e]==wire7[0] or wire3[e]==wire7[1]:
                                        print("A letter is used more than once. Rewiring...") 
                                        rewireplugs()
                                    if wire4[e]==wire5[0] or wire4[e]==wire5[1] or wire4[e]==wire6[0] or wire4[e]==wire6[1] or wire4[e]==wire7[0] or wire4[e]==wire7[1]:
                                        print("A letter is used more than once. Rewiring...") 
                                        rewireplugs()
                                    if wire5[e]==wire6[0] or wire5[e]==wire6[1] or wire5[e]==wire7[0] or wire5[e]==wire7[1]:
                                        print("A letter is used more than once. Rewiring...") 
                                        rewireplugs()
                                    if wire6[e]==wire7[0] or wire6[e]==wire7[1]:
                                        print("A letter is used more than once. Rewiring...") 
                                        rewireplugs()
                                if wired>=8:
                                    for e in range(0,2):
                                        #print(wire1[e],wire2[e],wire2[0],wire2[1],wire3[0],wire3[1])
                                        if wire1[e]==wire2[0] or wire1[e]==wire2[1] or wire1[e]==wire3[0] or wire1[e]==wire3[1] or wire1[e]==wire4[0] or wire1[e]==wire4[1] or wire1[e]==wire5[0] or wire1[e]==wire5[1] or wire1[e]==wire6[0] or wire1[e]==wire6[1] or wire1[e]==wire7[0] or wire1[e]==wire7[1] or wire1[e]==wire8[0] or wire1[e]==wire8[1]:
                                            print("A letter is used more than once. Rewiring...") 
                                            rewireplugs()
                                        if wire2[e]==wire3[0] or wire2[e]==wire3[1] or wire2[e]==wire4[0] or wire2[e]==wire4[1] or wire2[e]==wire5[0] or wire2[e]==wire5[1] or wire2[e]==wire6[0] or wire2[e]==wire6[1] or wire2[e]==wire7[0] or wire2[e]==wire7[1] or wire2[e]==wire8[0] or wire2[e]==wire8[1]:
                                            print("A letter is used more than once. Rewiring...") 
                                            rewireplugs()
                                        if wire3[e]==wire4[0] or wire3[e]==wire4[1] or wire3[e]==wire5[0] or wire3[e]==wire5[1] or wire3[e]==wire6[0] or wire3[e]==wire6[1] or wire3[e]==wire7[0] or wire3[e]==wire7[1] or wire3[e]==wire8[0] or wire3[e]==wire8[1]:
                                            print("A letter is used more than once. Rewiring...") 
                                            rewireplugs()
                                        if wire4[e]==wire5[0] or wire4[e]==wire5[1] or wire4[e]==wire6[0] or wire4[e]==wire6[1] or wire4[e]==wire7[0] or wire4[e]==wire7[1] or wire4[e]==wire8[0] or wire4[e]==wire8[1]:
                                            print("A letter is used more than once. Rewiring...") 
                                            rewireplugs()
                                        if wire5[e]==wire6[0] or wire5[e]==wire6[1] or wire5[e]==wire7[0] or wire5[e]==wire7[1] or wire5[e]==wire8[0] or wire5[e]==wire8[1]:
                                            print("A letter is used more than once. Rewiring...") 
                                            rewireplugs()
                                        if wire6[e]==wire7[0] or wire6[e]==wire7[1] or wire6[e]==wire8[0] or wire6[e]==wire8[1]:
                                            print("A letter is used more than once. Rewiring...") 
                                            rewireplugs()
                                        if wire7[e]==wire8[0] or wire7[e]==wire8[1]:
                                            print("A letter is used more than once. Rewiring...") 
                                            rewireplugs()
                                    if wired>=9:
                                        for e in range(0,2):
                                            #print(wire1[e],wire2[e],wire2[0],wire2[1],wire3[0],wire3[1])
                                            if wire1[e]==wire2[0] or wire1[e]==wire2[1] or wire1[e]==wire3[0] or wire1[e]==wire3[1] or wire1[e]==wire4[0] or wire1[e]==wire4[1] or wire1[e]==wire5[0] or wire1[e]==wire5[1] or wire1[e]==wire6[0] or wire1[e]==wire6[1] or wire1[e]==wire7[0] or wire1[e]==wire7[1] or wire1[e]==wire8[0] or wire1[e]==wire8[1] or wire1[e]==wire9[0] or wire1[e]==wire9[1]:
                                                print("A letter is used more than once. Rewiring...") 
                                                rewireplugs()
                                            if wire2[e]==wire3[0] or wire2[e]==wire3[1] or wire2[e]==wire4[0] or wire2[e]==wire4[1] or wire2[e]==wire5[0] or wire2[e]==wire5[1] or wire2[e]==wire6[0] or wire2[e]==wire6[1] or wire2[e]==wire7[0] or wire2[e]==wire7[1] or wire2[e]==wire8[0] or wire2[e]==wire8[1] or wire2[e]==wire9[0] or wire2[e]==wire9[1]:
                                                print("A letter is used more than once. Rewiring...") 
                                                rewireplugs()
                                            if wire3[e]==wire4[0] or wire3[e]==wire4[1] or wire3[e]==wire5[0] or wire3[e]==wire5[1] or wire3[e]==wire6[0] or wire3[e]==wire6[1] or wire3[e]==wire7[0] or wire3[e]==wire7[1] or wire3[e]==wire8[0] or wire3[e]==wire8[1] or wire3[e]==wire9[0] or wire3[e]==wire9[1]:
                                                print("A letter is used more than once. Rewiring...") 
                                                rewireplugs()
                                            if wire4[e]==wire5[0] or wire4[e]==wire5[1] or wire4[e]==wire6[0] or wire4[e]==wire6[1] or wire4[e]==wire7[0] or wire4[e]==wire7[1] or wire4[e]==wire8[0] or wire4[e]==wire8[1] or wire4[e]==wire9[0] or wire4[e]==wire9[1]:
                                                print("A letter is used more than once. Rewiring...") 
                                                rewireplugs()
                                            if wire5[e]==wire6[0] or wire5[e]==wire6[1] or wire5[e]==wire7[0] or wire5[e]==wire7[1] or wire5[e]==wire8[0] or wire5[e]==wire8[1] or wire5[e]==wire9[0] or wire5[e]==wire9[1]:
                                                print("A letter is used more than once. Rewiring...")
                                                rewireplugs()
                                            if wire6[e]==wire7[0] or wire6[e]==wire7[1] or wire6[e]==wire8[0] or wire6[e]==wire8[1] or wire6[e]==wire9[0] or wire6[e]==wire9[1]:
                                                print("A letter is used more than once. Rewiring...") 
                                            if wire7[e]==wire8[0] or wire7[e]==wire8[1] or wire7[e]==wire9[0] or wire7[e]==wire9[1]:
                                                print("A letter is used more than once. Rewiring...")
                                                rewireplugs()
                                            if wire8[e]==wire9[0] or wire8[e]==wire9[1]:
                                                print("A letter is used more than once. Rewiring...")
                                                rewireplugs()
                                        if wired>=10:
                                            for e in range(0,2):
                                                #print(wire1[e],wire2[e],wire2[0],wire2[1],wire3[0],wire3[1])
                                                if wire1[e]==wire2[0] or wire1[e]==wire2[1] or wire1[e]==wire3[0] or wire1[e]==wire3[1] or wire1[e]==wire4[0] or wire1[e]==wire4[1] or wire1[e]==wire5[0] or wire1[e]==wire5[1] or wire1[e]==wire6[0] or wire1[e]==wire6[1] or wire1[e]==wire7[0] or wire1[e]==wire7[1] or wire1[e]==wire8[0] or wire1[e]==wire8[1] or wire1[e]==wire9[0] or wire1[e]==wire9[1] or wire1[e]==wire10[0] or wire1[e]==wire10[1]:
                                                    print("A letter is used more than once. Rewiring...") 
                                                    rewireplugs()
                                                if wire2[e]==wire3[0] or wire2[e]==wire3[1] or wire2[e]==wire4[0] or wire2[e]==wire4[1] or wire2[e]==wire5[0] or wire2[e]==wire5[1] or wire2[e]==wire6[0] or wire2[e]==wire6[1] or wire2[e]==wire7[0] or wire2[e]==wire7[1] or wire2[e]==wire8[0] or wire2[e]==wire8[1] or wire2[e]==wire9[0] or wire2[e]==wire9[1] or wire2[e]==wire10[0] or wire2[e]==wire10[1]:
                                                    print("A letter is used more than once. Rewiring...") 
                                                    rewireplugs()
                                                if wire3[e]==wire4[0] or wire3[e]==wire4[1] or wire3[e]==wire5[0] or wire3[e]==wire5[1] or wire3[e]==wire6[0] or wire3[e]==wire6[1] or wire3[e]==wire7[0] or wire3[e]==wire7[1] or wire3[e]==wire8[0] or wire3[e]==wire8[1] or wire3[e]==wire9[0] or wire3[e]==wire9[1] or wire3[e]==wire10[0] or wire3[e]==wire10[1]:
                                                    print("A letter is used more than once. Rewiring...") 
                                                    rewireplugs()
                                                if wire4[e]==wire5[0] or wire4[e]==wire5[1] or wire4[e]==wire6[0] or wire4[e]==wire6[1] or wire4[e]==wire7[0] or wire4[e]==wire7[1] or wire4[e]==wire8[0] or wire4[e]==wire8[1] or wire4[e]==wire9[0] or wire4[e]==wire9[1] or wire4[e]==wire10[0] or wire4[e]==wire10[1]:
                                                    print("A letter is used more than once. Rewiring...")
                                                    rewireplugs()
                                                if wire5[e]==wire6[0] or wire5[e]==wire6[1] or wire5[e]==wire7[0] or wire5[e]==wire7[1] or wire5[e]==wire8[0] or wire5[e]==wire8[1] or wire5[e]==wire9[0] or wire5[e]==wire9[1] or wire5[e]==wire10[0] or wire5[e]==wire10[1]:
                                                    print("A letter is used more than once. Rewiring...")
                                                    rewireplugs()
                                                if wire6[e]==wire7[0] or wire6[e]==wire7[1] or wire6[e]==wire8[0] or wire6[e]==wire8[1] or wire6[e]==wire9[0] or wire6[e]==wire9[1] or wire6[e]==wire10[0] or wire6[e]==wire10[1]:
                                                    print("A letter is used more than once. Rewiring...")
                                                    rewireplugs()
                                                if wire7[e]==wire8[0] or wire7[e]==wire8[1] or wire7[e]==wire9[0] or wire7[e]==wire9[1] or wire7[e]==wire10[0] or wire7[e]==wire10[1]:
                                                    print("A letter is used more than once. Rewiring...")
                                                    rewireplugs()
                                                if wire8[e]==wire9[0] or wire8[e]==wire9[1] or wire8[e]==wire10[0] or wire8[e]==wire10[1]:
                                                    print("A letter is used more than once. Rewiring...")
                                                    rewireplugs()
                                                if wire9[e]==wire10[0] or wire9[e]==wire10[1]:
                                                    print("A letter is used more than once. Rewiring...")
                                                    rewireplugs()
                
        if wirenum>10:
            rewire=input("All wires used. Would you like to rewire them? (y/n) ")
            if rewire=="y":
                rewireplugs()
            else:
                displayplugs()
    #displayplugs()
    
def rewireplugs():
    global wirenum
    global wire1,wire2,wire3,wire4,wire5,wire6,wire7,wire8,wire9,wire10
    wirenum=0
    wire1,wire2,wire3,wire4,wire5,wire6,wire7,wire8,wire9,wire10=[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]
    plugboardsetup()
    
def displayplugs():
    plug="{:>3}-{:<3}{:>3}-{:<3}{:>3}-{:<3}{:>3}-{:<3}{:>3}-{:<3}{:>3}-{:<3}{:>3}-{:<3}{:>3}-{:<3}{:>3}-{:<3}{:>3}-{:<3}"
    plugout=plug.format(wire1[0],wire1[1],wire2[0],wire2[1],wire3[0],wire3[1],wire4[0],wire4[1],wire5[0],wire5[1],wire6[0],wire6[1],wire7[0],wire7[1],wire8[0],wire8[1],wire9[0],wire9[1],wire10[0],wire10[1])
    plugout=plugout.upper()
    print(plugout)
    
def plugboard():
    for s in range(len(messagelist)):
        w=0
        if messagelist[s]==wire1[0] or messagelist[s]==wire1[1]:
            if messagelist[s]==wire1[0] and w!=1:
                messagelist[s]=wire1[1]
                w+=1
                #print(messagelist[s],wire1[1])
            if messagelist[s]==wire1[1] and w!=1:
                messagelist[s]=wire1[0]
                w+=1
                #print(messagelist[s],wire1[0])
        if messagelist[s]==wire2[0] or messagelist[s]==wire2[1]:
            if messagelist[s]==wire2[0] and w!=1:
                messagelist[s]=wire2[1]
                w+=1
            if messagelist[s]==wire2[1] and w!=1:
                messagelist[s]=wire2[0]
                w+=1
        if messagelist[s]==wire3[0] or messagelist[s]==wire3[1]:
            if messagelist[s]==wire3[0] and w!=1:
                messagelist[s]=wire3[1]
                w+=1
            if messagelist[s]==wire3[1] and w!=1:
                messagelist[s]=wire3[0]
                w+=1
        if messagelist[s]==wire4[0] or messagelist[s]==wire4[1]:
            if messagelist[s]==wire4[0] and w!=1:
                messagelist[s]=wire4[1]
                w+=1
            if messagelist[s]==wire4[1] and w!=1:
                messagelist[s]=wire4[0]
                w+=1
        if messagelist[s]==wire5[0] or messagelist[s]==wire5[1]:
            if messagelist[s]==wire5[0] and w!=1:
                messagelist[s]=wire5[1]
                w+=1
            if messagelist[s]==wire5[1] and w!=1:
                messagelist[s]=wire5[0]
                w+=1
        if messagelist[s]==wire6[0] or messagelist[s]==wire6[1]:
            if messagelist[s]==wire6[0] and w!=1:
                messagelist[s]=wire6[1]
                w+=1
            if messagelist[s]==wire6[1] and w!=1:
                messagelist[s]=wire6[0]
                w+=1
        if messagelist[s]==wire7[0] or messagelist[s]==wire7[1]:
            if messagelist[s]==wire7[0] and w!=1:
                messagelist[s]=wire7[1]
                w+=1
            if messagelist[s]==wire7[1] and w!=1:
                messagelist[s]=wire7[0]
                w+=1
        if messagelist[s]==wire8[0] or messagelist[s]==wire8[1]:
            if messagelist[s]==wire8[0] and w!=1:
                messagelist[s]=wire8[1]
                w+=1
            if messagelist[s]==wire8[1] and w!=1:
                messagelist[s]=wire8[0]
                w+=1
        if messagelist[s]==wire9[0] or messagelist[s]==wire9[1]:
            if messagelist[s]==wire9[0] and w!=1:
                messagelist[s]=wire9[1]
                w+=1
            if messagelist[s]==wire9[1] and w!=1:
                messagelist[s]=wire9[0]
                w+=1
        if messagelist[s]==wire10[0] or messagelist[s]==wire10[1]:
            if messagelist[s]==wire10[0] and w!=1:
                messagelist[s]=wire10[1]
                w+=1
            if messagelist[s]==wire10[1] and w!=1:
                messagelist[s]=wire10[0]
                w+=1
    #print(messagelist)

def outplugboard():
    for s in range(len(finmessage)):
        w=0
        if finmessage[s]==wire1[0] or finmessage[s]==wire1[1]:
            if finmessage[s]==wire1[0] and w!=1:
                finmessage[s]=wire1[1]
                w+=1
                #print(finmessage[s],wire1[1])
            if finmessage[s]==wire1[1] and w!=1:
                finmessage[s]=wire1[0]
                w+=1
                #print(finmessage[s],wire1[0])
        if finmessage[s]==wire2[0] or finmessage[s]==wire2[1]:
            if finmessage[s]==wire2[0] and w!=1:
                finmessage[s]=wire2[1]
                w+=1
            if finmessage[s]==wire2[1] and w!=1:
                finmessage[s]=wire2[0]
                w+=1
        if finmessage[s]==wire3[0] or finmessage[s]==wire3[1]:
            if finmessage[s]==wire3[0] and w!=1:
                finmessage[s]=wire3[1]
                w+=1
            if finmessage[s]==wire3[1] and w!=1:
                finmessage[s]=wire3[0]
                w+=1
        if finmessage[s]==wire4[0] or finmessage[s]==wire4[1]:
            if finmessage[s]==wire4[0] and w!=1:
                finmessage[s]=wire4[1]
                w+=1
            if finmessage[s]==wire4[1] and w!=1:
                finmessage[s]=wire4[0]
                w+=1
        if finmessage[s]==wire5[0] or finmessage[s]==wire5[1]:
            if finmessage[s]==wire5[0] and w!=1:
                finmessage[s]=wire5[1]
                w+=1
            if finmessage[s]==wire5[1] and w!=1:
                finmessage[s]=wire5[0]
                w+=1
        if finmessage[s]==wire6[0] or finmessage[s]==wire6[1]:
            if finmessage[s]==wire6[0] and w!=1:
                finmessage[s]=wire6[1]
                w+=1
            if finmessage[s]==wire6[1] and w!=1:
                finmessage[s]=wire6[0]
                w+=1
        if finmessage[s]==wire7[0] or finmessage[s]==wire7[1]:
            if finmessage[s]==wire7[0] and w!=1:
                finmessage[s]=wire7[1]
                w+=1
            if finmessage[s]==wire7[1] and w!=1:
                finmessage[s]=wire7[0]
                w+=1
        if finmessage[s]==wire8[0] or finmessage[s]==wire8[1]:
            if finmessage[s]==wire8[0] and w!=1:
                finmessage[s]=wire8[1]
                w+=1
            if finmessage[s]==wire8[1] and w!=1:
                finmessage[s]=wire8[0]
                w+=1
        if finmessage[s]==wire9[0] or finmessage[s]==wire9[1]:
            if finmessage[s]==wire9[0] and w!=1:
                finmessage[s]=wire9[1]
                w+=1
            if finmessage[s]==wire9[1] and w!=1:
                finmessage[s]=wire9[0]
                w+=1
        if finmessage[s]==wire10[0] or finmessage[s]==wire10[1]:
            if finmessage[s]==wire10[0] and w!=1:
                finmessage[s]=wire10[1]
                w+=1
            if finmessage[s]==wire10[1] and w!=1:
                finmessage[s]=wire10[0]
                w+=1
    #print(messagelist)

setting=0
messagelist=[]
wirenum=0
wire1,wire2,wire3,wire4,wire5,wire6,wire7,wire8,wire9,wire10=[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]
s1list=[]
rotorturn,rotorturn2,rotorturn3,rotorturn4,rotorturn5=0,0,0,0,0
dr1,dr2,dr3,dr4,dr5=1,1,1,1,1
rotorlist=[]
finmessage=[]
rotorimport()
setrotors()
plugboardsetup()
displayrotors()
displayplugs()
inputmessage()
outplugboard()
#rotateRotors()
displayrotors()
displayplugs()
encoded=''.join(finmessage)
print("ENCODED/DECODED MESSAGE:",encoded)


