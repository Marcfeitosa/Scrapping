import streamlit as st
import matplotlib.pyplot as plt
from datetime import datetime

def read_temperatures():
    dates = []
    temperatures = []
    with open("data.txt", "r") as file:
        next(file)  # skip the header
        for line in file:
            date_str, temperature = line.strip().split(",")
            date = datetime.strptime(date_str, "%Y-%m-%d").date()
            dates.append(date)
            temperatures.append(int(temperature))
    return dates, temperatures

# Reading the temperatures
dates, temperatures = read_temperatures()

# Configuring the streamlit app
st.title('Viewing temperatures')
st.write('Temperatures across the dates')

# Ploting the graph with matplotlib
fig, ax = plt.subplots()
ax.plot(dates, temperatures, marker='o', linestyle='-')
ax.set_title('Temperatures across time')
ax.set_xlabel('Date')
ax.set_ylabel('Temperature')
plt.xticks(rotation=45)  # rotates the axis x to better visualization
ax.grid(True)
plt.tight_layout()  # Auto-fit the layout

# Ploting the graphs in streamlit
st.pyplot(fig)
