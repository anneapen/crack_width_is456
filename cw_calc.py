
#Determining acr
def acr(s:float,dc:float,db)->float:
    """
    Calculating acr
    """

    acr=((((s/2)**2)+(dc**2))**(1/2))-(db/2)
    return round(acr,2)
