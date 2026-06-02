import streamlit as st
from stats_utils import (prop1, prop2, t1, t2, tp)
st.set_page_config(page_title = "ap stats tests", layout = "wide")
st.title("ap stats significance tests")
test = st.sidebar.selectbox("test",["1 proportion", "2 proportion", "1 sample t", "2 sample t", "paired t"])
a = st.sidebar.number_input("alpha level", 0.001, 0.5, 0.05)
alt = st.sidebar.selectbox("alternate hypothesis",["two-sided", "larger", "smaller"])
def show(r):
    st.write("Answer) ")
    st.write("stat:", round(r["statistic"], 5))
    st.write("p:", round(r["p_value"], 5))
    if "df" in r:
        st.write("df:", round(r["df"], 3))
    if r["p_value"] < a:
        st.success(f"reject the null (p = {r['p_value']:.5f} < α = {a})")
    else:
        st.error(f"Fail to reject null hypothesis (p = {r['p_value']:.5f} ≥ α = {a})")
if test == "1 proportion":
    x = st.number_input("x", 0)
    n = st.number_input("n", 1)
    p = st.number_input("p", 0.5)
    if st.button("run"):
        r = prop1(int(x), int(n), float(p), alt)
        show(r)
elif test == "2 proportion":
    x1 = st.number_input("x1", 0)
    n1 = st.number_input("n1", 1)
    x2 = st.number_input("x2", 0)
    n2 = st.number_input("n2", 1)
    if st.button("run"):
        r = prop2(int(x1), int(n1), int(x2), int(n2), alt)
        show(r)
elif test == "1 sample t":
    xb = st.number_input("xbar")
    s = st.number_input("s", 0.0067)
    n = st.number_input("n", 2)
    mu = st.number_input("mu")
    if st.button("run"):
        r = t1(float(xb),float(s), int(n), float(mu), alt)
        show(r)
elif test == "2 sample t":
    m1 = st.number_input("m1")
    s1 = st.number_input("s1", 0.0067)
    n1 = st.number_input("n1", 2)
    m2 = st.number_input("m2")
    s2 = st.number_input("s2",0.0067)
    n2 = st.number_input("n2", 2)
    if st.button("run"):
        r = t2(float(m1), float(s1), int(n1),float(m2), float(s2), int(n2),alt=alt)
        show(r)
else:
    md = st.number_input("md")
    sd = st.number_input("sd", 0.0067)
    n = st.number_input("n",2)
    if st.button("run"):
        r = tp(float(md), float(sd), int(n),alt)
        show(r)
