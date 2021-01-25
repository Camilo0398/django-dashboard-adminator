import datetime

def valsuser(uonline,unew,ustatus):
    online=0
    new=0
    estatus=0
    for onlines in uonline:
        if onlines==1:
            online=online+1
        
    for news in unew:
        if news==1:
            new=new+1
        
    for status in ustatus:
        if status==1:
            estatus=estatus+1
        
    return online, new, estatus

def usuariospormes(dates):
    meses=[]
    for i in range(0,4): 
        meses.append(0)

    month=0
    hora = datetime.datetime.now()
    for date in dates:
        month=hora.month
        year = hora.year
        timestamp = datetime.datetime.fromtimestamp(date)
        for i in range(0,len(meses)):
            if month-1==0:
                if timestamp.month == month and timestamp.year ==year:
                    meses[i]=meses[i]+1
                month=12
                year =year-1
            else:
                if timestamp.month == month and timestamp.year ==year:
                    meses[i]=meses[i]+1
                month=month-1
    return meses

def usuariospormespas(dates):
    meses=[]
    for i in range(0,4): 
        meses.append(0)
    month=0
    hora = datetime.datetime.now()
    for date in dates:
        month=hora.month
        year = hora.year-1
        timestamp = datetime.datetime.fromtimestamp(date)
        for i in range(0,len(meses)):
            if month-1==0:
                if timestamp.month == month and timestamp.year ==year:
                    meses[i]=meses[i]+1
                month=12
                year =year-1
            else:
                if timestamp.month == month and timestamp.year ==year:
                    meses[i]=meses[i]+1
                month=month-1
    return meses
def statustrans(status):
    pedin=0
    comfrimed=0
    cancel=0
    for statu in status:
        
        if statu == 1 or statu == 2 or statu == 3:
            pedin=pedin+1
        if statu == 4:
            comfrimed=comfrimed+1
        if statu == 5 or statu == 6 or statu == 7:
            cancel=cancel+1
    return pedin,comfrimed,cancel