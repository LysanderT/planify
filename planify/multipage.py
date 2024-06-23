import streamlit as st

def main():
    st.sidebar.title("Navigation")
    pages = ["Initial Activity", "Add-On Activity", "Preferences", "Summary"]
    choice = st.sidebar.radio("Go to", pages)

    if choice == "Initial Activity":
        import InitialActivity
        InitialActivity.run()
    elif choice == "Add-On Activity":
        import AddOnActivity
        AddOnActivity.run()
    elif choice == "Preferences":
        import Preferences
        Preferences.run()
    elif choice == "Summary":
        import Summary
        Summary.run()

if __name__ == "__main__":
    main()
