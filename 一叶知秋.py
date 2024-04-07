# 打开网页，在cmd命令界面运行下面一段
# # streamlit run C:\Users\Tracy\Desktop\2024Winter\科研\04.07Python-oneleaf\一叶知秋.py [ARGUMENTS]

import streamlit as st
from streamlit_option_menu import option_menu
from PIL import Image
import pandas as pd
import numpy as np
import plotly.express as px
import os
import time
import datetime
# os.chdir(r'C:\Users\Tracy\Desktop\2024Winter\科研\04.07Python-oneleaf') # 设定文件路径
# 设置页面配置
st.set_page_config(page_title="CX-copilot 1.0", page_icon="⭐", layout="wide")
# 通过 css样式隐藏主菜单和页脚
hide_menu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(hide_menu,unsafe_allow_html=True)
# st.balloons()


with st.sidebar:
    choose = option_menu("教师端", ["首页", "课程管理", "学情评价","AI反馈"],
                         icons=['cloud-upload', 'person lines fill', 'app-indicator', "boombox-fill"],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#dceef8"}, # 整体颜色
        "icon": {"color": "#0e427a", "font-size": "15px"}, # 图标颜色和大小设定
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#f1f1f2"}, # 图标旁文字大小和点击时颜色设定
        "nav-link-selected": {"background-color": "#4FC8DD"} # 点击后背景色
    })

## ==================================  数据监控与分析  ==========================================
if choose == "首页":
    latest_iteration1 = st.empty() ##  显示进度
    bar1 = st.progress(0)
    for i in range(100): # Update the progress bar with each iteration.
        latest_iteration1.text(f'加载进度 {i + 1} %')
        bar1.progress(i + 1)
        time.sleep(0.01)
    st.success('1')

elif choose == "课程管理":
    latest_iteration1 = st.empty() ##  显示进度
    bar1 = st.progress(0)
    for i in range(100): # Update the progress bar with each iteration.
        latest_iteration1.text(f'加载进度 {i + 1} %')
        bar1.progress(i + 1)
        time.sleep(0.01)
    st.success('1')


elif choose == "学情评价":
    latest_iteration1 = st.empty() ##  显示进度
    bar1 = st.progress(0)
    for i in range(100): # Update the progress bar with each iteration.
        latest_iteration1.text(f'加载进度 {i + 1} %')
        bar1.progress(i + 1)
        time.sleep(0.01)
    st.success('1')


elif choose == "AI反馈":
    latest_iteration1 = st.empty() ##  显示进度
    bar1 = st.progress(0)
    for i in range(100): # Update the progress bar with each iteration.
        latest_iteration1.text(f'加载进度 {i + 1} %')
        bar1.progress(i + 1)
        time.sleep(0.01)
    st.success('1')




