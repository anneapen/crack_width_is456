import pandas as pd

#Determining acr
def acr(s:float,dc:float,db)->float:
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