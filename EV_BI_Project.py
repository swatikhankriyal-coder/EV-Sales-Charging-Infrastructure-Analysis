#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd

ev = pd.read_csv("EV_Dataset.csv")
st = pd.read_csv("ev-charging-stations-india.csv")
print("EV Dataset")
print(ev.head())
print("\n----------------------------------------------------------------------")
print("\nCharging Station Dataset")
print(st.head())
print("EV Dataset Information")
ev.info()

print("\n--------------------------------------\n")

print("Charging Station Dataset Information")
st.info()
print("\n--------------------------------------\n")
print("EV Dataset Shape",ev.shape)
print("\n--------------------------------------\n")
print("Charging Station Dataset shape",st.shape)

print("\n--------------------------------------\n")

print("EV Dataset columns",ev.columns)
print("\n--------------------------------------\n")
print("Charging Station Dataset shape",st.columns)
print("\n--------------------------------------\n")
print("Ev Missing Values")
print(ev.isnull().sum())
print("\n--------------------------------------\n")
print("Charging Stations Missing Values")
print(st.isnull().sum())
print("\n--------------------------------------\n")
print("Duplicate rows in Ev Datasets:",ev.duplicated().sum())
print("\n--------------------------------------\n")
print("Duplicate rows in Charging Dataset",st.duplicated().sum())
print("\n--------------------------------------\n")
print("uniques")
print(ev["State"].unique())
print("\n--------------------------------------\n")
print(st["state"].unique())
print("\n--------------------------------------\n")
st["state"]=st["state"].str.title()
st["state"]=st["state"].str.strip()
st["state"].unique()
st[st["state"].isin([
    "Kochi",
    "Ernakulam",
    "Hisar",
    "Rajahmundry",
    "Hyderabad",
    "Chikhali",
    "Jajpur",
    "Bhubhaneswar",
    "Limbdi"])]
print("\n--------------------------------------\n")
st["state"] = st["state"].replace({
    # Spelling mistakes
    "Tamilnadu": "Tamil Nadu",
    "Taminadu": "Tamil Nadu",
    "Uttrakhand": "Uttarakhand",
    "Uttarkhand": "Uttarakhand",
    "Harayana": "Haryana",
    "Maharashra": "Maharashtra",
    "Telengana": "Telangana",
    "Andra Pradesh": "Andhra Pradesh",
    "Andhrapradesh": "Andhra Pradesh",
    "Karala": "Kerala",
    "Chattisgarh": "Chhattisgarh",
    "Westbengal": "West Bengal",

    # Different naming conventions
    "Pondicherry": "Puducherry",
    "Jammu": "Jammu & Kashmir",
    "Jammu And Kashmir": "Jammu & Kashmir",
    "Andaman": "Andaman & Nicobar Islands",

    # Cities/Districts in the state column
    "Bhubhaneswar": "Odisha",
    "Jaipur": "Rajasthan",
    "Kochi": "Kerala",
    "Ernakulam": "Kerala",
    "Hisar": "Haryana",
    "Hyderabad": "Telangana",
    "Rajahmundry": "Andhra Pradesh",
    "Chikhali": "Gujarat",
    "Limbdi": "Gujarat",
    "Jajpur": "Odisha",

    # Miscellaneous
    "Delhi Ncr": "Delhi",
    "Hyderabadu00A0": "Telangana"})
print( st["state"].unique())
st = st.drop_duplicates()
print("\n--------------------------------------\n")
print("Duplicate rows in Ev Datasets:",ev.duplicated().sum())
print("\n--------------------------------------\n")
print("Duplicate rows in Charging Dataset",st.duplicated().sum())
print("\n--------------------------------------\n")
print("\n--------------------------------------\n")
# print("Exploratory Data Analysis (EDA)")
# print("\n--------------------------------------\n")
# print("Q1. What is the total number of EVs sold?")
# print(ev["EV_Sales_Quantity"].sum())
# print("\n--------------------------------------\n")
# print("Q2.How many states are in the dataset?")
# print(ev["State"].nunique())
# print("\n--------------------------------------\n")
# print("Q3.Which years are covered?")
# print(ev["Year"].unique())
# print("\n--------------------------------------\n")
# print("Q4.Which vehicle types exist?")
# print(ev["Vehicle_Type"].unique())
# print("\n--------------------------------------\n")
# print("Q5.Which vehicle categories exist?")
# print(ev["Vehicle_Category"].unique())
# print("\n--------------------------------------\n")
# print("Q6.Which state has the highest EV sales?")
# print(ev.groupby('State')["EV_Sales_Quantity"].sum())
ev_summary = ev.groupby("State")["EV_Sales_Quantity"].sum().reset_index()
ev_summary.head()
# print("\n--------------------------------------\n")
ev_summary = ev.groupby("State")["EV_Sales_Quantity"].sum().reset_index()

print(ev_summary.head())
station_summary = st.groupby("state").size().reset_index(name="Charging_Stations")

