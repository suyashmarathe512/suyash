%%writefile app.py
import streamlit as st
import pandas as pd
import random
import time
import os

# Initialize data file
if not os.path.exists("data.csv"):
    df = pd.DataFrame(columns=["timestamp", "user_id", "version", "action"])
    df.to_csv("data.csv", index=False)

st.title("🧪 A/B Testing - Product Display")

# Randomly assign version
version = random.choice(["A", "B"])
st.write(f"You're viewing **Version {version}**")

# Display based on version
if version == "A":
    st.image("https://via.placeholder.com/200", caption="Product A")
    st.write("Minimal layout with essential details.")
else:
    st.image("https://via.placeholder.com/300", caption="Product B")
    st.write("Detailed layout with larger image and reviews.")
    st.info("⭐⭐⭐⭐☆ (4.5/5 based on 120 reviews)")

# Simulate user interaction
user_id = random.randint(1000, 9999)
action = "view"

if st.button("🛒 Add to Cart"):
    action = "add_to_cart"
    st.success(f"Product added to cart! (User {user_id})")

# Log interaction
df = pd.read_csv("data.csv")
df = pd.concat([df, pd.DataFrame([{
    "timestamp": time.time(),
    "user_id": user_id,
    "version": version,
    "action": action
}])], ignore_index=True)
df.to_csv("data.csv", index=False)
