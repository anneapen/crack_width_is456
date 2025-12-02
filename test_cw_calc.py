import cw_calc as cw_calc

def test_acr():
    acr=cw_calc.acr(s=450,dc=25,db=10)
    assert acr==221.38