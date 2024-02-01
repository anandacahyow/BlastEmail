# Import necessary libraries
import streamlit as st
from dataclasses import dataclass
from snowflake.snowpark import Session

# Initialize connection
def init_connection() -> Session:
    return Session.builder.configs(st.secrets["snowpark"]).create()

@dataclass
class OurFilter:
    """This dataclass represents the filter that can be optionally enabled. 
    It is created to parametrize the creation of filters from Streamlit and to keep the state."""
    human_name: str
    widget_type: callable  # Should be one of st.checkbox or st.select_slider. Other elements could be implemented similarly
    widget_id: str
    is_enabled: bool = False  # Controls whether the filter has been enabled. Useful for filtering the list of filters
    _max_value: int = 0

if __name__ == "__main__":
    # Initialize the filters
    session = init_connection()

    # Implement the dynamic filters in the sidebar
    filter = OurFilter(human_name="Your Filter", widget_type=st.checkbox, widget_id="your_filter")

    # Display the dataframe
    ncol = st.sidebar.number_input("Number of dynamic columns", 0, 20, 1)
    cols = st.beta_columns(ncol)
    for i, x in enumerate(cols):
        x.selectbox(f"Input # {i}", [1,2,3], key=i)
