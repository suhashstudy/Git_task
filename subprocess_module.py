import streamlit as st
import subprocess

def get_git_branches():
    try:
        # Run the git branch command and capture the output
        result = subprocess.run(["git", "branch"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        
        # Check if the command was successful
        if result.returncode == 0:
            # Split the output into lines and extract branch names
            branches = [branch.strip() for branch in result.stdout.split('\n') if branch]
            return branches
        else:
            # Display an error message if the command failed
            st.error(f"Error retrieving Git branches:\n{result.stderr}")
            return None
    except Exception as e:
        # Display any unexpected errors
        st.error(f"An error occurred: {str(e)}")
        return None

# Streamlit app
def main():
    st.title("Git Branch Viewer")

    # Get Git branches
    branches = get_git_branches()

    # Display branches in a Streamlit selectbox
    if branches is not None:
        selected_branch = st.selectbox("Select Git Branch", branches)
        st.success(f"Selected branch: {selected_branch}")

if __name__ == "__main__":
    main()
