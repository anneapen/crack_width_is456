import pandas as pd
import math

#Determining acr
def concrete_area(s:float,dc:float,db)->float:
    """
    Calculating the distance from the point considered to the surface of the nearest longitudinal bar(acr)
    in mm, where
    s=spacing between bars,mm
    dc= clear cover,mm
    db= diameter of the bar,mm
    """    
    acr=((((s/2)**2)+(dc**2))**(1/2))-(db/2)
    return round(acr,2)

#Determining the concrete stress in compression
def concrete_stress_comp(fck:int):
    """
    Returns the permissible stress in compression in concrete(MPa) for the grade of concrete,fck as per IS 456:2000    
    """
    cbc_df=pd.read_csv("Concrete stress in compression.csv")
    cbc_df=cbc_df[:10]
    cbc_df=cbc_df.set_index("fck")
    cbc=cbc_df.loc[fck,'cbc']
    return cbc

#Determining the crack width
def crack_width(fck:float,b:float,D:float,dc:float,Cmin:float,s:float,db:float,M:float)->float:
    """
    To determine the design surface crack width(wcr,in mm) as per IS 456:2000 Annex F where,
    fck-grade of concrete,MPa
    b-width of the section at the centroid of the tension steel,mm
    D-the overall depth of the section,mm
    dc-clear cover,mm
    Cmin-minimum cover to the longitudinal bar,mm
    s-spacing between bars,mm
    db- diamter of the bar,mm
    M-Maximum moment at midspan (under service loads - dead plus live),kNm 
    a'-distance from the extreme compression fibre to the point at which the surface crack width is being calculated
    Here, a'=D as crack width at the surface remote from compression face is considered
    """
    Es=200000
    d=D-dc
    cbc=concrete_stress_comp(fck)
    #Modular ratio
    m=280/(3*cbc)
    #Area of tension reinforcement(mm2)
    Ast=(1000/s)*(math.pi/4*(db**2))
    pt=(Ast/(b*d))*100
    rho=pt/100
    k=math.sqrt((2*rho*m)+((rho*m)**2))-(rho*m)
    #Neutral axis depth,mm
    x=k*d
    #Moment of inertia,mm4
    Icr=((b*x**3/3)+((m*Ast)*((d-x)**2)))/(10**8)
    #Stress at the centroid of tension steel (cracked section)
    fst=((m*(M*10**6)*(d-x))/Icr)/(10**8)
    #Strain at the surface(where a'=D), calculated ignoring the stiffening of the concrete in the tension zone
    e1=(fst/Es)*((D-x)/(d-x))
    #Reduction due to tension stiffening effect
    e2=(b*(D-x)**2)/(3*Es*Ast*(d-x))
    #Mean tensile strain in concrete
    em=e1-e2
    acr=concrete_area(s,dc,db)
    wcr=(3*acr*em)/(1+(2*(acr-Cmin))/(d-x))
    return round(wcr,2)