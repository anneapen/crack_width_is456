import cw_calc as cw_calc

def test_concrete_area():
    acr=cw_calc.concrete_area(s=450,dc=25,db=10)
    assert acr==221.38

def test_concrete_stress_comp():
    cbc=cw_calc.concrete_stress_comp(fck=30)
    assert cbc==10.0

def test_crack_width():
    wcr=cw_calc.crack_width(30,160,850,25,25,450,10,45)
    assert wcr==0.23