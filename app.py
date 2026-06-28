import streamlit as st
import subprocess
import os

st.set_page_config(page_title="COS 102 Problem Solver", page_icon="⚙️", layout="centered")

# --- AUTO-COMPILATION FOR CLOUD HOSTING ---
# When deployed, the Linux server will compile logic.c automatically if 'logic' executable doesn't exist
if not os.path.exists("./logic"):
    try:
        os.system("gcc logic.c -o logic")
    except Exception as e:
        st.error(f"Compilation failed: {e}")

st.title("COS 102 Problem Solver Dashboard")
st.caption("Powered by a compiled C Binary Backend via Python Subprocesses")

# Modern Tab Layout
tab1, tab2 = st.tabs(["📐 Task 1: Triangle Checker", "🔢 Task 2: Palindrome Checker"])

with tab1:
    st.header("Right-Angled Triangle Verification")
    st.write("Input two angles to compute the missing angle and check for a 90° boundary.")
    
    col1, col2 = st.columns(2)
    with col1:
        a1 = st.number_input("First Angle (°)", min_value=1, max_value=179, value=45, key="angle1")
    with col2:
        a2 = st.number_input("Second Angle (°)", min_value=1, max_value=179, value=45, key="angle2")
        
    if st.button("Verify Geometry", type="primary"):
        if (a1 + a2) >= 180:
            st.error("Error: The sum of two angles must be strictly less than 180°.")
        else:
            # Execute backend C binary
            result = subprocess.run(['./logic', 'triangle', str(a1), str(a2)], capture_output=True, text=True)
            if result.stdout:
                third_angle, message = result.stdout.split('|')
                st.success(f"**Third Angle:** {third_angle}°")
                if "Not" in message:
                    st.warning(f"**Classification:** {message}")
                else:
                    st.info(f"**Classification:** {message} 🎉")

with tab2:
    st.header("Integer Sequence Palindrome Tester")
    st.write("Input any positive integer sequence to test structural symmetry.")
    
    num = st.number_input("Target Input Sequence", min_value=0, value=12321, step=1)
    
    if st.button("Run Symmetrical Analysis", type="primary"):
        # Execute backend C binary
        result = subprocess.run(['./logic', 'palindrome', str(num)], capture_output=True, text=True)
        if "Not" in result.stdout:
            st.error(f"Backend Verdict: {result.stdout}")
        else:
            st.success(f"Backend Verdict: {result.stdout} ✨")