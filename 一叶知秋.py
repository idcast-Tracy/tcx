# 打开网页，在cmd命令界面运行下面一段
# # streamlit run C:\Users\Tracy\Desktop\知识图谱2.0\知识图谱.py [ARGUMENTS]


import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os
import time
import base64
# os.chdir(r'C:\Users\Tracy\Desktop\知识图谱2.0') # 设定文件路径
# 设置页面配置
st.set_page_config(page_title="CX-copilot 1.0", page_icon="⭐", layout="wide")
# 通过 css样式隐藏主菜单和页脚
hide_menu = '''
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
'''
st.markdown(hide_menu,unsafe_allow_html=True)

def main_bg(main_bg):
    main_bg_ext = "back.png"
    st.markdown(
        f"""
         <style>
         .stApp {{
             background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()});
             background-size: cover
         }}
         </style>
         """,
        unsafe_allow_html=True
    )
# 调用
main_bg('back.png')

with st.sidebar:
    choose = option_menu("教师端", ["首页", "知识库补充" ,"课程管理", "学情评价","AI反馈","知识图谱"],
                         icons=['bar-chart', 'cloud-upload', 'person lines fill', 'app-indicator', "boombox-fill","list-task"],
                         menu_icon="list", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#dceef8"}, # 整体颜色
        "icon": {"color": "#0e427a", "font-size": "15px"}, # 图标颜色和大小设定
        "nav-link": {"font-size": "15px", "text-align": "left", "margin":"0px", "--hover-color": "#f1f1f2"}, # 图标旁文字大小和点击时颜色设定
        "nav-link-selected": {"background-color": "#4FC8DD"} # 点击后背景色
    })

## ==================================  数据监控与分析  ==========================================
if choose == "首页":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)

elif choose == "知识库补充":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)

elif choose == "课程管理":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)


elif choose == "学情评价":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)


elif choose == "AI反馈":
    with st.spinner('超星小助手正在努力加载中......'):
        time.sleep(1)

