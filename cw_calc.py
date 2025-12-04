import pandas as pd
import math

#Determining acr
def concrete_area(s:float,dc:float,db)->float:
    """
    Calculating acr
    """

    acr=((((s/2)**2)+(dc**2))**(1/2))-(db/2)
    return round(acr,2)

#Determining the concrete stress in compression
def concrete_stress_comp(fck:int):
    """
    Returns the compressive stress in concrete
    """
    cbc_df=pd.read_csv("Concrete stress in compression.csv")
    cbc_df=cbc_df[:10]
    cbc_df=cbc_df.set_index("fck")
    cbc=cbc_df.loc[fck,'cbc']
    return cbc

def crack_width(fck:float,b:float,D:float,dc:float,Cmin:float,s:float,db:float,M:float)->float:
    """
    To determine the crack width
    """
    Es=200000
    d=D-dc
    cbc=concrete_stress_comp(fck)
    m=280/(3*cbc)
    Ast=(1000/s)*(math.pi/4*(db**2))
    pt=(Ast/(b*d))*100
    rho=pt/100
    k=math.sqrt((2*rho*m)+((rho*m)**2))-(rho*m)
    x=k*d
    Icr=((b*x**3/3)+((m*Ast)*((d-x)**2)))/(10**8)
    fst=((m*(M*10**6)*(d-x))/Icr)/(10**8)
    e1=(fst/Es)*((D-x)/(d-x))
    e2=(b*(D-x)**2)/(3*Es*Ast*(d-x))
    em=e1-e2
    acr=concrete_area(s,dc,db)
    wcr=(3*acr*em)/(1+(2*(acr-Cmin))/(d-x))
    return round(wcr,2)