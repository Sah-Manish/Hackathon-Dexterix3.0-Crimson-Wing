from tkinter import *
from tkinter import font
from tkinter.font import Font
from tkinter import messagebox
# Main window of the Meeting Schedular API
root=Tk()
root.geometry('1920x800')
root.title("Meeting Schedular -By Crimson Wing")
# Declaring Variables
headingFont=Font(family="Times New Roman",size=42)
subHeadingFont=Font(family="Times New Roman",size=20)
buttonFont=Font(family="Times New Roman",size=12)
meetingLength=0000
def meetingSchedule(l1,finalList):
    for i in range(0,len(l1)-1):
        if(l1[i][1]>=l1[i+1][0]):
            if(l1[i][1]>=l1[i+1][1]):
                arr=[l1[i][0],l1[i][1]]
                finalList.append(arr)
            else:
                arr=[l1[i][0],l1[i+1][1]]
                finalList.append(arr)              
        else:
            arr=[l1[i][0],l1[i][1]]
            finalList.append(arr)
    finalList.remove([0,0])
# Shows Schedule of A
def ScheduleOfA():
    global subHeadingFont,root
    with open("ScheduleOfA.txt","r") as f1: 
        a=f1.readline()
        x=a.split(",")
        yaxisforA=200
        for i in x:
            tempLabel=Label(root,text=i,font=subHeadingFont).place(x=175,y=yaxisforA+50)
            yaxisforA+=50
        #f2.write(str(int(x[0])+1))
# Shows Schedule of B
def ScheduleOfB():
    global subHeadingFont,root
    with open("ScheduleOfB.txt","r") as f1:  
        a=f1.readline()
        x=a.split(",")
        yaxisforB=200
        for i in x:
            tempLabel=Label(root,text=i,font=subHeadingFont).place(x=475,y=yaxisforB+50)
            yaxisforB+=50
# function made for Valid slots function to read and display valid slots
def readAvailableSlots():
    with open("AvailableSLotsForA.txt","r") as f1:  
        a=f1.readline()
        x=a.split(",")
        titleA=Label(root,text="Valid Empty Slots of A",font=subHeadingFont).place(x=775,y=250)            
        yaxisforB=250
        for i in x:
            tempLabel=Label(root,text=i,font=subHeadingFont).place(x=775,y=yaxisforB+50)
            yaxisforB+=50
    with open("AvailableSLotsForB.txt","r") as f1:  
        a=f1.readline()
        x=a.split(",")
        titleA=Label(root,text="Valid Empty Slots of B",font=subHeadingFont).place(x=1075,y=250)
        yaxisforB=250
        for i in x:
            tempLabel=Label(root,text=i,font=subHeadingFont).place(x=1075,y=yaxisforB+50)
            yaxisforB+=50
# View Valid slots from both parties schedules







def ValidSlots():
    global subHeadingFont,root,meetingLength
    if(int(meetingLength)!=0000 and int(meetingLength)<2400):
        #code to generate available slot file

        with open("ScheduleOfA.txt","r") as f1:
            with open("AvailableSLotsForA.txt","w") as f2:
                x=f1.readline()
                listA=x.split(",")
                x1=[i.split("-") for i in listA]
                x=""
                for i in range(len(listA)-1):
                    if(int(x1[i+1][0])-int(x1[i][1]) > meetingLength):
                        x+= x1[i][1]+"-"+x1[i+1][0]+","
                f2.write(x)
                x=""
        with open("ScheduleOfB.txt","r") as f1:
            with open("AvailableSLotsForB.txt","w") as f2:
                x=f1.readline()
                listA=x.split(",")
                x1=[i.split("-") for i in listA]
                x=""
                for i in range(len(listA)-1):
                    if(int(x1[i+1][0])-int(x1[i][1]) > meetingLength):
                        x+= x1[i][1]+"-"+x1[i+1][0]+","
                f2.write(x)
                x=""
        #code to display available slot
        readAvailableSlots()
    else:
        messagebox.askretrycancel("Meeting Length Error","Please Enter Meeting Length")