elif choose == "知识图谱":
    # with st.spinner('超星小助手正在努力加载中......'):
    #     time.sleep(1)
    # df = pd.DataFrame({'Subject': ['养生','侍奉死者','姑娘','楚文王','臣不阴','汤临川','蔡锷','少年','父母','阳','家庭','孙中山','家长制的专权','国','弟子','孔子','道理','张苍梧','凭父','凭时'],
    #                    'Relationship': ['不足以当','如同','要','意欲','则','非','策划','雄于','为','不阳','会失去','发动','损害','胜于','被','批评','刚柔交错','尝语','未解','年数'],
    #                    'Object': ['大事','侍奉生者','出嫁','强娶','国必乱','敌手','武力反袁','欧洲','刚','父母','动力','护法战争','家庭','欧洲','打板子','他','自然','凭父','所以','岁']})
    # edited_df = st.data_editor(df, num_rows="dynamic",height=700,width=350)
    col1, col2 = st.columns(2)



    with col1:
        with st.spinner('超星小助手正在努力加载中......'):
            time.sleep(1)
        df = pd.DataFrame({'主体': ['孔孟', '孔孟', '分工', '愚昧落后的民族', '臣不阴', '臣过阴', '父母', '子女', '合作与良性竞争', '心地宁静', '安稳不乱', '朋友之间的关系', '朋友之间的关系', '朋友之间的关系', '诚意正心', '格物致知', '止于至善', '日日新',
                                       '养生','侍奉死者','姑娘','楚文王','臣不阴','汤临川','蔡锷','少年','父母','阳','家庭','孙中山','家长制的专权','国','弟子','孔子','道理','张苍梧','凭父','凭时',
                                       '养生', '侍奉死者', '姑娘', '楚文王', '臣不阴', '汤临川', '蔡锷', '少年', '父母', '阳', '家庭', '孙中山', '家长制的专权', '国', '弟子', '孔子', '道理', '张苍梧', '凭父', '凭时',
                                       '养生', '侍奉死者', '姑娘', '楚文王', '臣不阴', '汤临川', '蔡锷', '少年', '父母', '阳', '家庭', '孙中山', '家长制的专权', '国', '弟子', '孔子', '道理', '张苍梧', '凭父', '凭时',
                                       '养生', '侍奉死者', '姑娘', '楚文王', '臣不阴', '汤临川', '蔡锷', '少年', '父母', '阳', '家庭', '孙中山', '家长制的专权', '国', '弟子', '孔子', '道理', '张苍梧', '凭父', '凭时',
                                       '养生', '侍奉死者', '姑娘', '楚文王', '臣不阴', '汤临川', '蔡锷', '少年', '父母', '阳', '家庭', '孙中山', '家长制的专权', '国', '弟子', '孔子', '道理', '张苍梧', '凭父', '凭时',
                                       '养生', '侍奉死者', '姑娘', '楚文王', '臣不阴', '汤临川', '蔡锷', '少年', '父母', '阳', '家庭', '孙中山', '家长制的专权', '国', '弟子', '孔子', '道理', '张苍梧', '凭父', '凭时'
                                       ],
                           '关系': ['认为','认为','是','是','则','则','为','为','能够促进','方能','方能','最恰当的','最恰当的','最恰当的','是','是','是','是',
        '不足以当','如同','要','意欲','则','非','策划','雄于','为','不阳','会失去','发动','损害','胜于','被','批评','刚柔交错','尝语','未解','年数',
                                            '不足以当', '如同', '要', '意欲', '则', '非', '策划', '雄于', '为', '不阳', '会失去', '发动', '损害', '胜于', '被', '批评', '刚柔交错', '尝语', '未解', '年数',
                                            '不足以当', '如同', '要', '意欲', '则', '非', '策划', '雄于', '为', '不阳', '会失去', '发动', '损害', '胜于', '被', '批评', '刚柔交错', '尝语', '未解', '年数',
                                            '不足以当', '如同', '要', '意欲', '则', '非', '策划', '雄于', '为', '不阳', '会失去', '发动', '损害', '胜于', '被', '批评', '刚柔交错', '尝语', '未解', '年数',
                                            '不足以当', '如同', '要', '意欲', '则', '非', '策划', '雄于', '为', '不阳', '会失去', '发动', '损害', '胜于', '被', '批评', '刚柔交错', '尝语', '未解', '年数',
                                            '不足以当', '如同', '要', '意欲', '则', '非', '策划', '雄于', '为', '不阳', '会失去', '发动', '损害', '胜于', '被', '批评', '刚柔交错', '尝语', '未解', '年数'
                                            ],
                           '客体': ['君与臣的关系是相对的','君臣各有职责','文明发展之必然','分工不明的','国必乱','国必危','刚','柔','人类进步','安稳不乱','思虑周详','相互坦诚','不过分亲昵','相互扶持而不依赖','必备的科研心态','认知的唯一途径','追求臻美境界','强烈的创新意识',
        '不足以当','如同','要','意欲','则','非','策划','雄于','为','不阳','会失去','发动','损害','胜于','被','批评','刚柔交错','尝语','未解','年数',
                                      '不足以当', '如同', '要', '意欲', '则', '非', '策划', '雄于', '为', '不阳', '会失去', '发动', '损害', '胜于', '被', '批评', '刚柔交错', '尝语', '未解', '年数',
                                      '不足以当', '如同', '要', '意欲', '则', '非', '策划', '雄于', '为', '不阳', '会失去', '发动', '损害', '胜于', '被', '批评', '刚柔交错', '尝语', '未解', '年数',
                                      '不足以当', '如同', '要', '意欲', '则', '非', '策划', '雄于', '为', '不阳', '会失去', '发动', '损害', '胜于', '被', '批评', '刚柔交错', '尝语', '未解', '年数',
                                      '不足以当', '如同', '要', '意欲', '则', '非', '策划', '雄于', '为', '不阳', '会失去', '发动', '损害', '胜于', '被', '批评', '刚柔交错', '尝语', '未解', '年数',
                                      '不足以当', '如同', '要', '意欲', '则', '非', '策划', '雄于', '为', '不阳', '会失去', '发动', '损害', '胜于', '被', '批评', '刚柔交错', '尝语', '未解', '年数'
                                      ]})
        edited_df = st.data_editor(df, num_rows="dynamic",height=700,width=350)

    with col2:
        with st.spinner('知识图谱正在努力更新中......'):
            time.sleep(1)
