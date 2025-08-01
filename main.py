import streamlit as st
st.title('Điền thông tin')
bar=st.progress(0)
quiz=['Họ và tên: ','Ngày sinh: ','Sở thích: ']
answers=[]
lenquiz=len(quiz)
for i in range(lenquiz):
    answer=st.text_input(quiz[i],'')
    if answer!='':
        answers.append(answer)
if st.button('Confirm'):
    if len(answers)==lenquiz:
        bar.progress(100)
        st.write('Đã hoàn thành thông tin!')
        st.balloons()
    else:
        bar.progress(len(answers)/lenquiz)
        st.write('Chưa hoàn thành đủ thông tin!')
for i in range(len(answers)):
    st.write(quiz[i], answers[i])    