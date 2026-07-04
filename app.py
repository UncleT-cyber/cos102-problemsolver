import streamlit as st
import subprocess
import os

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="COS 102 | Lab Project",
    page_icon="⚖️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CLASSIC CUSTOM CSS INJECTION ---
st.markdown("""
<style>
    /* Global Styles */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=400;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    /* Sidebar Styling */
    section[data-testid="stSidebar"] {
        background-color: #0f172a;
        color: white;
    }
    
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] p,
    section[data-testid="stSidebar"] .st-emotion-cache-10trblm {
        color: white;
    }

    /* Professional Button Styling */
    .stButton > button {
        width: 100%;
        background-color: #2563eb;
        color: white;
        border-radius: 4px;
        border: none;
        padding: 12px 24px;
        font-weight: 600;
        letter-spacing: 0.5px;
        transition: all 0.2s ease;
        text-transform: uppercase;
        font-size: 14px;
        box-shadow: 0 1px 2px rgba(0,0,0,0.1);
    }

    .stButton > button:hover {
        background-color: #1d4ed8;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transform: translateY(-1px);
    }

    .stButton > button:active {
        transform: translateY(0);
    }

    /* Classic Input Styling */
    .stNumberInput input {
        border-radius: 4px !important;
        border: 1px solid #e2e8f0 !important;
    }

    /* Card/Container Simulation */
    .main-card {
        background: white;
        padding: 40px;
        border-radius: 8px;
        border: 1px solid #e2e8f0;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05);
        margin-bottom: 2rem;
    }
    
    .stDivider {
        margin: 2rem 0;
    }
</style>
""", unsafe_allow_html=True)

# --- AUTO-COMPILATION FOR CLOUD HOSTING ---
# Ensures the binary exists, is compiled fresh for Linux, and has proper execution flags
if os.path.exists("logic.c"):
    # Compile if binary is missing or code was updated
    if not os.path.exists("./logic") or os.path.getmtime("logic.c") > os.path.getmtime("./logic"):
        os.system("gcc logic.c -o logic")
    
    # CRITICAL FIX: Explicitly grant Linux execution permissions (chmod +x equivalent)
    if os.path.exists("./logic"):
        try:
            os.chmod("./logic", 0o755)
        except Exception as e:
            st.error(f"Permission Configuration Failed: {e}")
else:
    st.error("System Configuration Error: 'logic.c' was not detected in the repository workspace directory.")

# --- SIDEBAR NAVIGATION ---
with st.sidebar:
    st.title("COS 102")
    st.markdown("### Problem Solver")
    st.divider()
    
    page = st.radio(
        "NAVIGATION",
        ["Geometric Analysis", "Numerical Symmetry"],
        index=0
    )
    
    st.divider()
    st.caption("System Status: Operational 🟢")
    st.caption("Backend: Compiled C Binary")

# --- MAIN CONTENT AREA ---
if page == "Geometric Analysis":
    st.title("📐 Task 1: Right-Angled Triangle Checker")
    st.markdown("Verification of geometric properties using high-precision C logic.")
    
    with st.container():
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            a1 = st.number_input("Primary Angle (Alpha)", min_value=1, max_value=179, value=45)
        with col2:
            a2 = st.number_input("Secondary Angle (Beta)", min_value=1, max_value=179, value=45)
            
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("RUN VERIFICATION"):
            if (a1 + a2) >= 180:
                st.error("Geometric Constraint Violation: The sum of two angles must be < 180°.")
            else:
                # Execute C backend
                result = subprocess.run(['./logic', 'triangle', str(a1), str(a2)], capture_output=True, text=True)
                if result.stdout:
                    third_angle, message = result.stdout.split('|')
                    st.metric("Computed Third Angle", f"{third_angle}°")
                    
                    if "Not" in message:
                        st.warning(f"**Verdict:** {message}")
                    else:
                        st.success("The triangle IS a right-angled triangle. 🎉")
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "Numerical Symmetry":
    st.title("🔢 Task 2: Palindrome Checker")
    st.markdown("Sequence analysis and symmetry detection powered by native string processing.")
    
    with st.container():
        st.markdown('<div class="main-card">', unsafe_allow_html=True)
        
        target_num = st.number_input("Target Input Sequence", min_value=0, value=12321, step=1)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        if st.button("EXECUTE SYMMETRY TEST"):
            # Execute C backend
            result = subprocess.run(['./logic', 'palindrome', str(target_num)], capture_output=True, text=True)
            
            if "Not" in result.stdout:
                st.error(f"Backend Result: {result.stdout}")
            else:
                st.success(f"Yes! {target_num} is a Palindrome. 🎉")
        st.markdown('</div>', unsafe_allow_html=True)
