import os
import csv
import msvcrt as m
import time
import datetime
import tkinter
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter.scrolledtext import *
from tkinter import messagebox
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile

def main(): #(2 επιλογές: Είσοδος στο σύστημα - Έξοδος-->τερματισμός προγ/τος), να επιχειρήσω να δηλώνω ΕΔΩ όλα τα Frames του προγράμματος και να τα κάνω GLOBAL!!!
    global root
    global mainFrame
    global updateFlag
    global miss
    global false
    global status2
    global status3
    global status5
    root=Tk()
    miss=0
    false=0 
    updateFlag=0
    status2=""
    status3=""
    status5=""
    photo = PhotoImage(file = "art_flower_pic_1.png") #window icon
    root.iconphoto(False, photo)  
    root.state('zoomed')  #full screen window'''
    root.option_add("*Button.Background", "red") #attribute για όλα τα Buttons
    root.option_add("*Button.Foreground", "#ffffff")  #attribute για όλα τα Buttons
    root.option_add("*Button.cursor", "hand2")  #attribute για όλα τα Buttons, cursor="hand2" --> cursor: pointer   
    my_img=ImageTk.PhotoImage(Image.open("unesco_logo_2.jpg"))
    my_label=Label(image=my_img, bg="red", bd=0)
    my_label.grid(row=0, column=0, columnspan=2)
    my_img2=ImageTk.PhotoImage(Image.open("espaLogo_3.jpg"))
    my_label2=Label(image=my_img2, bg="red", bd=0) 
    my_label2.grid(row=0, column=17, columnspan=2)
    root.title("Όμιλος για την Unesco Πειραιώς και Νήσων - Πρόγραμμα παρακολούθησης και διαχείρισης δελτίων ανεργίας - UcM - Unemployment Cards Manager v.1.06.2 (Υφιστάμενη δομή)") #Υφιστάμενη δομή
    #root.title("Όμιλος για την Unesco Πειραιώς και Νήσων - Πρόγραμμα παρακολούθησης και διαχείρισης δελτίων ανεργίας - UcM - Unemployment Cards Manager v.1.06.2 (Νέα δομή)") #Υφιστάμενη δομή   
    label00= Label(root, bg="#00b3b3", fg="#ffffff", padx=0, pady=34, text="Όμιλος για την Unesco Πειραιώς και Νήσων", font=('bold', 19), bd=3)
    label00.grid(row=0, column=2, columnspan=15, sticky=W+E, pady=0)
    #label01= Label(root,  fg="#00b3b3", pady=0, padx=5, text="UcM", font=('bold', 50), bd=0)#bg="red"
    #label01.grid(row=1, column=7, sticky=E, pady=0)
    my_img5=ImageTk.PhotoImage(Image.open("art_flower_pic_2.png"))
    my_label=Label(image=my_img5, bg="red", bd=0)
    my_label.grid(row=1, column=7, sticky=E, pady=0)
    label01= Label(root,  fg="red", pady=0, padx=5, text=" Unemployment Cards Manager", font=('bold', 20), bd=0)#bg="red"
    label01.grid(row=1, column=8, sticky=W+E, pady=0)    
    label02= Label(root, padx=5, text="Πρόγραμμα παρακολούθησης και διαχείρισης δελτίων ανεργίας", font=('bold', 13), bd=5)#bg="red"fg="red", 
    label02.grid(row=2, column=0, columnspan=18, sticky=W+E, pady=0)    
    label= Label(root, padx=455, text="UcM - Unemployment Cards Manager v.1.06.2  - powered by Python v.3.10.5") #padx=511,bg="red"fg="red", 
    label.grid(row=3, column=0, columnspan=18, sticky=N, pady=0)   
    mainFrame=LabelFrame(root, padx=5, pady=5, bd=0)
    mainFrame.grid(row=5, column=0, columnspan=18)
    enterSystem=Button(mainFrame, text="Είσοδος στο σύστημα", padx=20, pady=11, command=logIn)    
    enterSystem.grid(row=5, column=2, pady=65, padx=35)
    root.bind('<Return>', lambda event: logIn())  #binding '<Enter>' key to function logIn()--> σαν να συνδέσαμε δηλαδή το '<Enter>' key με το κουμπί εισόδου>.
    exitSystem=Button(mainFrame, text="Έξοδος", padx=59, pady=11, command=greetings)
    exitSystem.grid(row=5, column=3, pady=65, padx=35)
    info=Button(mainFrame, text="Contact Service", padx=37, pady=11, command=fire)
    info.grid(row=5, column=4, pady=65, padx=35)
    image4 = Image.open("art_flower_pic_1.png")
    photo4 = ImageTk.PhotoImage(image4)
    shery_pic = Label(mainFrame, image = photo4, bd=0)
    shery_pic.image = photo4
    shery_pic.grid(row=9, column=0, columnspan=52, pady=15)      
    root.bind('<Escape>', lambda event: root.destroy())
    root.bind('<F11>', lambda event: goto(123))    
    root.mainloop()

def fire(): #μήνυμα στοιχείων επικοινωνίας για service.
    messagebox.showinfo('Service - Πληροφορίες επικοινωνίας:', 'Programmer / Designer/ Developer:\n\nShery Panagiotaki\n\n\n\nContact info:\n\nTel.: (+30) 6976929404\n\nE-mail: sherypanagiotaki@yahoo.com,\n             sherypamagiotaki@gmail.com')

def greetings(): #μήνυμα τερματισμού του προγ/τος (το πρόγραμμα σε αυτό το σημείο είναι ανενεργό αλλά το παράθυρό του (root()) κλείνει ΜΟΝΟ με κλικ στο κουμπί "Κλείσιμο παράθυρου")
    global finish
    global Frame0
    global x
    global status
    status=1
    mainFrame.grid_forget()
    Frame0=LabelFrame(root, bd=0)
    Frame0.grid(row=4, column=0, columnspan=18)  
    label0= Label(Frame0, text="Ευχαριστούμε πολύ που χρησιμοποιήσατε την εφαρμογή!\n\nProgrammed, designed and developed by Shery Panagiotaki, @copyright 2022\n\n\nContact info:\n\nTel.: (+30) 6976929404\n\nE-mail: sherypanagiotaki@yahoo.com,\n             sherypamagiotaki@gmail.com", bd=0)
    label0.grid(row=700, column=0, columnspan=18, pady=15, sticky=W+E)
    Frame00=LabelFrame(Frame0, bd=0)
    Frame00.grid(row=15, column=0, columnspan=18)
    image4 = Image.open("art_flower_pic_1.jpg")
    photo4 = ImageTk.PhotoImage(image4)
    shery_pic = Label(Frame0, image = photo4, bd=0)
    shery_pic.image = photo4
    shery_pic.grid(row=9, column=0, columnspan=52, pady=15)    
    finish=Button(Frame0, text="Κλείσιμο παράθυρου", padx=22, pady=11, command=lambda: root.destroy()) 
    restart=Button(Frame0, text="Επανείσοδος", padx=42, pady=11, command=lambda: goto(123))
    info=Button(Frame0, text="Contact Service", padx=37, pady=11, command=fire)
    restart.grid(row=16, column=8, padx=35, pady=35)
    finish.grid(row=16, column=9, padx=35, pady=35)
    info.grid(row=16, column=10, padx=35, pady=35)    
    if currentDate()[-2:]in ['01', '15', '30']:  #--> ενημέρωση αντιγράφων ασφαλείας κάθε 1η, 15η, και 30η αυτόματα στο τέλος του προγ/τος (θα γίνεται και μέσω χρήστη)
        restart.grid(row=16, column=8, padx=65, pady=35)
        finish.grid(row=16, column=9, padx=65, pady=35)
        status=0
        goto(3)
    else:
        backupButton=Button(Frame0, text="Αντίγραφα ασφαλείας", padx=16, pady=11, command=lambda: goto(3))
        backupButton.grid(row=16, column=7, padx=35, pady=35)
        message="Δεν έγινε αυτόματη ενημέρωση των αντιγράφων ασφαλείας."
        messagebox.showwarning('Σημαντικό:', message)            
       
def logIn(): #Είσοδος στο πρόγραμμα
    global checkLogin
    global Frame1    
    mainFrame.grid_forget()
    checkLogin=[]
    checkIn=[]
    if false>0:       
        Frame11.grid_forget()
    with open("password.csv", "r", newline="", encoding="utf-8") as file:
        ro=csv.reader(file, delimiter='$')
        for row in ro:
            checkLogin.append(row)
        if len(checkLogin)==0:
            messagebox.showerror('Σφάλμα:', "Παρακαλώ πολύ επικοινωνήστε με την προγραμματίστρια, κωδικός σφάλματος: EMPTY_PASSWORD_0" )
            finish=Button(root, text="Έξοδος", padx=74, pady=10, command=root.destroy())
            finish.grid(row=7, column=3, pady=15)             
        else:
            global enterUsername2
            global enterPassword2
            global submit            
            Frame1=LabelFrame(root, pady=10, bd=0)
            Frame1.grid(row=5, column=0, columnspan=18, padx=5, pady=20)
            enterUsername1=Label(Frame1, text="Username: ", pady=15, fg="red")
            enterUsername1.grid(row=6, column=4)
            enterUsername2=Entry(Frame1, width=50, bg= "#d9d9d9", borderwidth=5)
            enterUsername2.grid(row=6, column=5)
            enterPassword1=Label(Frame1, text="Password: ", pady=15, fg="red")
            enterPassword1.grid(row=7, column=4)
            enterPassword2=Entry(Frame1, width=50, bg= "#d9d9d9", borderwidth=5)
            enterPassword2.grid(row=7, column=5)                           
            submit=Button(Frame1, text="Υποβολή", padx=45, pady=10, command=lambda: checkMiss(miss, checkLogin)) 
            submit.grid(row=8, column=0, columnspan=9, pady=15)
            root.bind('<Return>', lambda event: checkMiss(miss, checkLogin))
            choice2=enterUsername2.get()
            choice2=choice2.strip()
            choice3=enterPassword2.get()
            choice3=choice3.strip()

def checkMiss(miss, checkLogin): #βοηθητική function της logIn(), παίρνει 2 παραμέτρους, miss--> αρ. αποτυχημένων προσπαθειών και checkLogin--> λίστα με κωδικούς εισόδου                              
    choice2=enterUsername2.get()
    choice2=choice2.strip()
    choice3=enterPassword2.get()
    choice3=choice3.strip()
    checkIn=[choice2.upper(), choice3.upper()]
    root.unbind('<Return>') #unbinding the '<Enter>' key.
    for x in checkLogin:
        if checkIn==x:            
            goto(2)
            #goto(1) #εκτύπωση μηνύματος επιτυχίας και αναμονή για είσοδο του χρήστη στο κεντρικό μενού
            break
        elif x==checkLogin[-1]: #τρεις προσπάθειες εισόδου αλλιώς τερματισμός του προγ/τος.            
            Frame1.grid_forget()
            submit.grid_forget()
            global Frame11
            global false  
            Frame11=LabelFrame(root, bd=0)
            Frame11.grid(row=4, column=0, columnspan=18)
            if false==2:
                close=Button(Frame11, text="Κλείσιμο παραθύρου", padx=22, pady=11, command=lambda: root.destroy()) 
                close.grid(row=60,  column=8, padx=65, pady=45)
                restart=Button(Frame11, text="Επανείσοδος", padx=42, pady=11, command=lambda: goto(123))             
                restart.grid(row=60, column=9, padx=65, pady=45)                
                messagebox.showerror('Σφάλμα:', "Λανθασμένοι κωδικοί χρήστη, το πρόγραμμα τερματίστηκε.\n\n\nProgrammed, designed and developed by Shery Panagiotaki, @copyright 2022")
                hello=Label(Frame11, text="UcM - Unemployment Cards Manager v.1.02.3\nProgrammed, designed and developed by Shery Panagiotaki, @copyright 2022", pady=15)             
                hello.grid(row=100, column=0, columnspan=18) 
            else:
                tryAgain=Button(Frame11, text="Επανάληψη", padx=30, pady=11, command=logIn) 
                tryAgain.grid(row=60, column=8, padx=65, pady=45)
                finish=Button(Frame11, text="Έξοδος", padx=50, pady=11, command=greetings) 
                finish.grid(row=60, column=9, padx=65, pady=45)                
                false=false+1
                miss=false
                Frame1.grid_forget()
                if false==2:                    
                    tries="Απομένει μία προσπάθεια."
                else:
                    tries="Απομένουν δύο προσπάθειες."
                messagebox.showwarning('Σφάλμα:', tries)
                
