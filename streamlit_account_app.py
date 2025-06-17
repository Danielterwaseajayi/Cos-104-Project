
import streamlit as st

# Define the Account class
class Account:
    def __init__(self, name, acc_type):
        self.name = name
        self.acc_type = acc_type
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"{amount} deposited into {self.acc_type} account."
        return "Enter a valid amount."

    def get_balance(self):
        return self.balance

# Streamlit App
st.title("Bank Account Manager")

# Sidebar input
st.sidebar.header("Create an Account")
name = st.sidebar.text_input("Enter your name:")
acc_type = st.sidebar.selectbox("Select account type:", ["Savings", "Current", "Fixed Deposit"])

if st.sidebar.button("Create Account"):
    if name:
        # Save the account object in session state
        st.session_state.account = Account(name, acc_type)
        st.success(f"Account created for {name} ({acc_type})")
    else:
        st.error("Name cannot be empty.")

# Only show options if account exists
if "account" in st.session_state:
    st.subheader(f"Welcome, {st.session_state.account.name}!")

    deposit_amount = st.number_input("Enter amount to deposit:", min_value=0.0, format="%.2f")
    if st.button("Deposit"):
        message = st.session_state.account.deposit(deposit_amount)
        st.info(message)

    if st.button("Check Balance"):
        balance = st.session_state.account.get_balance()
        st.success(f"Current Balance: ₦{balance:.2f}")
else:
    st.warning("Create an account using the sidebar to get started.")
