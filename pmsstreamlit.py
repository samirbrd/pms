# -*- coding: utf-8 -*-
"""
Created on Thu Dec 10 15:07:54 2020

@author: Administrator
"""


import streamlit as st
import pandas as pd

data = pd.read_csv('return analysis.csv')
st.title("Portfolio Management Scheme Analysis (WIP Check back on December 19, 2020)")
st.write("By Meet Shah")
st.dataframe(data)
