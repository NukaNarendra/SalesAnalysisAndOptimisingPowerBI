import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load JSON file with utf-8-sig encoding to handle BOM issue
file_path = "PowerBIPerformanceData.json"

with open(file_path, "r", encoding="utf-8-sig") as file:
    data = json.load(file)

# Extract relevant event data
events = data.get("events", [])

# Convert JSON data to a DataFrame
df = pd.DataFrame(events)

# Convert timestamps to datetime format
df["start"] = pd.to_datetime(df["start"], errors="coerce")
df["end"] = pd.to_datetime(df["end"], errors="coerce")

# Calculate event durations (handle missing values)
df["duration"] = (df["end"] - df["start"]).dt.total_seconds()
df_filtered = df.dropna(subset=["duration"])

### ---- PLOT 1: Box Plot (Event Duration by Event Name) ---- ###
plt.figure(figsize=(12, 6))
sns.boxplot(x="name", y="duration", data=df_filtered)
plt.xticks(rotation=90)
plt.title("Event Duration by Event Name")
plt.xlabel("Event Name")
plt.ylabel("Duration (seconds)")
plt.grid()
plt.show()

### ---- PLOT 2: Bar Chart (Event Frequency) ---- ###
plt.figure(figsize=(12, 6))
sns.countplot(y=df["name"], order=df["name"].value_counts().index, palette="viridis")
plt.title("Frequency of Events")
plt.xlabel("Count")
plt.ylabel("Event Name")
plt.grid(axis="x")
plt.show()

### ---- PLOT 3: Line Plot (Events Over Time) ---- ###
plt.figure(figsize=(12, 6))
df.set_index("start").resample("1T")["name"].count().plot(marker="o", linestyle="-", color="b")
plt.title("Number of Events Over Time")
plt.xlabel("Time")
plt.ylabel("Event Count")
plt.grid()
plt.show()
