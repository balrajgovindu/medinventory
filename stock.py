import streamlit as st

import sqlite3
conn = sqlite3.connect('data.db',check_same_thread=False)
c=conn.cursor()

def create_table():
    c.execute('CREATE TABLE IF NOT EXISTS medtable(product TEXT,Batch TEXT,code NUM,expiry DATE,pack NUM,quantity NUM,price Num,rate NUM)')

def add_data(product,Batch,code,expiry,pack,quantity,price,rate):
    c.execute('INSERT INTO medtable(product,Batch,code,expiry,pack,quantity,price,rate) VALUES(?,?,?,?,?,?,?,?)',(product,Batch,code,expiry,pack,quantity,price,rate))
    conn.commit()


def main():
    st.title('Stock Inventory')

    menu = ['Home','Purchase','Stock','Sale']
    choice = st.sidebar.selectbox('Menu',menu)

    if choice == 'Home':
        st.subheader('Home')

    elif choice == 'Purchase':
        #st.sidebar('Purchase Details')

        distributor = st.sidebar.text_input('Distributors Name')
        invoice=st.sidebar.text_input('Invoice Number')
        date=st.sidebar.date_input('Invoice Date')
        place=st.sidebar.text_input('Distributors City or Place')

        if st.sidebar.button('Add Invoice Details'):
           st.sidebar.success('Successfully added invoice details')
           create_table()
           col1,col2 = st.columns(2)

           with col1:
               product = st.text_input('Brand Name')
               Batch = st.text_input('Batch No.')
               code = st.text_input('HSN CODE')
               expiry = st.date_input('Expiry Date')

           with col2:
               pack = st.text_input('Quantity per unit')
               quantity = st.text_input('Quantity recieved ')
               price = st.text_input('M.R.P Including GST')
               rate = st.text_input('Purchase Rate')

               if st.checkbox('Add Purchase Details'):
                    add_data(product,Batch,code,expiry,pack,quantity, price, rate)
                    st.success('Succcefully added Purchase details')

        def get_sum(rate):
            n=len(rate)
            sum=0
            for i in range(0,n):
                sum=rate[i]
            return sum







    elif choice == 'Stock':
        st.subheader('Overall Stock')

    elif choice == 'Sale':
        st.subheader('Create sales bill')








if __name__ == '__main__':
    main()