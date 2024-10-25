# streamlit run chart_type.py --server.port 8506
import duckdb
import streamlit as st
import pandas as pd
import plotly.express as px
from lib.exception_handling import ExceptionHandling

def main():
    st.set_page_config(layout='wide')
    st.title('데이터 시각화 처리 응답속도')

    options = st.multiselect(
            "Select data for visualization",
            ["restaurant_2024", "restaurant_2023", "restaurant_2022", "restaurant_2021", "restaurant_2020"])

    if st.button('데이터 시각화 실행', use_container_width=True):    
        # 빈집
        try:
            ex = ExceptionHandling()
            conn = duckdb.connect('./data/restaurant/database.db')
            df = conn.execute(f'SELECT * FROM {options[0]}').df()

            conn.close()
        except IndexError:
            st.write('데이터를 선택해 주세요')

if __name__ == '__main__':
    main()