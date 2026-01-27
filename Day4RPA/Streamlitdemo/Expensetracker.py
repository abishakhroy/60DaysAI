import streamlit as st

st.set_page_config(page_title="Expense UI", layout="centered")
st.title("💸 Expense Tracker (Frontend Only)")
st.caption("UI + calculations only. No storage.")

st.divider()

# ---- Income ----
st.subheader("Income")
income = st.number_input(
    "Monthly income",
    min_value=0.0,
    step=1000.0,
    format="%.2f"
)

st.divider()

# ---- Expenses ----
st.subheader("Expenses")

col1, col2 = st.columns(2)

with col1:
    food = st.number_input("Food", min_value=0.0, step=100.0, format="%.2f")
    transport = st.number_input("Transport", min_value=0.0, step=100.0, format="%.2f")
    bills = st.number_input("Bills", min_value=0.0, step=100.0, format="%.2f")

with col2:
    shopping = st.number_input("Shopping", min_value=0.0, step=100.0, format="%.2f")
    health = st.number_input("Health", min_value=0.0, step=100.0, format="%.2f")
    other = st.number_input("Other", min_value=0.0, step=100.0, format="%.2f")

# ---- Calculations ----
total_expense = food + transport + bills + shopping + health + other
balance = income - total_expense

st.divider()

# ---- Summary ----
st.subheader("Summary")

c1, c2, c3 = st.columns(3)
c1.metric("Income", f"{income:,.2f}")
c2.metric("Total Expenses", f"{total_expense:,.2f}")
c3.metric("Remaining", f"{balance:,.2f}")

if balance < 0:
    st.error("⚠️ Expenses exceed income")

st.divider()

# ---- Breakdown (simple text UI) ----
st.subheader("Expense Breakdown")

st.write(f"🍔 Food: {food:,.2f}")
st.write(f"🚗 Transport: {transport:,.2f}")
st.write(f"💡 Bills: {bills:,.2f}")
st.write(f"🛍️ Shopping: {shopping:,.2f}")
st.write(f"🩺 Health: {health:,.2f}")
st.write(f"📦 Other: {other:,.2f}")