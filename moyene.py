try:
    n=int(input("ki kantite not ou vle sezi ?:"))
    while(n<=0):
        print("ere svp antre yon nonb ki pi gro ke zero")
        n=int(input("ki kantite not ou vle sezi ?:"))
    note_exam=[]
    i=0
    while(i<n):
        note=float(input("antre not nimero "+str(i+1)+" an :"))
        if(note>100):
            print("not la pa dwe depase 100 paske not yo sou 100 pou chak matye")
        else:
            i+=1
            note_exam.append(note)
    print("not yo pou evalyasyon sa se :"+str(note_exam))
    moyenne=sum(note_exam)/n
    a=""
    if(moyenne>=90):
        a="A"
    if(moyenne<90 and moyenne>=80):
        a="B"
    if(moyenne<80 and moyenne>=70):
       a= "C"
    if(moyenne<70 and moyenne>=60):
        a="D"
    if(moyenne<60):
        a="F"
    
    print("mwayen ou pou evalyasyon sa se :"+str(moyenne)+" klasifikasyon ou se :"+a)
        
except ValueError:
    print("antre yon nonb valid")
    n=int(input("ki kantite not ou vle sezi ?:"))

    

