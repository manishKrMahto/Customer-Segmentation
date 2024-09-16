import streamlit as st 
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

# loading final df to display 
final_df = pickle.load(open('final_df.pkl' ,'rb'))

st.title('Customer Segmentation project')

# showing first 10 rows of data
st.dataframe(final_df.head(10))

# used to filter data with country , month , day 
country_list = list(set(final_df['Country']))
month_name = list(set(final_df['monthName']))
day_name = list(set(final_df['DayName']))


# giving filter option to user into sidebar
st.sidebar.title('Filtering option')
country = st.sidebar.multiselect('choose country' , country_list)
month = st.sidebar.multiselect('choose month' , month_name)
day = st.sidebar.multiselect('choose day' , day_name)

status = st.sidebar.button('show')

if status :
    
    # if filtered country list has some names/ values then filter otherwise ignore
    if len(country) != 0 :
        final_df = final_df[final_df['Country'].isin(country)]
        
    if len(month) != 0:
        final_df = final_df[final_df['monthName'].isin(month)]
        
    if len(day) != 0:
        final_df = final_df[final_df['DayName'].isin(day)]
    
    # ploting charts for filtered data
    fig , ax = plt.subplots()
    sns.stripplot(data = final_df , x = 'Cluster' , y = 'AmountSpent' , ax =ax )
    plt.title('Amount Spent with each cluster')
    st.pyplot(fig)
    
    fig , ax = plt.subplots()
    sns.stripplot(data = final_df , x = 'Cluster' , y = 'frequency' , ax =ax )
    plt.title('Purchase frequency with each cluster')
    st.pyplot(fig)

