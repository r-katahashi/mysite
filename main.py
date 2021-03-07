import streamlit as st
import time

st.title('Streamlit')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st. progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'    

left_column, right_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ')
expander2.write('問い合わせ2の回答')
expander3 = st.beta_expander('問い合わせ')
expander3.write('問い合わせ3の回答')

# text = option = st.text_input('あなたの趣味を教えて下さい。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味は、',text
# 'コンディション', condition

# if st.checkbox('Show Image'):
#     img = Image.open('189.png')
#     st.image(img, caption='189', use_column_width=True)
