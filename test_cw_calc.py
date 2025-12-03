import cw_calc as cw_calc

def test_acr():
    acr=cw_calc.acr(s=450,dc=25,db=10)
    assert acr==221.38

def test_concrete_stress_comp():
    cbc=cw_calc.concrete_stress_comp(fck=30)
    assert cbc==10.0