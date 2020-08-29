import pandas as pd




VA=pd.read_csv('Dados/VALE3.csv')
AM=pd.read_csv('Dados/ABEV3.SA.csv')
BB=pd.read_csv('Dados/BBAS3.SA.csv')
BR=pd.read_csv('Dados/BBDC4.SA.csv')
IT=pd.read_csv('Dados/ITUB4.SA.csv')
ML=pd.read_csv('Dados/MGLU3.SA.csv')
PB3=pd.read_csv('Dados/PETR3.SA.csv')
PB4=pd.read_csv('Dados/PETR4.SA.csv')
B3=pd.read_csv('Dados/B3SA3.SA.csv')
WE=pd.read_csv('Dados/WEGE3.SA.csv')

num = 26
RV=[]   
RA=[]
RBB=[]
RBR=[]
RIT=[]
RML=[]
RP3=[]
RP4=[]
RB3=[]
RW=[]

i=10
while i<num:
    v=round((VA['Adj Close'][i+1]*100/VA['Adj Close'][i])-100,2)
    a=round((AM['Adj Close'][i+1]*100/AM['Adj Close'][i])-100,2)
    bb=round((BB['Adj Close'][i+1]*100/BB['Adj Close'][i])-100,2)
    br=round((BR['Adj Close'][i+1]*100/BR['Adj Close'][i])-100,2)
    it=round((IT['Adj Close'][i+1]*100/IT['Adj Close'][i])-100,2)
    ml=round((ML['Adj Close'][i+1]*100/ML['Adj Close'][i])-100,2)
    p3=round((PB3['Adj Close'][i+1]*100/PB3['Adj Close'][i])-100,2)
    p4=round((PB4['Adj Close'][i+1]*100/PB4['Adj Close'][i])-100,2)
    b3=round((B3['Adj Close'][i+1]*100/B3['Adj Close'][i])-100,2)
    we=round((WE['Adj Close'][i+1]*100/WE['Adj Close'][i])-100,2)

    RV.append(v)
    RA.append(a)
    RBB.append(bb)
    RBR.append(br)
    RIT.append(it)
    RML.append(ml)
    RP3.append(p3)
    RP4.append(p4)
    RB3.append(b3)
    RW.append(we)

    
    i+=1

r1=round(sum(RV),3)
r2=round(sum(RA),3)
r3=round(sum(RBB),3)
r4=round(sum(RBR),3)
r5=round(sum(RIT),3)
r6=round(sum(RML),3)
r7=round(sum(RP3),3)
r8=round(sum(RP4),3)
r9=round(sum(RB3),3)
r10=round(sum(RW),3)
SRES=[r1,r2,r3,r4,r5,r6,r7,r8,r9,r10]
print(SRES)

#Calculo Sharpe Ratio

vola=[32.69,37.92,36.93,40.93,41.01,42.39,33.71,34.55,37.79,42.40]
SELIC=1.89  
Sharpe=[]
for i in range(10):
    Resultado=round((SRES[i]-SELIC)/vola[i],2)
    Sharpe.append(Resultado)
    i+=1

#print(Sharpe)