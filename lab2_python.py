# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 13:24:56 2021

@author: jldun
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_excel(r"C:\Users\jldun\OneDrive\Desktop\PETE 3037\Lab 2 - Two Phase Flow.xlsx")

df


vsl_churn = []
vsg_churn = []
vsl_slug = []
vsg_slug = []
vsl_single = []
vsg_single = []
vsl_annular = []
vsg_annular = []

for i in df.index:
    if df['Vertical Flow Regime'][i] == "single":
        vsl_single.append(df['Vsl (m/s)'][i])
        vsg_single.append(df['Vsg(m/s)'][i])
    if df['Vertical Flow Regime'][i]== "slug" :
        vsl_slug.append(df['Vsl (m/s)'][i])
        vsg_slug.append(df['Vsg(m/s)'][i])
    if df['Vertical Flow Regime'][i] == "churn":
        vsl_churn.append(df['Vsl (m/s)'][i])
        vsg_churn.append(df['Vsg(m/s)'][i])
    if df['Vertical Flow Regime'][i] == "annular":
        vsl_annular.append(df['Vsl (m/s)'][i])
        vsg_annular.append(df['Vsg(m/s)'][i])
   
vsl_churn = np.array(vsl_churn)
vsg_churn = np.array(vsg_churn)
vsl_slug = np.array(vsl_slug)
vsg_slug = np.array(vsg_slug)
vsl_single = np.array(vsl_single)
vsg_single = np.array(vsg_single)
vsl_annular = np.array(vsl_annular)
vsg_annular = np.array(vsg_annular)

#begin plotting Vertical Flow Regime Chart

plt.scatter(vsg_slug,vsl_slug)
plt.plot(vsg_slug,vsl_slug, label = "Slug")
plt.scatter(vsl_single, vsg_single)
plt.plot(vsl_single, vsg_single, label = "Single Phase")
plt.scatter(vsl_churn, vsg_churn)
plt.plot(vsl_churn, vsg_churn, label  = "Churn")
plt.scatter(vsl_annular, vsg_annular)
plt.plot(vsl_annular, vsg_annular, label = "annular")
plt.legend()
plt.loglog(basex=10, basey=10)
plt.show
