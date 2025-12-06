import streamlit as st
import cw_calc as cw_calc


st.markdown("# Crack Width Calculator as per IS 456:2000")

fck=st.number_input("Compressive strength of concrete,fck=",min_value=0.0,value=10.0)

b=st.number_input("Width,b(mm)",min_value=0.0)
D=st.number_input("Overall depth, D(mm)",min_value=0.0)
dc=st.number_input("Clear cover,dc(mm)",min_value=0.0)
db=st.number_input("Diameter of the bar,db(mm)",min_value=0.0)
s=st.number_input("Spacing between bars, s(mm)",min_value=0.0)
Cmin=st.number_input("Minimum cover to the main bar, Cmin(mm)",min_value=0.0)
M=st.number_input("Maximum Moment(kNm)",min_value=0.0)

wcr=cw_calc.crack_width(fck,b,D,dc,Cmin,s,db,M)

st.write(f"Crack width={wcr}mm")




