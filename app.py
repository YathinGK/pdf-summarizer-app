import streamlit as st
import logging

# Set logging level to ERROR
logging.getLogger('tensorflow').setLevel(logging.ERROR)
logging.getLogger('streamlit').setLevel(logging.ERROR)

# Custom CSS to change background color and add hover effect
st.markdown(
    """
    <style>
    .stApp {
        background-color: 7091E6;
    }
    .container {
        display: flex;
        justify-content: space-around;
        margin-top: 50px;
    }
    .box {
        width: 45%;
        height: 200px;
        text-align: center;
        vertical-align: middle;
        line-height: 200px;
        font-size: 24px;
        color: white;
        cursor: pointer;
        border-radius: 10px;
        transition: background-color 0.3s ease;
    }
    .box:hover {
        background-color: 024950 !important;
    }
    .summary_box {
        background-color: #17a2b8;
    }
    .handwriting_box {
        background-color: #28a745;
    }
     .centered-title {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize session state for app selection
if 'selected_app' not in st.session_state:
    st.session_state.selected_app = None

def main():
    st.title("Readixer")

    st.markdown('<div class="container">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
           st.image("D:\Summary_Generator_Python\Images\sum.png")
           if st.button("Summary Generator", key="summary_generator", help="Click to summarize a PDF"):
           
            st.session_state.selected_app = "summary_generator"
           

    with col2:
        st.image("D:\Summary_Generator_Python\Images\Hand.png")
        if st.button("Handwriting Conversion", key="handwriting_conversion", help="Click to convert handwriting to digital text"):
            
             st.session_state.selected_app = "handwriting_conversion"
           
    st.markdown('</div>', unsafe_allow_html=True)
    st.write(" ")
    st.write(" ")
    st.write("Welcome to Readixer !!It is a comprehensive project aimed at enhancing document digitization and summarization capabilities using advanced Python tools and technologies. The project integrates two primary functionalities: summary generation and handwritten text to digital conversion, catering to diverse needs in document management and accessibility....")

    if st.session_state.selected_app == "summary_generator":
        import summary_generator
        summary_generator.summary_generator()
    elif st.session_state.selected_app == "handwriting_conversion":
        import handwriting_conversion
        handwriting_conversion.handwriting_conversion()

if __name__ == "__main__":
    main()
