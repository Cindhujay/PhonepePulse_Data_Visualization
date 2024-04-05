import os
import json
import sqlite3 as sql
import sqlite3
import mysql.connector
import pandas as pd
import plotly.express as px
from PIL import Image
import streamlit as st

st.set_page_config(page_title="Phonepe",layout='wide',initial_sidebar_state="expanded",menu_items=None)

#Aggregate Transaction

path1 = "C:/Users/Admin/Desktop/Project2/pulse/data/aggregated/transaction/country/india/state/"
trans_state = os.listdir(path1)

col1 = {'States':[], 'Year':[], 'Quarter':[], 'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in trans_state:
    state_list = path1+state+"/"
    year_list = os.listdir(state_list)
    
    for year in year_list:
        curr_year = state_list+year+"/"
        agg_year_list = os.listdir(curr_year)

        for file in agg_year_list:
            curr_file = curr_year+file
            Data = open(curr_file,"r")

            D = json.load(Data)

            for i in D['data']['transactionData']:
                Name = i['name']
                count = i['paymentInstruments'][0]['count']
                amount = i ['paymentInstruments'][0]['amount']
                col1['Transaction_type'].append(Name)
                col1['Transaction_count'].append(count)
                col1['Transaction_amount'].append(amount)
                col1['States'].append(state)
                col1['Year'].append(year)
                col1['Quarter'].append(int(file.strip('.json')))

Agg_Trans = pd.DataFrame(col1)
Agg_Trans['States']=Agg_Trans['States'].str.replace('-',' ')
Agg_Trans['States']=Agg_Trans['States'].str.title()
Agg_Trans['States']=Agg_Trans['States'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
Agg_Trans['States']=Agg_Trans['States'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')

#Aggregated User
path2 = "C:/Users/Admin/Desktop/Project2/pulse/data/aggregated/user/country/india/state/"
user_state = os.listdir(path2)

col2 = {'States':[], 'Year':[], 'Quarter':[], 'brand':[], 'Transaction_count':[], 'percentage':[]}

for state in user_state:
    state_list = path2+state+"/"
    year_list = os.listdir(state_list)
    
    for year in year_list:
        curr_year = state_list+year+"/"
        agg_year_list = os.listdir(curr_year)

        for file in agg_year_list:
            curr_file = curr_year+file
            Data = open(curr_file,"r")

            A = json.load(Data)
            
            try:

                for j in A['data']['usersByDevice']:
                    Brand = j['brand']
                    Count = j['count']
                    percentage=j['percentage']
                    col2['brand'].append(Brand)
                    col2['Transaction_count'].append(Count)
                    col2['percentage'].append(percentage)
                    col2['States'].append(state)
                    col2['Year'].append(year)
                    col2['Quarter'].append(int(file.strip('.json')))
            except:
                pass
                
Agg_user = pd.DataFrame(col2)
Agg_user['States']=Agg_user['States'].str.replace('-',' ')
Agg_user['States']=Agg_user['States'].str.title()
Agg_user['States']=Agg_user['States'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
Agg_user['States']=Agg_user['States'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


#Map Transaction
path3 = "C:/Users/Admin/Desktop/Project2/pulse/data/map/transaction/hover/country/india/state/"
trans_map = os.listdir(path3)

col3 = {'States':[], 'Year':[], 'Quarter':[], 'Districts':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in trans_map:
    state_list = path3+state+"/"
    year_list = os.listdir(state_list)
    
    for year in year_list:
        curr_year = state_list+year+"/"
        agg_year_list = os.listdir(curr_year)

        for file in agg_year_list:
            curr_file = curr_year+file
            Data = open(curr_file,"r")

            B = json.load(Data)
            for k in B['data']['hoverDataList']:
                    District = k['name']
                    Count = k['metric'][0]['count']
                    Amount=k['metric'][0]['amount']
                    col3['Districts'].append(District)
                    col3['Transaction_count'].append(Count)
                    col3['Transaction_amount'].append(Amount)
                    col3['States'].append(state)
                    col3['Year'].append(year)
                    col3['Quarter'].append(int(file.strip('.json')))

map_trans = pd.DataFrame(col3)

map_trans['States']=map_trans['States'].str.replace('-',' ')
map_trans['States']=map_trans['States'].str.title()
map_trans['States']=map_trans['States'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
map_trans['States']=map_trans['States'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')


map_trans           

#Map Users
path4 = "C:/Users/Admin/Desktop/Project2/pulse/data/map/user/hover/country/india/state/"
user_map = os.listdir(path4)

col4 = {'States':[], 'Year':[], 'Quarter':[], 'Districts':[], 'Registereduser':[], 'Appopens':[]}

for state in user_map:
    state_list = path4+state+"/"
    year_list = os.listdir(state_list)
    
    for year in year_list:
        curr_year = state_list+year+"/"
        agg_year_list = os.listdir(curr_year)

        for file in agg_year_list:
            curr_file = curr_year+file
            Data = open(curr_file,"r")

            C = json.load(Data)
            for l in C['data']['hoverData'].items():
                    District = l[0]
                    registereduser = l[1]['registeredUsers']
                    appOpens=l[1]['appOpens']
                    col4['Districts'].append(District)
                    col4['Registereduser'].append(registereduser)
                    col4['Appopens'].append(appOpens)
                    col4['States'].append(state)
                    col4['Year'].append(year)
                    col4['Quarter'].append(int(file.strip('.json')))

map_user = pd.DataFrame(col4)

map_user['States']=map_user['States'].str.replace('-',' ')
map_user['States']=map_user['States'].str.title()
map_user['States']=map_user['States'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
map_user['States']=map_user['States'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')
map_user

#Top Transaction Districts
path5 = "C:/Users/Admin/Desktop/Project2/pulse/data/top/transaction/country/india/state/"
top_trans = os.listdir(path5)

col5 = {'States':[], 'Year':[], 'Quarter':[], 'Districts':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in top_trans:
    state_list = path5+state+"/"
    year_list = os.listdir(state_list)
    
    for year in year_list:
        curr_year = state_list+year+"/"
        agg_year_list = os.listdir(curr_year)

        for file in agg_year_list:
            curr_file = curr_year+file
            Data = open(curr_file,"r")
            
            E = json.load(Data)

            for m in E['data']['districts']:
                entityname= m['entityName']
                count = m['metric']['count']
                amount = m['metric']['amount']
                col5['Districts'].append(entityname)
                col5['Transaction_count'].append(count)
                col5['Transaction_amount'].append(amount)
                col5['States'].append(state)
                col5['Year'].append(year)
                col5['Quarter'].append(int(file.strip('.json')))


trans_top = pd.DataFrame(col5)
trans_top['States']=trans_top['States'].str.replace('-',' ')
trans_top['States']=trans_top['States'].str.title()
trans_top['States']=trans_top['States'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
trans_top['States']=trans_top['States'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')
trans_top

#Top Transaction Pincodes
path6 = "C:/Users/Admin/Desktop/Project2/pulse/data/top/transaction/country/india/state/"
top_pin = os.listdir(path6)

col6 = {'States':[], 'Year':[], 'Quarter':[], 'Pincodes':[], 'Transaction_count':[], 'Transaction_amount':[]}

for state in top_trans:
    state_list = path6+state+"/"
    year_list = os.listdir(state_list)
    
    for year in year_list:
        curr_year = state_list+year+"/"
        agg_year_list = os.listdir(curr_year)

        for file in agg_year_list:
            curr_file = curr_year+file
            Data = open(curr_file,"r")
            
            F = json.load(Data)
            for n in F['data']['pincodes']:
                entity= n['entityName']
                count = n['metric']['count']
                amount = n['metric']['amount']
                col6['Pincodes'].append(entity)
                col6['Transaction_count'].append(count)
                col6['Transaction_amount'].append(amount)
                col6['States'].append(state)
                col6['Year'].append(year)
                col6['Quarter'].append(int(file.strip('.json')))

pin_top = pd.DataFrame(col6)
pin_top['States']=pin_top['States'].str.replace('-',' ')
pin_top['States']=pin_top['States'].str.title()
pin_top['States']=pin_top['States'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
pin_top['States']=pin_top['States'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')
pin_top


#Top User Districts

path7 = "C:/Users/Admin/Desktop/Project2/pulse/data/top/user/country/india/state/"
top_user = os.listdir(path7)

col7 = {'States':[], 'Year':[], 'Quarter':[], 'districts':[], 'registeredUsers':[]}

for state in top_trans:
    state_list = path7+state+"/"
    year_list = os.listdir(state_list)
    
    for year in year_list:
        curr_year = state_list+year+"/"
        agg_year_list = os.listdir(curr_year)

        for file in agg_year_list:
            curr_file = curr_year+file
            Data = open(curr_file,"r")
            
            G = json.load(Data)

            for o in G['data']['districts']:
                Name= o['name']
                registereduser = o['registeredUsers']
                col7['districts'].append(Name)
                col7['registeredUsers'].append(registereduser)
                col7['States'].append(state)
                col7['Year'].append(year)
                col7['Quarter'].append(int(file.strip('.json')))

user_top = pd.DataFrame(col7)
user_top['States']=user_top['States'].str.replace('-',' ')
user_top['States']=user_top['States'].str.title()
user_top['States']=user_top['States'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
user_top['States']=user_top['States'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')
user_top


#Top User Pincodes
path8 = "C:/Users/Admin/Desktop/Project2/pulse/data/top/user/country/india/state/"
top_pincode = os.listdir(path8)

col8 = {'States':[], 'Year':[], 'Quarter':[], 'pincodes':[], 'registeredUsers':[]}

for state in top_trans:
    state_list = path8+state+"/"
    year_list = os.listdir(state_list)
    
    for year in year_list:
        curr_year = state_list+year+"/"
        agg_year_list = os.listdir(curr_year)

        for file in agg_year_list:
            curr_file = curr_year+file
            Data = open(curr_file,"r")
            
            H = json.load(Data)
            for p in H['data']['pincodes']:
                Name = p["name"]
                registereduser = p['registeredUsers']
                col8['pincodes'].append(Name)
                col8['registeredUsers'].append(registereduser)
                col8['States'].append(state)
                col8['Year'].append(year)
                col8['Quarter'].append(int(file.strip('.json')))

pincode_top = pd.DataFrame(col8)
pincode_top['States']=pincode_top['States'].str.replace('-',' ')
pincode_top['States']=pincode_top['States'].str.title()
pincode_top['States']=pincode_top['States'].str.replace('Andaman & Nicobar Islands','Andaman & Nicobar')
pincode_top['States']=pincode_top['States'].str.replace('Dadra & Nagar Haveli & Daman & Diu','Dadra and Nagar Haveli and Daman and Diu')
pincode_top


#Converting DataFrames into CSV files
Agg_Trans.to_csv('Agg_Trans_file.csv',index=False)
Agg_user.to_csv('Agg_user_file.csv',index=False)
map_trans.to_csv('map_trans_file.csv',index=False)
map_user.to_csv('map_user_file.csv',index=False)
trans_top.to_csv('trans_top_file.csv',index=False)
pin_top.to_csv('pin_top_file.csv',index=False)
user_top.to_csv('user_top_file.csv',index=False)
pincode_top.to_csv('pincode_top_file.csv',index=False)

#Connecting with sqlite3
conn = sql.connect('pulse.db')
mycursor = conn.cursor()

#creating Tables Transaction Table
trans_table = '''CREATE TABLE IF NOT EXISTS table_trans (States VARCHAR(100),
                                                            Year INT,
                                                            Quarter INT,
                                                            Transaction_type VARCHAR,
                                                            Transaction_count INT,
                                                            Transaction_amount FLOAT)'''
mycursor.execute(trans_table)

#Inserting Values to Transaction Table
for i,row in Agg_Trans.iterrows():
    mysql = "INSERT INTO table_trans (States,Year,Quarter,Transaction_type,Transaction_count,Transaction_amount)VALUES (?,?,?,?,?,?)"
    val=(row['States'],row['Year'],row['Quarter'],row['Transaction_type'],row['Transaction_count'],row['Transaction_amount'])
    mycursor.execute(mysql,val)
conn.commit()

# Creating Agg_User table
user_table='''CREATE TABLE IF NOT EXISTS table2_users( States varchar(100), 
                                                        Year int,
                                                        Quarter int, 
                                                        brand varchar, 
                                                        Transaction_count int, 
                                                        percentage Float)'''
mycursor.execute(user_table)

# Inserting Values to Agg_User table
for i, row in Agg_user.iterrows():
    mysql = "INSERT INTO table2_users(States,Year,Quarter,brand,Transaction_count,percentage) VALUES (?,?,?,?,?,?)"
    val=(row['States'],row['Year'],row['Quarter'],row['brand'],row['Transaction_count'],row['percentage'])
    mycursor.execute(mysql,val)
conn.commit()

# Creating Map Transaction Table
map_trans_table = '''CREATE TABLE IF NOT EXISTS table3(States varchar(100),
                                                        Year int,
                                                        Quarter int,
                                                        Districts varchar,
                                                        Transaction_count int,
                                                        Transaction_amount float)'''
mycursor.execute(map_trans_table)

# Inserting Values to Map Transaction table
for i, row in map_trans.iterrows():
    mysql = "Insert INTO table3(States,Year,Quarter,Districts,Transaction_count,Transaction_amount) VALUES(?,?,?,?,?,?)"
    val=(row['States'],row['Year'],row['Quarter'],row['Districts'],row['Transaction_count'],row['Transaction_amount'])
    mycursor.execute(mysql,val)
conn.commit()

# Creating Map User Table
map_user_table = '''CREATE TABLE IF NOT EXISTS table4(States varchar(100),
                                                        Year int,
                                                        Quarter int,
                                                        Districts varchar,
                                                        Registereduser int,
                                                        Appopens int)'''
mycursor.execute(map_user_table)

# Inserting Values to Map User table
for i, row in map_user.iterrows():
    mysql = "Insert INTO table4(States,Year,Quarter,Districts,Registereduser,Appopens) VALUES(?,?,?,?,?,?)"
    val=(row['States'],row['Year'],row['Quarter'],row['Districts'],row['Registereduser'],row['Appopens'])
    mycursor.execute(mysql,val)
conn.commit()

#creating Top Transaction Table
trans_top_table = '''CREATE TABLE IF NOT EXISTS table5(States VARCHAR(100),
                                                        Year INT,
                                                        Quarter INT,
                                                        Districts VARCHAR,
                                                        Transaction_count INT,
                                                        Transaction_amount FLOAT)'''
mycursor.execute(trans_top_table)

#Inserting Values top Transaction Table
for i,row in trans_top.iterrows():
    mysql = "INSERT INTO table5 (States,Year,Quarter,Districts,Transaction_count,Transaction_amount)VALUES (?,?,?,?,?,?)"
    val=(row['States'],row['Year'],row['Quarter'],row['Districts'],row['Transaction_count'],row['Transaction_amount'])
    mycursor.execute(mysql,val)
conn.commit()

#creating Top Pincode Table
pin_top_table = '''CREATE TABLE IF NOT EXISTS table6(States VARCHAR(100),
                                                        Year INT,
                                                        Quarter INT,
                                                        Pincodes VARCHAR,
                                                        Transaction_count INT,
                                                        Transaction_amount FLOAT)'''
mycursor.execute(pin_top_table)

# Inserting Values to Top Pincode table
for i, row in pin_top.iterrows():
    mysql = "INSERT INTO table6(States,Year,Quarter,Pincodes,Transaction_count,Transaction_amount) VALUES (?,?,?,?,?,?)"
    val=(row['States'],row['Year'],row['Quarter'],row['Pincodes'],row['Transaction_count'],row['Transaction_amount'])
    mycursor.execute(mysql,val)
conn.commit()

#creating Top User Table
user_top_table = '''CREATE TABLE IF NOT EXISTS table7(States VARCHAR(100),
                                                        Year INT,
                                                        Quarter INT,
                                                        districts VARCHAR,
                                                        registeredUsers INT)'''
mycursor.execute(user_top_table)

# Inserting Values to Top User table
for i, row in user_top.iterrows():
    mysql = "INSERT INTO table7(States,Year,Quarter,districts,registeredUsers) VALUES (?,?,?,?,?)"
    val=(row['States'],row['Year'],row['Quarter'],row['districts'],row['registeredUsers'])
    mycursor.execute(mysql,val)
conn.commit()

#creating Top User Pincode Table
user_pin_table = '''CREATE TABLE IF NOT EXISTS table8(States VARCHAR(100),
                                                        Year INT,
                                                        Quarter INT,
                                                        pincodes VARCHAR,
                                                        registeredUsers INT)'''
mycursor.execute(user_pin_table)

# Inserting Values to Top User Pincode table
for i, row in pincode_top.iterrows():
    mysql = "INSERT INTO table8(States,Year,Quarter,pincodes,registeredUsers) VALUES (?,?,?,?,?)"
    val=(row['States'],row['Year'],row['Quarter'],row['pincodes'],row['registeredUsers'])
    mycursor.execute(mysql,val)
conn.commit()

mycursor.execute('SELECT * From sqlite_master where type="table" ')
mycursor.fetchall()

conn1=sqlite3.connect(r"C:\Users\Admin\Desktop\Project2\pulse.db")
mycursor = conn1.cursor()



Menu = ['Home','Top Charts','Explore Data']
choice = st.sidebar.selectbox("Menu",Menu)

if choice == 'Home':
    image1 = Image.open(r"C:\Users\Admin\Desktop\Project2\phonepe.jpg")
    st.image(image1)
    st.markdown("# :violet[Data Visualization and Exploration]")
    st.markdown("## :violet[A User-Friendly Tool Using Streamlit and Plotly]")
    column1,column2 = st.columns([2,2],gap='medium')

    with column1:
      st.write(" ")
      st.write(' ')
      st.markdown('### :blue[Domain:] Fintech')
      st.markdown('### :blue[Technologies Used:]  Github Cloning, Python, Pandas, sqlite3,Streamlit, and Plotly')
      st.markdown('### :blue[Overview:]  In this streamlit web app you can visualize the phonepe pulse data and gain lot of insights on transactions, number of users, top 10 state, district, pincode and which brand has most number of users and so on. Bar charts, Pie charts and Geo map visualization are used to get some insights."')

    with column2:
      image2 = Image.open(r"C:\Users\Admin\Desktop\Project2\india.jpg")
      st.image(image2)   

if choice=="Top Charts":
    st.markdown("## :red[Top Charts]")
    Type=st.sidebar.selectbox('**Type**',("Transactions","Users"))
    col1,col2=st.columns([2,1.5],gap='Large')
    with col1:
        Year = st.selectbox('**Select Year**',(2018,2019,2020,2021,2022),key='in_to_year')
        Quarter =st.selectbox('**Select Quarter**',(1,2,3,4),key='in_to_qtr')
    with col2:
        st.info("""
                #### From this menu we can get insights like :
                - Overall ranking on a particular Year and Quarter.
                - Top 10 State, District, Pincode based on Total number of transaction and Total amount spent on phonepe.
                - Top 10 State, District, Pincode based on Total phonepe users and their app opening frequency.
                - Top 10 mobile brands and its percentage based on the how many people use phonepe.
                """,icon="🔍"
                )
    if Type=='Transactions':
        column1,column2,column3=st.columns([1,1,1],gap='small')
        with column1:
            st.markdown('## blue[States]')
            mycursor.execute(f"Select States ,sum(Transaction_count)as Total_Transaction_count,sum(Transaction_amount) as Total_Transaction_amount from table_trans where Year={Year} and Quarter={Quarter} group by States order by Total_Transaction_amount desc limit 10")

            df = pd.DataFrame(mycursor.fetchall(),columns=['States','Transaction_count','Total_amount'])
            st.dataframe(df)
            fig=px.pie(df,values='Total_amount',
                       names='States',
                       title='Top 10',
                       color_discrete_sequence=px.colors.sequential.Agsunset,
                       hover_data=['Transaction_count'],
                       labels={'Transaction_count':'Transaction_count'})
            fig.update_traces(textposition='inside',textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

        with column2:
            st.markdown("## :orange[districts]")
            mycursor.execute(f"select districts,sum(Transaction_count) as Total_count,sum(Transaction_amount)as Total_amount from table3 where Year={Year} and Quarter={Quarter} group by districts order by Total_amount desc limit 10")
            df=pd.DataFrame(mycursor.fetchall(),columns=['districts','Transaction_count','Total_amount'])
            st.dataframe(df)
            fig=px.pie(df,values='Total_amount',
                       names='districts',
                       title='Top 10',
                       color_discrete_sequence=px.colors.sequential.Agsunset,
                       hover_data = {'Transaction_count':'Transaction_count'})
            fig.update_traces(textposition='inside',textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)

        with column3:
            st.markdown("## :violet[Pincodes]")
            mycursor.execute(f"select Pincodes,sum(Transaction_count) as Total_Transaction_count, sum(Transaction_amount) as Total_amount from table6 where Year={Year} and Quarter={Quarter} group by Pincodes order by Total_amount desc limit 10")   
            df=pd.DataFrame(mycursor.fetchall(),columns=['Pincodes','Transaction_count','Total_amount'])
            st.dataframe(df)
            fig=px.pie(df,values="Total_amount",
                       names="Pincodes",
                       title="Top 10",
                       color_discrete_sequence=px.colors.sequential.Agsunset,
                       hover_data=["Transaction_count"],
                       labels={"Transaction_count":"Transaction_count"})
            fig.update_traces(textposition='inside',textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
    if Type =='Users':
        column1,column2,column3,column4=st.columns([1,1,1,1],gap='small')
        with column1:
            st.markdown('## :violet[brand]')
            if Year==2022 and Quarter in [2,3,4]:
                st.markdown('### sorry no data available for Year 2022 in qtr 2,3,4')
            else:
                mycursor.execute(f"select brand,sum(Transaction_count) as Total_Transaction_count,(AVG(percentage)*100) as Avg_per from table2_users where Year={Year} and Quarter={Quarter} group by brand order by Total_Transaction_count desc limit 10")
                df=pd.DataFrame(mycursor.fetchall(),columns=['brand','Total_Users','Avg_per'])
                st.dataframe(df)
                fig=px.bar(df,
                           title="Top 10",
                           x="Total_Users",
                           y="brand",
                           orientation="h",
                           color="Avg_per",
                           color_continuous_scale=px.colors.sequential.Agsunset)
                st.plotly_chart(fig,use_container_width=True)
        with column2:
            st.markdown('## :violet[Districts]')
            mycursor.execute(f"select Districts,sum(Registereduser) as Total_Users,sum(Appopens) as Total_appopen from table4 where Year={Year} and Quarter={Quarter} group by Districts order by Total_Users desc limit 10")
            df=pd.DataFrame(mycursor.fetchall(),columns=['Districts',"Total_Users",'Total_appopen'])
            st.dataframe(df)
            df.Total_Users = df.Total_Users.astype(float)
            fig=px.bar(df,title='Top 10',
                       x='Total_Users',
                       y="Districts",
                       orientation='h',
                       color='Total_Users',
                       color_continuous_scale=px.colors.sequential.Agsunset)
            st.plotly_chart(fig,use_container_width=True)
        with column3:
            st.markdown('## :violet[pincodes]')
            mycursor.execute(f"Select pincodes,sum(registeredUsers) as Total_Users from table8 where Year={Year} and Quarter={Quarter} group by pincodes order by Total_Users desc limit 10")
            df=pd.DataFrame(mycursor.fetchall(),columns=['pincodes','Total_Users'])
            st.dataframe(df)
            fig=px.pie(df,values="Total_Users",
                       names='pincodes',
                       title='Top 10',
                       color_discrete_sequence=px.colors.sequential.Agsunset,
                       hover_data=['Total_Users'])
            fig.update_traces(textposition='inside',textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)
        with column4:
            st.markdown('## :violet[States]')
            mycursor.execute(f"select States,sum(Registereduser) as Total_regusers,sum(Appopens) as Total_appopen from table4 where Year={Year} and Quarter={Quarter} group by States order by Total_regusers desc limit 10")
            df=pd.DataFrame(mycursor.fetchall(),columns=['States','Total_appopen','Total_regusers'])
            st.dataframe(df)
            fig=px.pie(df,values='Total_appopen',
                       names='States',
                       title='Top 10',
                       color_discrete_sequence=px.colors.sequential.Agsunset,
                       hover_data=['Total_appopen'],
                       labels={'Total_appopen':'Total_appopen'})
            fig.update_traces(textposition='inside',textinfo='percent+label')
            st.plotly_chart(fig,use_container_width=True)         

if choice=="Explore Data":
    Year= st.selectbox('**Select Year**',(2018,2019,2020,2021,2022),key='in_to_year')
    Quarter = st.selectbox('**Select Quarter**',(1,2,3,4),key='in_to_qtr')
    Type = st.sidebar.selectbox('**Type**',("Transactions","Users"))
    column1,column2=st.columns(2)

    if Type == "Transactions":
        with column1:
            st.markdown("## :violet[Transaction count according to district]")
            selected_state=st.selectbox("** Please select state to visualize**",
                                        ('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                        'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                        'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                        'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                        'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                        'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                        'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                        'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                        'Uttarakhand', 'West Bengal'),index=22)
            mycursor.execute(f"Select States,Districts,Year,Quarter,sum(Transaction_count) as Total_count from table3 where Year={Year} and Quarter={Quarter} and States='{selected_state}' group by States,Districts,Year,Quarter order by States,Districts")
            df1 = pd.DataFrame(mycursor.fetchall(),columns=["States","Districts","Year","Quarter","Total_count"])
            st.dataframe(df1)
            fig=px.bar(df1,
                       title="Transaction count according to district",
                       x="Districts",
                       y="Total_count",
                       orientation='h',
                       color="Total_count",
                       color_continuous_scale=px.colors.sequential.Peach)
            st.plotly_chart(fig,use_container_width=True)

            st.markdown("## :violet[Payment Method]")
            selected_state=st.selectbox("** Please select state to visualize**",
                                        ('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                        'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                        'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                        'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                        'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                        'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                        'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                        'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                        'Uttarakhand', 'West Bengal'),index=22,key="state_to_selectbox")
            
            Type=st.selectbox("**Please select values to Visualize**",('Transaction_count','Transaction_amount'))
            if Type == "Transaction_count":
                mycursor.execute(f"Select Transaction_type,sum(Transaction_count) as Total_count from table_trans where Year={Year} and Quarter ={Quarter} group by Transaction_type order by Transaction_type")
                df=pd.DataFrame(mycursor.fetchall(),columns=['Transaction_type','Total_count'])
                st.dataframe(df)
                fig=px.bar(df,
                           title="Transaction_type vs Total_count",
                           x="Transaction_type",
                           y="Total_count",
                           orientation="h",
                           color="Transaction_type",
                           color_continuous_scale=px.colors.sequential.Peach)
                st.plotly_chart(fig,use_container_width=True)
            if Type=="Transaction_amount":
                mycursor.execute(f"Select Transaction_type,sum(Transaction_amount) as Total_amount from table_trans where Year={Year} and Quarter={Quarter} group by Transaction_type order by Transaction_type")
                df=pd.DataFrame(mycursor.fetchall(),columns=['Transaction_type','Total_amount'])
                st.dataframe(df)
                fig=px.bar(df,
                           title="Transaction_type vs Total_amount",
                           x="Transaction_type",
                           y="Total_amount",
                           orientation='h',
                           color="Transaction_type",
                           color_continuous_scale=px.colors.sequential.Peach)
                st.plotly_chart(fig,use_container_width=True)

            Select1 = st.selectbox("Select one",["Transaction_count","Transaction_amount"])
            st.markdown(":violet[This Geomap is used to visualize state based data according to Transaction_count and Transaction_amount]")
            mycursor.execute(f"select States,sum(Transaction_count) as Total_count,sum(Transaction_amount) as Total_amount from table3 where Year={Year} and Quarter={Quarter} group by States order by States")
            df1=pd.DataFrame(mycursor.fetchall(),columns=["States","Total_count","Total_amount"])
            df2=pd.read_csv(r"C:\Users\Admin\Desktop\Project2\States.csv")
            df1.States=df2
            if Select1=="Transaction_count":
                fig1=px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
                                   featureidkey="properties.ST_NM",
                                   locations="States",
                                   color="Total_count",
                                   color_continuous_scale="Aggrnyl")
                fig1.update_geos(fitbounds="locations",visible=False)
                st.plotly_chart(fig1,use_container_width=True)
    
    if Type== "Users":
        st.markdown("## :violet[overall state data user app opening range]")
        mycursor.execute(f"Select States, sum(Registereduser) as Total_User,sum(Appopens) as Total_appopen from table4 where Year={Year} and Quarter={Quarter} group by States order by States")
        df1=pd.DataFrame(mycursor.fetchall(),columns=['States','Total_User','Total_appopen'])
        df2=pd.read_csv(r"C:\Users\Admin\Desktop\Project2\States.csv")
        df1.Total_appopen=df1.Total_appopen.astype(float)
        df1.States=df2
        fig=px.choropleth(df1,geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.",
                          featureidkey="properties.ST_NM",
                          locations="States",
                          color="Total_appopen",
                          color_continuous_scale="sunset")
        fig.update_geos(fitbounds="locations",visible=False)
        st.plotly_chart(fig,use_container_width=True)

        st.markdown("## :violet[Select any state to explore more]")
        selected_state=st.selectbox("**Please select state to visualize**",
                                   ('Andaman & Nicobar', 'Andhra Pradesh', 'Arunachal Pradesh',
                                        'Assam', 'Bihar', 'Chandigarh', 'Chhattisgarh',
                                        'Dadra and Nagar Haveli and Daman and Diu', 'Delhi', 'Goa',
                                        'Gujarat', 'Haryana', 'Himachal Pradesh', 'Jammu & Kashmir',
                                        'Jharkhand', 'Karnataka', 'Kerala', 'Ladakh', 'Lakshadweep',
                                        'Madhya Pradesh', 'Maharashtra', 'Manipur', 'Meghalaya', 'Mizoram',
                                        'Nagaland', 'Odisha', 'Puducherry', 'Punjab', 'Rajasthan',
                                        'Sikkim', 'Tamil Nadu', 'Telangana', 'Tripura', 'Uttar Pradesh',
                                        'Uttarakhand', 'West Bengal'),index=22,key="state_to_selectbox")
        mycursor.execute(f"Select States,Year,Quarter,Districts,sum(Registereduser) as Total_User, sum(Appopens) as Total_appopen from table4 where Year={Year} and Quarter={Quarter} and States='{selected_state}' group by States,Year,Quarter,Districts order by States,Districts")
        df=pd.DataFrame(mycursor.fetchall(),columns=["States","Year","Quarter","Districts","Total_User","Total_appopen"])
        df.Total_User=df.Total_User.astype(int)
        fig=px.bar(df,title="selected_state",
                   x="Districts",
                   y="Total_User",
                   orientation='v',
                   color="Total_User",
                   color_continuous_scale=px.colors.sequential.Agsunset)
        st.plotly_chart(fig,use_container_width=True)


                               

