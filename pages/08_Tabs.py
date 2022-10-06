# Tabs test
import streamlit as st

tab_list = ['thomas', 'claus', 'jaksen']
# for tab in st.tabs(tab_list):
#   with tab:
#     st.write(dir(tab))
tabs = list(st.tabs(tab_list))

# i = 0
for i, tab in enumerate(tabs):
  with tab:
    st.write(tab_list[i])
  i += 1
