import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit超超超入門')
st.write('プログレスバーの表示')
'Start!!'

latest_interation = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_interation.text(f'Itaration {i+1}')
    bar.progress(i + 1)
    time.sleep(0.01)
    
'Done!'

left_column, righth_column = st.beta_columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
        righth_column.write('ここは右カラム')

expander1 = st.beta_expander('問い合わせ1')
expander1.write('問い合わせ1の回答')
expander2 = st.beta_expander('問い合わせ2')
expander2.write('問い合わせ2の回答')
expander3 = st.beta_expander('問い合わせ3')
expander3.write('問い合わせ3の回答')


# text = st.text_input('あなたの趣味を教えて下さい。')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味:', text
# 'あなたのコンディション', condition


# if st.checkbox('Show Image'):
#     img = Image.open('dokuringo.jpg')
#     st.image(img, caption='Toshi', use_column_width=True)