print(station_summary.head())
(station_summary.rename(columns={"state":"State"},inplace=True))
print(station_summary.head())
final_df = pd.merge(
    ev_summary,
    station_summary,
    on="State",
    how="inner"
)

final_df.head()

final_df.shape

final_df["EV_per_Charging_Station"] = (
    final_df["EV_Sales_Quantity"] /
    final_df["Charging_Stations"]
)

# final_df.head()
# final_df.to_csv("Final_EV_BI.csv", index=False)
print(ev["State"].nunique())
print(st["state"].nunique())
print(final_df["State"].nunique())

ev_states = set(ev["State"].unique())
st_states = set(st["state"].unique())

print("Only in EV:", sorted(ev_states - st_states))
print("Only in Charging:", sorted(st_states - ev_states))

print(ev["State"].nunique())
print(st["state"].nunique())
print(final_df["State"].nunique())
print(sorted(ev_states - st_states))
print(sorted(st_states - ev_states))
sorted(ev["State"].unique())

state_mapping = {
    "TamilNadu": "Tamil Nadu",
    "TamiNadu": "Tamil Nadu",
    "TAMIL NADU": "Tamil Nadu",
    "Maharashra": "Maharashtra",
    "Harayana": "Haryana",
    "TELENGANA": "Telangana",
    "Andra Pradesh": "Andhra Pradesh",
    "Andhra pradesh": "Andhra Pradesh",
    "Uttrakhand": "Uttarakhand",
    "Delhi NCR": "Delhi"}
city_mapping = {
    "Bangalore": "Bengaluru",
    "Banglore": "Bengaluru",
    "HYDERBAD": "Hyderabad",
    "NEW DELHI": "New Delhi",
    "MUMBAI": "Mumbai"
}
city_state = {
    "Guwahati":"Assam",
    "Pune":"Maharashtra",
    "Mumbai":"Maharashtra",
    "Nashik":"Maharashtra",
    "Bengaluru":"Karnataka",
    "Hyderabad":"Telangana",
    "Kochi":"Kerala",
    "Ahmedabad":"Gujarat",
    "Jaipur":"Rajasthan",
    "Lucknow":"Uttar Pradesh",
    "Chennai":"Tamil Nadu",
    "Bhubaneswar":"Odisha",
    "Patna":"Bihar",
    "Indore":"Madhya Pradesh"
}
ev_states = set(ev_summary["State"])
st_states = set(station_summary["State"])

print(sorted(ev_states - st_states))
print(sorted(st_states - ev_states))
# Fix state name inconsistencies
st["state"] = st["state"].replace({
    "Andaman & Nicobar Islands": "Andaman & Nicobar Island",
    "Jammu & Kashmir": "Jammu and Kashmir",
    "Delhi NCR": "Delhi",
    "Harayana": "Haryana",
    "Maharashra": "Maharashtra",
    "TELENGANA": "Telangana",
    "Andra Pradesh": "Andhra Pradesh",
    "Andhra pradesh": "Andhra Pradesh",
    "Uttrakhand": "Uttarakhand",
    "Uttarkhand": "Uttarakhand",
    "TamilNadu": "Tamil Nadu",
    "TamiNadu": "Tamil Nadu",
    "TAMIL NADU": "Tamil Nadu"
})

# Recreate station summary
station_summary = (
    st.groupby("state")
      .size()
      .reset_index(name="Charging_Stations")
)

# Compare states
ev_states = set(ev_summary["State"])
st_states = set(station_summary["state"])

print("EV Dataset States:", len(ev_states))
print("Charging Dataset States:", len(st_states))

print("\nOnly in EV:")
print(sorted(ev_states - st_states))

print("\nOnly in Charging:")
print(sorted(st_states - ev_states))

import pandas as pd
import numpy as np

# Merge EV sales with charging station data (keeps all EV states)
final_df = pd.merge(
    ev_summary,
    station_summary,
    left_on="State",
    right_on="state",
    how="left"
)

# Remove duplicate state column
final_df.drop(columns=["state"], inplace=True)

# Replace missing charging station values with 0
final_df["Charging_Stations"] = final_df["Charging_Stations"].fillna(0).astype(int)

# Calculate EV per Charging Station safely
final_df["EV_per_Charging_Station"] = np.where(
    final_df["Charging_Stations"] > 0,
    final_df["EV_Sales_Quantity"] / final_df["Charging_Stations"],
    np.nan
)

# Display summary
print("Total States:", final_df["State"].nunique())
print(final_df.head())

# Save the cleaned dataset
final_df.to_csv("Final_EV_BI.csv", index=False)

print("✅ Final_EV_BI.csv has been created successfully.")

import os

# Save the updated dataframe as an Excel file
final_df.to_excel("Final_EV_BI_Updated.xlsx", index=False)
print(final_df.shape)
final_df.head()
final_df["EV_per_Charging_Station"] = final_df["EV_per_Charging_Station"].round(2)



# In[ ]:





# In[ ]:




