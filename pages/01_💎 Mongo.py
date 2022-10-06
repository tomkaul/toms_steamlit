import streamlit as st
import pandas as pd
from utils import Mongo

# st.title('🎈 My MongoDB')

# Create sidebar
db_name = 'tk_db'
st.sidebar.markdown(f'## Database name: {db_name}')
# st.write(st.secrets['database'])
# DB stuff
local = st.sidebar.checkbox('Use local MongoDB', value=True)
if local:
  db = Mongo(db_name, 'fedeklubben', {'host': 'local'})
else:
  db = Mongo(db_name, 'fedeklubben', st.secrets['database'])
colls = db.get_all_collections()

coll = st.sidebar.selectbox('Select collection:', colls)
db.get_collection(coll)

# Create main page
df = pd.DataFrame(db.get_all_records())
# Remove ObjectID from _id
try:
  df._id = df._id.apply(str)
  df._id = df._id.apply(int)
except ValueError:
  pass
st.markdown(f'__Collection: {coll}__')
st.dataframe(df)