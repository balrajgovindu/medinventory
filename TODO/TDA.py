import streamlit as st

import pandas as pd

from TDA1 import create_table,add_data,view_all_data,view_unique_tasks,get_task,edit_task_data,delete_data

def main():
    st.title('TODO APP')
    menu=['Create','Read','Update','Delete','About']
    choice=st.sidebar.selectbox('Menu',menu)

    create_table()
    if choice=='Create':
        st.subheader('ADD ITEMS')

        col1,col2=st.columns(2)

        with col1:
            task=st.text_area('Task To Do')

        with col2:
            task_status=st.selectbox('Status',['ToDO','Doing','Done'])
            task_due_date=st.date_input('Due Date')

        if st.button('Add Task'):
            add_data(task,task_status,task_due_date)
            st.success('Successfullly added data:{}'.format(task))

        elif choice=='Read':
            st.subheader('VIEW ITEMS')
            result=view_all_data()
            st.write(result)
            df=pd.DataFrame(result,columns=['Task','Status','Due Date'])
            with st.expander('View All Data'):
                st.dataframe(df)

            with st.expander('Task Status'):
              task_df=df['Status'].value_counts().to_frame()
              task_df=task_df.reset_in
              st.dataframe(task_df)

        elif choice=='Update':
            st.subheader('Edit/Update Items')
            result=view_all_data()
            st.write(result)
            df=pd.DataFrame(result,columns=['Task','Status','Due Date'])
            with st.expander('Current Data'):
                st.dataframe(df)
            st.write('view_unique_tasks()')
            list_of_task=[i[0] for i in view_unique_tasks()]
            st.write(list_of_task)

            selected_task=st.selectbox('Task to Edit',list_of_task)
            selected_result=get_task(selected_task)
            st.write(selected_result)

            if selected_result:
              task = selected_result[0][0]
              task_status = selected_result[0][1]
              task_due_date = selected_result[0][2]

            with col1:
                new_task = st.text_area('Task To Do',task)

            with col2:
                new_task_status = st.selectbox('task_Status', ['ToDO', 'Doing', 'Done'])
                new_task_due_date = st.date_input('Task_Due_Date')

            if st.button('Update Task'):
                edit_task_data(new_task, new_task_status, new_task_due_date,task,task_status,task_due_date)
                st.success('Successfullly Updated ::{} TO :: {}'.format(task,new_task))
                result2=view_all_data()
                df2=pd.DataFrame(result2,columns=['Task','Status','Due date'])
                with st.expander('Update Data'):
                    st.dataframe(df2)

            elif choice=='Delete':
                st.subheader('Delete Items')
                result = view_all_data()
                df = pd.DataFrame(result, columns=['Task', 'Status', 'Due date'])
                with st.expander('Current Data'):
                    st.dataframe(df)

                list_of_task=[i[0] for i in view_unique_tasks()]
                st.write(list_of_task)

                selected_task=st.selectbox('Task to Delete',list_of_task)
                st.warning('Do You Want to Delete {}'.format(selected_task))
                if st.button('Delete Task'):
                    delete_data(selected_task)
                    st.success('Task has been successfully deleted')

            else:
                st.subheader('About')






if __name__ =='__main__':
    main()