# Meeting length Getting from user
def getMeetingLength():
    global meetingLength
    meetingLength=int(e1.get())
    if(int(meetingLength)!=0000 and int(meetingLength)<2400):
        info=str(meetingLength)+" Hrs. is the duration of Meeting."
        messagebox.showinfo("Duration of Meeting",info)
        return
    else:
        messagebox.showwarning("Meeting Length Error","Meeting Length cannot be zero")
 
# Generate slots for Meeting possible....... V. Imp
def generateSlots():
    global subHeadingFont,root,meetingLength
    print(meetingLength)
    l1=[]
    l2=[]
    with open("AvailableSlotsForA.txt","r") as a1:
        a=a1.readline()
        temp1=a.split(",")
        for i in range(len(temp1)-1):
            x=temp1[i].split("-")
            arr=[]
            print(x)
            arr.append(int(x[0]))
            arr.append(int(x[1]))
            l1.append(arr)
    with open("AvailableSlotsForB.txt","r") as b1:
        b=b1.readline()
        temp2=b.split(",")
        for i in range(len(temp1)-1):
            x=temp1[i].split("-")
            arr=[]
            print(x)
            arr.append(int(x[0]))
            arr.append(int(x[1]))
            l2.append(arr)
            
    l3=l1+l2
    l3.sort()
    # final blow to list to get all sorted out our free time expenses
    #main code  
    slotForFreeTime=[]
    timespan=[]
    finalList=[[0]*2]*(len(slotForFreeTime)+1)
    # getting time length of all free time
    for i in l3:
        x=int(i[1]-i[0])
        timespan.append(x)
    # adding valid free slotForFreeTime to valid meeting time
    for i in range(0,len(l3)):
        if(timespan[i]>meetingLength):
            slotForFreeTime.append(l3[i])
    # printing our main lists after all calculations
    meetingSchedule(slotForFreeTime,finalList)
    print("Final List for output")
    print(finalList)
    data=""
    for i in range(0,len(finalList)):
        x=str(finalList[i][0])+"-"+str(+finalList[i][1])+","
        data+=x
    # finalMeetingSchedule.txt       final support file name for meeting file
    with open("finalMeetingSchedule.txt","w") as ms:
        ms.write(data)
    # Dimension of Screen 1920x1080
    #global subHeadingFont,root,meetingLength
    if(int(meetingLength)!=0000 and int(meetingLength)<2400):
        with open("finalMeetingSchedule.txt","r") as f1:  
            a=f1.readline()
            x=a.split(",")
            xaxisline1=450+425
            xaxisline2=450+425
            for i in x:
                if(xaxisline1<1400):
                    tempLabel=Label(root,text=i,font=subHeadingFont).place(x=xaxisline1+50,y=650)
                    xaxisline1+=150
                else:
                    tempLabel=Label(root,text=i,font=subHeadingFont).place(x=xaxisline2+50,y=750)
                    xaxisline2+=150
    else:
        messagebox.askretrycancel("Meeting Length Error","Please Enter Meeting Length")
        return
# Main Screen View Coding
label=Label(root,text="Meeting Schedular",font=headingFont).pack()
label=Label(root,text="-Made by Crimson Wing Team",font=subHeadingFont).pack()
# Main Buttons
buttonA=Button(root, text='Show Schedule of A',width=40,height=5,font=buttonFont,command=ScheduleOfA).place(x=75,y=120)
buttonB=Button(root, text='Show Schedule of B',width=40,height=5,font=buttonFont,command=ScheduleOfB).place(x=375,y=120)
buttonToShowFreeValidSlots=Button(root,text="Show Valid Available Slots....",width=60,height=5,font=buttonFont,command=ValidSlots).place(x=775,y=120)
# Meeting length Entry
meetingLengthLabel=Label(root,text="Enter Meeting Duration (in 2400 Hrs.)",font=subHeadingFont).place(x=25,y=600)
e1=Entry(root,borderwidth=5,width=50)
e1.place(x=60,y=650)
e1.insert(0,0000)
acceptButton=Button(root,text="Submit",font=buttonFont,width=30,height=5,command=getMeetingLength).place(x=25,y=700)
# generate meeting available Slots
generateSchedule=Button(root,text="Generate Available Slots....",width=50,height=5,font=buttonFont,command=generateSlots).place(x=450,y=650)
root.mainloop()
