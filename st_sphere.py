import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.title('Superquadrics')

@st.cache
def superquadrics(a,b,c,n1,n2,x,y,z):
    values = np.power(np.power(np.abs(x/a),n2) \
                    + np.power(np.abs(y/b),n2),n1/n2) \
            + np.power(np.abs(z/c),n1)
    return values

st.sidebar.subheader('Parameters')
a  = 1.
b  = 1.
c  = st.sidebar.slider('c (a=b=1)', .2, 2., 1., .2)
n1 = st.sidebar.slider('n1', 1, 10, 10, 1)
n2 = st.sidebar.slider('n2', 1, 10, 2, 1)

X, Y, Z = np.mgrid[-1:1:20j, -1:1:20j, -2:2:40j]

fig = go.Figure(data=go.Isosurface(
    x = X.flatten(),
    y = Y.flatten(),
    z = Z.flatten(),
    value = superquadrics(a,b,c,n1,n2,X,Y,Z).flatten(),
    isomin = .5,
    isomax = 1,
    showscale = False,
))
st.write(fig)