def goto(x):
    global Frame2
    if x==1:
        miss=0
        Frame1.grid_forget()
        Frame2.grid_forget()
        greetings()
    elif x==2:
        Frame1.grid_forget()
        show1()
        messagebox.showinfo('Κωδικός αποδεκτός', 'Επιτυχημένη είσοδος στο σύσημα')        
    elif x==3: #ενημέρωση αντιγράφων ασφαλείας
        global message
        global copyPrevious
        global copyCurrent
        global copyFuture
        global copyPast
        global copyPassword
        copyPrevious=[]
        copyCurrent=[]
        copyFuture=[]
        copyPast=[]
        copyPassword=[]
        with open("previous.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for i in ro:
                copyPrevious.append(i)
            with open("..\\..\\backup_previous.csv", "w", encoding="utf-8", newline="") as file:
                wo=csv.writer(file, delimiter='$')
                for i in copyPrevious:
                    wo.writerow(i)                    
        with open("current.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for i in ro:
                copyCurrent.append(i)                  
            with open("..\\..\\backup_current.csv", "w", encoding="utf-8", newline="") as file:
                wo=csv.writer(file, delimiter='$')
                for i in copyCurrent:
                    wo.writerow(i)
        with open("future.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for i in ro:
                copyFuture.append(i)                  
            with open("..\\..\\backup_future.csv", "w", encoding="utf-8", newline="") as file:
                wo=csv.writer(file, delimiter='$')
                for i in copyFuture:
                    wo.writerow(i)
        with open("past.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for i in ro:
                copyPast.append(i)                  
            with open("..\\..\\backup_past.csv", "w", encoding="utf-8", newline="") as file:
                wo=csv.writer(file, delimiter='$')
                for i in copyPast:
                    wo.writerow(i)
        with open("password.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for i in ro:
                copyPassword.append(i)
            if len(copyPassword)==0:
                message="Παρακαλώ πολύ επικοινωνήστε με την προγραμματίστρια, κωδικός σφάλματος: EMPTY_PASSWORD_0"
                messagebox.showwarning('Σφάλμα:', message)
            else:
                with open("..\\..\\backup_password.csv", "w", encoding="utf-8", newline="") as file:
                    wo=csv.writer(file, delimiter='$')
                    for i in copyPassword:
                        wo.writerow(i)
                    if status ==0:
                        message="Αυτόματη ενημέρωση αντιγράφων ασφαλείας: επιτυχής."
                    else:
                        message="Ενημέρωση αντιγράφων ασφαλείας: επιτυχής."
                    messagebox.showinfo('Σημαντικό:', message)
    elif x==4: #<<Επιστροφή στο κεντρικό μενού μετά από την προβολή των ενεργών δελτίων ή από τη φόρμα νέας εγγραφής.
        global Frame13
        Frame13.grid_forget()
        menu()
    elif x==5: #διορθωση κάρτας ανεργίας
        global Frame14
        Frame14.grid_forget()
        show1()
    elif x==6: #εμφάνιση ενεργών χρηστών και δελτίων που εχει ανοίξει το παράθυρό τους για ανανέωση. 
        global activeList
        Frame14=LabelFrame(root, bd=0)
        ektyposi1(Frame14, activeList)              
    elif x==7: #οριστική υποβολή ανανέωσης κάρτας ανεργίας
        Frame14=LabelFrame(root,bd=0)
        Frame14.grid(row=6, column=0, columnspan=18)
        activeLabel=Label(Frame14, text="ΕΝΕΡΓΑ ΔΕΛΤΙΑ ΑΝΕΡΓΙΑΣ ΠΟΥ ΕΧΕΙ ΑΝΟΙΞΕΙ ΤΟ ΠΑΡΑΘΥΡΟ ΓΙΑ ΑΝΑΝΕΩΣΗ", pady=25, fg="red", bg="#d9d9d9")
        activeLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        ektyposi1(Frame14, today)
    elif x==8: #μετάβαση στο κεντρικό μενού μετά από την εκτέλεση της show1() (ΚΑΙ μεταφορά παρελθουσών ενεργειών στο αρχείο, σε περίπτωση που δεν επιλέξει να τις δει ο χρήστης κατά
        Frame2.grid_forget() #την είσοδό του στο πρόγραμμα.
        previousList=[]
        if len(doneList)>0:
            previousList=[]
            with open("past.csv", "r", encoding="utf-8", newline="") as file: 
                ro=csv.reader(file, delimiter='$')
                for row in ro:
                    previousList.append(row)
            for k in doneList:
                if k not in previousList: #κόψιμο διπλοεγγραφής
                    previousList.append(k)
            with open("past.csv", "w", encoding="utf-8", newline="") as file: #καταχώρηση των παρελθουσών ενεργειών στο αρχείο μετά από την εμφάνισή τους στην οθόνη.
                wo=csv.writer(file, delimiter='$')
                for row in previousList:
                    wo.writerow(row)            
            with open("future.csv", "w", encoding="utf-8", newline="") as file: #αναδιαμόρφωση του αρχείου τρεχουσών ενεργειών (κρατάει πλέον ημ/νίες από την τρέχουσα και έπειτα).
                wo=csv.writer(file, delimiter='$')
                for k in toDoList: #ενέργειες τρέχουσας ημέρας.
                    wo.writerow(k)
                for k in futureList: #μελλοντικές ενέργειες.
                    wo.writerow(k)
        global status2
        status2=""
        menu()
    elif x==9: #μετάβαση στην show2() μετά από την εκτέλεση της show1().
        Frame2.grid_forget()
        show2()
    elif x==10: #ακύρωση ανανέωσης κάρτας ανεργίας (και <<Επιστροφή στο κεντρικό μενού).
        Frame8.grid_forget()   
        menu()
    elif x==11: #<<Επιστροφή στην show1() μετά από αποτυχημένη/επιτυχημένη ανανέωση κάρτας.
        Frame9.grid_forget()
        show1()
    elif x==12: #ανακατεύθυνση από την show1() προς την ektyposi1() --> εκτύπωση των ενεργών δελτίων ανεργίας που εμφανίζονται στο σύστημα να μην έχουν ανανεωθεί.
        global enterMenu
        global back
        Frame2.grid_forget()
        global Frame71
        Frame71=LabelFrame(root, bd=0)
        Frame71.grid(row=5, column=0, columnspan=18)
        #global status2
        status2='check_card'
        ektyposi1(Frame71, fail)                
    elif x==13: #εκτύπωση των ενεργών δελτίων ανεργίας προς ανανέωση.
        Frame2.grid_forget()
        Frame71=LabelFrame(root, bd=0)
        Frame71.grid(row=5, column=0, columnspan=18)
        ektyposi1(Frame71, today)
    elif x==14: #<<Επιστροφή στην αρχική οθόνη της show1() μετά από την αναλυτκή εμφάνιση των αποτελεσμάτων της.
        insert(Frame2, 4)
    elif x==15: #τερματισμός (έξοδοςο) του προγ/τος από το κεντρικό μενού.
        mainMenu.grid_forget()
        greetings()
    elif x==16: #<<Επιστροφή στην αρχική οθόνη της show1() από την show2().
        Frame12.grid_forget()
        show1()
    elif x==17: #μετάβαση στο κεντρικό μενού μετά από την εκτέλεση της show2().
        Frame12.grid_forget()
        menu()
    elif x==18: #<<Επιστροφή στο κεντρικό μενού από την προβολή ενεργών δελτίων.
        Frame14.grid_forget()
        menu()
    elif x==19: #<<Επιστροφή στην προβολή ενεργών δελτίων από τη φόρμα ανανέωσης.
        Frame14.grid_forget()
        menu()
    elif x==20: #έλεγχος ορθότητας στοιχείων νέας εγγραφής και οριστική υποβολή της.
        global errorFlag
        global Frame15
        errorFlag=0
        message=""
        Frame13.grid_forget()
        Frame15=LabelFrame(root, bd=0)
        Frame15.grid(row=6, column=0, columnspan=18)
        surname=surnamePrint2.get() 
        name=namePrint2.get() 
        card=cardPrint2.get()
        global date1
        date1=update1Print2.get()
        global date2
        date2=update2Print2.get()       
        amka2=amkaPrint2.get()
        afm2=afmPrint2.get()
        dypa1=DYPA1Print2.get() 
        dypa2=DYPA2Print2.get() 
        taxis1=TAXIS1Print2.get() 
        taxis2=TAXIS2Print2.get() 
        akha=akhaPrint2.get() 
        active=activePrint2.get() 
        plan=planPrint2.get() 
        tel=telPrint2.get() 
        mail=mailPrint2.get() 
        notes=notesPrint2.get("1.0","end")
        if notes=="": #πατέντα, αν μείνει κενό το πεδίο των παρατηρήσεων, δημιουργούμε ένα whitespace, ώστε να αποκτήσει len() το πεδίο και να μπει η ',' στο .csv (αλλιώς ΔΕΝ ΜΠΑΙΝΕΙ!)
            notes=" "
        notes=notes[0:-1] #κόβει τα "" στην τελική καταχώρηση.
        date1.strip()
        date2.strip()
        if not card.isdigit():
            errorFlag=1
            message=message+"Δεν είναι σωστή η καταχώρηση του αριθμού δελτίου ΔΥΠΑ."
        amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
        amka=""
        for i in amka2:
            amka=amka+i
        amka=amka.strip()
        if amka.isdigit() and len(amka)==11: #σωστός ΑΜΚΑ
            pass
        else:
            errorFlag=1
            message=message+"\nΔεν είναι σωστή η καταχώρηση, ο ΑΜΚΑ πρέπει να περιέχει (11) ψηφία."
        afm2=afm2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΦΜ
        afm=""
        for i in afm2:
            afm=afm+i
        afm=afm.strip()
        if afm.isdigit() and len(afm)==9: #σωστός ΑΦΜ
            pass
        else:
            errorFlag=1
            message=message+"\nΔεν είναι σωστή η καταχώρηση, ο ΑΦΜ πρέπει να περιέχει (9) ψηφία."
        day1=checkDate(date1)
        day2=checkDate(date2)
        if day1==0 or day2==0:
            errorFlag=1
            message=message+"\nΜη έγκυρη ημερομηνία."
        else:
            global checkList
            checkList=[]
            with open("current.csv", "r", encoding="utf-8", newline="") as file:
                ro=csv.reader(file, delimiter='$')
                for row in ro:
                    checkList.append(row)
            for y in checkList:                    
                if amka==y[5] or afm==y[6]:
                    errorFlag=1
                    message=message+"\nΒρέθηκε εγγραφή στο σύστημα με ίδιο ΑΦΜ ή/και ΑΜΚΑ."
                    break
        if errorFlag==1:
            message=message[:-1]+", η ενέργεια ακυρώθηκε."
            messagebox.showwarning('Σφάλμα:', message)
        else:
            checkList.append([surname.upper(), name.upper(), card, day1, day2, amka, afm, akha, dypa1, dypa2, taxis1, taxis2, active.upper(), plan.upper(), tel, mail, notes ])
            with open("current.csv", "w", encoding="utf-8", newline="") as file:
                wo=csv.writer(file, delimiter='$')
                for k in checkList:
                    wo.writerow(k)
                message="Η εγγραφή καταχωρήθηκε με επιτυχία."
                messagebox.showinfo('', message)
        newEntry=Button(Frame15, text="Νέα εγγραφή", padx=40, pady=11, command=lambda: goto(21))
        newEntry.grid(row=100, column=8, padx=50, pady=25)
        newReturn=Button(Frame15, text="Κεντρικό μενού", padx=35, pady=11, command=lambda: goto(22))
        newReturn.grid(row=100, column=9, padx=50, pady=25)
    elif x==21: #<<Επιστροφή στην φόρμα υποβολής νέας εγγραφής μετά από εξέταση κάποιας άλλης.
        insert(Frame15, 2)
    elif x==22: # <<Επιστροφή στο κεντρικό μενού μετά από εξέτασης υποβολής νέας εγγραφής.                        
        Frame15.grid_forget()
        menu()
    elif x==23: #<<Επιστροφή στο κεντρικό μενού από τη φόρμα αναζήτησης.   
        Frame16.grid_forget()
        menu()
    elif x==24: #<<Επιστροφή στο κεντρικό μενού μετά από αναζήτηση (ΔΙΑΦΟΡΕΤΙΚΟ ΣΗΜΕΙΟ από τη φόρμα αναζήτησης).        
        Frame17.grid_forget()
        menu()
    elif x==25: #εμφάνιση αποτελεσμάτων σύμφωνα με κριτίρια αναζήτησης (ακολουθεί διαγραφή δελτίων ανεργίας).
        #global Frame17
        global newSearch
        Frame17.grid_forget()
        global Frame25
        Frame25=LabelFrame(root, bd=0)
        Frame25.grid(row=5, column=0, columnspan=18)       
        ektyposi3(Frame25, printList)         
    elif x==26: #Νέα αναζήτηση δελτίου ανεργίας (για διαγραφή).
        #insert(Frame25, 5)
        insert(FrameForScroll2, 5)
    elif x==27: #<<Επιστροφή στο κεντρικό μενού μετά από αναζήτηση (για διαγραφή).
        #Frame25.grid_forget()
        FrameForScroll2.grid_forget()
        menu()
    elif x==28: #φόρμα αναζήτησης για Τροποποίηση δελτίου στοιχείων δελτίων ανεργίας.        
        global surnameAlter2
        global cardAlter2
        global amkaAlter2
        global afmAlter2
        global akhaAlter2
        global update1Alter2
        global update2Alter2
        global activeAlter2
        global Frame18
        alterLabel2=Label(Frame18, text="ΤΡΟΠΟΠΟΙΗΣΗ ΔΕΛΤΙΟΥ (ανεύρεση με βάση):", fg="red", bg="#d9d9d9", pady=25)
        alterLabel2.grid(row=7, column=0, columnspan=18, sticky=W+E)
        surnameAlter1=Label(Frame18, fg="red", text="ΕΠΩΝΥΜΟ:", padx=15, pady=15)
        surnameAlter1.grid(row=8, column=7, sticky=E, pady=5)
        surnameAlter2=Entry(Frame18, width=50, relief=SUNKEN, borderwidth=5)
        surnameAlter2.grid(row=8, column=8, pady=5)
        cardAlter1=Label(Frame18, fg="red", text="ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ:", padx=15, pady=20)
        cardAlter1.grid(row=9, column=7, sticky=E)
        cardAlter2=Entry(Frame18, width=50, relief=SUNKEN, borderwidth=5)
        cardAlter2.grid(row=9, column=8, pady=5)        
        amkaAlter1=Label(Frame18, fg="red", text="ΑΜΚΑ:", padx=15, pady=20)
        amkaAlter1.grid(row=10, column=7, sticky=E)
        amkaAlter2=Entry(Frame18, width=50, relief=SUNKEN, borderwidth=5)
        amkaAlter2.grid(row=10, column=8, pady=5)
        afmAlter1=Label(Frame18, fg="red", text="ΑΦΜ:", padx=15, pady=20)
        afmAlter1.grid(row=11, column=7, sticky=E)
        afmAlter2=Entry(Frame18, width=50, relief=SUNKEN, borderwidth=5)
        afmAlter2.grid(row=11, column=8, pady=5)
        akhaAlter1=Label(Frame18, fg="red", text="ΚΩΔΙΚΟΣ ΑΚΗΑ:", padx=15, pady=20)
        akhaAlter1.grid(row=12, column=7, sticky=E)
        akhaAlter2=Entry(Frame18, width=50, relief=SUNKEN, borderwidth=5)
        akhaAlter2.grid(row=12, column=8, pady=5)        
        for i in range(5):
            choiceAlter=Button(Frame18, text="Επιλογή", padx=40, pady=11, command=lambda i=i: alter(Frame18, i))
            choiceAlter.grid(row=8+i, column=9, padx=15)
        backAlter=Button(Frame18, text="<<Επιστροφή", padx=31, pady=11, command=lambda: goto(33))
        backAlter.grid(row=100, column=0, columnspan=18, pady=45)
    elif x==29: #<<Επιστροφή στο μενού επιλογών Τροποποίηση δελτίους από τη φόρμα Τροποποίηση δελτίους δελτίων.        
        insert(Frame18, 4)
    elif x==30: #ανανέωση δελτίου ανεργίας (από τη φόρμα Τροποποίηση δελτίους).
        Frame18.grid_forget()
        show1()
    elif x==31: #<<Επιστροφή στο κεντρικό μενού από την Τροποποίηση δελτίου στοιχείων κάρτας ανεργίας.
        Frame21.grid_forget()
        menu()
    elif x==32: #εμφάνιση εγγραφών δελτίων ανεργίας που πληρούν τα κριτίρια αναζήτησης (ακολουθεί ενέργεια Τροποποίηση δελτίους).
        Frame19.grid_forget()
        global Frame20
        Frame20=LabelFrame(root, bd=0)
        Frame20.grid(row=5, column=0, columnspan=18)       
        resultsSearchLabel=Label(Frame20, text="ΑΠΟΤΕΛΕΣΜΑΤΑ ΑΝΑΖΗΤΗΣΗΣ ΔΕΛΤΙΩΝ ΑΝΕΡΓΙΑΣ ΓΙΑ ΤΡΟΠΟΠΟΙΗΣΗ", fg="red", bg="#d9d9d9", pady=25)
        resultsSearchLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        ektyposi2(Frame20, printList)
    elif x==33: #<<Επιστροφή στο κεντρικό μενού από τη φόρμα τροποποίσης στοιχείων δελτίων ανεργίας.
        Frame18.grid_forget()
        menu()
    elif x==34: #<<Επιστροφή στο κεντρικό μενού από τη φόρμα Τροποποίηση δελτίους.
        Frame20.grid_forget()
        menu()
    elif x==35: #<<Επιστροφή στο κεντρικό μενού μετά από Τροποποίηση δελτίου.
        Frame19.grid_forget()
        menu()
    elif x==36: #νέα Τροποποίηση δελτίου μετά από προσπάθεια Τροποποίηση δελτίους.)
        insert(Frame19, 4)
    elif x==37: #<<Επιστροφή στο κεντρικό μενού από τη φόρμα αναζήτησης για διαγραφή δελτίων ανεργίας.
        Frame22.grid_forget()
        menu()
    elif x==38: #Νέα αναζήτηση δελτίου ανεργίας (για Τροποποίηση δελτίου).
        Frame20.grid_forget()
        Frame18=LabelFrame(root, bd=0)
        Frame18.grid(row=5, column=0, columnspan=18)
        goto(28)
    elif x==39: #<<Επιστροφή στο κεντρικό μενού μετά από αναζήτηση (για Τροποποίηση δελτίου).
        #resultsSearchLabel.grid_forget()
        Frame20.grid_forget()
        FrameForScroll2.grid_forget()
        menu()
    elif x==40: ##Νέα αναζήτηση δελτίου ανεργίας (για Τροποποίηση δελτίου) ΑΠΟ ΑΛΛΟ ΣΗΜΕΙΟ.
        Frame19.grid_forget()
        Frame18=LabelFrame(root, bd=0)
        Frame18.grid(row=5, column=0, columnspan=18)
        goto(28)
    elif x==41: #νέα διαγραφή μετά από διαγραφή.
        insert(Frame24, 5)
    elif x==42: #<<Επιστροφή στο κεντρικό μενού μετά από διαγραφή.
        Frame24.grid_forget()
        menu()
    elif x==43: #<<Επιστροφή στην show1() από την επιλογή ανανέωσης δελτίου.
        if k==today:
            insert(Frame8, 1)
            Frame13.grid_forget()
            Frame14=LabelFrame(root,bd=0)
            Frame14.grid(row=6, column=0, columnspan=18)
            activeLabel=Label(Frame14, text="ΕΝΕΡΓΑ ΔΕΛΤΙΑ ΑΝΕΡΓΙΑΣ ΠΟΥ ΕΧΕΙ ΑΝΟΙΞΕΙ ΤΟ ΠΑΡΑΘΥΡΟ ΓΙΑ ΑΝΑΝΕΩΣΗ", pady=25, fg="red", bg="#d9d9d9")
            activeLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
            ektyposi1(Frame14, today)          
        elif k==fail:
            pass
    elif x==44: #προβολή ανενεργών χρηστών (και δικαίωμα επιλογής επανενεργοποίησής τους).
        Frame13.grid_forget()
        global deactive
        temp=[]
        deactive=[]
        with open("current.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                temp.append(row)
            for element in temp: #ανεύρεση των ανενεργών χρηστών.
                if element[12]=='ΟΧΙ':
                    deactive.append(element) 
        global Frame26
        Frame26=LabelFrame(root, bd=0)
        Frame26.grid(row=6, column=0, columnspan=18)
        ektyposi2(Frame26, deactive)       
    elif x==45: #ενεργοποίηση ανενεργών δελτίων.
        global temp1
        temp1=[]
        with open("current.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                temp1.append(row)
            for record in temp1:
                if record[5]==y[i][5] and record[6]==y[i][6]: #έλεγχος ταυτοποίησης με βάση: ΑΜΚΑ, ΑΦΜ.
                    record[12]='ΝΑΙ'
        with open("current.csv", "w", encoding="utf-8", newline="") as file:
            wo=csv.writer(file, delimiter='$')
            for record in temp:
                wo.writerow(record)
            Frame21.grid_forget()
            global Frame27
            Frame27=LabelFrame(root, bd=0)
            Frame27.grid(row=6, column=0, columnspan=18)
            returnActive=Button(Frame27, text="<<Επιστροφή", padx=40, pady=11, command=lambda: insert(Frame14, 1))
            returnActive.grid(row=10, column=8, padx=50, pady=25)
            menuActive=Button(Frame27, text="Κεντρικό μενού", padx=32, pady=11, command=lambda: goto(47))
            menuActive.grid(row=10, column=9, padx=50, pady=25)            
            messagebox.showinfo('', "Η ενεργοποίηση του δελτίου ανεργίας έγινε με επιτυχία.")
    elif x==46: #<<Επιστροφή στην προβολή των ανενεργών δελτίων.
        Frame27.grid_forget()
        goto(44)
    elif x==47: #<<Επιστροφή στο κεντρικό μενού μετά από ενεργοποίηση δελτίου.
        Frame27.grid_forget()
        menu()
    elif x==48: #<<Επιστροφή στο κεντρικό μενού από την προβολή των δελτίων για Τροποποίηση δελτίου/ ενεργοποίηση.
        insert(z, 1)
    elif x==49: #εμφάνιση αποτελεσμάτων αναζήτησης.        
        Frame20=LabelFrame(root, bd=0)
        Frame20.grid(row=5, column=0, columnspan=18)       
        resultsSearchLabel=Label(Frame20, text="ΑΠΟΤΕΛΕΣΜΑΤΑ ΑΝΑΖΗΤΗΣΗΣ ΔΕΛΤΙΩΝ ΑΝΕΡΓΙΑΣ (ΠΡΟΒΟΛΗ)", fg="red", bg="#d9d9d9", pady=25)
        resultsSearchLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        ektyposi4(Frame20, printList)
    elif x==50: #<<Επιστροφή στο μενού 'Ενέργειες (δελτία)' από το ευρετήριο.
        Frame28.grid_forget()
        menu()
    elif x==51: #νεά αναζήτηση δελτίου ανεργίας.
        insert(FrameForScroll2, 3)    
    elif x==52: #
        Frame8.grid_forget()
        goto(6)
    elif x==53: #ενεργοποίηση δελτίου ανεργίας.
        z.grid_forget()
        y[i][12]='ΝΑΙ'
        temp=[]
        with open("current.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                  temp.append(row)
                  for record in temp:
                      if record[5]==y[i][5] and record[6]==y[i][6]:
                          record[12]==y[i][12] #ενεργοποίηση δελτίου.
        with open("current.csv", "w", encoding="utf-8", newline="") as file:
            wo=csv.writer(file, delimiter='$')
            for row in temp:
                wo.writerow(row)
        Frame30=LabelFrame(root, bd=0)
        Frame30.grid(row=5, column=0, columnspan=18)
        messagebox.showinfo('', "Το συγκεκριμένο δελτίο ενεργοποιήθηκε με επιτυχία.")
        newActivate=Button(Frame30, text="<<Επιστροφή", padx=40, pady=11, command=lambda: goto(54))
        newActivate.grid(row=10, column=8, padx=65)  
        returnSactivate=Button(Frame30, text="Κεντρικό μενού", padx=32, pady=11, command=lambda: goto(55))
        newActivate.grid(row=10, column=8, padx=65)
    elif x==54: #νέα ενεργοποίηση δελτίου ανεργίας.
        Frame30.grid_forget()
        Frame26=LabelFrame(root, bd=0)
        Frame26.grid(row=5, column=0, columnspan=18)
        for record in deactive: #ανεύρεση και αφαίρεση από την λίστα των ανενεργών δελτίων αυτό που ενεργοποιήθηκε νωρίτερα.
            if y==record:
                deactive.pop(record)
        ektyposi2(Frame26, deactive)
    elif x==55: #<<Επιστροφή στο κεντρικό μενού μετά από ενεργοποίηση δελτίου ανεργίας.
        Frame30.grid_forget()
        menu()              
    elif x==56: #νέα Τροποποίηση δελτίου στοιχείων δελτίου μετά από Τροποποίηση δελτίου.
        insert(Frame32, 4)
    elif x==57: #<<Επιστροφή στο κεντρικό μενού μετά από Τροποποίηση δελτίου.
        Frame32.grid_forget()
        menu()
    elif x==58: # <<Επιστροφή στον πίνακα των εγγραφών (αναζήτηση) μετά από πλήρη προβολή στοιχείων συγκεκριμένης εγγραφής.
        insert(Frame21, 1)
    elif x==59: #<<Επιστροφή στο κεντρικό μενού από την προβολή ανενεργών δελτίων.
        FrameForScroll2.grid_forget()
        menu()
    elif x==60: #επαναφορά διαγραμμένου δελτίου ανεργίας.
        Frame13.grid_forget()
        global deletedList
        deletedList=[]
        with open("previous.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                deletedList.append(row)       
        Frame14=LabelFrame(root,bd=0)
        Frame14.grid(row=6, column=0, columnspan=18)
        if len(deletedList)==0: #δεν υπάρχουν διαγραμμένα δελτία.            
            activeBack=Button(Frame14, text="<<Επιστροφή", padx=40, pady=11, command=lambda: insert(Frame14, 1))
            activeBack.grid(row=1000, column=8, pady=45, padx=65)
            activeReturn=Button(Frame14, text="Κεντρικό μενού", padx=40, pady=11, command=lambda: goto(18))
            activeReturn.grid(row=1000, column=9, pady=45, padx=65)
            messagebox.showinfo('Ενημέρωση:', "Δεν υπάρχουν διαγραμμένα δελτία στο σύστημα.")
        else:
            global status5
            status5='del_cards'
            ektyposi1(Frame14, deletedList)
    elif x==61: #<<Επιστροφή στο κεντρικό μενού μετά απο επαναφορά δελτίου ανεργίας.
        Frame33.grid_forget()
        menu()
    elif x==62: #νέα επαναφορά δελτίου μετά από προηγούμενη επαναφορά.
        Frame33.grid_forget()
        Frame13.grid(row=0, column=0, columnspan=18) #πατέντα, προκειμένου αμέσως μετά να καλέσω την goto(60) και να μην μου χτυπήσει σφάλμα.
        goto(60)
    elif x==63: #ανακατεύθυνση προς την εκτύπωσ των ενεργών δελτίων (ακολουθεί ενέργεια ανανέωσης).
        insert(Frame18, 1)
        goto(88)
    elif x==64: #<<Επιστροφή στο κεντρικό μενού μετά από αποτυχημένη κατάργηση λογαριασμού χρήστη.
        changes.grid_forget()
        menu()
    elif x==65: #<<Επιστροφή στο κεντρικό μενού μετά από επιτυχημένη κατάργηση λογαριασμού χρήστη.
        Frame34.grid_forget()
        menu()
    elif x==66: #νέα κατάργηση λογαριασμού χρήστη μετά από επιτυχημένη κατάργηση.
        Frame34.grid_forget()
        changePass(2)
    elif x==67: #<<Επιστροφή στο κεντρικό μενού μετά από αποτυχημένη προσθήκη λογαριασμού χρήστη.
        Frame35.grid_forget()
        menu()
    elif x==68: #<<Επιστροφή στην προσθήκη λογαριασμού χρήστη μετά από αποτυχημένη προσθήκη λογαριασμού χρήστη.
        Frame35.grid_forget()
        changePass(1)
    elif x==69: #ανακατεύθυνση (εμφάνιση νέων δελτίων).
        Frame13.grid_forget()
        goto(6)
    elif x==70: #<<Επιστροφή στην αρχική οθόνη του προγράμματος.
        status5=''
        global FrameForScroll
        Frame100.grid_forget()
        FrameForScroll.grid_forget()
        show1()
    elif x==71: #<<Επιστροφή στο κεντρικό μενού μετά από την προβολή των ενεργών δελτίων.
        status5=''
        status2=""
        Frame100.grid_forget()
        FrameForScroll.grid_forget()
        menu()
    elif x==72: #<<Επιστροφή στο κεντρικό μενού μετά από την προβολή του μενού ενεργειών (memo).
        global Frame36
        Frame36.grid_forget()
        menu()
    elif x==73: #εισαγωγή ενεργειών (memo).
        Frame36.grid_forget()
        global Frame37
        global dateMemo2
        global notesMemo2
        Frame37=LabelFrame(root, bd=0)
        Frame37.grid(row=5, column=0, columnspan=18)
        insertMemo=Label(Frame37, text="Εισαγωγή ενεργειών (memo)", fg="red", bg="#d9d9d9", pady=25)
        insertMemo.grid(row=5, column=0, columnspan=18, sticky=W+E)
        dateMemo1=Label(Frame37, text="Ημ/νία ενέργειας (ηη-μμ-εεεε ή ηη/μμ/εεεε):", fg="red")
        dateMemo1.grid(row=6, column=8, pady=10, padx=10)
        dateMemo2=Entry(Frame37, width=50, borderwidth=5, relief=SUNKEN)
        dateMemo2.grid(row=6, column=9, pady=10, padx=10)
        notesMemo1=Label(Frame37, text="Ενέργεια:", fg="red")
        notesMemo1.grid(row=7, column=0, pady=5)
        notesMemo2=Text(Frame37, width=111, height=20, borderwidth=1, relief=SUNKEN)
        notesMemo2.grid(row=8, column=0, columnspan=18, padx=5)
        backMemo=Button(Frame37, text="<<Επιστροφή", padx=30, pady=11, command=lambda: goto(74))
        backMemo.grid(row=100, column=8, padx=65, pady=25)
        submitMemo=Button(Frame37, text="Υποβολή", padx=45, pady=11, command=lambda: goto(75))
        submitMemo.grid(row=100, column=9, padx=65, pady=25)
    elif x==74: #<<Επιστροφή στο μενού ενεργειών (memo) από την εισαγωγή ενέργειας (memo).
        insert(Frame37, 6)
    elif x==75: #έλεγχος και οριστική καταχώρηση νέας ενέργειας (memo).
        Frame37.grid_forget()
        global Frame38
        global date
        Frame38=LabelFrame(root, bd=0)
        Frame38.grid(row=5, column=0, columnspan=18)
        day=dateMemo2.get()
        day=day.strip()
        date=checkDate(day)
        newMemo=Button(Frame38, text="Νέα εισαγωγή (memo)", padx=11, pady=11, command=lambda: goto(76))
        newMemo.grid(row=100, column=8, padx=65, pady=45)            
        backMemo=Button(Frame38, text="<<Επιστροφή", padx=35, pady=11, command=lambda: goto(77))
        backMemo.grid(row=100, column=9, padx=65, pady=45)
        returnMemo=Button(Frame38, text="Κεντρικό μενού", padx=32, pady=11, command=lambda: goto(78))
        returnMemo.grid(row=100, column=10, padx=65, pady=45)        
        global message3
        message3=""
        global flag3
        flag3=1
        if date==0:            
            message3="Μη έγκυρη ημερομηνία, η ενέργεια ακυρώθηκε."
            flag3=0
        else:
            notes=notesMemo2.get('1.0', END) #παίρνουμε ολόκληρο το κείμενο των σημειώσεων.
            notes=notes[:-1] #πατέντα για να φύγουν τα "" από το string των σημειώσεων (memo).
            if len(notes)==0:
                message3="Δε βρέθηκαν σημειώσεις για καταχώρηση, η ενέργεια ακυρώθηκε."
                flag3=0
            else:
                temp=[]
                temp2=[]
                with open("future.csv", "r", encoding="utf-8", newline="") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        temp.append(row)
                    for record in temp:
                        if date==record[0]:
                            if notes.strip()==record[1].strip():                   
                                message3="Υπάρχει αυτή η εγγραφή ήδη καταχωρημένη στο σύστημα, η ενέργεια ακυρώθηκε."
                                flag3=0
                                break
                            else:
                                temp2.append(record)
                                flag3=1
        if flag3==0: #μήνυμα σφάλματος (κόκκινα γράμματα).
            messagebox.showerror('Σφάλμα:', message3)
        else:                                
            with open("future.csv", "a", encoding="utf-8", newline="") as file:
                wo=csv.writer(file, delimiter='$')                 
                wo.writerow([date, notes])
                messagebox.showinfo('', "Η ενέργεια (memo) καταχωρήθηκε με επιτυχία.")           
        
    elif x==76: #νέα εισαγωγή ενέργειας (memo).
        insert(Frame38, 6)
        goto(73)
    elif x==77: #<<Επιστροφή στο μενού ενεργειών (memo) μετά από εισαγωγή (επιτυχημένη η αποτυχημένη) ενέργειας (memo).
        insert(Frame38, 6)
    elif x==78: #<<Επιστροφή στο κεντρικό μενού μετά από εισαγωγή (επιτυχημένη η αποτυχημένη) ενέργειας (memo).
        Frame38.grid_forget()
        menu()
    elif x==79: #φόρμα Τροποποίηση δελτίους Τροποποίηση δελτίου εγγραφής (memo).        
        global request2
        Frame36.grid_forget()
        global Frame39
        Frame39=LabelFrame(root, bd=0)
        Frame39.grid(row=5, column=0, columnspan=18)
        global action
        action=''
        alterLabel=Label(Frame39, text="ΔΙΟΡΘΩΣΗ ΕΓΓΡΑΦΗΣ (MEMO)", fg="red", bg="#d9d9d9", pady=25)
        alterLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        request1=Label(Frame39, text="Ημερομηνία εγγραφής:", fg="red", pady=25)
        request1.grid(row=6, column=8, padx=5)
        request2=Entry(Frame39, width=50, borderwidth=5, relief=SUNKEN, bg="#d9d9d9")
        request2.grid(row=6, column=9, padx=5, pady=25)
        request3=Button(Frame39, text="Υποβολή", padx=35, pady=11, command=lambda: goto(80))
        request3.grid(row=6, column=10, padx=15)
        request4=Button(Frame39, text="<<Επιστροφή", padx=30, pady=11, command=lambda: goto(92))
        request4.grid(row=1000, column=0, columnspan=18, pady=15)
    elif x==80: #έλεγχος ημερομηνίας εγγραφής και αναζήτηση σημειώσεων (memo) με βάση την ημερομηνία που έδωσε ο χρήστης (για ενεργειες διόρθωσης/ακύρωσης).
        day=request2.get()
        date=checkDate(day)                  
        if action=='del': #για ενέργεια ακύρωσης.
            global Frame43
            Frame43.grid_forget()
        else:             #για ενέργεια διόρθωσης.
            Frame39.grid_forget()            
        global Frame40
        Frame40=LabelFrame(root, bd=0)
        Frame40.grid(row=5, column=0, columnspan=18)        
        if date==0: #λανθασμένη ημ/νία.
            text1="Μη έγκυρη ημερομηνία, η ενέργεια ακυρώθηκε."
            flag=0
        elif date<currentDate():            
            if action=='del': #επιλογή διαγραφής ενέργειας (memo) σε προγενέστερη ημ/νία (ΔΕΝ ΕΠΙΤΡΕΠΕΤΑΙ!)                
                text1="Δεν επιτρέπεται διαγραφή ενέργειας (memo) προγενέστερης ημερομηνίας, η ενέργεια ακυρώθηκε."
            else:             #επιλογή διορθωσης ενέργειας (memo) σε προγενέστερη ημ/νία (ΔΕΝ ΕΠΙΤΡΕΠΕΤΑΙ!)
                text1="Δεν επιτρέπεται διόρθωση ενέργειας (memo) προγενέστερης ημερομηνίας, η ενέργεια ακυρώθηκε."
            flag=2 #warning και ΟΧΙ σφάλμα.
        else:
            temp=[]            
            if date>=currentDate():                     #τρέχουσες ενέργειες (memo)
                with open("future.csv", "r", encoding="utf-8", newline="") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        temp.append(row)
            else:                           #παρελθούσες ενέργειες (memo)
                temp=[]
                with open("past.csv", "r", encoding="utf-8", newline="") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        temp.append(row)                                     
            temp2=[]
            for record in temp:     
                if date==record[0]:
                    temp2.append(record)                    
            if len(temp2)==0:
                text1="Δε βρέθηκαν ενέργειες (memo) με βάση την συγκεκριμένη ημερομηνία ("+date[-2:]+"-"+date[-4:-2]+"-"+date[:4]+")."
                flag=2
            else:
                if len(temp2)==1:
                    end1="ε "
                    end2="ή."
                else:
                    end1="αν συνολικά "
                    end2="ές."
                text1="Βρέθηκ"+end1+str(len(temp2))+" εγγραφ"+end2
                flag=1



                FrameForScroll=LabelFrame(root, bd=0) #scrollbar attempt!!!
                FrameForScroll.grid(row=5, column=0, columnspan=18)
                #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
                canvas=Canvas(FrameForScroll, bd=0, height=480, width=1220) 
                canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
                Frame40=LabelFrame(canvas, bd=0)
                scrollbar = Scrollbar(FrameForScroll, orient="vertical", command=canvas.yview)
                scrollbar.grid(row=0, column=18, sticky=N+S)
                Frame40.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
                canvas.create_window((0, 0), window=Frame40, anchor="nw", width=2000)
                canvas.configure(yscrollcommand=scrollbar.set)
                Frame100=LabelFrame(FrameForScroll, bd=0)
                Frame100.grid(row=500, column=0, columnspan=18)
                if action=='del':
                    backMemo=Button(Frame100, text="<<Επιστροφή", padx=32, pady=11, command=lambda: goto(97))
                    backMemo.grid(row=1000, column=8, padx=65, pady=15)
                else:
                    backMemo=Button(Frame100, text="<<Επιστροφή", padx=32, pady=11, command=lambda: goto(81))
                    backMemo.grid(row=1000, column=8, padx=65, pady=15)
                menuMemo=Button(Frame100, text="Κεντρικό μενού", padx=25, pady=11, command=lambda: goto(82))
                menuMemo.grid(row=1000, column=11, sticky=E, padx=65, pady=15)
                
                showMemo=Label(Frame40, text="ΕΝΕΡΓΕΙΕΣ (MEMO) ΤΗΣ "+date[-2:]+"-"+date[-4:-2]+"-"+date[:4]+".", fg='red', bg="#d9d9d9", pady=25)
                showMemo.grid(row=5, column=0, columnspan=18, sticky=W+E)
                dayMemo1=Label(Frame40, text='ΗΜΕΡΟΜΗΝΙΑ', fg="red", pady=10)
                dayMemo1.grid(row=6, column=0, sticky=W)                
                notesMemo1=Label(Frame40, text="ΕΝΕΡΓΕΙΕΣ", fg="red", pady=10)
                notesMemo1.grid(row=6, column=2, sticky=W+E, columnspan=15)               
                for i in range(len(temp2)):
                    dayMemo2=Text(Frame40,width=15, borderwidth=1, relief=SUNKEN, height=3)                  
                    dayMemo2.grid(row=7+i, column=0)
                    dayMemo2.insert(INSERT, str(date[-2:]+"-"+date[-4:-2]+"-"+date[:4]))
                    notesMemo2=Text(Frame40, width=111, borderwidth=1, relief=SUNKEN, height=3)
                    notesMemo2.grid(row=7+i, column=2, columnspan=15)
                    notesMemo2.insert(INSERT, temp2[i][1])
                    #global message
                    global method
                    if action=='del':
                        message="Διαγραφή"
                        method=3
                    else:
                        message="Τροποποίηση δελτίου"
                        method=1
                    alterMemo=Button(Frame40, text=message, padx=30, pady=11, command=lambda i=i: memoChange(temp, temp2, i, method, ''))
                    alterMemo.grid(row=7+i, column=17, padx=15)                
        if flag==0: #error.
            messagebox.showerror('Σφάλμα:', text1)
        elif flag==2:#warning.
            messagebox.showwarning('Ενημέρωση:', text1)
        else: #δεν υπάρχει σφάλμα.
            messagebox.showinfo('', text1)
    elif x==81: #<<Επιστροφή στη φόρμα αναζήτησης ενεργειών (memo) μετά από αποτυχημένη αναζήτηση για Τροποποίηση δελτίου.
        insert(FrameForScroll, 6)
        goto(79)
    elif x==82: #<<Επιστροφή στο κεντρικό μενού μετά από αποτυχημένη αναζήτηση για Τροποποίηση δελτίου.
        FrameForScroll.grid_forget()
        menu()
    elif x==83: #νέα Τροποποίηση δελτίου μετά από επιτυχημένη Τροποποίηση δελτίου.
        Frame41.grid_forget()
        Frame36=LabelFrame(root, bd=0)
        Frame36.grid(row=5, column=0)
        goto(79)
    elif x==84: #<<Επιστροφή στο κεντρικό μενού από επιτυχημένη Τροποποίηση δελτίου ενέργειας memo.
        Frame41.grid_forget()
        menu()
    elif x==85: #<<Επιστροφή στη φόρμα ενεργειών (memo) από τη φόρμα υποβολής Τροποποίηση δελτίους.
        insert(Frame41,6)
    elif x==86: #<<Επιστροφή στο κεντρικό μενού από επιτυχημένη Τροποποίηση δελτίου ενέργειας memo (από ΑΛΛΗ διαδρομή).
        Frame42.grid_forget()
        menu()        
    elif x==87: #<<Επιστροφή στη φόρμα ενεργειών (memo) από τη φόρμα υποβολής Τροποποίηση δελτίους (από ΑΛΛΗ διαδρομή).
        insert(Frame42,6)
    elif x==88: #ανακατεύθυνση (από ανανέωση δελτίου ανεργίας).
        Frame13.grid_forget()
        goto(6)
    elif x==89: #<<Επιστροφή στην show1() μετά από την προβολή των δελτίων που χρειάζεται έλεγχος.
        Frame71.grid_forget()
        goto(2)
    elif x==90: #ακύρωση ενέργειας (memo).
        Frame36.grid_forget()
        Frame43=LabelFrame(root, bd=0)
        Frame43.grid(row=5, column=0, columnspan=18)
        action='del'
        delMemo=Label(Frame43, text="ΑΚΥΡΩΣΗ ΕΓΓΡΑΦΗΣ (MEMO)", fg="red", bg="#d9d9d9", pady=25)
        delMemo.grid(row=5, column=0, columnspan=18, sticky=W+E)
        request1=Label(Frame43, text="Ημερομηνία εγγραφής:", fg="red", pady=25)
        request1.grid(row=6, column=8, padx=5)
        request2=Entry(Frame43, width=50, borderwidth=5, relief=SUNKEN, bg="#d9d9d9")
        request2.grid(row=6, column=9, padx=5, pady=25)
        request3=Button(Frame43, text="Υποβολή", padx=35, pady=11, command=lambda: goto(80)) #συνοδεύεται από την μεταβλητή action='del'.
        request3.grid(row=6, column=10, padx=15)
        request4=Button(Frame43, text="<<Επιστροφή", padx=30, pady=11, command=lambda: goto(93))
        request4.grid(row=1000, column=0, columnspan=18, pady=15)        
    elif x==91: #<<Επιστροφή στο κεντρικό μενού μετά από ενέργειας (memo).
        action=""
        Frame45.grid_forget()
        menu()
    elif x==92: #<<Επιστροφή στο μενού (memo) από την φόρμα αναζήτησης (για διόρθωση ενέργειας memo).
        insert(Frame39, 6)
    elif x==93: #<<Επιστροφή στο μενού (memo) από την φόρμα αναζήτησης (για ακύρωση ενέργειας memo).
        insert(Frame43, 6)
    elif x==94: #<<Επιστροφή στο μενού  (memo) από τη φόρμα ακύρωσης ενέργειας (memo).
        action=""
        global Frame44
        insert(Frame44, 6)
    elif x==95: #<<Επιστροφή στο κεντρικό μενού από τη φόρμα ακύρωσης ενέργειας (memo).
        Frame44.grid_forget()
        menu()
    elif x==96: #νέα διαγραφή ενέργειας (memo).
        Frame45.grid_forget()
        Frame36=LabelFrame(root, bd=0)
        Frame36.grid(row=5, column=0, columnspan=18)
        goto(90)
    elif x==97:#<<Επιστροφή στη φόρμα ενεργειών (memo) από τη φόρμα υποβολής ακύρωσης.
        insert(FrameForScroll, 6)
        goto(90)
    elif x==98: #προβολή ενεργειών (memo).
        Frame36.grid_forget()
        global Frame46
        Frame46=LabelFrame(root, bd=0)
        Frame46.grid(row=5, column=0, columnspan=18)
        showLabel=Label(Frame46, text="ΠΡΟΒΟΛΗ ΕΝΕΡΓΕΙΩΝ (MEMO)", fg="red", bg="#d9d9d9", pady=25)
        showLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        backMemo=Button(Frame46, text="<<Επιστροφή", padx=29, pady=11, command=lambda: goto(101))
        backMemo.grid(row=6, column=7, pady=45, padx=65)
        nowMemo=Button(Frame46, text="Σημερινές", padx=40, pady=11, command=lambda: goto(99))
        nowMemo.grid(row=6, column=8, pady=45, padx=65)
        calendarMemo=Button(Frame46, text="Ιστορικό", padx=40, pady=11, command=lambda: goto(100))
        calendarMemo.grid(row=6, column=9, pady=45, padx=65)
        returnMemo=Button(Frame46, text="Κεντρικό μενού", padx=23, pady=11, command=lambda: goto(102))
        returnMemo.grid(row=6, column=10, pady=45, padx=65)        
    elif x==99: #προβολή σημερινών ενεργειών (memo).
        Frame46.grid_forget()
        global Frame50
        Frame50=LabelFrame(root, bd=0)
        Frame50.grid(row=5, column=0, columnspan=18)
        global flag4
        flag4=1
        global tempList
        tempList=[]
        with open("future.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                tempList.append(row)
            global printList2
            printList2=[]
            for record in tempList:
                if record[0]==currentDate():
                    printList2.append(record)
            if len(printList2)==0:
                messagebox.showwarning('Ενημέρωση:', "Δε βρέθηκαν στο σύστημα σημερινές ενέργειες (memo).")
            else:
                FrameForScroll=LabelFrame(root, bd=0) #scrollbar attempt!!!
                FrameForScroll.grid(row=5, column=0, columnspan=18)
                #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
                canvas=Canvas(FrameForScroll, bd=0, height=480, width=1220) 
                canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
                Frame50=LabelFrame(canvas, bd=0)
                scrollbar = Scrollbar(FrameForScroll, orient="vertical", command=canvas.yview)
                scrollbar.grid(row=0, column=18, sticky=N+S)
                Frame50.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
                canvas.create_window((0, 0), window=Frame50, anchor="nw", width=2000)
                canvas.configure(yscrollcommand=scrollbar.set)
                Frame100=LabelFrame(FrameForScroll, bd=0)
                Frame100.grid(row=500, column=0, columnspan=18)                
                date=str(currentDate())
                showLabel=Label(Frame50, text="ΠΡΟΒΟΛΗ ΣΗΜΕΡΙΝΏΝ ΕΝΕΡΓΕΙΩΝ (MEMO) ("+date[-2:]+"-"+date[-4:-2]+"-"+date[:4]+").", fg="red", bg="#d9d9d9", pady=25)
                showLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)                
                aaMemo=Label(Frame50, text="Α/Α", fg="red")
                aaMemo.grid(row=6, column=0, pady=10)
                dateMemo=Label(Frame50, text="ΗΜ/ΝΙΑ", fg="red")
                dateMemo.grid(row=6, column=1, pady=10, sticky=W+E)
                notesMemo=Label(Frame50, text="ΕΝΕΡΓΕΙΕΣ", fg="red")
                notesMemo.grid(row=6, column=1, columnspan=16, pady=10)
                for i in range(len(printList2)):
                    aaMemo2=Text(Frame50, bd=0, width=3, height=3, borderwidth=1, relief=SUNKEN)
                    aaMemo2.grid(row=7+i, column=0, sticky=N+S)
                    aaMemo2.insert(INSERT, str(i+1))
                    dateMemo2=Text(Frame50, bd=0, width=11, height=3, borderwidth=1, relief=SUNKEN)
                    dateMemo2.grid(row=7+i, column=1)
                    dateMemo2.insert(INSERT, str(date[-2:]+"-"+date[-4:-2]+"-"+date[:4]))
                    notesMemo2=Text(Frame50, bd=0, width=111, height=3, borderwidth=1, relief=SUNKEN)
                    notesMemo2.grid(row=7+i, column=2, columnspan=15)
                    actionMemo=Button(Frame50, text="Επεξεργασία", padx=30, pady=11, command=lambda i=i: todayMemo(printList2, i, 1))
                    actionMemo.grid(row=7+i, column=17, padx=25)
                    temp=printList2[i][1]
                    #global k
                    k=150
                    global final2
                    final2=''
                    if len(temp)>256: #επιτρέπονται να εμφανίζονται μέχρι 256 χαρακτήρες στην συγκεκριμένη εκτύπωση (για εξοικονόμηση χώρου) και με επιλογή 'Πλήρης εμφάνιση (memo)'       
                        temp=temp[:256]+" (συνεχίζεται...)" #μέσω του κουμπιού εμφανίζεται το πλήρες κείμενο.                    
                    if len(temp)>k: #loop που αλλάζει γραμμή κάθε k=150 χαρακτήρες κειμένου.
                        n=1
                        while len(temp)>0:
                            final2=final2+temp[:n*k]+'\n'
                            temp=temp[n*k:]
                            if len(temp)<k:
                                final2=final2+temp
                                break
                            else:
                                n=n+1                                
                        notesMemo2.insert(INSERT, final2)
                        notesMemo2.config(fg="red")
                    else:
                        notesMemo2.insert(INSERT, str(printList2[i][1]))                
            backMemo=Button(Frame100, text="<<Επιστροφή", padx=33, pady=11, command=lambda: goto(116))
            backMemo.grid(row=1000, column=8, pady=15, padx=65)
            returnMemo=Button(Frame100, text="Κεντρικό μενού", padx=30, pady=11, command=lambda: goto(117))
            returnMemo.grid(row=1000, column=9, pady=15, padx=65)                    
    elif x==100: #προβολή ιστορικού ενεργειών (memo).
        Frame46.grid_forget()
        global Frame47
        global viewMemoDay2
        global viewMemoDay4     
        Frame47=LabelFrame(root, bd=0)
        Frame47.grid(row=5, column=0, columnspan=18)
        viewLabel=Label(Frame47, text="ΑΝΑΖΗΤΗΣΗ ΕΝΕΡΓΕΙΩΝ ΜΕ ΒΑΣΗ ΤΗΝ ΗΜΕΡΟΜΗΝΙΑ (ΙΣΤΟΡΙΚΟ)", fg="red",  bg="#d9d9d9", pady=25)
        viewLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        viewMemoDay1=Label(Frame47, text="Αρχική ημερομηνία:", fg="red")
        viewMemoDay1.grid(row=6, column=7, padx=5, pady=20, sticky=E)
        viewMemoDay2=Entry(Frame47, width=50, borderwidth=5, relief=SUNKEN)
        viewMemoDay2.grid(row=6, column=8, padx=5, pady=0)        
        viewMemoDay3=Label(Frame47, text="Τελική ημερομηνία:", fg="red")
        viewMemoDay3.grid(row=7, column=7, padx=5, pady=10, sticky=E)
        viewMemoDay4=Entry(Frame47, width=50, borderwidth=5, relief=SUNKEN)
        viewMemoDay4.grid(row=7, column=8, padx=5, pady=10)
        backMemo=Button(Frame47, text="<<Επιστροφή", padx=29, pady=11, command=lambda: goto(103))
        backMemo.grid(row=100, column=7, pady=45, padx=65)        
        viewMemoSubmit=Button(Frame47, text=" Υποβολή", padx=40, pady=11, command=lambda: goto(104)) 
        viewMemoSubmit.grid(row=100, column=8, padx=65, pady=45)
        returnMemo=Button(Frame47, text="Κεντρικό μενού", padx=23, pady=11, command=lambda: goto(108))
        returnMemo.grid(row=100, column=9, pady=45, padx=65)        
    elif x==101: #<<Επιστροφή στο μενού ενεργειών (memo) από τη φόρμα αναζήτησης ιστορικού ενεργειών (memo).
        insert(Frame46, 6)
    elif x==102: #<<Επιστροφή στο κεντρικό μενού από τη φόρμα αναζήτησης ιστορικού ενεργειών (memo).
        Frame46.grid_forget()
        menu()
    elif x==103: #<<Επιστροφή στο μενού ενεργειών (memo) από τη φόρμα αναζήτησης - προβολής ιστορικού ενεργειών (memo).
        Frame47.grid_forget()
        Frame36.grid(row=5, column=0, columnspan=18)
        goto(98)        
    elif x==104: #υποβολή ημ/νιών για έλεγχο (για προβολή ενεργειών (memo)).        
        Frame47.grid_forget()
        global Frame48
        Frame48=LabelFrame(root, bd=0)
        Frame48.grid(row=5, column=0, columnspan=18)
        global flag2
        flag2=1
        day1=viewMemoDay2.get()
        day1=day1.strip()
        date1=checkDate(day1)
        day2=viewMemoDay4.get()
        day2=day2.strip()
        date2=checkDate(day2)
        if (date1==0 or date2==0) or date1>date2: #date1>date2 --> η ημ/νία 'από...' είναι μεγαλύτερη από την ημ/νία 'έως...'.
            message="Μη έγκυρες ημερομηνίες, η ενέργεια ακυρώθηκε."
            flag2=0 #δείχνει σφάλμα.
        else:
            flag2=1
            global memoList            
            checkList=[]
            memoList=[]
            checkList.clear()
            memoList.clear()          
            if date1>=currentDate() and date2>=currentDate():
                with open("future.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)
                    for x in checkList:
                        if x[0]>=date1 and x[0]<=date2:
                            memoList.append(x)                   
            elif date1<currentDate() and date2<currentDate():
                with open("past.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)
                    for x in checkList:
                        if x[0]>=date1 and x[0]<=date2:
                            memoList.append(x)
            else:
                with open("past.csv", "r", newline="", encoding="utf-8") as file:
                    ro=csv.reader(file, delimiter='$')
                    for row in ro:
                        checkList.append(row)                    
                    for x in checkList:
                        if x[0]>=date1 and x not in memoList:
                            memoList.append(x)
                    checkList.clear()
                    with open("future.csv", "r", newline="", encoding="utf-8") as file:
                        ro=csv.reader(file, delimiter='$')
                        for row in ro:
                            checkList.append(row)
                        for x in checkList:
                            if x[0]<=date2 and x not in memoList:
                                memoList.append(x)
            if len(memoList)==0:
                flag2=2 #warning και ΟΧΙ σφάλμα δείχνει η τιμή 2. 
                message="Δε βρέθηκε καταχωρημένη ενέργεια (memo) σύμφωνα με τα κριτίρια αναζήτησης (από: "+date1[-2:]+"-"+date1[-4:-2]+"-"+date1[:4]+" έως: "+date2[-2:]+"-"+date2[-4:-2]+"-"+date2[:4]+")."                       
        if flag2==1:
            goto(107)
        else: #σφάλμα ή warning.
            if flag2==0: #error.
                messagebox.showerror('Σφάλμα:', message)
            else: #warning.
                messagebox.showwarning('Ενημέρωση:', message)
            memoAgain=Button(Frame48, text="Νέα αναζήτηση", padx=35, pady=11, command=lambda: goto(110))                              
            memoAgain.grid(row=30, column=8, padx=65, pady=45)                                
            memoReturn=Button(Frame48, text="Κεντρικό μενου", padx=35, pady=11, command=lambda: goto(106))                            
            memoReturn.grid(row=30, column=9, padx=65, pady=45)            
    elif x==105: #<<Επιστροφή στο μενού ενεργειών από τη φόρμα αναζήτησης ιστορικού ενεργειών (memo).
        insert(Frame48, 6)
    elif x==106: #<<Επιστροφή στο κεντρικό μενού μετά από αποτυχημένη αναζήτηση.
        Frame48.grid_forget()
        menu()
    elif x==107: #προβολή ενεργειών (memo). #bg="#f2f2f2"
        memoList=sorted(memoList, key= lambda i:i[0])#ταξινόμηση της λίστας εκτύπωσης με βάση την ημ/νία, πατέντα για να 'τραβήξω' τις ημ/νίες εκτύπωσης από την λίστα.
        #FrameForScroll.grid_forget()

        
        FrameForScroll=LabelFrame(root, bd=0) #scrollbar attempt!!!
        FrameForScroll.grid(row=5, column=0, columnspan=18)
        #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
        canvas=Canvas(FrameForScroll, bd=0, height=480, width=1220) 
        canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
        Frame48=LabelFrame(canvas, bd=0)
        scrollbar = Scrollbar(FrameForScroll, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=18, sticky=N+S)
        Frame48.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=Frame48, anchor="nw", width=2000)
        canvas.configure(yscrollcommand=scrollbar.set)
        Frame100=LabelFrame(FrameForScroll, bd=0)
        Frame100.grid(row=500, column=0, columnspan=18)



        showMemo=Label(Frame48, text="ΠΡΟΒΟΛΗ ΕΝΕΡΓΕΙΩΝ (MEMO) από: "+date1[-2:]+"-"+date1[-4:-2]+"-"+date1[:4]+" έως: "+date2[-2:]+"-"+date2[-4:-2]+"-"+date2[:4], fg="red",  bg="#d9d9d9", pady=25)
        showMemo.grid(row=5, column=0, columnspan=18, sticky=W+E)
        indexMemo=Label(Frame48, text="Α/Α", fg="red",  pady=10)
        indexMemo.grid(row=6, column=0, sticky=W+E)
        dateMemo=Label(Frame48, text="ΗΜ/ΝΙΑ", fg="red",  pady=10)
        dateMemo.grid(row=6, column=1)        
        notesMemo=Label(Frame48, text="ΕΝΕΡΓΕΙΕΣ", fg="red",  pady=10)
        notesMemo.grid(row=6, column=2, columnspan=17, sticky=W+E)
        for i in range(len(memoList)):
            aaMemo2=Text(Frame48, width=2, height=2, borderwidth=1, relief=SUNKEN, bg="#f2f2f2")
            aaMemo2.grid(row=7+i, column=0, pady=5)
            aaMemo2.insert(INSERT, str(i+1))
            dateMemo2=Text(Frame48, width=11, height=2, borderwidth=1, relief=SUNKEN, bg="#f2f2f2")
            dateMemo2.grid(row=7+i, column=1, pady=5)
            dateMemo2.insert(INSERT, memoList[i][0][-2:]+"-"+memoList[i][0][-4:-2]+"-"+memoList[i][0][:4])
            global memoText
            memoText=memoList[i][1]
            if len(memoText)>256: #επιτρέπονται να εμφανίζονται μέχρι 256 χαρακτήρες στην συγκεκριμένη εκτύπωση (για εξοικονόμηση χώρου) και με επιλογή 'Διόρθωση (memo)' μέσω                
                memoText=memoText[:256]+" (συνεχίζεται...)" #του κουμπιού εμφανίζεται το πλήρες κείμενο.                    
            notesMemo2=Text(Frame48, width=111, height=2, borderwidth=1, relief=SUNKEN, bg="#f2f2f2")
            notesMemo2.grid(row=7+i, column=2, columnspan=15, pady=5)
            notesMemo2.insert(INSERT, memoText)
            if len(memoText)>256:
                notesMemo2.config(fg="red")    
            alterMemo=Button(Frame48, text="Εμφάνιση (memo)", padx=20, pady=11, command=lambda i=i: changeMemo(memoList, i))                    
            alterMemo.grid(row=7+i, column=17, padx=10, pady=5)
        memoBack=Button(Frame100, text="<<Επιστροφή", padx=40, pady=11, command=lambda: goto(109))
        memoBack.grid(row=1000, column=8, pady=15, padx=65)
        memoReturn=Button(Frame100, text="Κεντρικό μενού", padx=37, pady=11, command=lambda: goto(108))
        memoReturn.grid(row=1000, column=12, pady=15, padx=65, sticky=E)           
    elif x==108: #<<Επιστροφή στο κεντρικό μενού από τη φόρμα αναζήτησης ιστορικού ενεργειών (memo).
        FrameForScroll.grid_forget()
        #Frame47.grid_forget()
        menu()
    elif x==109: #<<Επιστροφή στο κεντρικό μενού μετά από προβολή ενεργειών (memo).
        FrameForScroll.grid_forget()
        #Frame48.grid_forget()
        goto(98)
    elif x==110: #νέα αναζήτηση μετά από αποτυχημένη αναζήτηση ενεργειών (memo).
        Frame48.grid_forget()
        Frame46.grid(row=5, column=0, columnspan=18)
        goto(100)
    elif x==111: #<<Επιστροφή  στο μενού ενεργειών (memo) από την φόρμα εμφάνισης συγκεκριμένης ενέργειας (memo).
        insert(Frame49, 6)
    elif x==112: #<<Επιστροφή  στο κεντρικό μενού από την φόρμα εμφάνισης συγκεκριμένης ενέργειας (memo).
        Frame49.grid_forget()
        menu()
    elif x==113: #ανακατεύθυνση με προορισμό τη διόρθωση ενέργειας (memo).
        Frame49.grid_forget()
        Frame40=LabelFrame(root, bd=0)
        Frame40.grid(row=5, column=0, columnspan=18)        
        memoChange(checkList, m, l, 1, '')
    elif x==114: #ανακατεύθυνση με προορισμό τη διαγραφή ενέργειας (memo).
        Frame49.grid_forget()
        Frame40=LabelFrame(root, bd=0)
        Frame40.grid(row=5, column=0, columnspan=18)
        memoChange(checkList, x, l, 3, '')
    elif x==115: #<<Επιστροφή στον πίνακα των εγγραφών (αναζήτηση) μετά από πλήρη προβολή στοιχείων συγκεκριμένης εγγραφής.
        Frame17.grid_forget()
        goto(49)
    elif x==116: #<<Επιστροφή στο μενού εγγραφών (memo) μετά από εκτύπωση των σημερινών ενεργειών (memo).
        insert(FrameForScroll, 6)
    elif x==117: #<<Επιστροφή στο κεντρικό μενού μετά από εκτύπωση των σημερινών ενεργειών (memo).
        FrameForScroll.grid_forget()
        #Frame50.grid_forget()
        menu()
    elif x==118: #φόρμα εργ. συμβούλων.
        Frame52.grid_forget()
        global Frame53
        global kwdikos2
        global hmeromhnia2
        global sumvoulos2
        global paratiriseis2
        global ekthesi2
        Frame53=LabelFrame(root, bd=0)
        Frame53.grid(row=5, column=0, columnspan=18)
        titlos=Label(Frame53, text=" ΦΟΡΜΑ ΕΡΓΑΣΙΑΚΩΝ ΣΥΜΒΟΥΛΩΝ", fg="red", bg= "#d9d9d9", padx=7, pady=15)
        titlos.grid(row=5, column=1, columnspan=16, sticky=W+E)
        image5 = Image.open("unesco_form_1.jpg")
        photo5 = ImageTk.PhotoImage(image5)
        top_logo = Label(Frame53, image = photo5, bd=0)
        top_logo.image = photo5
        top_logo.grid(row=6, column=1, rowspan=3, sticky=W+S)
        kwdikos1=Label(Frame53, text="ΚΩΔΙΚΟΣ ΩΦΕΛΟΥΜΕΝΟΥ", pady=3)
        kwdikos1.grid(row=6, column=15, sticky=E)
        kwdikos2=Entry(Frame53, width=35, bd=1, relief=SUNKEN)
        kwdikos2.grid(row=6, column=16, sticky=E, pady=3)
        hmeromhnia1=Label(Frame53, text="ΗΜΕΡΟΜΗΝΙΑ", pady=3)
        hmeromhnia1.grid(row=7, column=15, sticky=E)
        hmeromhnia2=Entry(Frame53, width=35, bd=1, relief=SUNKEN)
        hmeromhnia2.grid(row=7, column=16, sticky=E, pady=3)
        sumvoulos1=Label(Frame53, text="ΕΡΓΑΣΙΑΚΟΣ ΣΥΜΒΟΥΛΟΣ", pady=3)
        sumvoulos1.grid(row=8, column=15, sticky=E)
        sumvoulos2=Entry(Frame53, width=35, bd=1, relief=SUNKEN)
        sumvoulos2.grid(row=8, column=16, sticky=E, pady=3)
        upografi1=Label(Frame53, text="ΥΠΟΓΡΑΦΗ ΕΡΓΑΣΙΑΚΟΥ ΣΥΜΒΟΥΛΟΥ", pady=1)
        upografi1.grid(row=9, column=15, sticky=E)
        upografi2=Entry(Frame53, width=35, bd=1, relief=SUNKEN)
        upografi2.grid(row=9, column=16, sticky=E, pady=3)
        signature=Label(Frame53, text="(υπογραφή)")
        signature.grid(row=11, column=1, columnspan=18)
        paratiriseis1=Label(Frame53, text="ΠΑΡΑΤΗΡΗΣΕΙΣ:")
        paratiriseis1.grid(row=13, column=1, columnspan=16, sticky=W)
        paratiriseis2=Text(Frame53, width=128, bd=3, relief=SUNKEN, height=12)
        paratiriseis2.grid(row=14, column=1, columnspan=16, pady=5, sticky=W)
        ekthesi1=Label(Frame53, text="ΕΚΘΕΣΗ ΕΡΓΑΣΙΑΚΟΥ ΣΥΜΒΟΥΛΟΥ", bd=0, font=("bold", 9))
        ekthesi1.grid(row=15, column=0, columnspan=18, pady=2, sticky=S)    
        ekthesi2=Text(Frame53, width=128, bd=3, relief=SUNKEN, height=3)
        ekthesi2.grid(row=16, column=1, columnspan=18, pady=3, sticky=W)
        Frame54=LabelFrame(Frame53, bd=0)
        Frame54.grid(row=100, column=0, columnspan=18)
        backMemo=Button(Frame54, text="<<Επιστροφή", padx=30, pady=11, fg="#ffffff", bg="red", command=lambda: fileHandler(2)) 
        backMemo.grid(row=100, column=7, pady=15, padx=80)       
        saveAs=Button(Frame54, text="Αποθήκευση", padx=33, pady=11, fg="#ffffff", bg="red", command=lambda: goto(125)) 
        saveAs.grid(row=100, column=10, pady=15, padx=80)          
        image6 = Image.open("unesco_form_2.jpg")
        photo6 = ImageTk.PhotoImage(image6)
        bottom_logo = Label(Frame54, image = photo6, bd=0)
        bottom_logo.image = photo6
        bottom_logo.grid(row=100, column=8, columnspan=2)            
    elif x==119: #<<Επιστροφή στην προβολή σημερινών ενεργειών (memo) μετά από πλήρη προβολή συγκεκριμένης ενέργειας (memo).
        Frame40.grid_forget()
        Frame46=LabelFrame(root, bd=0)
        Frame46.grid(row=5, column=0, columnspan=18)
        goto(99)
    elif x==120: #<<Επιστροφή στο κεντρικό μενού μετά από πλήρη προβολή συγκεκριμένης ενέργειας (memo).
        Frame40.grid_forget()
        menu()
    elif x==121: #<<Επιστροφή στη φόρμα ενέργειες (δελτίο) μετά από προβολή αυτών.
        status5=''        
        status2=""
        insert(FrameForScroll, 1)
    elif x==122: #<<Επιστροφή στο κεντρικό μενού  από τη διαχείριση αρχείων (φόρμας εργ. συμβούλου).
        Frame52.grid_forget()
        menu()
    elif x==123: #επανείσοδος στο πρόγραμμα από την τελική φόρμα (greetings()).
        root.destroy()
        main()
    elif x==124: #αναζήτηση αρχείου (memo).
        Frame52.grid_forget()
        global txt1
        txt1=''
        global txt2
        txt2=''
        global Frame56
        Frame56=LabelFrame(root, bd=0)
        Frame56.grid(row=5, column=0, columnspan=18)
        label=Label(Frame56, text="ΕΝΕΡΓΕΙΕΣ (MEMO)\nΔιαχείριση αρχείων (φόρμα εργ. συμβούλου) - Αναζήτηση αρχείου", fg="red", bg="#d9d9d9", pady=15)
        label.grid(row=5, column=0, columnspan=18, sticky=E+W)
        image5 = Image.open("unesco_form_1.jpg")
        photo5 = ImageTk.PhotoImage(image5)
        top_logo = Label(Frame56, image = photo5, bd=0)
        top_logo.image = photo5
        top_logo.grid(row=6, column=1, rowspan=3, sticky=W+S)
        kwdikos1=Label(Frame56, text="ΚΩΔΙΚΟΣ ΩΦΕΛΟΥΜΕΝΟΥ", pady=3)
        kwdikos1.grid(row=6, column=15, sticky=E)
        kwdikos2=Entry(Frame56, width=35, bd=1, relief=SUNKEN)
        kwdikos2.grid(row=6, column=16, sticky=E, pady=3)
        hmeromhnia1=Label(Frame56, text="ΗΜΕΡΟΜΗΝΙΑ", pady=3)
        hmeromhnia1.grid(row=7, column=15, sticky=E)
        hmeromhnia2=Entry(Frame56, width=35, bd=1, relief=SUNKEN)
        hmeromhnia2.grid(row=7, column=16, sticky=E, pady=3)
        sumvoulos1=Label(Frame56, text="ΕΡΓΑΣΙΑΚΟΣ ΣΥΜΒΟΥΛΟΣ", pady=3)
        sumvoulos1.grid(row=8, column=15, sticky=E)
        sumvoulos2=Entry(Frame56, width=35, bd=1, relief=SUNKEN)
        sumvoulos2.grid(row=8, column=16, sticky=E, pady=3)
        upografi1=Label(Frame56, text="ΥΠΟΓΡΑΦΗ ΕΡΓΑΣΙΑΚΟΥ ΣΥΜΒΟΥΛΟΥ", pady=1)
        upografi1.grid(row=9, column=15, sticky=E)
        upografi2=Entry(Frame56, width=35, bd=1, relief=SUNKEN)
        upografi2.grid(row=9, column=16, sticky=E, pady=3)
        signature=Label(Frame56, text="(υπογραφή)")
        signature.grid(row=11, column=1, columnspan=18)
        paratiriseis1=Label(Frame56, text="ΠΑΡΑΤΗΡΗΣΕΙΣ:")
        paratiriseis1.grid(row=13, column=1, columnspan=16, sticky=W)
        paratiriseis2=Text(Frame56, width=128, bd=3, relief=SUNKEN, height=12)
        paratiriseis2.grid(row=14, column=1, columnspan=16, pady=5, sticky=W)
        ekthesi1=Label(Frame56, text="ΕΚΘΕΣΗ ΕΡΓΑΣΙΑΚΟΥ ΣΥΜΒΟΥΛΟΥ", bd=0, font=("bold", 9))
        ekthesi1.grid(row=15, column=0, columnspan=18, pady=2, sticky=S)    
        ekthesi2=Text(Frame56, width=128, bd=3, relief=SUNKEN, height=3)
        ekthesi2.grid(row=16, column=1, columnspan=18, pady=3, sticky=W)
        Frame54=LabelFrame(Frame56, bd=0)
        Frame54.grid(row=100, column=0, columnspan=18)         
        image6 = Image.open("unesco_form_2.jpg")
        photo6 = ImageTk.PhotoImage(image6)
        bottom_logo = Label(Frame54, image = photo6, bd=0)
        bottom_logo.image = photo6
        bottom_logo.grid(row=100, column=8, columnspan=2)
        backMemo=Button(Frame54, text="<<Επιστροφή", padx=24, pady=11, command=lambda: goto(126)) 
        backMemo.grid(row=100, column=6, pady=12, padx=35)
        editMemo=Button(Frame54, text="Επεξεργασία", padx=24, pady=11, command=lambda: goto(129)) 
        editMemo.grid(row=100, column=7,pady=12, padx=35)        
        returnMemo=Button(Frame54, text="Διαγραφή", padx=25, pady=11, command=lambda: goto(128)) 
        returnMemo.grid(row=100, column=10, pady=12,  padx=35)
        returnMemo=Button(Frame54, text="Κεντρικό μενού", padx=21, pady=11, command=lambda: goto(127))
        returnMemo.grid(row=100, column=11, pady=12,  padx=35)         
        global path
        path= filedialog.askopenfilename(title="Select a file", filetypes=(("text files","*.txt"), ("all files","*.*")))        
        global txt
        txt=[]
        global arxeio
        with open(path, 'r', encoding='utf-8', newline="") as arxeio:
            for row in arxeio:
                txt.append(row)
        kwdikos2.insert(INSERT, txt[0])
        txt[1]=txt[1][:-1] #πατέντα για να κοπεί η αλλαγή γραμμής (που προσμετράται ως χαρακτήρας!!!).
        hmeromhnia2.insert(INSERT, txt[1][-2:]+"-"+txt[1][-4:-2]+"-"+txt[1][:4])  
        sumvoulos2.insert(INSERT, txt[2])
        for line in range(3, len(txt)):           
            if txt[line]=='ΠΑΡΑΤΗΡΗΣΕΙΣ:\n':
                temp1=[]
                for row in txt[3:line]: 
                    temp1.append(row)              
                txt1=''
                for element in temp1: #πατέντα για να εξαλειφθούν οι αλλαγές γραμμής ('\n') από το κείμενο και να μην εμφανιστούν στην προβολή των κειμένων.
                    if '\n' in element:
                        txt1+=str(element[:-1])+'\n'
                    else:
                        txt1+=str(element)        
                temp2=[]
                for row in txt[line+1:]: 
                    temp2.append(row)                
                txt2=''
                for element in temp2: #πατέντα για να εξαλειφθούν οι αλλαγές γραμμής ('\n') από το κείμενο και να μην εμφανιστούν στην προβολή των κειμένων.
                    if '\n' in element:
                        txt2+=str(element[:-1])+'\n'
                    else:
                        txt2+=str(element)
                paratiriseis2.insert(INSERT, txt1)
                ekthesi2.insert(INSERT, txt2)
                break             
    elif x==125: #ορισμός δεδομένων (ακολουθεί ο έλεχος ορθότητας στοιχειων και ανακατεύθυνση με στόχο την αποθήκευση αρχείου (memo)).
        global line1
        line1=kwdikos2.get()
        line1.strip()
        goto(130)
    elif x==126: #<<Επιστροφή στη φόρμα ενεργειών (memo) - διαχείρισης αρχείων από τη φόρμα αναζήτησης αρχείων (memo).
        Frame56.grid_forget()
        Frame36=LabelFrame(root, bd=0)
        Frame36.grid(row=5, column=0, columnspan=18)
        fileHandler(1)
    elif x==127: #<<Επιστροφή στο κεντρικό μενού από τη φόρμα αναζήτησης αρχείων (memo).
        Frame56.grid_forget()
        menu()
    elif x==128: #διαγραφή αρχείου (memo).
        os.remove(path)
        messagebox.showinfo('Διαγραφή αρχείου (memo):', 'Το αρχείο διαγράφηκε με επιτυχία.')
        kwdikos2.delete(0, END) #στα entry widgets στη μέθοδο .delete() παίρνει πρώτο όρισμα 0(!!!).
        hmeromhnia2.delete(0, END)
        sumvoulos2.delete(0, END)
        paratiriseis2.delete(1.0, END) #στα text widgets στη μέθοδο .delete() παίρνει πρώτο όρισμα 1.0(!!!).
        ekthesi2.delete(1.0, END)
    elif x==129: #επεξεργασία αρχείου (memo)--> Τροποποίηση δελτίου στοιχείων.
        os.remove(path)       
        Frame56.grid_forget()
        Frame36=LabelFrame(root, bd=0)
        Frame36.grid(row=5, column=0, columnspan=18)
        Frame53=LabelFrame(root, bd=0)
        Frame53.grid(row=5, column=0, columnspan=18)        
        line1=kwdikos2.get()
        line1.strip()
        line1=line1[:-1]  #πατέντα για να κρατήσει το πρόγραμμα μόνο τα ψηφία του κωδ. ΑΚΗΑ.'
        global status3 #για να γίνει η ενέργεια Τροποποίηση δελτίους.        
        status3='edit_file'        
        goto(130)
    elif x==130: #έλεχος ορθότητας στοιχειων και ανακατεύθυνση με στόχο την αποθήκευση αρχείου (memo).
        error=0
        global line2
        line2=hmeromhnia2.get()
        line2=line2.strip()
        line2=int(checkDate(line2))
        txt1=paratiriseis2.get('1.0', END)
        txt1=txt1.strip()
        if not line1.isdigit(): #έλεγχος ορθότητας κωδ. ΑΚΗΑ.
            messagebox.showerror('Σφάλμα:', 'Ο κωδικός ΑΚΗΑ πρέπει να αποτελείται μόνο από ψηφία,\nπαρακαλώ ελέγξτε την ακρίβεια των στοιχείων.')
            error=1
        if line2==0: #έλεγχος ορθότητας ημερομηνίας.
            messagebox.showerror('Σφάλμα:', 'Μη έγκυρη ημερομηνία, παρακαλώ ελέγξτε την ακρίβεια των στοιχείων.')
            error=1        
        temp=[]
        with open("current.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                temp.append(row)
            with open("previous.csv", "r", encoding="utf-8", newline="") as file:
                ro=csv.reader(file, delimiter='$')
                for record in ro:
                    if record[5] not in temp and record[6] not in temp and record[7] not in temp: #δεν υπάρχει εγγραφή εξυπηρετούμενου στο τρέχον αρχείο (με βάση τα: ΑΜΚΑ, ΑΦΜ, ΑΚΗΑ).
                        temp.append(record)
        global line4
        line4='' #αντιστοίχιση του κωδ. ΑΚΗΑ με το επώνυμο του εξυπηρετούμενου.
        for record in temp:
            if line1==record[7]:
                line4=record[0]
        if len(line4)==0:
            messagebox.showerror('Σφάλμα:', 'Δε βρέθηκε εξυπηρετούμενος με τον συγκεκριμένο κωδικό\nΑΚΗΑ, παρακαλώ ελέγξτε την ακρίβεια των στοιχείων.')
            error=1
        if len(txt1)==0:
            messagebox.showerror('Σφάλμα:', 'Το πεδίο των παρατηρήσεων δεν πρέπει να είναι κενό.')
            error=1
        if error==0:
            Frame53.grid_forget()
            Frame36=LabelFrame(Frame53, bd=0)
            Frame36.grid(row=100, column=0, columnspan=18)
            #if os.path.exists(arxeio):#περίπτωση τροποποιησης--> διαγραφή του προηγούμενου αρχείου (επιλογή αντί του 'w' - mode για την περίπτωση να 
                #os.remove(path) #τροποποιηθεί η ημερομηνία (στην περίπτωση αυτή θα δημιουργηθεί νέο αρχείο με διαφορετική ονομασία, καθώς το πρώτο τμήμα του ονόματος του αρχείου 
            fileHandler(3)   #ξεκινά με την ημερομηνία).
    elif x==131: #απενεργοποίηση (οριστική) δελτίου ανεργίας.
        temp1=[]
        with open("current.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                temp1.append(row)
            for record in temp1:
                if record[5]==y[i][5] and record[6]==y[i][6]: #έλεγχος ταυτοποίησης με βάση: ΑΜΚΑ, ΑΦΜ.
                    record[12]='ΟΧΙ'
        with open("current.csv", "w", encoding="utf-8", newline="") as file:
            wo=csv.writer(file, delimiter='$')
            for record in temp:
                wo.writerow(record)
            Frame21.grid_forget()
            Frame27=LabelFrame(root, bd=0)
            Frame27.grid(row=6, column=0, columnspan=18)
            messagebox.showinfo('', "Η απενεργοποίηση του δελτίου ανεργίας έγινε με επιτυχία.")
            returnActive=Button(Frame27, text="<<Επιστροφή", padx=40, pady=11, command=lambda: insert(Frame14, 1))
            returnActive.grid(row=10, column=8, padx=50, pady=25)
            menuActive=Button(Frame27, text="Κεντρικό μενού", padx=32, pady=11, command=lambda: goto(47))
            menuActive.grid(row=10, column=9, padx=50, pady=25)
    elif x==132: #ανακατεύθυνση για προβολή δελτίων που έχει ανοίξει το παράθυρο για ανανέωση.
        status5='active_cards'
        goto(69)
    elif x==133: #επιστροφή στο δευτερεύον μενού μετά από επιλογή τροποποίησης.
        Frame20.grid_forget()
        insert(FrameForScroll2, 1)
    elif x==134: #ανακατεύθυνση (επιστροφή) μετά από αποτυχημένη διαδικασία αναζήτησης (ή διαγραφής).
        if option==1:
            insert(Frame17, 3)
        else:
            insert(Frame17, 5)

def todayMemo(printList, i, num):#πλήρης προβολή επιλεγμένης ενέργειας (memo). Παίρνει τρία ορίσματα: printList--> η λίστα που γίνονται οι ενέργειες i--> το επιλεγμένο στοιχείο
    global status
    status=''
    FrameForScroll.grid_forget()  #num (1--> πλήρης προβολή, 2--> διόρθωση, 3--> ακύρωση)
    #Frame50.grid_forget()        
    if num==1: #πλήρης προβολή επιλεγμένης ενέργειας (memo).
        global Frame40
        Frame40=LabelFrame(root, bd=0)
        Frame40.grid(row=5, column=0, columnspan=18)        
        showLabel=Label(Frame40, text="ΠΡΟΒΟΛΗ ΣΗΜΕΡΙΝΏΝ ΕΝΕΡΓΕΙΩΝ (MEMO) ("+date[-2:]+"-"+date[-4:-2]+"-"+date[:4]+").", fg="red", bg="#d9d9d9", pady=25)
        showLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)                
        notesMemo=Label(Frame40, text="ΕΝΕΡΓΕΙΕΣ", fg="red")
        notesMemo.grid(row=6, column=1, columnspan=16, pady=10)
        notesMemo2=Text(Frame40, bd=0, width=111, height=20, borderwidth=1, relief=SUNKEN)
        notesMemo2.grid(row=7, column=0, columnspan=16, rowspan=3) 
        notesMemo2.insert(INSERT, str(printList[i][1]))
        backMemo=Button(Frame40, text="<<Επιστροφή", padx=28, pady=11, command=lambda: goto(119))
        backMemo.grid(row=1000, column=7, pady=25, padx=45)        
        alterMemo=Button(Frame40, text="Διόρθωση", padx=39, pady=11, command=lambda: todayMemo(printList, i, 2))
        alterMemo.grid(row=1000, column=8, padx=15)
        alterMemo=Button(Frame40, text="Ακύρωση", padx=40, pady=11, command=lambda: todayMemo(printList, i, 3))
        alterMemo.grid(row=1000, column=9, padx=15)
        returnMemo=Button(Frame40, text="Κεντρικό μενού", padx=25, pady=11, command=lambda: goto(120))
        returnMemo.grid(row=1000, column=10, pady=25, padx=45)        
    else:
        Frame40.grid_forget()                
        if num==2: #διόρθωση επιλεγμένης ενέργειας (memo) --> ανακατεύθυνση για Τροποποίηση δελτίου ενέργειας (memo).
            memoChange(tempList, printList2, i, 1, 'today')
        elif num==3: #ακύρωση επιλεγμένης ενέργειας (memo) --> ανακατεύθυνση για ακύρωση ενέργειας (memo).
            memoChange(tempList, printList, i, 3, 'today')
                
def changeMemo(x, i): #διόρθωση εγγραφής (memo) --> επιλογή μέσω της προβολής ενεργειών (memo). x--> λίστα ενεργειών (memo), i--> επιλεγμένη ενέργεια (memo).
    global l
    l=i
    global m
    m=x
    FrameForScroll.grid_forget()
    #Frame48.grid_forget()
    global Frame49
    Frame49=LabelFrame(root, bd=0)
    Frame49.grid(row=5, column=0, columnspan=18)
    showMemo=Label(Frame49, text="ΕΝΕΡΓΕΙΕΣ (MEMO) ΤΗΣ "+x[i][0][-2:]+"-"+x[i][0][-4:-2]+"-"+x[i][0][:4]+".", fg='red', bg="#d9d9d9", pady=25)
    showMemo.grid(row=5, column=0, columnspan=18, sticky=W+E)
    dayMemo1=Label(Frame49, text='ΗΜΕΡΟΜΗΝΙΑ', fg="red", pady=10)
    dayMemo1.grid(row=6, column=0, sticky=W+E)                
    notesMemo1=Label(Frame49, text="ΕΝΕΡΓΕΙΕΣ", fg="red", pady=10)
    notesMemo1.grid(row=6, column=2, sticky=W+E, columnspan=15)               
    dayMemo2=Text(Frame49,width=15, borderwidth=1, relief=SUNKEN, height=10, bg="#f2f2f2")                  
    dayMemo2.grid(row=7, column=0, sticky=N, pady=5)
    dayMemo2.insert(INSERT, str(x[i][0][-2:]+"-"+x[i][0][-4:-2]+"-"+x[i][0][:4]))
    notesMemo2=Text(Frame49, width=111, borderwidth=1, relief=SUNKEN, height=10, bg="#f2f2f2")
    notesMemo2.grid(row=7, column=2, columnspan=15, pady=5)
    notesMemo2.insert(INSERT, x[i][1])
    changeBack=Button(Frame49, text="<<Επιστροφή", padx=27, pady=11, command=lambda: goto(111))
    changeBack.grid(row=100, column=7, padx=45, pady=25)
    if x[i][0]>=currentDate(): #επιτρέπονται διόρθωση/ακύρωση ενέργειας (memo) ΜΟΝΟ για τρέχουσες ενέργειες!
        global checkList
        checkList=[]
        with open("future.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                checkList.append(row)
        changeAlter=Button(Frame49, text="Διαγραφή", padx=38, pady=11, command=lambda: goto(114))#παίρνει 4 ορίσματα!!!
        changeAlter.grid(row=100, column=8, padx=45, pady=25)
        changeDel=Button(Frame49, text="Διορθωση", padx=35, pady=11, command=lambda: goto(113))
        changeDel.grid(row=100, column=9, padx=45, pady=25)        
    changeReturn=Button(Frame49, text="Κεντρικό μενού", padx=22, pady=11, command=lambda: goto(112))
    changeReturn.grid(row=100, column=10, padx=45, pady=25)        
            
def currentDate():#υπολογισμός τρέχουσας ημ/νίας και δημιουργία string.
    x = str(datetime.date.today())  #current date
    x=x.split('-')
    x="".join(x)                    #current date as one string!
    return x
    
def memoChange(k, y, i, num, status):     
    if num==1: #πρώτη κλήση της function, προβολή της επιλεγμένης ενέργειας (memo) και υποβολή της διόρθωσής της. Για num==2 --> έλεγχος και οριστική Τροποποίηση δελτίου (ή μήνυμα σφάλματος).
        global dayMemo2        #Για num==3 --> ακύρωση ενέργειας (memo). Παίρνει τέσσερα ορίσματα (k--> συνολική λίστα, y--> επιλεγμένη λίστα (με βάση την ημερομηνία), i--> επιλεγμένο 
        global aaMemo2         #στοιχείο της λίστας y, num-->βλ. πιο πάνω), status--> βοηθητικός δείκτης.        
        global notesMemo2
        #Frame40.grid_forget()
        global Frame41
        Frame41=LabelFrame(root, bd=0)
        Frame41.grid(row=5, column=0, columnspan=18)                 
        changeMemo=Label(Frame41, text="ΤΡΟΠΟΠΟΙΗΣΗ ΕΓΓΡΑΦΗΣ (memo)", fg="red", bg="#d9d9d9", pady=25)
        changeMemo.grid(row=5, column=0, columnspan=18, sticky=W+E)
        dayMemo1=Label(Frame41, text='ΗΜΕΡΟΜΗΝΙΑ', fg="red", pady=10)
        dayMemo1.grid(row=6, column=0, sticky=W)                
        notesMemo1=Label(Frame41, text="ΕΝΕΡΓΕΙΑ", fg="red", pady=10)
        notesMemo1.grid(row=6, column=2, sticky=W+E, columnspan=15)    
        dayMemo2=Text(Frame41,width=15, borderwidth=1, relief=SUNKEN, height=8)                  
        dayMemo2.grid(row=7, column=0)        
        dayMemo2.insert(INSERT, str(y[i][0][-2:])+"-"+str(y[i][0][-4:-2])+"-"+str(y[i][0][:4]))
        notesMemo2=Text(Frame41, width=150, borderwidth=1, relief=SUNKEN, height=8)
        notesMemo2.grid(row=7, column=2, columnspan=15)
        notesMemo2.insert(INSERT, y[i][1])
        newAlter=Button(Frame41, text="Οριστική Τροποποίηση δελτίου", padx=5, pady=11, command=lambda: memoChange(k, y, i, 2, status))
        newAlter.grid(row=1000, column=9, padx=65, pady=25)
        backAlter=Button(Frame41, text="<<Επιστροφή", padx=28, pady=11, command=lambda: goto(85))
        backAlter.grid(row=1000, column=8, padx=65, pady=25)
        menuAlter=Button(Frame41, text="Κεντρικό μενού", padx=26, pady=11, command=lambda: goto(84))
        menuAlter.grid(row=1000, column=10, padx=65, pady=25)        
    else:
        #global status
        #if status!='today':
        Frame41.grid_forget()
        if num==2: #έλεγχος και οριστική Τροποποίηση δελτίου ενέργειας (memo) ή μήνυμα σφάλματος.
            global Frame42
            Frame42=LabelFrame(root, bd=0)
            Frame42.grid(row=5, column=0, columnspan=18)
            if status!='today':
                day=dayMemo2.get('1.0', END)
                day=day[:-1]              
                Frame41.grid_forget()           
                date=checkDate(day)
                if date==0:
                    text1="Μη έγκυρη ημερομηνία, η Τροποποίηση δελτίου ακυρώθηκε."
                    flag=0 
            else:            
                date=currentDate()            
            notes=notesMemo2.get('1.0', END) 
            notes=notes[:-1] #πατέντα, για να φύγουν τα "".           
            if len(notes)==0:
                text1="Δε βρέθηκε κείμενο στις σημειώσεις, η Τροποποίηση δελτίου ακυρώθηκε."
                flag=0            
            else: #έγκυρη Τροποποίηση δελτίου.                                
                for record in k:
                    if y[i]==record:
                        record[0]=date
                        record[1]=notes                       
                        break                                  
                if date>=currentDate(): #ανάλογα με την τιμή της νέας ημ/νίας, άνοιγμα του αντίστοιχου αρχείου και εγγραφή σε αυτό.
                    with open("future.csv", "w", encoding="utf-8", newline="") as file:
                        wo=csv.writer(file, delimiter='$')
                        for record in k:
                            wo.writerow(record)                    
                else:
                    with open("past.csv", "w", encoding="utf-8", newline="") as file:
                        wo=csv.writer(file, delimiter='$')                    
                        for record in k:
                            wo.writerow(record)  
                text1="Η ενέργεια (memo) τροποποιήθηκε με επιτυχία."
                flag=1
            if flag==0:
                messagebox.showerror('Σφάλμα:', text1)
            else:
                messagebox.showinfo('', text1)
            backAlter=Button(Frame42, text="<<Επιστροφή", padx=28, pady=11, command=lambda: goto(87))
            backAlter.grid(row=1000, column=8, padx=65, pady=25)
            menuAlter=Button(Frame42, text="Κεντρικό μενού", padx=26, pady=11, command=lambda: goto(86))
            menuAlter.grid(row=1000, column=10, padx=65, pady=25)
        elif num==3: #ακύρωση ενέργειας (memo).
            global Frame44
            Frame44=LabelFrame(root, bd=0)
            Frame44.grid(row=5, column=0, columnspan=18)
            delMemo=Label(Frame44, text="ΑΚΥΡΩΣΗ ΕΓΓΡΑΦΗΣ (memo)", fg="red", bg="#d9d9d9", pady=25)
            delMemo.grid(row=5, column=0, columnspan=18, sticky=W+E)
            dayMemo1=Label(Frame44, text='ΗΜΕΡΟΜΗΝΙΑ', fg="red", pady=10)
            dayMemo1.grid(row=6, column=0, sticky=W)                
            notesMemo1=Label(Frame44, text="ΕΝΕΡΓΕΙΑ", fg="red", pady=10)
            notesMemo1.grid(row=6, column=2, sticky=W+E, columnspan=15)    
            dayMemo2=Text(Frame44,width=15, borderwidth=1, relief=SUNKEN, height=8)                  
            dayMemo2.grid(row=7, column=0)
            dayMemo2.insert(INSERT, str(y[i][0][-2:]+"-"+y[i][0][-4:-2]+"-"+y[i][0][:4]))
            notesMemo2=Text(Frame44, width=150, borderwidth=1, relief=SUNKEN, height=8)
            notesMemo2.grid(row=7, column=2, columnspan=15)
            notesMemo2.insert(INSERT, y[i][1])
            backAlter=Button(Frame44, text="<<Επιστροφή", padx=29, pady=11, command=lambda: goto(94)) 
            backAlter.grid(row=1000, column=8, padx=65, pady=25)        
            newAlter=Button(Frame44, text="Οριστική διαγραφή", padx=15, pady=11, command=lambda: memoChange(k, y, i, 4, status))
            newAlter.grid(row=1000, column=9, padx=65, pady=25)
            menuAlter=Button(Frame44, text="Κεντρικό μενού", padx=26, pady=11, command=lambda: goto(95)) 
            menuAlter.grid(row=1000, column=10, padx=65, pady=25)
        elif num==4: #οριστική διαγραφή ενέργειας (memo).
            if status=='today':
                day=currentDate()            
            else:
                day=dayMemo2.get('1.0', END)
            Frame44.grid_forget()            
            global Frame45
            Frame45=LabelFrame(root, bd=0)
            Frame45.grid(row=5, column=0, columnspan=18)
            global temp
            temp=[]
            with open("future.csv", "r", encoding="utf-8", newline="") as file:
                ro=csv.reader(file, delimiter='$')
                for row in ro:
                    temp.append(row)
            for record in temp: #εντοπισμός - στην λίστα - της ενέργειας (memo) που ειναι προς διαγραφή και απομάκρυνσή της από αυτή.
                if y[i]==record:
                    temp.pop(temp.index(record))
                    break
            with open("future.csv", "w", encoding="utf-8", newline="") as file:
                wo=csv.writer(file, delimiter='$')
                for row in temp:
                    wo.writerow(row)
            messgabox.showinfo('', "Η ενέργεια (memo) διαγράφηκε με επιτυχία.")
            delNew=Button(Frame45, text="Νέα διαγραφή", padx=30, pady=11, command=lambda: goto(96)) 
            delNew.grid(row=101, column=8, pady=15, padx=65)
            delMenu=Button(Frame45, text="Κεντρικό μενού", padx=28, pady=11, command=lambda: goto(91)) 
            delMenu.grid(row=101, column=9, pady=15, padx=65)
        elif x==5: #ανακατεύθυνση για Τροποποίηση δελτίου εγγραφής (memo).
            Frame51.grid_forget() 
            memoChange(tempList, printList2, i, 2, '')
  
def tropopoiisi (k, i): #οριστική Τροποποίηση δελτίου στοιχείων δελτίου ανεργίας.
    a=surnamePrint2.get()    
    a=a.split()
    a[0].upper() #πατέντα, για να κάνει κεφαλαία τα περιεχόμενα της λίστας(!!!) a[].
    k[i][0]==a[0]    
    b=namePrint2.get()   
    b=b.split()
    b[0].upper() #πατέντα, για να κάνει κεφαλαία τα περιεχόμενα της λίστας(!!!) b[].
    k[i][1]=b[0]    
    k[i][2]=cardPrint2.get()
    k[i][5]=amkaPrint2.get()
    k[i][6]=afmPrint2.get()
    k[i][7]=akhaPrint2.get()
    k[i][8]=DYPA1Print2.get()
    k[i][9]=DYPA2Print2.get()
    k[i][10]=TAXIS1Print2.get()
    k[i][11]=TAXIS2Print2.get()
    a=activePrint2.get()
    k[i][12]=a.upper()
    b=planPrint2.get()
    k[i][13]=b.upper()
    k[i][14]=telPrint2.get()
    k[i][15]=mailPrint2.get()
    k[i][16]=notesPrint2.get(1.0, END)
    k[i][16]=k[i][16][:-1] #πατέντα για να φύγουν τα "".  
    if k[i][16]=="": #πατέντα, αν μείνει κενό το πεδίο των παρατηρήσεων, δημιουργούμε ένα whitespace, ώστε να αποκτήσει len() το πεδίο και να μπει η ',' στο .csv (αλλιώς ΔΕΝ ΜΠΑΙΝΕΙ!)
        k[i][16]=" "
    a=update11Print2.get()    
    b=update21Print2.get()    
    if checkDate(a)==0 or checkDate(b)==0 or checkDate(a)>checkDate(b):
        messagebox.showerror('Σφάλμα:', 'Μη έγκυρη ημερομηνία, η ενέργεια ακυρώθηκε.')
    else: #επιτυχής  ολοκλήρωση τροποποίησης.
        k[i][3]=checkDate(a)
        k[i][4]=checkDate(b)  
        Frame21.grid_forget()
        global Frame32
        Frame32=LabelFrame(root, bd=0)
        Frame32.grid(row=5, column=0, columnspan=18)
        temp=[]
        with open("current.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                temp.append(row)
        for record in temp: #εντοπισμός της εγγραφής που τροποποιήθηκαν τα στοιχεία και αντικατάστασής της με την νέα (τροποποιημένη) εγγραφή. -->με βάση: ΑΜΚΑ, ΑΦΜ.
            if record[5]==k[i][5] and record[6]==k[i][6]:
                for j in range(len(record)):
                    if record[j]!=k[i][j] and k[i][j]!="":
                        record[j]=k[i][j]
        with open("current.csv", "w", encoding="utf-8", newline="") as file:
            wo=csv.writer(file, delimiter='$')
            for row in temp:
                wo.writerow(row)
        messagebox.showinfo('', "Η Τροποποίηση δελτίου του δελτίου πραγματοποιήθηκε με επιτυχία.")
    newAlter=Button(Frame32, text="Νέα Τροποποίηση δελτίου", padx=10, pady=11, command=lambda: goto(56))
    newAlter.grid(row=100, column=8, padx=65, pady=15)
    returnAlter=Button(Frame32, text="Κεντρικό μενού", padx=42, pady=11, command=lambda: goto(57))
    returnAlter.grid(row=100, column=9, padx=65, pady=15)
    
def alter(x, k): #παίρνει δύο ορίσματα -->x, το Frame που καταργείται και -->k, το στοιχείο που επιλέχθηκε από την προηγούμενη φόρμα (φόρμα Τροποποίηση δελτίους).
    x.grid_forget()
    global Frame19
    Frame19=LabelFrame(root, bd=0)
    Frame19.grid(row=5, column=0, columnspan=18)
    surname=surnameAlter2.get()
    card2=cardAlter2.get()
    amka2=amkaAlter2.get()
    afm2=afmAlter2.get()
    akha2=akhaAlter2.get()
    errorFlag=0
    message=""
    surname=surname.strip()
    surname=surname.upper()
    if k==0 and len(surname)==0:
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, το πεδίο ΕΠΩΝΥΜΟ δεν επιτρέπεται να είναι κενό."
    card2=card2.strip()
    card2=card2.split() #κόψιμο κενών ανάμεσα στα ψηφία του κωδικού της κάρτας ΔΥΠΑ.
    card=""
    for i in card2:
        card=card+i
    card=card.strip()
    if k==1 and not card.isdigit(): #σωστός κωδικός δελτίου ανεργίας.
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, ο κωδικός του δελτίου ανεργίας πρέπει να περιέχει (16) ψηφία."
    amka2=amka2.strip()
    amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
    amka=""
    for i in amka2:
        amka=amka+i    
    if k==2 and (not (amka.isdigit() and len(amka)==11)): #σωστός ΑΜΚΑ
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, ο ΑΜΚΑ πρέπει να περιέχει (11) ψηφία."
    afm2=afm2.strip()
    afm2=afm2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
    afm=""
    for i in afm2:
        afm=afm+i
    if k==3 and (not (afm.isdigit() and len(afm)==9)): #σωστός ΑΜΚΑ--> τα κριτίρια της παρένθεσης.
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, ο ΑΦΜ πρέπει να περιέχει (9) ψηφία."
    akha2=akha2.strip()
    akha2=akha2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΚΗΑ
    akha=""
    for i in akha2:
        akha=akha+i    
    if k==4 and (not akha.isdigit()): #σωστός κωδικός ΑΚΗΑ
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, ο κωδικός ΑΚΗΑ περιλαμβάνει μόνο ψηφία."
    if errorFlag==1:
        newAlter=Button(Frame19, text="Νέα Τροποποίηση δελτίου", padx=20, pady=11, command=lambda: goto(36))
        newAlter.grid(row=10, column=8, padx=50, pady=35)
        returnAlter=Button(Frame19, text="Κεντρικό μενού", padx=32, pady=11, command=lambda: goto(35))
        returnAlter.grid(row=10, column=9, padx=50, pady=35)
        message=message[:-1]+", η ενέργεια ακυρώθηκε."
        messagebox.showerror('Σφάλμα:', message)        
    else:
        tempList1=[]
        tempList2=[]
        searchList=[surname, card, amka, afm, akha]
        global printList
        printList=[]
        global criterion
        criterion=["ΕΠΩΝΥΜΟ", "ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ", "ΑΜΚΑ", "ΑΦΜ", "ΚΩΔΙΚΟΣ ΑΚΗΑ"]        
        with open("previous.csv", "r", encoding="utf-8", newline="") as file: #στο 'previous.csv' καταχωρούνται τα διεγραμμένα και τα τροποποιημένα δελτία, ώστε αν χρειαστεί 
            ro=csv.reader(file, delimiter='$')                                #κάτι από αυτά να μπορούμε να τα επανακτήσουμε ή και να τα επαναφέρουμε εξολοκλήρου.
            for row in ro:
                tempList1.append(row)
        with open("current.csv", "r", encoding="utf-8", newline="") as file: #ενεργά και ανενεργά δελτία ανεργίας, αλλά ΟΧΙ διεγραμμένα.
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                tempList2.append(row)            
            for record in tempList1: #κόψιμο διπλοεγγραφής.
                if (record[5] not in tempList2) and (record[6] not in tempList2) and (record[7] not in tempList2): #έλεγχος με βάση τους: ΑΜΚΑ, ΑΦΜ και κωδ. ΑΚΗΑ.
                    tempList2.append(record)           
            for record in tempList2:
                if searchList[k] in record: #έλεγχος αν η τιμή του κριτιρίου αναζήτησης (πχ τιμή ΑΜΚΑ) αντιστοιχεί σε εγγραφή στο σύστημα (αν ΝΑΙ, εγγραφή στην λίστα για εκτύπωση).
                    printList.append(record)            
            if len(printList)==0:                
                messagebox.showwarning('', "Δε βρέθηκαν εγγραφές στο σύστημα σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+").")
            else:
                newAlter=Button(Frame19, text="<<Επιστροφή", padx=40, pady=11, command=lambda: goto(40))
                newAlter.grid(row=1000, column=8, padx=50,  pady=25)            
                returnAlter=Button(Frame19, text="Κεντρικό μενού", padx=35, pady=11, command=lambda: goto(35))
                returnAlter.grid(row=1000, column=9, padx=50,  pady=25)                
                if len(printList)==1:
                    message="Βρέθηκε μία εγγραφή στο σύστημα σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+")."
                else:
                    message="Βρέθηκαν "+str(len(printList))+" εγγραφές στο σύστημα σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+")."
                messagebox.showinfo('', message)
                showAlter=Button(Frame19, text="Εμφάνιση", padx=40, pady=11, command=lambda criterion=criterion[k]: goto(32)) 
                showAlter.grid(row=1000, column=11, padx=50, pady=25)

                    
def checkDate(date): #έλεγχος αν η ημερομηνία είναι σωστή
    if '/' not in date and '-' not in date or len(date)<=5 or len(date)>10:
        return 0
    else:         
        if date[-3] in ['/', '-']:
            year='20'+date[-2:]
        elif date[-5] in ['/', '-']:
            year=date[-4:]
        else:
            return 0
        if len(date)>8 and date[-8] in ['/', '-']:
            month=date[-7:-5]
            day=date[-len(date):-8]
        elif len(date)>6 and date[-6] in ['/', '-']:
            month=date[-5:-3]
            day=date[-len(date):-6]
            if '/' in month or '-' in month:
                return 0
        elif len(date)>7 and date[-7] in ['/', '-']:
            month='0'+date[-6]
            day=date[-len(date):-7]
        elif len(date)>5 and date[-5] in ['/', '-']:
            if date[-4] not in year:
                month='0'+date[-4]
                day=date[-len(date):-5]
            else:
                return 0                    
        if '/' in day or '-' in day or len(day)>2 or len(day)==0:
            return 0                
        elif len(day)==1:
            day='0'+day
    finalDate=year+month+day
    return finalDate            
        
def show1():
    global Frame2
    global today
    global fail
    global z
    global toDoList
    global doneList
    global futureList
    copyPrevious=[]
    backupCurrent=[]
    tempMemo=[]
    toDoList=[]
    doneList=[]
    futureList=[]
    with open("current.csv", "r", newline="", encoding="utf-8") as file:
        temp=[]
        today=[]
        fail=[]
        rest=[]
        ro=csv.reader(file, delimiter='$')
        for row in sorted(ro, key=lambda j:j[4]): #ταξινόμηση με βάση την καταληκτική ημερομηνία ανανέωσης ενεργών δελτίων.
            temp.append(row)
        for y in temp:
            if currentDate() >= y[3] and currentDate()<=y[4] and y[12]=='ΝΑΙ': #ενεργοί χρήστες που έχει ανοίξει το παράθυρο ανανέωσης της κάρτας τους.        
                today.append(y)                        
            elif currentDate()<y[3]: #ενεργοί χρήστες που ΔΕΝ έχει ανοίξει το παράθυρο ανανέωσης της κάρτας τους.       
                rest.append(y) 
            elif currentDate()>y[4] and y[12]=='ΝΑΙ': #ενεργοί χρήστες που φαίνονται να μην ανανεώθηκε έγκαιρα (ή που ανανεώθηκε και δεν έχει περαστεί στο σύστημα) η κάρτα τους.    
                fail.append(y)
        Frame2=LabelFrame(root, bd=0)
        Frame2.grid(row=5, column=0, columnspan=18)
        title=Label(Frame2, pady=25, fg="red", bg="#d9d9d9", text="ΕΚΚΡΕΜΟΤΗΤΕΣ ΗΜΕΡΑΣ")
        title.grid(row=4, column=0, columnspan=18, sticky=W+E)
        if len(fail)==0:
            message="" 
        else: #βρέθηκαν δελτία που φαίνονται να μην ανανεώθηκαν στο διάστημα που προβλεπόταν, θα εμφανίζεται μήνυμα προτροπής χειροκίνητου ελέγχου μέσα στο site της ΔΥΠΑ.
            global failMessage
            global failShow
            message="Υπάρχουν ενεργοί χρήστες που τα δελτία ανεργίας τους φαίνονται να μην έχουν ανανεωθεί, \nσυνιστάται έλεγχος των δελτίων αυτών στο site της ΔΥΠΑ."
            failMessage=Label(Frame2, text=message, pady=15, fg="red", padx=45)
            failMessage.grid(row=50, column=6, columnspan=5, sticky=W+E)
            failShow=Button(Frame2, text="Εμφάνιση δελτίων", padx=25, pady=11, command=lambda: goto(12)) 
            failShow.grid(row=50, column=14, pady=25)
        if len(today)==0: #ΔΕΝ υπάρχουν ανοιχτές εκκρεμότητες ανανέωσης δελτίων
            empty=Label(Frame2, text="\nΔεν υπάρχουν αυτήν την στιγμή δελτία ανεργίας για ανανέωση.", pady=10)
            empty.grid(row=65, column=0, columnspan=18, sticky=W+E) 
        else: #υπάρχουν ανοιχτές εκκρεμότητες ανανέωσης δελτίων
            global last
            global resultToday
            last2=today[len(today)-1][4] #η απώτατη ανοιχτή ημερομηνία για ανανέωση ενεργής κάρτας.
            last=last2[-2:]+"-"+last2[-4:-2]+"-"+last2[:4]  #μορφοποίηση της παραπάνω ημερομηνίας (ηη-μμ-εεεε).
            if len(today)==1:
                resultToday=Label(Frame2, text="\nΒρέθηκε "+ str(len(today))+" δελτίο ανεργίας για ανανέωση.", padx=45)
                resultToday.grid(row=65, column=6, columnspan=5, sticky=W+E) 
            else:
                global results
                resultToday=Label(Frame2, text="\nΒρέθηκαν συνολικά "+ str(len(today))+" δελτία ανεργίας για ανανέωση.", padx=45)
                resultToday.grid(row=65, column=6, columnspan=5, sticky=W+E)               
            results=Button(Frame2, text="Εμφάνιση δελτίων", padx=25, pady=11, command= lambda: goto(13)) 
            results.grid(row=65, column=14, pady=25)
    with open("future.csv", "r", encoding="utf-8", newline="") as file:
        ro=csv.reader(file, delimiter='$')
        for row in ro:
            tempMemo.append(row)        
        for k in tempMemo:
            if currentDate()==k[0]:
                toDoList.append(k)
            elif currentDate()>k[0]:
                doneList.append(k)
            else:
                futureList.append(k)
        if len(toDoList)==0:
            #x=str(currentDate())
            actions=Label(Frame2, text="\nΔεν υπάρχουν προγραμματισμένες ενέργειες για σήμερα ("+str(currentDate()[-2:])+"-"+str(currentDate()[-4:-2])+"-"+str(currentDate()[:4])+").", padx=45)
            actions.grid(row=70, column=0, columnspan=18, sticky=W+E)
        else: 
            if len(toDoList)==1:
                actions=Label(Frame2, text="\nΒρέθηκε "+ str(len(toDoList))+" προγραμματισμένη ενέργεια για σήμερα ("+str(currentDate()[-2:])+"-"+str(currentDate()[-4:-2])+"-"+str(currentDate()[:4])+").", padx=45)
                actions.grid(row=70, column=6, columnspan=5, sticky=W+E)
            elif len(toDoList)>1:
                actions=Label(Frame2, text="\nΒρέθηκαν συνολικά "+ str(len(toDoList))+" προγραμματισμένες ενέργειες για σήμερα ("+str(currentDate()[-2:])+"-"+str(currentDate()[-4:-2])+"-"+str(currentDate()[:4])+").", padx=45)
                actions.grid(row=70, column=6, columnspan=5, sticky=W+E)
            enterMemo=Button(Frame2, text="Εμφάνιση ενεργειών", padx=20, pady=11, command=lambda: show2(1)) 
            enterMemo.grid(row=70, column=14, pady=25)
        if len(doneList)>0:
            actions2=Label(Frame2, text="\nΥπάρχουν προγραμματισμένες ενέργειες προηγούμενων ημερών \nπερασμένες στο σύστημα που δεν έχετε δει.", padx=45, fg="red")
            actions2.grid(row=60, column=6, columnspan=5, sticky=E)
            actions3=Button(Frame2, text="Εμφάνιση ενεργειών", padx=20, pady=11, command= lambda: show2(2)) 
            actions3.grid(row=60, column=14, pady=25)
        global Frame10
        global enterMenu 
        global back
        Frame10=LabelFrame(Frame2, bd=0)
        Frame10.grid(row=500, column=0, columnspan=18)        
        exitMenu=Button(Frame10, text="Έξοδος", padx=50, pady=11, command=lambda:  goto(1))
        exitMenu.grid(row=500, column=8, padx=65, pady=35, sticky=E)
        enterMenu=Button(Frame10, text="Κεντρικό Μενού", padx=27, pady=11, command=lambda:  goto(8))
        enterMenu.grid(row=500, column=9, padx=65, pady=35, sticky=E)        
        
def show2(m): #παίρνει μία παράμετρο --> (1) αν πρόκειται για τρέχουσες ενέργειες και (2) αν πρόκειται για ενέργειες προηγούμενων ημερών που δεν έχει ενημερωθεί ο χρήστης.
    Frame2.grid_forget()
    Frame7=LabelFrame(root, bd=0)
    Frame7.grid(row=5, column=0, columnspan=18)
    global Frame12
    Frame12=LabelFrame(root, bd=0)
    Frame12.grid(row=5, column=0, columnspan=18)
    global message
    global toDoList
    if m==1:
        message="ΠΡΟΓΡΑΜΜΑΤΙΣΜΕΝΕΣ ΕΝΕΡΓΕΙΕΣ ΓΙΑ ΣΗΜΕΡΑ ("+str(toDoList[0][0][-2:])+"-"+str(toDoList[0][0][-4:-2])+"-"+str(toDoList[0][0][:4])+")."
        memoLabel=Label(Frame12, text=message, fg="red", bg= "#d9d9d9", pady=25)
        memoLabel.grid(row=6, column=0, columnspan=18, sticky=W+E)        
        for i in range(len(toDoList)):
            memoDate=Text(Frame12, bd=0, width=12, height=3, borderwidth=1, relief=SUNKEN)        
            memoDate.grid(row=8+i, column=0, sticky=N+S)
            memoDate.insert(INSERT, toDoList[i][0][-2:]+"-"+toDoList[i][0][-4:-2]+"-"+toDoList[i][0][:4])
            memoNotes=Text(Frame12, bd=0, width=111, height=3, borderwidth=1, relief=SUNKEN)        
            memoNotes.grid(row=8+i, column=1, columnspan=16)           
            global temp
            temp=str(toDoList[i][1])
            k=150            
            if len(str(toDoList[i][1]))>150: #loop που αλλάζει γραμμή κάθε 150 χαρακτήρες κειμένου.
                global final2
                final2=''
                n=1
                while len(temp)>0:
                    final2=final2+temp[:n*k]+'\n'
                    temp=temp[n*k:]
                    if len(temp)<k:
                        final2=final2+temp
                        break
                    else:
                        n=n+1
                if len(str(toDoList[i][1]))>256: #επιτρέπονται να εμφανίζονται μέχρι 256 χαρακτήρες στην συγκεκριμένη εκτύπωση (για εξοικονόμηση χώρου) και με επιλογή 'Διόρθωση (memo)'              
                    final2=final2[:256]+" (συνεχίζεται...)" #μέσω του κουμπιού εμφανίζεται το πλήρες κείμενο.
                    memoNotes.config(fg="red")
                memoNotes.insert(INSERT, final2)
            else:
                memoNotes.insert(INSERT, str(toDoList[i][1]))
        memoDate=Label(Frame12, text="ΗΜΕΡΟΜΗΝΙΑ", fg="red")
        memoDate.grid(row=7, column=0)
        memoNotes=Label(Frame12, text="ΕΝΕΡΓΕΙΕΣ", fg="red")
        memoNotes.grid(row=7, column=1, columnspan=17, sticky=W+E)
        returnButton=Button(Frame12, text="<<Επιστροφή", padx=40, pady=11, command=lambda: goto(16))
        returnButton.grid(row=1000, column=8, padx=35, pady=25)
        menuButton=Button(Frame12, text="Κεντρικό μενού", padx=32, pady=11, command=lambda:goto(17))
        menuButton.grid(row=1000, column=9, padx=35, pady=25)                 
    else:
        doneList.sort(key=lambda j:j[0], reverse=True) #ταξινόμηση με βάση την ημερομηνία και με φθίνουσα σειρά (από την παλαιότερη προς την νεότερη).
        message="ΠΡΟΓΡΑΜΜΑΤΙΣΜΕΝΕΣ ΕΝΕΡΓΕΙΕΣ ΠΡΟΗΓΟΥΜΕΝΩΝ ΗΜΕΡΩΝ"
        memoLabel=Label(Frame12, text=message, fg="red", bg= "#d9d9d9", pady=25)
        memoLabel.grid(row=6, column=0, columnspan=18, sticky=W+E)
        for i in range(len(doneList)):          
            memoDate=Text(Frame12, bd=0, width=12, height=3, borderwidth=1, relief=SUNKEN)    
            memoDate.grid(row=8+i, column=0, sticky=N+S)
            memoDate.insert(INSERT, doneList[i][0][-2:]+"-"+doneList[i][0][-4:-2]+"-"+doneList[i][0][:4])
            temp=str(doneList[i][1])
            if len(temp)>256: #επιτρέπονται να εμφανίζονται μέχρι 256 χαρακτήρες στην συγκεκριμένη εκτύπωση (για εξοικονόμηση χώρου) και με επιλογή 'Διόρθωση (memo)' μέσω                
                temp=temp[:256]+" (συνεχίζεται...)" #του κουμπιού εμφανίζεται το πλήρες κείμενο.            
            if len(temp)>150: #loop που αλλάζει γραμμή κάθε 150 χαρακτήρες κειμένου.                                
                k=150
                final2=''
                n=1
                while len(temp)>k:
                    final2=final2+temp[:n*k]+'\n'
                    temp=temp[n*k:]
                    if len(temp)<k:
                        final2=final2+temp
                        break
                    else:
                        n=n+1
                memoNotes=Text(Frame12, bd=0, width=111, height=3, borderwidth=1, relief=SUNKEN)
                memoNotes.insert(INSERT, final2)
            else:
                memoNotes=Text(Frame12, bd=0, width=111, height=3, borderwidth=1, relief=SUNKEN)
                memoNotes.insert(INSERT, temp)
            memoNotes.grid(row=8+i, column=1, columnspan=16)
        previousList=[]
        with open("past.csv", "r", encoding="utf-8", newline="") as file: 
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                previousList.append(row)
        for k in doneList:
            if k not in previousList: #κόψιμο διπλοεγγραφής
                previousList.append(k)
        with open("past.csv", "w", encoding="utf-8", newline="") as file: #καταχώρηση των παρελθουσών ενεργειών στο αρχείο μετά από την εμφάνισή τους στην οθόνη.
            wo=csv.writer(file, delimiter='$')
            for row in previousList:
                wo.writerow(row)            
        with open("future.csv", "w", encoding="utf-8", newline="") as file: #αναδιαμόρφωση του αρχείου τρεχουσών ενεργειών (κρατάει πλέον ημ/νίες από την τρέχουσα και έπειτα).
            wo=csv.writer(file, delimiter='$')
            for k in toDoList: #ενέργειες τρέχουσας ημέρας.
                wo.writerow(k)
            for k in futureList: #μελλοντικές ενέργειες.
                wo.writerow(k)
            successPast=Label(Frame12, text="Το αρχείο ενεργειών ενημερώθηκε με επιτυχία.", pady=15)
            successPast.grid(row=950, column=0, columnspan=18, sticky=W+E)                    
        memoDate=Label(Frame12, text="ΗΜΕΡΟΜΗΝΙΑ", fg="red")
        memoDate.grid(row=7, column=0, padx=30)
        memoNotes=Label(Frame12, text="ΕΝΕΡΓΕΙΕΣ", fg="red")
        memoNotes.grid(row=7, column=2, columnspan=16, padx=30, sticky=W+E)
        returnButton=Button(Frame12, text="<<Επιστροφή", padx=40, pady=11, command=lambda: goto(16))
        returnButton.grid(row=1000, column=8, padx=35, pady=15)
        menuButton=Button(Frame12, text="Κεντρικό μενού", padx=32, pady=11, command=lambda:goto(17))
        menuButton.grid(row=1000, column=9, padx=35, pady=15)    
            

def checkDate(date): #έλεγχος αν η ημερομηνία είναι σωστή
    if '/' not in date and '-' not in date or len(date)<=5 or len(date)>10:
        return 0
    else:         
        if date[-3] in ['/', '-']:
            year='20'+date[-2:]
        elif date[-5] in ['/', '-']:
            year=date[-4:]
        else:
            return 0
        if len(date)>8 and date[-8] in ['/', '-']:
            month=date[-7:-5]
            day=date[-len(date):-8]
        elif len(date)>6 and date[-6] in ['/', '-']:
            month=date[-5:-3]
            day=date[-len(date):-6]
            if '/' in month or '-' in month:
                return 0
        elif len(date)>7 and date[-7] in ['/', '-']:
            month='0'+date[-6]
            day=date[-len(date):-7]
        elif len(date)>5 and date[-5] in ['/', '-']:
            if date[-4] not in year:
                month='0'+date[-4]
                day=date[-len(date):-5]
            else:
                return 0                    
        if '/' in day or '-' in day or len(day)>2 or len(day)==0:
            return 0                
        elif len(day)==1:
            day='0'+day
    finalDate=year+month+day
    return finalDate
    
def ektyposi1(x, k): #εκτυπώσεις πριν την ανανέωση (παίρνει 2 παραμέτρους: x-->το Frame μέσα στο οποίο θα γίνουν οι εκτυπώσεις, k-->η λίστα που θα εκτυπωθεί (για ΑΝΑΝΕΩΣΗ ή ΕΠΑΝΑΦΟΡΑ).
    global i        
    global y
    y=k
    global q
    global status5
    global FrameForScroll
    global Frame100
    global margin
    FrameForScroll=LabelFrame(root, bd=0) #scrollbar attempt!!!
    FrameForScroll.grid(row=5, column=0, columnspan=18)
    Frame100=LabelFrame(FrameForScroll, bd=0)     
    if status2=='check_card': #<<Επιστροφή στην αρχική οθόνη με τις ειδοποιήσεις πριν από την είσοδο στο κεντρικό μενού.
        Frame100.grid(row=500, column=0, columnspan=18)   
        back=Button(Frame100, text="<<Επιστροφή", padx=43, pady=11, command=lambda: goto(70))
        back.grid(row=500, column=8, padx=65, pady=25)
        enterMenu=Button(Frame100, text="Κεντρικό Μενού", padx=38, pady=11, command=lambda:  goto(71))
        enterMenu.grid(row=500, column=9, padx=65, pady=25)          
    else:
        Frame100.grid(row=500, column=0, columnspan=18)     
    if len(y)==0:
        messagebox.showinfo('Ενημέρωση:','Δε βρέθηκαν εγγραφές στο σύστημα.')
    else:      
        FrameForScroll=LabelFrame(root, bd=0) #scrollbar attempt!!!
        FrameForScroll.grid(row=5, column=0, columnspan=18)
        #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
        canvas=Canvas(FrameForScroll, bd=0, height=480, width=1220) 
        canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
        q=LabelFrame(canvas, bd=0)
        scrollbar = Scrollbar(FrameForScroll, orient="vertical", command=canvas.yview)
        scrollbar.grid(row=0, column=18, sticky=N+S)
        q.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=q, anchor="nw", width=2000)
        canvas.configure(yscrollcommand=scrollbar.set)
        Frame100=LabelFrame(FrameForScroll, bd=0)
        Frame100.grid(row=500, column=0, columnspan=18)
        enterMenu=Button(Frame100, text="Κεντρικό Μενού", padx=38, pady=11, command=lambda:  goto(71))
        enterMenu.grid(row=9+2*len(y), column=9, padx=65, pady=5)
        back=Button(Frame100, text="<<Επιστροφή", padx=43, pady=11, command=lambda: goto(121)) #<<Επιστροφή στη φόρμα δελτίων (στο κεντρικό μενού).
        back.grid(row=9+2*len(y), column=8, padx=65, pady=5)
        if status5=='active_cards':
            text1="ΔΕΛΤΙΑ ΑΝΕΡΓΙΑΣ ΓΙΑ ΑΝΑΝΕΩΣΗ"
            margin=515
        if status5=='del_cards':
            margin=515
            text1="ΔΙΑΓΡΑΜΜΕΝΑ ΔΕΛΤΙΑ ΑΝΕΡΓΙΑΣ"
        if not (status5=='active_cards' or status5=='del_cards'):
            text1="ΕΝΕΡΓΟΙ ΧΡΗΣΤΕΣ"
            margin=570
        activeLabel=Label(q, text=text1, pady=25, padx=margin, fg="red", bg="#d9d9d9")
        activeLabel.grid(row=0, column=0, columnspan=18, sticky=W+E)
        if status5=='active_cards':
            activeLabel.config(padx=530)
        if k[0][3]!="": #μη κενή ημ/νία (για να διαχωρίζονται από τα διαγραμμένα δελτία που έχουν κενή ημ/νία).
            y= sorted(k, key=lambda k:k[3]) #sort με βάση την ημ/νία ανανέωσης (από...)
        else:
            y= sorted(k, key=lambda k:k[0]) #sort με βάση το επώνυμο (για τα διαγραμμένα δελτία).
        aaPrint1=Label(q, fg="red", text="Α/Α", pady=5, padx=1)
        aaPrint1.grid(row=7, column=4,  sticky=W)
        surnamePrint1=Label(q, fg="red", text="ΕΠΩΝΥΜΟ", pady=5, padx=3)
        surnamePrint1.grid(row=7, column=5, sticky=W)
        namePrint1=Label(q, fg="red", text="ΟΝΟΜΑ", pady=5, padx=3)
        namePrint1.grid(row=7, column=6, sticky=W)
        cardPrint1=Label(q, fg="red", text="ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ", pady=5, padx=3)
        cardPrint1.grid(row=7, column=7, sticky=W)
        update1Print1=Label(q, fg="red", text="ΑΝΑΝΕΩΣΗ από:", pady=5, padx=3)
        update1Print1.grid(row=7, column=8, sticky=W)
        update2Print1=Label(q, fg="red", text="ΑΝΑΝΕΩΣΗ έως:", pady=5, padx=3)
        update2Print1.grid(row=7, column=9, sticky=W)
        amkaPrint1=Label(q, fg="red", text="ΑΜΚΑ", pady=5, padx=3)
        amkaPrint1.grid(row=7, column=10, sticky=W)
        afmPrint1=Label(q, fg="red", text="ΑΦΜ", pady=5, padx=3)
        afmPrint1.grid(row=7, column=11, sticky=W)
        akhaPrint1=Label(q, fg="red", text="ΚΩΔΙΚΟΣ ΑΚΗΑ", pady=5, padx=1)
        akhaPrint1.grid(row=7, column=12, sticky=W)   
        activePrint1=Label(q, fg="red", text="ΕΝΕΡΓΟΣ ΧΡΗΣΤΗΣ", pady=5, padx=1)
        activePrint1.grid(row=7, column=13, sticky=W)
        i=0
        if y[i][3]=="":
            activeLabel.config(padx=357)  
        while i<len(y):
            if status5=='active_cards' and y[i][3]>currentDate(): #'κόβουμε' τους ενεργούς χρήστες των οποίων τα δελτία δεν είναι ακόμα προς ανανέωση.
                i=i+1
                continue
            aaPrint2=Label(q, text=str(i+1))
            aaPrint2.grid(row=8+2*i, column=4, sticky=W, pady=16, padx=1)           
            surnamePrint2=Label(q, text=str(y[i][0]))
            surnamePrint2.grid(row=8+2*i, column=5, sticky=W, pady=16, padx=3)        
            namePrint2=Label(q, text=str(y[i][1]))
            namePrint2.grid(row=8+2*i, column=6, sticky=W, pady=16, padx=3)
            cardPrint2=Label(q, text=str(y[i][2]))
            cardPrint2.grid(row=8+2*i, column=7, sticky=W, pady=16, padx=3)
            update1Print2=Label(q, text=y[i][3][6:]+"-"+str(y[i][3][4:6])+"-"+str(y[i][3][:4]))
            update1Print2.grid(row=8+2*i, column=8, sticky=W, pady=16, padx=3)
            update2Print2=Label(q, text=y[i][4][6:]+"-"+str(y[i][4][4:6])+"-"+str(y[i][4][:4]))
            update2Print2.grid(row=8+2*i, column=9, sticky=W, pady=16, padx=3)
            amkaPrint2=Label(q, text=str(y[i][5]))
            amkaPrint2.grid(row=8+2*i, column=10, sticky=W, pady=16, padx=3)
            afmPrint2=Label(q, text=str(y[i][6]))
            afmPrint2.grid(row=8+2*i, column=11, sticky=W, pady=16, padx=3)
            akhaPrint2=Label(q, text=str(y[i][7]))
            akhaPrint2.grid(row=8+2*i, column=12, sticky=W, pady=16, padx=1)
            activePrint2=Label(q, text=str(y[i][12]))
            activePrint2.grid(row=8+2*i, column=13, sticky=W, pady=16, padx=1)
            if status5=='del_cards':
                update1Print2.config(padx=100)
                update2Print2.config(padx=100)
            if y[i][3]=="":
                activate=Button(q, text="Επαναφορά στο σύστημα", padx=1, pady=11, command=lambda i=i: diagrafi(y[i], 3))
                activate.grid(row=8+2*i, column=15, sticky=W, padx=1, pady=5)        
            elif y[i][3]<=currentDate(): #αν έχει ανοίξει το παράθυρο για την ανανέωση, να εμφανίζεται το αντίστοιχο κουμπί δίπλα από την εγγραφή.
                btn=Button(q, text="Ανανέωση δελτίου", padx=4, pady=11, command=lambda i=i: update(FrameForScroll, y, i))
                btn.grid(row=8+2*i, column=14, sticky=W, padx=1, pady=5)
                deactivate=Button(q, text="Απενεργοποίηση χρήστη", padx=1, pady=11, command=lambda i=i: change(FrameForScroll, y, i, 5))
                deactivate.grid(row=8+2*i, column=15, sticky=W, padx=1, pady=5)
            else:
                deactivate=Button(q, text="Απενεργοποίηση χρήστη", padx=1, pady=11, command=lambda i=i: change(FrameForScroll, y, i, 5))
                deactivate.grid(row=8+2*i, column=15, sticky=W, padx=1, pady=5)            
            i=i+1

        
def ektyposi2(x, k): #εκτυπώσεις πριν την Τροποποίηση δελτίου (παίρνει 2 παραμέτρους: x-->το Frame μέσα στο οποίο θα γίνουν οι εκτυπώσεις, k-->η λίστα που θα εκτυπωθεί. (ΓΙΑ ΤΡΟΠΟΠΟΙΗΣΗ)
    global i
    global y
    global z
    z=x
    y=k
    global FrameForScroll2
    FrameForScroll2=LabelFrame(root, bd=0) #scrollbar attempt!!!
    FrameForScroll2.grid(row=5, column=0, columnspan=18)
    #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
    canvas=Canvas(FrameForScroll2, bd=0, height=460, width=1220) 
    canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
    z=LabelFrame(canvas, bd=0)
    scrollbar = Scrollbar(FrameForScroll2, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=18, sticky=N+S)
    z.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=z, anchor="nw", width=2000)
    canvas.configure(yscrollcommand=scrollbar.set)    
    Frame100=LabelFrame(FrameForScroll2, bd=0)
    Frame100.grid(row=500, column=0, columnspan=18)
    deactiveLabel=Label(z, text="ΑΝΕΝΕΡΓΟΙ ΧΡΗΣΤΕΣ", fg="red", bg="#d9d9d9", pady=25, padx=553)
    deactiveLabel.grid(row=0, column=0, columnspan=18, sticky=W+E)
    Frame1000=LabelFrame(FrameForScroll2, bd=0)
    Frame1000.grid(row=1000, column=0, columnspan=18)
    activeBack=Button(Frame1000, text="<<Επιστροφή", padx=40, pady=11, command=lambda: goto(133) )
    activeBack.grid(row=1000, column=8, pady=25, padx=65)
    activeReturn=Button(Frame1000, text="Κεντρικό μενού", padx=40, pady=11, command=lambda: goto(59)) 
    activeReturn.grid(row=1000, column=12, pady=25, padx=65)
    if len(y)==0:
        messagebox.showinfo('Ενημέρωση:', 'Δε βρέθηκαν ανενεργοί χρήστες.')
    else:
        aaPrint1=Label(z, fg="red", text="Α/Α", padx=1, pady=5)
        aaPrint1.grid(row=7, column=4,  sticky=W)
        surnamePrint1=Label(z, fg="red", text="ΕΠΩΝΥΜΟ", padx=3, pady=5)
        surnamePrint1.grid(row=7, column=5, sticky=W)
        namePrint1=Label(z, fg="red", text="ΟΝΟΜΑ", padx=3, pady=5)
        namePrint1.grid(row=7, column=6, sticky=W)
        cardPrint1=Label(z, fg="red", text="ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ", padx=3, pady=5)
        cardPrint1.grid(row=7, column=7, sticky=W)
        update1Print1=Label(z, fg="red", text="ΑΝΑΝΕΩΣΗ από:", pady=5)
        update1Print1.grid(row=7, column=8, sticky=W)
        update2Print1=Label(z, fg="red", text="ΑΝΑΝΕΩΣΗ έως:", pady=5)
        update2Print1.grid(row=7, column=9, sticky=W)
        amkaPrint1=Label(z, fg="red", text="ΑΜΚΑ", padx=3, pady=5)
        amkaPrint1.grid(row=7, column=10, sticky=W)
        afmPrint1=Label(z, fg="red", text="ΑΦΜ", padx=3, pady=5)
        afmPrint1.grid(row=7, column=11, sticky=W)
        akhaPrint1=Label(z, fg="red", text="ΚΩΔΙΚΟΣ ΑΚΗΑ", padx=3, pady=5)
        akhaPrint1.grid(row=7, column=12, sticky=W)   
        activePrint1=Label(z, fg="red", text="ΕΝΕΡΓΟΣ ΧΡΗΣΤΗΣ", padx=1, pady=5)
        activePrint1.grid(row=7, column=13, sticky=W)
        i=0
        while i<len(y):
            aaPrint2=Label(z, text=str(i+1))
            aaPrint2.grid(row=8+2*i, column=4, sticky=W, padx=1)           
            surnamePrint2=Label(z, text=str(y[i][0]))
            surnamePrint2.grid(row=8+2*i, column=5, sticky=W, padx=3)        
            namePrint2=Label(z, text=str(y[i][1]))
            namePrint2.grid(row=8+2*i, column=6, sticky=W, padx=3)
            cardPrint2=Label(z, text=str(y[i][2]))
            cardPrint2.grid(row=8+2*i, column=7, sticky=W, padx=3)
            update1Print2=Label(z, text=y[i][3][6:]+"-"+str(y[i][3][4:6])+"-"+str(y[i][3][:4]))
            update1Print2.grid(row=8+2*i, column=8, sticky=W)
            update2Print2=Label(z, text=y[i][4][6:]+"-"+str(y[i][4][4:6])+"-"+str(y[i][4][:4]))
            update2Print2.grid(row=8+2*i, column=9, sticky=W)
            amkaPrint2=Label(z, text=str(y[i][5]))
            amkaPrint2.grid(row=8+2*i, column=10, sticky=W, padx=3)
            afmPrint2=Label(z, text=str(y[i][6]))
            afmPrint2.grid(row=8+2*i, column=11, sticky=W, padx=3)
            akhaPrint2=Label(z, text=str(y[i][7]))
            akhaPrint2.grid(row=8+2*i, column=12, sticky=W, padx=3)
            activePrint2=Label(z, text=str(y[i][12]))
            activePrint2.grid(row=8+2*i, column=13, sticky=W, padx=1)
            if y[i][12]=='ΟΧΙ': #ανενεργός χρήστης, ΔΕΝ επιτρέπεται η τροποποίηση (ΠΡΩΤΑ χρειάζεται να γίνει ενεργοποίηση).
                reactiveButton=Button(z, text="Ενεργοποίηση χρήστη", padx=9, pady=11, command=lambda i=i: change(FrameForScroll2, y, i, 3)) 
                reactiveButton.grid(row=8+2*i, column=14, sticky=W, padx=0, pady=5)
            else:
                alterButton=Button(z, text="Τροποποίηση δελτίου", padx=10, pady=11, command=lambda i=i: change(FrameForScroll2, y, i, 1))
                alterButton.grid(row=8+2*i, column=14, sticky=W, padx=0, pady=5)
            i=i+1           
        
def ektyposi3(x, k): #εκτυπώσεις πριν την Τροποποίηση δελτίου (παίρνει 2 παραμέτρους: x-->το Frame μέσα στο οποίο θα γίνουν οι εκτυπώσεις, k-->η λίστα που θα εκτυπωθεί. (ΓΙΑ ΔΙΑΓΡΑΦΗ)
    global i
    global y
    y=k

    global FrameForScroll2
    FrameForScroll2=LabelFrame(root, bd=0) #scrollbar attempt!!!
    FrameForScroll2.grid(row=5, column=0, columnspan=18)
    #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
    canvas=Canvas(FrameForScroll2, bd=0, height=460, width=1220) 
    canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
    x=LabelFrame(canvas, bd=0)
    scrollbar = Scrollbar(FrameForScroll2, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=18, sticky=N+S)
    x.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=x, anchor="nw", width=2000)
    canvas.configure(yscrollcommand=scrollbar.set)    
    Frame100=LabelFrame(FrameForScroll2, bd=0)
    Frame100.grid(row=500, column=0, columnspan=18)

    resultsSearchLabel=Label(x, text="ΑΠΟΤΕΛΕΣΜΑΤΑ ΑΝΑΖΗΤΗΣΗΣ ΔΕΛΤΙΩΝ ΑΝΕΡΓΙΑΣ ΓΙΑ ΔΙΑΓΡΑΦΗ", fg="red", bg="#d9d9d9", pady=25)
    resultsSearchLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
    aaPrint1=Label(x, fg="red", text="Α/Α", padx=10, pady=5)
    aaPrint1.grid(row=7, column=4,  sticky=W)
    surnamePrint1=Label(x, fg="red", text="ΕΠΩΝΥΜΟ", padx=10, pady=5)
    surnamePrint1.grid(row=7, column=5, sticky=W)
    namePrint1=Label(x, fg="red", text="ΟΝΟΜΑ", padx=10, pady=5)
    namePrint1.grid(row=7, column=6, sticky=W)
    cardPrint1=Label(x, fg="red", text="ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ", padx=10, pady=5)
    cardPrint1.grid(row=7, column=7, sticky=W)
    update1Print1=Label(x, fg="red", text="ΑΝΑΝΕΩΣΗ από:", pady=5)
    update1Print1.grid(row=7, column=8, sticky=W)
    update2Print1=Label(x, fg="red", text="ΑΝΑΝΕΩΣΗ έως:", pady=5)
    update2Print1.grid(row=7, column=9, sticky=W)
    amkaPrint1=Label(x, fg="red", text="ΑΜΚΑ", padx=10, pady=5)
    amkaPrint1.grid(row=7, column=10, sticky=W)
    afmPrint1=Label(x, fg="red", text="ΑΦΜ", padx=10, pady=5)
    afmPrint1.grid(row=7, column=11, sticky=W)
    akhaPrint1=Label(x, fg="red", text="ΚΩΔΙΚΟΣ ΑΚΗΑ", padx=10, pady=5)
    akhaPrint1.grid(row=7, column=12, sticky=W)   
    activePrint1=Label(x, fg="red", text="ΕΝΕΡΓΟΣ ΧΡΗΣΤΗΣ", padx=10, pady=5)
    activePrint1.grid(row=7, column=13, sticky=W)
    i=0
    while i<len(y):
        aaPrint2=Label(x, text=str(i+1))
        aaPrint2.grid(row=8+2*i, column=4, sticky=W, padx=10)           
        surnamePrint2=Label(x, text=str(y[i][0]))
        surnamePrint2.grid(row=8+2*i, column=5, sticky=W, padx=10)        
        namePrint2=Label(x, text=str(y[i][1]))
        namePrint2.grid(row=8+2*i, column=6, sticky=W, padx=10)
        cardPrint2=Label(x, text=str(y[i][2]))
        cardPrint2.grid(row=8+2*i, column=7, sticky=W, padx=10)
        update1Print2=Label(x, text=y[i][3][6:]+"-"+str(y[i][3][4:6])+"-"+str(y[i][3][:4]))
        update1Print2.grid(row=8+2*i, column=8, sticky=W)
        update2Print2=Label(x, text=y[i][4][6:]+"-"+str(y[i][4][4:6])+"-"+str(y[i][4][:4]))
        update2Print2.grid(row=8+2*i, column=9, sticky=W)
        amkaPrint2=Label(x, text=str(y[i][5]))
        amkaPrint2.grid(row=8+2*i, column=10, sticky=W, padx=10)
        afmPrint2=Label(x, text=str(y[i][6]))
        afmPrint2.grid(row=8+2*i, column=11, sticky=W, padx=10)
        akhaPrint2=Label(x, text=str(y[i][7]))
        akhaPrint2.grid(row=8+2*i, column=12, sticky=W, padx=10)
        activePrint2=Label(x, text=str(y[i][12]))
        activePrint2.grid(row=8+2*i, column=13, sticky=W, padx=10)            
        alterButton=Button(x, text="Διαγραφή", padx=49, pady=11, command=lambda i=i: change(x, y, i, 2))
        alterButton.grid(row=8+2*i, column=14, sticky=W, padx=10, pady=5)            
        i=i+1
    #Frame1000=LabelFrame(x, bd=0)
   # Frame1000.grid(row=1000, column=0, columnspan=18)        
    returnSearch=Button(Frame100, text="<<Επιστροφή", padx=35, pady=11, command=lambda: goto(27))
    returnSearch.grid(row=1000, column=8, pady=25, padx=65) 
    newSearch=Button(Frame100, text="Νέα διαγραφή", padx=35, pady=11, command=lambda: goto(26))
    newSearch.grid(row=1000,  column=9, pady=25, padx=65)
    
def ektyposi4(x, k): #εκτυπώσεις πριν την Τροποποίηση δελτίου (παίρνει 2 παραμέτρους: x-->το Frame μέσα στο οποίο θα γίνουν οι εκτυπώσεις, k-->η λίστα που θα εκτυπωθεί. 
    global i         #(ΓΙΑ ΠΡΟΒΟΛΗ ΣΤΟΙΧΕΙΩΝ ΜΟΝΟ)
    global y
    global z
    z=x
    y=k


    global FrameForScroll2
    FrameForScroll2=LabelFrame(root, bd=0) #scrollbar attempt!!!
    FrameForScroll2.grid(row=5, column=0, columnspan=18)
    #ΝΑ ΕΛΕΓΞΩ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ ΤΟΥ MONITOR ΓΙΑ ΝΑ ΓΙΟΥΝ ADJUSTMENTS ΣΤΗΝ ΕΠΟΜΕΝΗ ΓΡΑΜΜΗ(HEIGHT, WIDTH)!!!
    canvas=Canvas(FrameForScroll2, bd=0, height=460, width=1220) 
    canvas.grid(row=0, column=0, columnspan=18, sticky=N+S+E+W)
    x=LabelFrame(canvas, bd=0)
    scrollbar = Scrollbar(FrameForScroll2, orient="vertical", command=canvas.yview)
    scrollbar.grid(row=0, column=18, sticky=N+S)
    x.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
    canvas.create_window((0, 0), window=x, anchor="nw", width=2000)
    canvas.configure(yscrollcommand=scrollbar.set)    
    Frame100=LabelFrame(FrameForScroll2, bd=0)
    Frame100.grid(row=500, column=0, columnspan=18)
    
    aaPrint1=Label(x, fg="red", text="Α/Α", padx=15, pady=5)
    aaPrint1.grid(row=7, column=4,  sticky=W)
    surnamePrint1=Label(x, fg="red", text="ΕΠΩΝΥΜΟ", padx=15, pady=5)
    surnamePrint1.grid(row=7, column=5, sticky=W)
    namePrint1=Label(x, fg="red", text="ΟΝΟΜΑ", padx=15, pady=5)
    namePrint1.grid(row=7, column=6, sticky=W)
    cardPrint1=Label(x, fg="red", text="ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ", padx=15, pady=5)
    cardPrint1.grid(row=7, column=7, sticky=W)
    update1Print1=Label(x, fg="red", text="ΑΝΑΝΕΩΣΗ από:", pady=5)
    update1Print1.grid(row=7, column=8, sticky=W)
    update2Print1=Label(x, fg="red", text="ΑΝΑΝΕΩΣΗ έως:", pady=5)
    update2Print1.grid(row=7, column=9, sticky=W)
    amkaPrint1=Label(x, fg="red", text="ΑΜΚΑ", padx=15, pady=5)
    amkaPrint1.grid(row=7, column=10, sticky=W)
    afmPrint1=Label(x, fg="red", text="ΑΦΜ", padx=15, pady=5)
    afmPrint1.grid(row=7, column=11, sticky=W)
    akhaPrint1=Label(x, fg="red", text="ΚΩΔΙΚΟΣ ΑΚΗΑ", padx=15, pady=5)
    akhaPrint1.grid(row=7, column=12, sticky=W)   
    activePrint1=Label(x, fg="red", text="ΕΝΕΡΓΟΣ ΧΡΗΣΤΗΣ", padx=15, pady=5)
    activePrint1.grid(row=7, column=13, sticky=W)
    i=0
    while i<len(y):
        aaPrint2=Label(x, text=str(i+1))
        aaPrint2.grid(row=8+2*i, column=4, sticky=W, padx=15)           
        surnamePrint2=Label(x, text=str(y[i][0]))
        surnamePrint2.grid(row=8+2*i, column=5, sticky=W, padx=15)        
        namePrint2=Label(x, text=str(y[i][1]))
        namePrint2.grid(row=8+2*i, column=6, sticky=W, padx=15)
        cardPrint2=Label(x, text=str(y[i][2]))
        cardPrint2.grid(row=8+2*i, column=7, sticky=W, padx=15)
        update1Print2=Label(x, text=y[i][3][6:]+"-"+str(y[i][3][4:6])+"-"+str(y[i][3][:4]))
        update1Print2.grid(row=8+2*i, column=8, sticky=W)
        update2Print2=Label(x, text=y[i][4][6:]+"-"+str(y[i][4][4:6])+"-"+str(y[i][4][:4]))
        update2Print2.grid(row=8+2*i, column=9, sticky=W)
        amkaPrint2=Label(x, text=str(y[i][5]))
        amkaPrint2.grid(row=8+2*i, column=10, sticky=W, padx=15)
        afmPrint2=Label(x, text=str(y[i][6]))
        afmPrint2.grid(row=8+2*i, column=11, sticky=W, padx=15)
        akhaPrint2=Label(x, text=str(y[i][7]))
        akhaPrint2.grid(row=8+2*i, column=12, sticky=W, padx=15)
        activePrint2=Label(x, text=str(y[i][12]))
        activePrint2.grid(row=8+2*i, column=13, sticky=W, padx=15)
        alterButton=Button(x, text="Πλήρη στοιχεία", padx=32, pady=11, command=lambda i=i: change(x, y, i, 4))
        alterButton.grid(row=8+2*i, column=14, sticky=W, padx=15, pady=5)
        i=i+1
    #Frame1002=LabelFrame(x,bd=0)
    #Frame1002.grid(row=1000, column=0, columnspan=18)
    newSearch=Button(Frame100, text="Νέα αναζήτηση", padx=35, pady=11, command=lambda: goto(51)) 
    newSearch.grid(row=1000, column=8, pady=25, padx=65)
    returnSearch=Button(Frame100, text="Κεντρικό μενού", padx=40, pady=11, command=lambda: goto(39)) 
    returnSearch.grid(row=1000, column=10, pady=25, padx=65)        
        
def change(x, y, i, n): #συνάρτηση με 4 ορίσματα (x--> Frame που καταργείται, y--> λίστα μέσα στην οποία θα γίνει η ενέργεια, i--> η τρέχουσα εγγραφή της λίστας, n--> ποια ενέργεια θα 
    x.grid_forget() #εκτελεστεί (Τροποποίηση δελτίου --> n==1, διαγραφή --> n==2, ενεργοποποίηση --> n==3, προβολή --> n==4, απενεργοποίηση -->n==5, επαναφορά -->n==6.).
    global Frame21
    global surnamePrint2
    global namePrint2
    global cardPrint2
    global update11Print2
    global update21Print2
    global amkaPrint2
    global afmPrint2
    global akhaPrint2
    global DYPA1Print2
    global DYPA2Print2
    global TAXIS1Print2
    global TAXIS2Print2
    global activePrint2
    global planPrint2
    global telPrint2
    global mailPrint2
    global notesPrint2
    global Frame1000          
    Frame21=LabelFrame(root, bd=0)
    Frame21.grid(row=5, column=0, columnspan=18)
    Frame1000=LabelFrame(Frame21, bd=0)
    Frame1000.grid(row=100, column=0, columnspan=18)      
    surnamePrint1=Label(Frame21, fg="red", text="ΕΠΩΝΥΜΟ:", padx=10, pady=5)
    surnamePrint1.grid(row=8, column=7, sticky=E)
    surnamePrint2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    surnamePrint2.grid(row=8, column=8)    
    namePrint1=Label(Frame21, fg="red", text="ΟΝΟΜΑ:", padx=10, pady=5)
    namePrint1.grid(row=9, column=7, sticky=E)
    namePrint2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    namePrint2.grid(row=9, column=8)
    cardPrint1=Label(Frame21, fg="red", text="ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ:", padx=10, pady=5)
    cardPrint1.grid(row=10, column=7, sticky=E)
    cardPrint2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    cardPrint2.grid(row=10, column=8)
    change1Print1=Label(Frame21, fg="red", text="ΑΝΑΝΕΩΣΗ (ηη-μμ-εεεε ή ηη/μμ/εεεε) από:", padx=10, pady=5)
    change1Print1.grid(row=11, column=7, sticky=E)
    update11Print2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    update11Print2.grid(row=11, column=8) 
    change2Print1=Label(Frame21, fg="red", text="ΑΝΑΝΕΩΣΗ (ηη-μμ-εεεε ή ηη/μμ/εεεε) έως:", padx=10, pady=5)
    change2Print1.grid(row=12, column=7, sticky=E)
    update21Print2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    update21Print2.grid(row=12, column=8) 
    amkaPrint1=Label(Frame21, fg="red", text="ΑΜΚΑ:", padx=10, pady=5)
    amkaPrint1.grid(row=13, column=7, sticky=E)
    amkaPrint2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    amkaPrint2.grid(row=13, column=8)    
    afmPrint1=Label(Frame21, fg="red", text="ΑΦΜ:", padx=10, pady=5)
    afmPrint1.grid(row=14, column=7, sticky=E)
    afmPrint2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    afmPrint2.grid(row=14, column=8)    
    akhaPrint1=Label(Frame21, fg="red", text="ΚΩΔΙΚΟΣ ΑΚΗΑ:", padx=10, pady=5)
    akhaPrint1.grid(row=15, column=7, sticky=E)
    akhaPrint2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    akhaPrint2.grid(row=15, column=8)        
    DYPA1Print1=Label(Frame21, fg="red", text="ΚΩΔΙΚΟΙ ΔΥΠΑ (Username):", padx=10, pady=5)
    DYPA1Print1.grid(row=8, column=9, sticky=E)
    DYPA1Print2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    DYPA1Print2.grid(row=8, column=10)    
    DYPA2Print1=Label(Frame21, fg="red", text="ΚΩΔΙΚΟΙ ΔΥΠΑ (Password):", padx=10, pady=5)
    DYPA2Print1.grid(row=9, column=9, sticky=E)   
    DYPA2Print2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    DYPA2Print2.grid(row=9, column=10)      
    TAXIS1Print1=Label(Frame21, fg="red", text="ΚΩΔΙΚΟΙ TAXISnet (Username):", padx=10, pady=5)
    TAXIS1Print1.grid(row=10, column=9, sticky=E)
    TAXIS1Print2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    TAXIS1Print2.grid(row=10, column=10)      
    TAXIS2Print1=Label(Frame21, fg="red", text="ΚΩΔΙΚΟΙ TAXISnet (Password):", padx=10, pady=5)
    TAXIS2Print1.grid(row=11, column=9, sticky=E)
    TAXIS2Print2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    TAXIS2Print2.grid(row=11, column=10)         
    activePrint1=Label(Frame21, fg="red", text="ΕΝΕΡΓΟΣ ΧΡΗΣΤΗΣ:", padx=10, pady=5)
    activePrint1.grid(row=12, column=9, sticky=E)
    activePrint2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    activePrint2.grid(row=12, column=10)       
    planPrint1=Label(Frame21, fg="red", text="ΑΤΟΜ. ΣΧΕΔΙΟ ΔΡΑΣΗΣ:", padx=10, pady=5)
    planPrint1.grid(row=13, column=9, sticky=E)
    planPrint2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    planPrint2.grid(row=13, column=10)        
    telPrint1=Label(Frame21, fg="red", text="ΤΗΛΕΦΩΝΟ:", padx=10, pady=5)
    telPrint1.grid(row=14, column=9, sticky=E)
    telPrint2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    telPrint2.grid(row=14, column=10)           
    mailPrint1=Label(Frame21, fg="red", text="E-MAIL:", padx=10, pady=5)
    mailPrint1.grid(row=15, column=9, sticky=E)
    mailPrint2=Entry(Frame21, width=50, relief=SUNKEN, borderwidth=5)
    mailPrint2.grid(row=15, column=10)         
    notesPrint1=Label(Frame21, fg="red", text="ΠΑΡΑΤΗΡΗΣΕΙΣ:", padx=10, pady=5)
    notesPrint1.grid(row=22, column=7, sticky=E+N)
    surnamePrint2.insert(0, y[i][0])
    namePrint2.insert(0, y[i][1])
    cardPrint2.insert(0, y[i][2])
    update11Print2.insert(0, y[i][3][-2:]+"-"+y[i][3][-4:-2]+"-"+y[i][3][:4])
    update21Print2.insert(0, y[i][4][-2:]+"-"+y[i][4][-4:-2]+"-"+y[i][4][:4])        
    amkaPrint2.insert(0, y[i][5])
    afmPrint2.insert(0, y[i][6])
    akhaPrint2.insert(0, y[i][7])        
    DYPA1Print2.insert(0, y[i][8])
    DYPA2Print2.insert(0, y[i][9])
    TAXIS1Print2.insert(0, y[i][10])
    TAXIS2Print2.insert(0, y[i][11])    
    if n==1: #Τροποποίηση δελτίου δελτίων ανεργίας.
        changeLabel=Label(Frame21, text="ΤΡΟΠΟΠΟΙΗΣΗ ΔΕΛΤΙΟΥ ΑΝΕΡΓΙΑΣ", pady=15, fg="red", bg= "#d9d9d9")
        changeLabel.grid(row=6, column=0, columnspan=18, sticky=W+E)
        global message
        message="Τροποποίηση δελτίου"
        activePrint2.insert(0, y[i][12])
        planPrint2.insert(0, y[i][13])
        telPrint2.insert(0, y[i][14])
        mailPrint2.insert(0, y[i][15])           
        notesPrint2=Text(Frame21, width=101, height=10, relief=SUNKEN, borderwidth=5)
        notesPrint2.grid(row=22, column=8, columnspan=3)
        notesPrint2.insert(INSERT,y[i][16])            
        global newchange
        newchange=Button(Frame1000,text=message, padx=15, pady=11, command=lambda: tropopoiisi(y, i))
        newchange.grid(row=100, column=9, pady=30, sticky=W)
    elif n==2 or n==3 or n==4 or n==5 or n==6: #2-->διαγραφή δελτίων ανεργίας, 3-->ενεργοποίηση δελτίων ανεργίας, 4-->προβολή πλήρων στοιχείων δελτίου ανεργίας, 5-->απενεργοποίηση δελτίων ανεργίας.
        #global message
        if n==2: #διαγραφή δελτίων ανεργίας
            changeLabel=Label(Frame21, text="ΔΙΑΓΡΑΦΗ ΔΕΛΤΙΟΥ ΑΝΕΡΓΙΑΣ", pady=15, fg="red", bg= "#d9d9d9")
            changeLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        elif n==3:#ενεργοποίηση δελτίων ανεργίας
            changeLabel=Label(Frame21, text="ΕΝΕΡΓΟΠΟΙΗΣΗ ΧΡΗΣΤΗ", pady=15, fg="red", bg= "#d9d9d9")
            changeLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        elif n==4: #προβολή πλήρων στοιχείων δελτίου ανεργίας.
            changeLabel=Label(Frame21, text="ΠΡΟΒΟΛΗ ΣΤΟΙΧΕΙΩΝ ΔΕΛΤΙΟΥ ΑΝΕΡΓΙΑΣ", pady=15, fg="red", bg= "#d9d9d9")
            changeLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        elif n==5: #απενεργοποίηση δελτίων ανεργίας
            changeLabel=Label(Frame21, text="ΑΠΕΝΕΡΓΟΠΟΙΗΣΗ ΧΡΗΣΤΗ", pady=15, fg="red", bg= "#d9d9d9")
            changeLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        elif n==6: #επαναφορά διαγραμμένου δελτίου ανεργίας.
            activeLabel=Label(Frame21, text="ΕΠΑΝΑΦΟΡΑ ΔΙΑΓΡΑΜΜΕΝΟΥ ΧΡΗΣΤΗ", pady=15, fg="red", bg= "#d9d9d9")
            activeLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        if n==3 or n==5: #3-->ενεργοποίηση δελτίου ανεργίας, 5-->απενεργοποίηση δελτίου ανεργίας.
            if n==3:
                y[i][12]='ΝΑΙ'
            else:
                y[i][12]='ΟΧΙ'
            global temp
            temp=[]
            with open("current.csv", "r", encoding="utf-8", newline="") as file:
                ro=csv.reader(file, delimiter='$')
                for row in ro:
                    temp.append(row)
                for record in temp: #ταυτοποίηση (με βάση: ΑΜΚΑ, ΑΦΜ και αρ. δελτίου) της εγγραφής δελτίου που (απ)ενεργοποιείται και καταχώρηση στο σύστημα ως ενεργοποιημένο/απενεργοποιημένο.
                    if record[5]==y[i][5] and record[6]==y[i][6] and record[2]==y[i][2]:
                        if record[12]=='ΝΑΙ':
                            record[12]='ΟΧΙ'
                        else:
                            record[12]='ΝΑΙ'
                with open("current.csv", "w", encoding="utf-8", newline="") as file:
                    wo=csv.writer(file, delimiter='$')
                    for row in temp:
                        wo.writerow(row)
        activePrint2.insert(0, y[i][12])
        notesPrint2=Text(Frame21, width=101, height=10, relief=SUNKEN, borderwidth=5)
        notesPrint2.grid(row=22, column=8, columnspan=3)     
        if n==2:            
            message="Διαγραφή"
            newchange=Button(Frame1000,text=message, padx=38, pady=11, command=lambda y=y[i]: diagrafi(y, 1))
            newchange.grid(row=100, column=9, pady=25, padx=65)
        elif n==6:
            message="Επαναφορά"
            newchange=Button(Frame1000,text=message, padx=38, pady=11, command=lambda: goto(60))
            newchange.grid(row=100, column=9, pady=25, padx=65)
        planPrint2.insert(0, y[i][13])
        telPrint2.insert(0, y[i][14])
        mailPrint2.insert(0, y[i][15])
        notesPrint2.insert(INSERT, y[i][16])
    if n==4 or n==5 or n==3:
        newCancel=Button(Frame1000, text="<<Επιστροφή", padx=36, pady=11, command=lambda: goto(58))
        newCancel.grid(row=100, column=0, columnspan=18, pady=25, padx=65)
    else:
        newCancel=Button(Frame1000, text="<<Επιστροφή", padx=36, pady=11, command=lambda: goto(31))
        newCancel.grid(row=100, column=8, pady=25, padx=65)
    if n==3:
        messagebox.showinfo('Ενεργοποίηση δελτίου ανεργίας:', 'Το δελτίο ενεργοποιήθηκε με επιτυχία.')
    elif n==5:
         messagebox.showinfo('Απνεργοποίηση δελτίου ανεργίας:', 'Το δελτίο απενεργοποιήθηκε με επιτυχία.')        

def diagrafi(y, k): #παίρνει 2 ορίσματα, y --> το στοιχείο (εγγραφή) στην οποία θα γίνει κάποια ενέργεια, k --> (1, 2 για διαγραφή, 3 για επαναφορά από τα διαγραμμένα).
    if k==1: #υποβολή κωδικού για διαγραφή δελτίων ανεργίας. y[i] 
        global delValid2
        global delValid4
        global Frame23        
        Frame21.grid_forget() 
        Frame23=LabelFrame(root, bd=0)
        Frame23.grid(row=5, column=0, columnspan=18)
        delValid0=Label(Frame23, text="Για να πραγματοποιηθεί διαγραφή δελτίου από το σύστημα πρέπει να διαθέτετε \nδικαίωμα πρόσβασης στη βάση δεδομένων. Παρακαλώ εισάγετε στοιχεία χρήστη:", fg="red")
        delValid0.grid(row=5, column=0, columnspan=10, pady=25)
        delValid1=Label(Frame23, text="Username:", fg="red")
        delValid1.grid(row=6, column=4, padx=20, pady=15)                
        delValid2=Entry(Frame23, relief=SUNKEN, borderwidth=5, width=50)
        delValid2.grid(row=6, column=5, padx=20, pady=15)
        delValid3=Label(Frame23, text="Password:", fg="red")
        delValid3.grid(row=7, column=4, padx=20)                
        delValid4=Entry(Frame23, relief=SUNKEN, borderwidth=5, width=50)
        delValid4.grid(row=7, column=5, padx=20)
        delValidSubmit=Button(Frame23, text="Υποβολή", padx=35, pady=11, command=lambda: diagrafi(y, 2)) 
        delValidSubmit.grid(row=8, column=0, columnspan=10, pady=15)
    elif k==2: #οριστική διαγραφή δελτίων ανεργίας (ουσιαστικά, ΔΙΑΓΡΑΦΟΝΤΑΙ από το 'current.csv' ΚΑΙ ΕΓΓΡΑΦΟΝΤΑΙ ΓΙΑ ΠΙΘΑΝΗ ΜΕΛΛΟΝΤΙΚΗ ΧΡΗΣΗ (ΕΠΑΝΑΦΟΡΑ) στο 'previous.csv'.
        Frame23.grid_forget()
        global Frame24
        Frame24=LabelFrame(root, bd=0)
        Frame24.grid(row=5, column=0, columnspan=18)
        checkLogin=[]
        with open("password.csv", "r", newline="", encoding="utf-8") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                checkLogin.append(row)
            if len(checkLogin)==0:
                messagebox.showerror('Σφάλμα:', "Παρακαλώ πολύ επικοινωνήστε με την προγραμματίστρια, κωδικός σφάλματος: EMPTY_PASSWORD_0.")
            else:
                username=delValid2.get()
                password=delValid4.get()
                username=username.strip()
                password=password.strip()
                checkIn=[username.upper(), password.upper()]                         
                for x in checkLogin:
                    if checkIn==x:
                        delete=[]
                        with open("current.csv", "r", newline="", encoding="utf-8") as file:
                            ro=csv.reader(file, delimiter='$')
                            for row in ro:
                                delete.append(row)
                            for i in range(len(delete)):
                                if y==delete[i]:
                                    delete.pop(i)
                                    break
                        with open("current.csv", "w", newline="", encoding="utf-8") as file:
                            wo=csv.writer(file, delimiter='$')
                            for x in delete:
                                wo.writerow(x)
                            y[3]="" #από default σε όλα τα διαγραμμένα δελτία ημ/νίες (από... - έως...) ορίζονται '01-01-2022' και active - status: 'ΟΧΙ' -->  απενεργοποιημένη.
                            y[4]=""
                            y[12]='ΟΧΙ'
                            with open("previous.csv", "a", encoding="utf-8", newline="") as file:
                                wo=csv.writer(file, delimiter='$')
                                wo.writerow(y)
                        messagebox.showinfo('', "Η ενέργεια πραγματοποιήθηκε με επιτυχία, το δελτίο ανεργίας διαγράφηκε από το τρέχον \nαρχείο διαχείρισης, υπάρχει ωστόσο δυνατότητα επαναφοράς του οποτεδήποτε στο μέλλον.")                     
                        break
                    elif x==checkLogin[-1]:
                        messagebox.showerror('Σφάλμα:', "Αποτυχία επιβεβαίωσης στοιχείων πρόσβασης, το αίτημα διαγραφής απορρίφθηκε.")
                        break                    
    elif k==3: #επαναφορά από τα διαγραμμένα.
        FrameForScroll.grid_forget() 
        global deletedList
        global Frame33
        Frame33=LabelFrame(root, bd=0)
        Frame33.grid(row=5, column=0, columnspan=18)
        delAgain=Button(Frame33, text="Νέα επαναφορά", padx=25, pady=11, command=lambda: goto(62))
        delAgain.grid(row=100, column=8, padx=65, pady=45)            
        delReturnMenu=Button(Frame33, text="Κεντρικό μενού", padx=30, pady=11, command=lambda: goto(61)) 
        delReturnMenu.grid(row=100, column=9, padx=65, pady=45)        
        for i in range(len(deletedList)): #αφαίρεση του δελτίου ανεργίας από τα διαγραμμένα.
            if y==deletedList[i]:
                deletedList.pop(i)
                break
        with open("previous.csv", "w", encoding="utf-8", newline="") as file:
            wo=csv.writer(file, delimiter='$')
            for row in deletedList:
                wo.writerow(row)
        y[3]=20220101 #επαναφορά του (πρώην πλέον) διαγραμμένου δελτίου (από default: day1==day2==20220101, active='ΟΧΙ')
        y[4]=20220101
        y[12]='ΟΧΙ'  
        with open("current.csv", "a", encoding="utf-8", newline="") as file: 
            wo=csv.writer(file, delimiter='$')            
            wo.writerow(y)
            message="Η ενέργεια πραγματοποιήθηκε με επιτυχία, το δελτίο ανεργίας επαναφέρθηκε στο τρέχον \nαρχείο διαχείρισης, υπάρχει ωστόσο δυνατότητα διαγραφής του οποτεδήποτε στο μέλλον."
            messagebox.showinfo('Μήνυμα:', message)
    if k==2: #διαγραφή.
        delAgain=Button(Frame24, text="Νέα διαγραφή", padx=30, pady=11, command=lambda: goto(41))
        delAgain.grid(row=100, column=8, padx=65, pady=45)
        delReturnMenu=Button(Frame24, text="Κεντρικό μενού", padx=30, pady=11, command=lambda: goto(42)) 
        delReturnMenu.grid(row=100, column=9, padx=65, pady=45)  
                        
def update(x, y, i): #συνάρτηση με τρία ορίσματα (x--> Frame, y--> today[], i--> η τρέχουσα εγγραφή της λίστας today[]), ανακατευθύνει για ανανέωση κάρτας --> (newDate(Frame8, y[i])).    
    x.grid_forget()
    global Frame8
    global update1Print2
    global update2Print2
    global activeList
    activeList=y
    Frame2.grid_forget()
    Frame8=LabelFrame(root, bd=0)
    Frame8.grid(row=5, column=0, columnspan=18)
    updateLabel=Label(Frame8, text="ΑΝΑΝΕΩΣΗ ΚΑΡΤΑΣ ΑΝΕΡΓΙΑΣ", pady=15, fg="red", bg= "#d9d9d9")
    updateLabel.grid(row=6, column=0, columnspan=18, sticky=W+E)
    surnamePrint1=Label(Frame8, fg="red", text="ΕΠΩΝΥΜΟ:", padx=15, pady=5)
    surnamePrint1.grid(row=8, column=7, sticky=E)
    surnamePrint2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    surnamePrint2.grid(row=8, column=8)
    surnamePrint2.insert(0, y[i][0])
    namePrint1=Label(Frame8, fg="red", text="ΟΝΟΜΑ:", padx=15, pady=5)
    namePrint1.grid(row=9, column=7, sticky=E)
    namePrint2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    namePrint2.grid(row=9, column=8)
    namePrint2.insert(0, y[i][1])
    cardPrint1=Label(Frame8, fg="red", text="ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ:", padx=15, pady=5)
    cardPrint1.grid(row=10, column=7, sticky=E)
    cardPrint2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    cardPrint2.grid(row=10, column=8)
    cardPrint2.insert(0, y[i][2])
    update1Print1=Label(Frame8, fg="red", text="ΑΝΑΝΕΩΣΗ (ηη-μμ-εεεε ή ηη/μμ/εεεε) από:", padx=15, pady=5)
    update1Print1.grid(row=11, column=7, sticky=E)
    update1Print2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5)
    update1Print2.grid(row=11, column=8) 
    update2Print1=Label(Frame8, fg="red", text="ΑΝΑΝΕΩΣΗ (ηη-μμ-εεεε ή ηη/μμ/εεεε) έως:", padx=15, pady=5)
    update2Print1.grid(row=12, column=7, sticky=E)
    update2Print2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5)
    update2Print2.grid(row=12, column=8) 
    amkaPrint1=Label(Frame8, fg="red", text="ΑΜΚΑ:", padx=15, pady=5)
    amkaPrint1.grid(row=13, column=7, sticky=E)
    amkaPrint2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    amkaPrint2.grid(row=13, column=8)
    amkaPrint2.insert(0, y[i][5]) 
    afmPrint1=Label(Frame8, fg="red", text="ΑΦΜ:", padx=15, pady=5)
    afmPrint1.grid(row=14, column=7, sticky=E)
    afmPrint2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    afmPrint2.grid(row=14, column=8)
    afmPrint2.insert(0, y[i][6])
    akhaPrint1=Label(Frame8, fg="red", text="ΚΩΔΙΚΟΣ ΑΚΗΑ:", padx=15, pady=5)
    akhaPrint1.grid(row=15, column=7, sticky=E)
    akhaPrint2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    akhaPrint2.grid(row=15, column=8)
    akhaPrint2.insert(0, y[i][7])    
    DYPA1Print1=Label(Frame8, fg="red", text="ΚΩΔΙΚΟΙ ΔΥΠΑ (Username):", padx=15, pady=5)
    DYPA1Print1.grid(row=8, column=9, sticky=E)
    DYPA1Print2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    DYPA1Print2.grid(row=8, column=10)
    DYPA1Print2.insert(0, y[i][8])
    DYPA2Print1=Label(Frame8, fg="red", text="ΚΩΔΙΚΟΙ ΔΥΠΑ (Password):", padx=15, pady=5)
    DYPA2Print1.grid(row=9, column=9, sticky=E)   
    DYPA2Print2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    DYPA2Print2.grid(row=9, column=10)
    DYPA2Print2.insert(0, y[i][9])  
    TAXIS1Print1=Label(Frame8, fg="red", text="ΚΩΔΙΚΟΙ TAXISnet (Username):", padx=15, pady=5)
    TAXIS1Print1.grid(row=10, column=9, sticky=E)
    TAXIS1Print2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    TAXIS1Print2.grid(row=10, column=10)
    TAXIS1Print2.insert(0, y[i][10])   
    TAXIS2Print1=Label(Frame8, fg="red", text="ΚΩΔΙΚΟΙ TAXISnet (Password):", padx=15, pady=5)
    TAXIS2Print1.grid(row=11, column=9, sticky=E)
    TAXIS2Print2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    TAXIS2Print2.grid(row=11, column=10)
    TAXIS2Print2.insert(0, y[i][11])       
    activePrint1=Label(Frame8, fg="red", text="ΕΝΕΡΓΟΣ ΧΡΗΣΤΗΣ:", padx=15, pady=5)
    activePrint1.grid(row=12, column=9, sticky=E)
    activePrint2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    activePrint2.grid(row=12, column=10)
    activePrint2.insert(0, y[i][12])    
    planPrint1=Label(Frame8, fg="red", text="ΑΤΟΜ. ΣΧΕΔΙΟ ΔΡΑΣΗΣ:", padx=15, pady=5)
    planPrint1.grid(row=13, column=9, sticky=E)
    planPrint2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    planPrint2.grid(row=13, column=10)
    planPrint2.insert(0, y[i][13])        
    telPrint1=Label(Frame8, fg="red", text="ΤΗΛΕΦΩΝΟ:", padx=15, pady=5)
    telPrint1.grid(row=14, column=9, sticky=E)
    telPrint2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    telPrint2.grid(row=14, column=10)
    telPrint2.insert(0, y[i][14])        
    mailPrint1=Label(Frame8, fg="red", text="E-MAIL:", padx=15, pady=5)
    mailPrint1.grid(row=15, column=9, sticky=E)
    mailPrint2=Entry(Frame8, width=50, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    mailPrint2.grid(row=15, column=10)
    mailPrint2.insert(0, y[i][15])      
    notesPrint1=Label(Frame8, fg="red", text="ΠΑΡΑΤΗΡΗΣΕΙΣ:", padx=15, pady=5)
    notesPrint1.grid(row=22, column=7, sticky=E)
    notesPrint2=Text(Frame8, width=101, height=10, relief=SUNKEN, borderwidth=5, bg="#b3b3b3")
    notesPrint2.grid(row=22, column=8, columnspan=3)    
    notesPrint2.insert(INSERT, y[i][16])
    Frame1001=LabelFrame(Frame8,bd=0)
    Frame1001.grid(row=100, column=0, columnspan=18)
    newCancel=Button(Frame1001, text="<<Επιστροφή", padx=34, pady=11, command=lambda: goto(52)) 
    newCancel.grid(row=100, column=7, pady=30, padx=45)
    newUpdate=Button(Frame1001,text="Ανανέωση", padx=40, pady=11, command=lambda i=i: newDate(Frame8, y[i]))
    newUpdate.grid(row=100, column=8, pady=30, padx=45)
    newReturn=Button(Frame1001,text="Κεντρικό μενού", padx=30, pady=11, command=lambda: goto(10))
    newReturn.grid(row=100, column=10, pady=30, padx=45)    

def newDate(x, y):
    global day1
    global day2
    global messageDate
    day1=update1Print2.get()
    day2=update2Print2.get()
    x.grid_forget()
    a=checkDate(day1)
    b=checkDate(day2)
    global Frame9
    Frame9=LabelFrame(root, bd=0)
    Frame9.grid(row=5, column=0, columnspan=28)
    returnDate=Button(Frame9, text="<<Επιστροφή", padx=35, pady=11, command=lambda: goto(11))        
    returnDate.grid(row=120, column=0, columnspan=18, pady=45)    
    if a==0 or b==0:
        message="Μη έγκυρη ημερομηνία ανανέωσης της κάρτας, η ενέργεια ακυρώθηκε."
        messagebox.showerror('Σφάλμα:', message)
    else:
        y[3]=a #νέα ημ/νία 'από...', το [0] στο y[0][3], y[0][4] το πήρα από σύμβαση (για να έχω πρόσβαση στην ημ/νία χρησιμοποιώ το 1ο στοιχείο της λίστας).
        y[4]=b #νέα ημ/νία 'έως...'           
        newList=[]        
        with open("current.csv", "r", newline="", encoding="utf-8") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                newList.append(row)
            for k in newList:              
                if str(k[5])==str(y[5]) and str(k[6])==str(y[6]): #έλεγχος ταυτότητας με βάση: ΑΜΚΑ, ΑΦΜ, ΟΧΙ με αρ. κάρτας ΔΥΠΑ γιατί μπορεί να αλλάξει ενώ οι άλλοι αριθμοί είναι σταθεροί.
                    if int(y[3])<=int(k[3]) or int(y[4])<=int(k[3]) or int(y[3])<int(currentDate()) or int(y[4])<int(currentDate()): #έλεγχος αν οι νέες ημ/νίες ειναι μικρότερες από
                        message="Μη αποδεκτές ημερομηνίες, η ενέργεια ακυρώθηκε." #τις προηγούμενες ή αν η νέα ημ/νία('έως') είναι προγενέστερη της ημ/νίας ('από') ή τέλος αν οι νέες
                        messagebox.showerror('Σφάλμα:', message)                  #ημ/νίες είναι μικρότερες από την τρέχουσα.
                        break
                    else:
                        k[3]=y[3]
                        k[4]=y[4]                                              
                        with open("current.csv", "w", newline="", encoding="utf-8") as file:
                            wo=csv.writer(file, delimiter='$')
                            for m in newList:
                                wo.writerow(m)
                            message="Η ανανέωση πραγματοποιήθηκε με επιτυχία."
                            messagebox.showinfo('', message)                           
                    break     
                elif k==newList[-1]:
                    message="Δε βρέθηκε η κάρτα ανεργίας με βάση τα στοιχεία αναζήτησης, ελέγξτε την εγκυρότητά τους, η ενέργεια ακυρώθηκε."
                    messagebox.showerror('Σφάλμα:', message)                                                                           

def insert(x, m): #παίρνει δύο παραμέτρους -->x, το Frame που καταργείται, m-->counter που δηλώνει ποια ενέργεια εκτελεί η function def insert().
    x.grid_forget()
    global ananewseis
    ananewseis=''
    if m==1: #προβολή ενεργών/ανενεργών δελτίων.
        global Frame13
        Frame13=LabelFrame(root, bd=0)
        Frame13.grid(row=6, column=0, columnspan=18)        
        energeies=Label(Frame13, text="ΕΝΕΡΓΕΙΕΣ (ΔΕΛΤΙΑ)", fg="red", bg="#d9d9d9", pady=25)
        energeies.grid(row=5, column=0, columnspan=18, sticky=W+E)
        global activeList
        global deletedList
        tempList=[]
        activeList=[]
        deletedList=[]
        global update2
        update2=0
        with open("current.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                tempList.append(row)
            for y in tempList:
                if y[12]=='ΝΑΙ': #ο χρήστης είναι ενεργός.
                    activeList.append(y)
                    if y[3]<=currentDate():
                        update2+=1
            if update2!=0:                
                ananewseis="\n\nΒρέθηκαν στο σύστημα "+str(update2)+" δελτία για ανανέωση."
            if len(tempList)-len(activeList)==0:
                global deactivated
                deactivated="και κανένας ανενεργός χρήστης." 
            else:                                         
                deactivated="και "+str(len(tempList)-len(activeList))+" ανενεργοί χρήστες."
        with open("previous.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                deletedList.append(row)
            if len(deletedList)==0: #δεν υπάρχουν διαγραμμένα δελτία.
                global message2
                message2="\n\nΔεν υπάρχουν αυτή την στιγμή στο σύστημα διαγραμμένα δελτία."
            else:
                global total
                if len(deletedList)==1:
                     total=" διαγραμμένο δελτίο."
                else:
                    total=" διαγραμμένα δελτία."
                message2="\n\nΒρέθηκαν στο σύστημα "+str(len(deletedList))+total                
            if len(activeList)==0: #δεν υπάρχουν ενεργοί χρήστες (πολύ 'οριακή' - και μάλλον απίθανη - περίπτωση, αλλά καλό είναι να υπάρχει.
                message="Δεν υπάρχουν αυτή την στιγμή στο σύστημα ενεργοί χρήστες "+deactivated+message2+ananewseis                
            else:
                if len(activeList)==1:
                    message="Βρέθηκε στο σύστημα ένας ενεργός χρήστης "+deactivated+message2+ananewseis
                else:
                    message="Βρέθηκαν στο σύστημα "+str(len(activeList))+" ενεργοί χρήστες "+deactivated+message2+ananewseis
            activeResults=Label(Frame13, text=message)
            activeResults.grid(row=10, column=0, columnspan=18, pady=25)
            activeReturn=Button(Frame13, text="<<Επιστροφή", padx=35, pady=11, command=lambda: goto(4))
            activeReturn.grid(row=50, column=6, padx=35)
            updateCards=Button(Frame13, text="Δελτία για ανανέωση", padx=17, pady=11, command=lambda: goto(132))
            updateCards.grid(row=50, column=7, padx=35)
            activeShow=Button(Frame13, text="Ενεργοί χρήστες", padx=27, pady=11, command=lambda: goto(69))
            activeShow.grid(row=50, column=8, padx=35)
            deactiveShow=Button(Frame13, text="Ανενεργοί χρήστες", padx=24, pady=11, command=lambda: goto(44)) 
            deactiveShow.grid(row=50, column=9, padx=35)
            deletedShow=Button(Frame13, text="Διαγραμμένα δελτία", padx=23, pady=11, command=lambda: goto(60)) 
            deletedShow.grid(row=50, column=10, padx=35)                               
    elif m==2: #Εισαγωγή/Νέα εγγραφή δελτίου ανεργίας
        global surnamePrint2
        global namePrint2
        global cardPrint2
        global update1Print2      
        global update2Print2       
        global amkaPrint2
        global afmPrint2
        global DYPA1Print2
        global DYPA2Print2
        global TAXIS1Print2
        global TAXIS2Print2
        global akhaPrint2
        global activePrint2
        global planPrint2
        global telPrint2
        global mailPrint2
        global notesPrint2
        Frame13=LabelFrame(root, bd=0)
        Frame13.grid(row=6, column=0, columnspan=18) 
        updateLabel=Label(Frame13, text="ΔΗΜΙΟΥΡΓΙΑ ΝΕΑΣ ΚΑΡΤΑΣ ΑΝΕΡΓΙΑΣ", pady=25, fg="red", bg= "#d9d9d9")
        updateLabel.grid(row=6, column=0, columnspan=18, sticky=W+E)
        surnamePrint1=Label(Frame13, fg="red", text="ΕΠΩΝΥΜΟ:", padx=15, pady=5)
        surnamePrint1.grid(row=8, column=7, sticky=E)
        surnamePrint2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        surnamePrint2.grid(row=8, column=8)
        namePrint1=Label(Frame13, fg="red", text="ΟΝΟΜΑ:", padx=15, pady=5)
        namePrint1.grid(row=9, column=7, sticky=E)
        namePrint2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        namePrint2.grid(row=9, column=8)
        cardPrint1=Label(Frame13, fg="red", text="ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ:", padx=15, pady=5)
        cardPrint1.grid(row=10, column=7, sticky=E)
        cardPrint2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        cardPrint2.grid(row=10, column=8)
        update1Print1=Label(Frame13, fg="red", text="ΑΝΑΝΕΩΣΗ από:", padx=15, pady=5)
        update1Print1.grid(row=11, column=7, sticky=E)
        update1Print2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        update1Print2.grid(row=11, column=8) 
        update2Print1=Label(Frame13, fg="red", text="ΑΝΑΝΕΩΣΗ έως:", padx=15, pady=5)
        update2Print1.grid(row=12, column=7, sticky=E)
        update2Print2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        update2Print2.grid(row=12, column=8) 
        amkaPrint1=Label(Frame13, fg="red", text="ΑΜΚΑ:", padx=15, pady=5)
        amkaPrint1.grid(row=13, column=7, sticky=E)
        amkaPrint2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        amkaPrint2.grid(row=13, column=8)
        afmPrint1=Label(Frame13, fg="red", text="ΑΦΜ:", padx=15, pady=5)
        afmPrint1.grid(row=14, column=7, sticky=E)
        afmPrint2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        afmPrint2.grid(row=14, column=8)
        akhaPrint1=Label(Frame13, fg="red", text="ΚΩΔΙΚΟΣ ΑΚΗΑ:", padx=15, pady=5)
        akhaPrint1.grid(row=15, column=7, sticky=E)
        akhaPrint2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        akhaPrint2.grid(row=15, column=8)        
        DYPA1Print1=Label(Frame13, fg="red", text="ΚΩΔΙΚΟΙ ΔΥΠΑ (Username):", padx=15, pady=5)
        DYPA1Print1.grid(row=8, column=9, sticky=E)
        DYPA1Print2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        DYPA1Print2.grid(row=8, column=10)
        DYPA2Print1=Label(Frame13, fg="red", text="ΚΩΔΙΚΟΙ ΔΥΠΑ (Password):", padx=15, pady=5)
        DYPA2Print1.grid(row=9, column=9, sticky=E)   
        DYPA2Print2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        DYPA2Print2.grid(row=9, column=10)
        TAXIS1Print1=Label(Frame13, fg="red", text="ΚΩΔΙΚΟΙ TAXISnet (Username):", padx=15, pady=5)
        TAXIS1Print1.grid(row=10, column=9, sticky=E)
        TAXIS1Print2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        TAXIS1Print2.grid(row=10, column=10)   
        TAXIS2Print1=Label(Frame13, fg="red", text="ΚΩΔΙΚΟΙ TAXISnet (Password):", padx=15, pady=5)
        TAXIS2Print1.grid(row=11, column=9, sticky=E)
        TAXIS2Print2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        TAXIS2Print2.grid(row=11, column=10)          
        activePrint1=Label(Frame13, fg="red", text="ΕΝΕΡΓΟΣ ΧΡΗΣΤΗΣ:", padx=15, pady=5)
        activePrint1.grid(row=12, column=9, sticky=E)
        activePrint2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        activePrint2.grid(row=12, column=10, )    
        planPrint1=Label(Frame13, fg="red", text="ΑΤΟΜ. ΣΧΕΔΙΟ ΔΡΑΣΗΣ:", padx=15, pady=5)
        planPrint1.grid(row=13, column=9, sticky=E)
        planPrint2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        planPrint2.grid(row=13, column=10, )        
        telPrint1=Label(Frame13, fg="red", text="ΤΗΛΕΦΩΝΟ:", padx=15, pady=5)
        telPrint1.grid(row=14, column=9, sticky=E)
        telPrint2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        telPrint2.grid(row=14, column=10,)       
        mailPrint1=Label(Frame13, fg="red", text="E-MAIL:", padx=15, pady=5)
        mailPrint1.grid(row=15, column=9, sticky=E)
        mailPrint2=Entry(Frame13, width=50, relief=SUNKEN, borderwidth=5)
        mailPrint2.grid(row=15, column=10, )     
        notesPrint1=Label(Frame13, fg="red", text="ΠΑΡΑΤΗΡΗΣΕΙΣ:", padx=15, pady=5)
        notesPrint1.grid(row=22, column=7, sticky=E+N)
        notesPrint2=Text(Frame13, width=101, height=10, relief=SUNKEN, borderwidth=5)
        notesPrint2.grid(row=22, column=8, columnspan=3)
        Frame31=LabelFrame(Frame13, bd=0)
        Frame31.grid(row=100, column=0, columnspan=18)
        newCancel=Button(Frame31, text="<<Επιστροφή", padx=35, pady=11, command=lambda: goto(4))
        newCancel.grid(row=100, column=8, padx=65, pady=10)
        newUpdate=Button(Frame31,text="Εγγραφή", padx=45, pady=11, command=lambda: goto(20))
        newUpdate.grid(row=100, column=9, padx=65, pady=10)
    elif m==3: #Αναζήτηση δελτίων ανεργίας.
        global Frame16
        global surnameSearch2
        global cardSearch2
        global amkaSearch2
        global afmSearch2
        global akhaSearch2
        global update1Search2
        global update2Search2
        global activeSearch2
        Frame16=LabelFrame(root, bd=0)
        Frame16.grid(row=5, column=0, columnspan=18)
        searchLabel1=Label(Frame16, text="ΑΝΑΖΗΤΗΣΗ ΔΕΛΤΙΩΝ ΑΝΕΡΓΙΑΣ", fg="red", bg="#d9d9d9",  pady=25, padx=550)
        searchLabel1.grid(row=6, column=0, columnspan=18, sticky=W+E)
        searchLabel2=Label(Frame16, text="Αναζήτηση με βάση:", fg="red", pady=15)
        searchLabel2.grid(row=7, column=0, columnspan=18)
        surnameSearch1=Label(Frame16, fg="red", text="ΕΠΩΝΥΜΟ:", padx=15, pady=20)
        surnameSearch1.grid(row=8, column=6, sticky=E)
        surnameSearch2=Entry(Frame16, width=50, relief=SUNKEN, borderwidth=5)
        surnameSearch2.grid(row=8, column=7)
        cardSearch1=Label(Frame16, fg="red", text="ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ:", padx=15, pady=20)
        cardSearch1.grid(row=9, column=6, sticky=E)
        cardSearch2=Entry(Frame16, width=50, relief=SUNKEN, borderwidth=5)
        cardSearch2.grid(row=9, column=7)        
        amkaSearch1=Label(Frame16, fg="red", text="ΑΜΚΑ:", padx=15, pady=20)
        amkaSearch1.grid(row=10, column=6, sticky=E)
        amkaSearch2=Entry(Frame16, width=50, relief=SUNKEN, borderwidth=5)
        amkaSearch2.grid(row=10, column=7)
        afmSearch1=Label(Frame16, fg="red", text="ΑΦΜ:", padx=15, pady=20)
        afmSearch1.grid(row=11, column=6, sticky=E)
        afmSearch2=Entry(Frame16, width=50, relief=SUNKEN, borderwidth=5)
        afmSearch2.grid(row=11, column=7)
        akhaSearch1=Label(Frame16, fg="red", text="ΚΩΔΙΚΟΣ ΑΚΗΑ:", padx=15, pady=20)
        akhaSearch1.grid(row=8, column=9, sticky=E)
        akhaSearch2=Entry(Frame16, width=50, relief=SUNKEN, borderwidth=5)
        akhaSearch2.grid(row=8, column=10)
        update1Search1=Label(Frame16, fg="red", text="ΑΝΑΝΕΩΣΗ από:", padx=15, pady=20)
        update1Search1.grid(row=9, column=9, sticky=E)
        update1Search2=Entry(Frame16, width=50, relief=SUNKEN, borderwidth=5)
        update1Search2.grid(row=9, column=10) 
        update2Search1=Label(Frame16, fg="red", text="ΑΝΑΝΕΩΣΗ έως:", padx=15, pady=20)
        update2Search1.grid(row=10, column=9, sticky=E)
        update2Search2=Entry(Frame16, width=50, relief=SUNKEN, borderwidth=5)
        update2Search2.grid(row=10, column=10)
        activeSearch1=Label(Frame16, fg="red", text="ΕΝΕΡΓΟΣ ΧΡΗΣΤΗΣ (ΝΑΙ/ΟΧΙ):", padx=15, pady=20)
        activeSearch1.grid(row=11, column=9, sticky=E)
        activeSearch2=Entry(Frame16, width=50, relief=SUNKEN, borderwidth=5)
        activeSearch2.grid(row=11, column=10)        
        for i in range(4):
            choiceSearch=Button(Frame16, text="Επιλογή", padx=40, pady=11, command=lambda i=i: search(Frame16, i, 1))
            choiceSearch.grid(row=8+i, column=8, padx=15)
        for i in range(4, 8):
            choiceSearch=Button(Frame16, text="Επιλογή", padx=40, pady=11, command=lambda i=i: search(Frame16, i, 1))            
            choiceSearch.grid(row=4+i, column=11, padx=15)
        returnSearch=Button(Frame16, text="<<Επιστροφή", padx=40, pady=11, command=lambda: goto(23))
        returnSearch.grid(row=100, column=0, columnspan=18, pady=140)
    elif m==4: #Τροποποίηση δελτίου στοιχείων δελτίου ανεργίας (Ή στοιχείων ωφελούμενου, πχ αρ. κάρτας ΔΥΠΑ)-->ΕΔΩ ΥΠΑΡΧΕΙ ΚΑΙ Η ΑΝΑΝΕΩΣΗ ΤΗΣ ΗΜ/ΝΙΑΣ ΤΩΝ ΔΕΛΤΙΩΝ ΑΝΕΡΓΙΑΣ!!!
        global Frame18
        Frame18=LabelFrame(root, bd=0)
        Frame18.grid(row=5,column=0, columnspan=18)
        global changeCard        
        global update
        global returnCard
        global changeLabel
        goto(28)
    elif m==5: #διαγραφή δελτίων ανεργίας. ΠΡΟΣΟΧΗ!!! ΔΙΑΦΟΡΕΤΙΚΌ ΑΠΟ ΤΗΝ ΑΠΕΝΕΡΓΟΠΟΙΗΣΗ (ΜΗ ΕΝΕΡΓΉ ΚΑΡΤΑ ΠΟΥ ΔΕΝ ΤΗΝ ΠΑΡΑΚΟΛΟΥΘΟΥΜΕ ΠΙΑ ΑΛΛΑ ΥΠΑΡΧΕΙ ΣΤΗ ΒΑΣΗ ΔΕΔΟΜΕΝΩΝ, ΣΤΟ 
        global Frame22 #'CURRENT.CSV') H ΔΙΑΓΡΑΦΉ ΠΗΓΑΙΝΕΙ ΣΤΟ 'PREVIOUS.CSV' ΚΑΙ ΤΗ ΧΡΗΣΙΜΟΠΟΙΟΥΜΕ ΜΟΝΟ ΑΝ ΘΕΛΟΥΜΕ ΝΑ ΕΞΑΦΑΝΙΣΟΥΜΕ ΚΑΠΟΙΑ ΕΓΓΡΑΦΗ, ΑΛΛΙΩΣ ΚΑΝΟΥΜΕ ΔΙΟΡΘΩΣΗ ΣΤΟΙΧΕΙΩΝ 
        Frame22=LabelFrame(root, bd=0) #(ΤΡΟΠΟΠΟΙΗΣΗ) Ή ΑΠΕΝΕΡΓΟΠΟΙΗΣΗ.
        Frame22.grid(row=5, column=0, columnspan=18)
        searchLabel1=Label(Frame22, text="ΔΙΑΓΡΑΦΗ ΔΕΛΤΙΩΝ ΑΝΕΡΓΙΑΣ", fg="red", bg="#d9d9d9",  pady=25)
        searchLabel1.grid(row=6, column=0, columnspan=18, sticky=W+E)
        searchLabel2=Label(Frame22, text="Αναζήτηση με βάση:", fg="red", pady=15)
        searchLabel2.grid(row=7, column=0, columnspan=18)
        surnameSearch1=Label(Frame22, fg="red", text="ΕΠΩΝΥΜΟ:", padx=15, pady=20)
        surnameSearch1.grid(row=8, column=7, sticky=E)
        surnameSearch2=Entry(Frame22, width=50, relief=SUNKEN, borderwidth=5)
        surnameSearch2.grid(row=8, column=8)
        cardSearch1=Label(Frame22, fg="red", text="ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ:", padx=15, pady=20)
        cardSearch1.grid(row=9, column=7, sticky=E)
        cardSearch2=Entry(Frame22, width=50, relief=SUNKEN, borderwidth=5)
        cardSearch2.grid(row=9, column=8)        
        amkaSearch1=Label(Frame22, fg="red", text="ΑΜΚΑ:", padx=15, pady=20)
        amkaSearch1.grid(row=10, column=7, sticky=E)
        amkaSearch2=Entry(Frame22, width=50, relief=SUNKEN, borderwidth=5)
        amkaSearch2.grid(row=10, column=8)
        afmSearch1=Label(Frame22, fg="red", text="ΑΦΜ:", padx=15, pady=20)
        afmSearch1.grid(row=11, column=7, sticky=E)
        afmSearch2=Entry(Frame22, width=50, relief=SUNKEN, borderwidth=5)
        afmSearch2.grid(row=11, column=8)
        akhaSearch1=Label(Frame22, fg="red", text="ΚΩΔΙΚΟΣ ΑΚΗΑ:", padx=15, pady=20)
        akhaSearch1.grid(row=12, column=7, sticky=E)
        akhaSearch2=Entry(Frame22, width=50, relief=SUNKEN, borderwidth=5)
        akhaSearch2.grid(row=12, column=8)        
        for i in range(5):
            choiceSearch=Button(Frame22, text="Επιλογή", padx=40, pady=11, command=lambda i=i: search(Frame22, i, 2))
            choiceSearch.grid(row=8+i, column=9, padx=15)
        returnSearch=Button(Frame22, text="<<Επιστροφή", padx=40, pady=11, command=lambda: goto(37))
        returnSearch.grid(row=100, column=0, columnspan=18, pady=70)
    elif m==6: #Ενέργειες (Memo).
        global Frame36
        Frame36=LabelFrame(root, bd=0)
        Frame36.grid(row=5, column=0, columnspan=18)
        memoLabel=Label(Frame36, text="ΕΝΕΡΓΕΙΕΣ (MEMO)", fg="red", bg="#d9d9d9",  pady=25)
        memoLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        newMemo=Button(Frame36, text="Εισαγωγή (memo)", padx=26, pady=11, command=lambda: goto(73))
        newMemo.grid(row=6, column=6, padx=20, pady=45)
        alterMemo=Button(Frame36, text="Διόρθωση (memo)", padx=24, pady=11, command=lambda: goto(79))
        alterMemo.grid(row=6, column=7, padx=20, pady=45)
        delMemo=Button(Frame36, text="Ακύρωση (memo)", padx=27, pady=11, command=lambda: goto(90))
        delMemo.grid(row=6, column=8, padx=20, pady=45)
        showMemo=Button(Frame36, text="Προβολή (memo)", padx=28, pady=11, command=lambda: goto(98))
        showMemo.grid(row=6, column=9, padx=20, pady=45)
        showMemo=Button(Frame36, text="Έκθεση εργ. συμβούλου", padx=12, pady=11, command=lambda: fileHandler(1))
        showMemo.grid(row=6, column=10, padx=20, pady=45)        
        returnMemo=Button(Frame36, text="<<Επιστροφή", padx=34, pady=11, command=lambda: goto(72))
        returnMemo.grid(row=6, column=11, padx=20, pady=45)
    elif m==7: #ευρετήριο.
        x.grid_forget()
        global Frame28
        Frame28=LabelFrame(root, bd=0)
        Frame28.grid(row=5, column=0, columnspan=18)
        indexLabel=Label(Frame28, text="ΕΥΡΕΤΗΡΙΟ ΕΞΥΠΗΡΕΤΟΥΜΕΝΩΝ ΑΝΕΡΓΩΝ", fg="red", bg="#d9d9d9", pady=25)
        indexLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
        global tempIndex
        tempIndex=[]
        temp=[]
        with open("current.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                temp.append([row[0], row[1]])
        with open("previous.csv", "r", encoding="utf-8", newline="") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                temp.append([row[0], row[1]])  
            for record in temp:
                if not record in tempIndex: #κόψιμο διπλοεγγραφής (διαγραμμένο δελτίο με ίδια ΑΜΚΑ, ΑΦΜ)., or (record[6] in tempIndex))
                    tempIndex.append(record)
            tempIndex.sort() #ταξινόμηση με βάση το επώνυμο (για το ευρετήριο).
        for i in range(len(tempIndex)):
            j=i//20 #--> το ακέραιο πηλίκο της διαίρεσης i, 20 (θα το χρησιμοποιήσουμε μαζί με το modulo για το layout της εκτύπωσης).
            q=i%20
            indexCategory0=Label(Frame28, text="Α/Α", fg="red")
            indexCategory0.grid(row=6, column=0+3*j, sticky=W, pady=5, padx=5)
            indexCategory1=Label(Frame28, text="ΟΝΟΜΑΤΕΠΩΝΥΜΟ", fg="red")
            indexCategory1.grid(row=6, column=1+3*j, sticky=W, pady=5, padx=5)                    
            indexAa=Text(Frame28, width=3, height=1, borderwidth=0, bg="#f2f2f2")
            indexAa.grid(row=7+q, column=0+3*j, sticky=W, padx=10)
            indexAa.insert(INSERT, str(i+1)) 
            indexSurname=Text(Frame28, width=40, height=1, borderwidth=0, bg="#f2f2f2")
            indexSurname.grid(row=7+q, column=1+3*j, sticky=W, padx=10)
            indexSurname.insert(INSERT, str(tempIndex[i][0])+" "+str(tempIndex[i][1])) 
            indexName=Text(Frame28, width=20, height=1, borderwidth=0)       
        Frame29=LabelFrame(Frame28, bd=0)
        Frame29.grid(row=1000, column=0, columnspan=18)
        indexReturn=Button(Frame29, text="<<Επιστροφή", padx=40, pady=11, command=lambda: goto(50))
        indexReturn.grid(row=1000, column=8, pady=25, padx=65)

def fileHandler(x): #διαχείριση αρχείων (memo), παίρνει ένα όρισμα που δείχνει ποια ενέργεια εκτελείται.
    global status3
    if status3=='edit_file':
        Frame53.grid_forget()
        status3=''        
        Frame53.grid_forget()    
    global Frame36
    Frame36.grid_forget()
    global Frame52
    Frame52=LabelFrame(root, bd=0)
    Frame52.grid(row=5, column=0, columnspan=18)
    memoLabel=Label(Frame52, text="ΕΝΕΡΓΕΙΕΣ (MEMO)\n\nΔιαχείριση αρχείων (φόρμα εργ. συμβούλου)", fg="red", bg="#d9d9d9",  pady=15)
    memoLabel.grid(row=5, column=0, columnspan=18, sticky=W+E)
    if x==1: #menu fileHandler.
        delFile=Button(Frame52, text="<<Επιστροφή", padx=31, pady=11, command=lambda: insert(Frame52, 6)) 
        delFile.grid(row=10, column=6, padx=25, pady=45)        
        newFile=Button(Frame52, text="Εισαγωγή", padx=42, pady=11, command=lambda: goto(118)) 
        newFile.grid(row=10, column=7, padx=25, pady=45)
        showFile=Button(Frame52, text="Αναζήτηση", padx=38, pady=11, command=lambda: goto(124)) 
        showFile.grid(row=10, column=10, padx=25, pady=45 )  
        delFile=Button(Frame52, text="Κεντρικό μενού", padx=28, pady=11, command=lambda: goto(122)) 
        delFile.grid(row=10, column=11, padx=25, pady=45)
    else:        
        if x==2: #<<Επιστροφή στο μενού της φόρμας εργ. συμβούλου από τη φόρμα εισαγωγής δεδομένων.
            Frame53.grid_forget()
            Frame36=LabelFrame(root, bd=0)
            Frame36.grid(row=5, column=0, columnspan=18)
            fileHandler(1)        
        elif x==3: #αποθήκευση της έκθεσης εργ. συμβούλων σε αρχείο ('.txt').
            global Frame55
            Frame55=LabelFrame(root, bd=0)
            Frame55.grid(row=5, column=0, columnspan=18)
            line3=sumvoulos2.get()
            line3=line3.strip()
            line3=line3.upper()
            text1=paratiriseis2.get('1.0', END)
            text1=text1.strip()
            text2=ekthesi2.get('1.0', END)
            text2=text2.strip()
            global name2
            name2=str(line2)[-2:]+"-"+str(line2)[-4:-2]+"-"+str(line2)[:4]+"_"+str(line4)+'_0' #το όνομα του αρχείου που θα καταχωρηθεί θα προέλθει από την ημερομηνία εγγραφής του 
            global name                                                                        #αρχείου και το επώνυμο του εξυπηρετούμενου (σε string) διαχωρισμένα με '_'.
            if not os.path.exists('Φόρμες εργ. συμβούλων\\'+name2+'.txt'): #νέο αρχείο.
                name=name2
            else: #υπάρχει το αρχείο, δύο περιπτπώσεις στην συνέχεια:--> Τροποποίηση δελτίου (επομένως, αντικατάστασή του) ή νέα φόρμα για ίδια ημ/νία και ίδιο εξυπηρετούμενο.
                name=str(checkName(name2)) #περίπτωση τροποποιησης--> διαγραφή του προηγούμενου αρχείου (επιλογή αντί του 'w' - mode για την περίπτωση να τροποποιηθεί η ημερομηνία                     
                                           #(στην περίπτωση αυτή θα δημιουργηθεί νέο αρχείο με διαφορετική ονομασία, καθώς το πρώτο τμήμα του ονόματος του αρχείου ξεκινά με την     
                                           #ημερομηνία).            
            with open('Φόρμες εργ. συμβούλων\\'+name+'.txt', "w", encoding="utf-8", newline="") as file:
                file.write(str(line1)+'\n')
                file.write(str(line2)+'\n')
                file.write(str(line3)+'\n')
                for line in text1:
                    file.write(line)
                file.write('\n'+'ΠΑΡΑΤΗΡΗΣΕΙΣ:'+'\n') #πατέντα, θα λειτουργήσει ως διαχωριστικό ανάμεσα στο κείμενο των παρατηρήσεων και το κείμενο της έκθεσης στο τέλος (να μπορούμε
                for line in text2:                #εντοπίζοντας τη φράση 'ΠΑΡΑΤΗΡΗΣΕΙΣ' να ξεχωρίζουμε μεταξύ τους τα δύο κείμενα.
                    file.write(line)
            newEntry=Button(Frame55, text="Νέα καταχώρηση", padx=25, pady=11, command=lambda: fileHandler(4))
            newEntry.grid(row=10, column=7, padx=65, pady=45)
            newEntry=Button(Frame55, text="<<Επιστροφή", padx=35, pady=11, command=lambda: fileHandler(5))
            newEntry.grid(row=10, column=8, padx=65, pady=45)
            newEntry=Button(Frame55, text="Κεντρικό μενού", padx=32, pady=11, command=lambda: fileHandler(6))
            newEntry.grid(row=10, column=9, padx=65, pady=45)                    
            if os.path.exists('Φόρμες εργ. συμβούλων\\'+name+'.txt'): #έλεγχος αν δημιουργήθηκε το αρχείο και αντίστοιχο μήνυμα στην οθόνη. Το πρώτο κομμάτι ('Φόρμες...' είναι το 
              messagebox.showinfo('Εγγραφή αρχείου:', 'Το αρχείο αποθηκεύτηκε με επιτυχία.') #μονοπάτι του φακέλου στο οποίο αποθηκεύονται τα αρχεία (memo).
            else:
              messagebox.showerror('Σφάλμα:', 'Το αρχείο δεν αποθηκεύτηκε.')
        elif x==4: #νέα καταχώρηση στη φόρμα εργ. συμβούλων.
            Frame55.grid_forget()
            Frame52.grid(row=5, column=0, columnspan=18)
            goto(118)
        elif x==5: #<<Επιστροφή στη φόρμα μενού ενεργειών μετά από καταχώρηση φόρμας εργ. συμβούλου.
            status3=''
            Frame55.grid_forget()
            Frame36.grid(row=5, column=0, columnspan=18)
            fileHandler(1)
        elif x==6: #<<Επιστροφή στο κεντρικό μενού μετά από καταχώρηση φόρμας εργ. συμβούλου.
            Frame55.grid_forget()
            menu()            

def checkName(arg): #έλεγχος διαθεσιμότητας ονόματος αρχείου για αποθήκευση και αλγόριθμος για να δοθεί το πρώτο διαθέσιμο όνομα στο υπό έλεγχο αρχείο (αν χεριαστεί).
    i=0
    j=-1 #δείκτης που 'δείχνει' σε ποια θέση του string γίνεται ο έλεγχος.
    while i<=9:
        while os.path.exists('Φόρμες εργ. συμβούλων\\'+arg+'.txt') and arg[j].isdigit(): #έλεγχος αν υπάρχει ήδη αρχείο με το συγκεκριμένο όνομα.
            i=i+1
            arg=str(arg[:j])+str(i)
            if not os.path.exists('Φόρμες εργ. συμβούλων\\'+arg+'.txt'):
                return str(arg)
            if i==9: #πηγαίνει μία θέση προς τα αριστερά ο έλεγχος των ψηφίων.
                arg[j]=0
                addNumber(arg, j-1)
                break
            
def addNumber(arg, x):
    if arg[x].isdigit():
        if arg[x]<9:
            arg[x]=int(arg[x])+1
        else: #μηδενίζει το ψηφίο και αυξάνει κατά ένα στην συνέχεια το προηγουμενό του.
            arg[x]=0
            x=x-1
            addNumber(arg[x]) #self-invoke.
    else: #φτάσαμε στο πρώτο κατά σειρά ψηφίο. Ίδια λογική και εδώ, με τη διαφορά πως αν αυτό ισούται με 9, τότε θα πρέπει να μηδενιστεί και στην συγκεκριμένη θέση του string θα
        if arg[x]<9:  #χρειαστεί να προσθέσουμε μία μονάδα (πχ, αν είχαμε αρχικά 999, τώρα θα γίνει -->1000)
            arg[x]=str(int(arg[x])+1)
        else:
            arg[x]=0
            arg=arg[:x]+"1"+arg[x:]                        
    
def search(x, k, n): #Αναζήτηση δελτίου ανεργίας, παίρνει 3 ορίσματα-->x (Frame που θα καταργηθεί), -->k (επιλογή από την insert(x, 3) που δείχνει το κριτίριο αναζήτησης, 
    x.grid_forget() #n-->ενέργεια που θα ακολουθήσει(πχ διαγραφή), αναζήτηση, n==1 -->διαγραφή, n==2.
    global Frame17
    Frame17=LabelFrame(root, bd=0)
    Frame17.grid(row=5, column=0, columnspan=18)
    global option
    option=n
    if option==1:
        labelText="ΑΝΑΖΗΤΗΣΗ ΔΕΛΤΙΩΝ ΑΝΕΡΓΙΑΣ"
    else:
        labelText="ΔΙΑΓΡΑΦΗ ΔΕΛΤΙΩΝ ΑΝΕΡΓΙΑΣ"
    label=Label(Frame17, text=labelText, fg="red", bg="#d9d9d9",  pady=15)
    label.grid(row=5, column=0, columnspan=18, sticky=W+E)
    errorFlag=0
    message=""
    surname=surnameSearch2.get()
    card2=cardSearch2.get()
    amka2=amkaSearch2.get()
    afm2=afmSearch2.get()
    akha2=akhaSearch2.get()
    surname=surname.strip()
    surname=surname.upper()
    if k==0 and len(surname)==0:
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση."
    card2=card2.strip()
    card2=card2.split() #κόψιμο κενών ανάμεσα στα ψηφία του κωδικού της κάρτας ΔΥΠΑ.
    card=""
    for i in card2:
        card=card+i
    card=card.strip()
    if k==1 and not card.isdigit(): # εσφαλμένος κωδικός δελτίου ανεργίας.
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, ο κωδικός του δελτίου ανεργίας πρέπει να περιέχει (16) ψηφία."
    amka2=amka2.strip()
    amka2=amka2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
    amka=""
    for i in amka2:
        amka=amka+i    
    if k==2 and (not (amka.isdigit() and len(amka)==11)): #σωστός ΑΜΚΑ
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, ο ΑΜΚΑ πρέπει να περιέχει (11) ψηφία."
    afm2=afm2.strip()
    afm2=afm2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΜΚΑ
    afm=""
    for i in afm2:
        afm=afm+i
    if k==3 and (not (afm.isdigit() and len(afm)==9)): #σωστός ΑΜΚΑ
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, ο ΑΦΜ πρέπει να περιέχει (9) ψηφία."
    akha2=akha2.strip()
    akha2=akha2.split() #κόψιμο κενών ανάμεσα στα ψηφία του ΑΚΗΑ
    akha=""
    for i in akha2:
        akha=akha+i    
    if k==4 and (not akha.isdigit()): #εσφαλμένος κωδικός ΑΚΗΑ
        errorFlag=1
        message=message+"\nΔεν είναι σωστή η καταχώρηση, ο κωδικός ΑΚΗΑ περιλαμβάνει μόνο ψηφία."
    if n==1: #διαδικασία αναζήτησης δελτίων.        
        date1=update1Search2.get()
        date2=update2Search2.get()
        date1.strip()
        date2.strip()        
        day1=checkDate(date1)
        day2=checkDate(date2)    
        if k==5 and day1==0:
            errorFlag=1
            message=message+"\nΜη έγκυρη ημερομηνία."
        if k==6 and day2==0:
            errorFlag=1
            message=message+"\nΜη έγκυρη ημερομηνία."
        active=activeSearch2.get()
        active=active.strip()
        active=active.upper()
        if k==7 and active not in ['ΝΑΙ', 'ΟΧΙ']:
            errorFlag=1
            message=message+"\nΥπάρχουν μόνο δύο επιλογές για την ενεργή/ ανενεργή κάρτα (ΝΑΙ/ΟΧΙ)."
    if errorFlag==1: #Ύπαρξη σφάλματος, εκτύπωση μηνύματος και επιλογές επιστροφής / νέας ενέργειας.
        backSearch=Button(Frame17, text="<<Επιστροφή", padx=32, pady=11, command=lambda: goto(134))#insert(Frame17, 5)
        backSearch.grid(row=1000, column=8, padx=65, pady=45)          
        returnSearch=Button(Frame17, text="Κεντρικό μενού", padx=28, pady=11, command=lambda: goto(24))
        returnSearch.grid(row=1000,  column=9, padx=65, pady=45)
        message=message[:-1]+", η ενέργεια ακυρώθηκε."
        messagebox.showerror('Σφάλμα:', message)        
    else:
        tempList1=[]
        tempList2=[]
        global criterion
        with open("current.csv", "r", encoding="utf-8", newline="") as file: #ενεργά και ανενεργά δελτία ανεργίας, αλλά ΟΧΙ διεγραμμένα (τα διεγραμμένα βρίσκονται από default στο 
            ro=csv.reader(file, delimiter='$')                               #αρχείο 'previous.csv').
            for row in ro:
                tempList2.append(row)        
        if n==1: #αναζήτηση.
            searchList=[surname, card, amka, afm, akha, day1, day2, active]
            criterion=["ΕΠΩΝΥΜΟ", "ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ", "ΑΜΚΑ", "ΑΦΜ", "ΚΩΔΙΚΟΣ ΑΚΗΑ", "ΑΝΑΝΕΩΣΗ από:", "ΑΝΑΝΕΩΣΗ έως:", "ΕΝΕΡΓΟΣ ΧΡΗΣΤΗΣ (ΝΑΙ/ΟΧΙ)"]
            with open("previous.csv", "r", encoding="utf-8", newline="") as file: #στο 'previous.csv' καταχωρούνται τα διεγραμμένα δελτία, ώστε αν χρειαστεί κάποτε να τα επαναφέρουμε.
                ro=csv.reader(file, delimiter='$')
                for row in ro:
                    tempList1.append(row)
                for record in tempList1: #κόψιμο διπλοεγγραφής.
                    if (record[5] not in tempList2) and (record[6] not in tempList2) and (record[7] not in tempList2):
                        tempList2.append(record)                    
        else: #διαγραφή.
            searchList=[surname, card, amka, afm, akha]
            criterion=["ΕΠΩΝΥΜΟ", "ΑΡ. ΚΑΡΤΑΣ ΔΥΠΑ", "ΑΜΚΑ", "ΑΦΜ", "ΚΩΔΙΚΟΣ ΑΚΗΑ"]        
        global printList
        printList=[]
        printList.clear()     
        with open("previous.csv", "r", encoding="utf-8", newline="") as file: #στο 'previous.csv' καταχωρούνται τα διεγραμμένα δελτία, ώστε αν χρειαστεί κάποτε να τα επαναφέρουμε.
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                tempList1.append(row) 
        for record in tempList2:
            if searchList[k] in record: #έλεγχος αν η τιμή του κριτιρίου αναζήτησης (πχ τιμή ΑΜΚΑ) αντιστοιχεί σε εγγραφή στο σύστημα (αν ΝΑΙ, εγγραφή στην λίστα για εκτύπωση).
                printList.append(record)            
        if len(printList)==0:
            returnSearch=Button(Frame17, text="Κεντρικό μενού", padx=32, pady=11, command=lambda: goto(24))
            returnSearch.grid(row=1000, column=9, padx=50, pady=45)
            if n==1: #αναζήτηση.
                backSearch=Button(Frame17, text="Νέα αναζήτηση", padx=25, pady=11, command=lambda: insert(Frame17, 3))
                backSearch.grid(row=1000, column=8, padx=50, pady=45)                
            elif n==2: #διαγραφή.
                backSearch=Button(Frame17, text="Νέα διαγραφή", padx=32, pady=11, command=lambda: insert(Frame17, 5))
                backSearch.grid(row=1000, column=8, padx=50, pady=45)            
            message="\nΔε βρέθηκαν εγγραφές στο σύστημα σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+")."
            messagebox.showwarning('Σφάλμα:', message)
            for record in tempList1:
                if searchList[k] in record: #έλεγχος αν η τιμή του κριτιρίου αναζήτησης (πχ τιμή ΑΜΚΑ) αντιστοιχεί σε εγγραφή στο σύστημα που έχει ΗΔΗ διαγραφεί.
                    printList.append(record)
                if len(printList)>0:
                     message="\nΗ εγγραφή σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+") έχει ήδη διαγραφεί."
                     messagebox.showwarning('Σφάλμα:', message)
        else:
            global newSearch
            if n==1: #στο επόμενο Frame ακολουθεί ενέργεια αναζήτησης (ΜΟΝΟ προβολή στοιχείων).                
                showSearch=Button(Frame17, text="Εμφάνιση", padx=40, pady=11, command=lambda criterion=criterion[k]: goto(115))
                showSearch.grid(row=1000, column=9,  padx=65, pady=45)
            elif n==2: #στο επόμενο Frame ακολουθεί ενέργεια αναζήτησης για διαγραφή.                
                showSearch=Button(Frame17, text="Εμφάνιση", padx=45, pady=11, command=lambda criterion=criterion[k]: goto(25)) 
                showSearch.grid(row=1000, column=9, padx=65, pady=45)
            newSearch=Button(Frame17, text="<<Επιστροφή", padx=34, pady=11, command=lambda: insert(Frame17, 5))
            newSearch.grid(row=1000, column=8,  padx=65, pady=45)            
            if len(printList)==1:
                message="Βρέθηκε στο σύστημα ένα δελτίο για διαγραφή σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+")."
            else:
                message="Βρέθηκαν στο σύστημα "+str(len(printList))+" δελτία για διαγραφή σύμφωνα με τα κριτίρια αναζήτησης (με βάση: "+criterion[k]+")."
            messagebox.showinfo('', message)


def changePass(x): #Προσθήκη/Κατάργηση λογ/μού χρήστη, η changePass(x) παίρνει μία παράμετρο x--> (1,4=προσθήκη, 2,3=κατάργηση)
    global passist
    global newEntry
    global passList
    global newUsername2
    global newPassword2
    global changes
    global newUser
    global returnNew
    global verifyNew
    mainMenu.grid_forget()
    changes=LabelFrame(root, bd=0, fg="#000080")
    changes.grid(row=5, column=0, columnspan=18)
    if x==1:  #Προσθήκη Λογαριασμού
        passList=[]
        newList=[]
        newEntry=[]
        newUser=Label(changes, text="Προσθήκη Λογαριασμού χρήστη", bg= "#d9d9d9", fg="red", pady=25)
        newUser.grid(row=5, column=0, columnspan=18, sticky=W+E)
        newUsername1=Label(changes, text="Εισάγετε Username:", fg="red", pady=10)
        newUsername1.grid(row=6, column=8, pady=15)
        newUsername2=Entry(changes, width=50, bg= "#d9d9d9", borderwidth=5, relief=SUNKEN)
        newUsername2.grid(row=6, column=9, pady=15)   
        newPassword1=Label(changes, text="Εισάγετε Password:", fg="red", pady=10)
        newPassword1.grid(row=7, column=8)
        newPassword2=Entry(changes, width=50, bg= "#d9d9d9", borderwidth=5, relief=SUNKEN)
        newPassword2.grid(row=7, column=9)
        returnNew=Button(changes, text="<<Επιστροφή", padx=36, pady=11, command=lambda: goto(64)) 
        returnNew.grid(row=100, column=8, pady=25, sticky=W)        
        verifyNew=Button(changes, text="Υποβολή", padx=50, pady=11, command=lambda: changePass(4))
        verifyNew.grid(row=100, column=9, pady=25, sticky=E) 
    elif x==2: #Κατάργηση Λογαριασμού
        global newDelete
        global verifyDel
        global eraseList
        global delUsername1
        global delUsername2
        global delPassword1
        global delPassword2        
        global verifyDel
        global erase        
        erase=[]
        eraseList=[]
        finalList=[]
        delUser=Label(changes, text="Κατάργηση Λογαριασμού χρήστη", bg= "#d9d9d9", fg="red", pady=25)
        delUser.grid(row=5, column=0, columnspan=18, sticky=W+E)
        with open("password.csv", "r", newline="", encoding="utf-8") as file:
            ro=csv.reader(file, delimiter='$')
            for row in ro:
                eraseList.append(row)
            if len(eraseList)==1:
                messagebox.showerror('Σφάλμα:', "Δε γίνεται να καταργηθεί ο Λογαριασμός χρήστη γιατί είναι μοναδικός, η ενέργεια απέτυχε.")
                returnMenu=Button(changes, text="Κεντρικό Μενού", padx=30, pady=11, command=lambda: goto(64))
                returnMenu.grid(row=100, column=5, pady=15, padx=20)
            else:
                delUsername1=Label(changes, text="Εισάγετε Username:", fg="red", pady=10)
                delUsername1.grid(row=6, column=8, pady=15)
                delUsername2=Entry(changes, width=50, bg= "#d9d9d9", borderwidth=5, relief=SUNKEN)
                delUsername2.grid(row=6, column=9, pady=15)   
                delPassword1=Label(changes, text="Εισάγετε Password:", fg="red", pady=10)
                delPassword1.grid(row=7, column=8)
                delPassword2=Entry(changes, width=50, bg= "#d9d9d9", borderwidth=5, relief=SUNKEN)
                delPassword2.grid(row=7, column=9)
                returnNew=Button(changes, text="<<Επιστροφή", padx=36, pady=11, command=lambda: goto(64)) 
                returnNew.grid(row=100, column=8, pady=25, sticky=W)                
                verifyDel=Button(changes, text="Οριστική διαγραφή χρήστη", padx=1, pady=11, command=lambda: changePass(3)) #lambda: transition(10) --->ΝΑ ΦΤΙΑΞΩ ΤΙΣ FUNCTIONS!!!
                verifyDel.grid(row=100, column=9, pady=25, sticky=E)
    elif x==3: #Οριστική διαγραφή λογαριασμού χρήστη
        global failDelete2
        global Frame34
        delName=delUsername2.get()
        delPwd=delPassword2.get()
        delName=delName.strip()
        delPwd=delPwd.strip()
        erase=[delName.upper(),delPwd.upper()]
        global flag #δείκης, αν η τιμή είναι διάφορη του 1, το μήνυμα θα τυπωθεί με κόκκινα γράμματα (θα πρόκειται για μήνυμα σφάλματος).
        changes.grid_forget()
        global Frame34
        Frame34=LabelFrame(root, bd=0)
        Frame34.grid(row=5, column=0, columnspan=18)
        delUser=Label(Frame34, text="Κατάργηση Λογαριασμού χρήστη", bg= "#d9d9d9", fg="red", pady=25)
        delUser.grid(row=5, column=0, columnspan=18, sticky=W+E)        
        delUsername1.grid_forget()
        delUsername2.grid_forget()
        delPassword1.grid_forget()
        delPassword2.grid_forget()
        returnNew.grid_forget()
        verifyDel.grid_forget()         
        if erase not in eraseList:                     
            message="Δεν υπάρχει Λογαριασμός χρήστη με τα συγκεκριμένα στοιχεία, η ενέργεια απέτυχε."
            messagebox.showerror('Σφάλμα:', message)
            #flag=0
        else:
            i=0
            while i<len(eraseList): #πατέντα διαγραφής κωδικών που μπορεί χειροκίνητα) να μπήκαν περισσότερες από μία φορές στο σύστημα (διαγραφή διπλοεγγραφών).
                if erase==eraseList[i]:
                    eraseList.remove(eraseList[i])
                    i=0
                else:
                    i=i+1
            with open("password.csv", "w", newline="", encoding="utf-8") as file:
                global successDel
                wo=csv.writer(file, delimiter='$')
                for x in eraseList:
                    wo.writerow(x)
                message="Ο Λογαριασμός χρήστη διαγράφηκε με επιτυχία."
                messagebox.showinfo('', message)
                flag=1
        newDelete=Button(Frame34, text="Νέα διαγραφή", padx=30, pady=11, command=lambda: goto(66))
        newDelete.grid(row=102, column=4, pady=15, padx=45)                    
        returnMenu=Button(Frame34, text="Κεντρικό Μενού", padx=30, pady=11, command=lambda: goto(65))
        returnMenu.grid(row=102, column=5, pady=15, padx=45)                
    elif x==4: #έλεγχος υποβολής στοιχείων για εισαγωγή νέου χρήστη για ΠΡΩΤΗ ΦΟΡΑ ΜΟΝΟ
        newName=newUsername2.get()
        newPwd=newPassword2.get()
        newName=newName.strip()
        newPwd=newPwd.strip()  
        newEntry=[newName.upper(),newPwd.upper()]
        changes.grid_forget()
        returnNew.grid_forget()
        verifyNew.grid_forget()
        newUser.grid_forget()
        global Frame35
        Frame35=LabelFrame(root, bd=0)
        Frame35.grid(row=5, column=0, columnspan=18)
        newUser=Label(Frame35, text="Προσθήκη Λογαριασμού χρήστη", bg= "#d9d9d9", fg="red", pady=25)
        newUser.grid(row=5, column=0, columnspan=18, sticky=W+E)        
        if len(newName)!=0 and len(newPwd)!=0:           
            with open("password.csv", "r", newline="", encoding="utf-8") as file:
                wo=csv.reader(file, delimiter='$')
                for row in wo:
                    passList.append(row)
                if newEntry in passList:
                    message2="Ο συγκεκριμένος Λογαριασμός χρήστη υπάρχει ήδη, η ενέργεια προσθήκης απέτυχε."
                    messagebox.showwarning('Σφάλμα:', message2)
                    flag=0
                else:
                    passList.append(newEntry)
                    with open("password.csv", "w", newline="", encoding="utf-8") as file:
                        wo=csv.writer(file, delimiter='$')
                        for x in passList:
                            wo.writerow(x)
                        message2="Τα στοιχεία του νέου χρήστη (Username/Password) καταχωρήθηκαν και ο νέος Λογαριασμός δημιουργήθηκε με επιτυχία."
                        messagebox.showinfo('', message2)
                        flag=1
        else:
            message2="Δεν πρέπει να υπάρχει κενό πεδίο (Username/Password), η ενέργεια ακυρώθηκε."
            messagebox.showerror('Σφάλμα:', message2)
            flag=0
        newUserEntry=Button(Frame35, text="Νέα προσθήκη", padx=30, pady=11, command=lambda: goto(68))
        newUserEntry.grid(row=101, column=8, pady=15, padx=45)
        returnMenu=Button(Frame35, text="Κεντρικό Μενού", padx=30, pady=11, command=lambda: goto(67))
        returnMenu.grid(row=101, column=9, pady=15, padx=45)            
        
def menu():#Κεντρικό μενού
    global mainMenu
    global action
    action=""
    mainMenu=LabelFrame(root, padx=5, pady=10, bd=0)
    mainMenu.grid(row=5, column=0, columnspan=18, padx=10, pady=15)                           
    epilogi4=Button(mainMenu, text="Ενέργειες (δελτία)", padx=24, pady=10, command=lambda: insert(mainMenu, 1))
    epilogi4.grid(row=6, column=5, padx=33, pady=15)
    epilogi5=Button(mainMenu, text="Νέο δελτίο", padx=41, pady=10, command=lambda: insert(mainMenu, 2))
    epilogi5.grid(row=6, column=7, padx=33, pady=15)
    epilogi6=Button(mainMenu, text="Αναζήτηση", padx=40, pady=10, command=lambda: insert(mainMenu, 3))
    epilogi6.grid(row=6, column=9, padx=33, pady=15)                               
    epilogi7=Button(mainMenu, text="Τροποποίηση δελτίου", padx=12, pady=10, command=lambda: insert(mainMenu, 4))
    epilogi7.grid(row=6, column=11, padx=33, pady=15)
    epilogi1=Button(mainMenu, text="Διαγραφή", padx=43, pady=10, command=lambda: insert(mainMenu, 5))
    epilogi1.grid(row=6, column=13, padx=33, pady=15)
    epilogi2=Button(mainMenu, text="Ενέργειες (memo)", padx=23, pady=10, command=lambda: insert(mainMenu, 6))
    epilogi2.grid(row=7, column=5, padx=33, pady=15)
    epilogi11=Button(mainMenu, text="Ευρετήριο", padx=41, pady=10, command=lambda: insert(mainMenu, 7))
    epilogi11.grid(row=7, column=7, padx=33, pady=15)    
    epilogi8=Button(mainMenu, text="Νέος Λογαριασμός", padx=19, pady=10, command=lambda: changePass(1))
    epilogi8.grid(row=7, column=9, padx=33, pady=15)
    epilogi10=Button(mainMenu, text="Κατάργηση Λογαριασμού", padx=2, pady=10, command=lambda: changePass(2))
    epilogi10.grid(row=7, column=11, padx=33, pady=15)        
    epilogi9=Button(mainMenu, text="Έξοδος", padx=50, pady=10, command=lambda:goto(15)) 
    epilogi9.grid(row=7, column=13, padx=33, pady=15)    

main()

#Αντιμετωπίζω πρόβλημα με το scrollbar, δεν μπορώ να βρω ακόμα τον σωστό τρόπο για να το περάσω μέσα στο Frame (δουλεύω μέσα στην ektyposi1()).
#ΒΛΕΠΕ ΓΡΑΜΜΗ 2193, 2214, 2248 ("ΝΑ ΕΛΕΓΞΩ...").
#Να βρω τρόπο να φύγει το path από το filename των αρχείων που γίνονται upload στο cloud.
