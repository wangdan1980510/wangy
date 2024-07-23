'''我的主页'''
import streamlit as st
from PIL import Image
import wordcloud
import matplotlib.pyplot as plt
import base64
import streamlit as st

def bar_bg(img):
    last = 'png'
    st.markdown(
        f"""
        <style>
        [data-testid='stSidebar'] > div:first-child {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )

def page_bg(img):
    last = 'png'
    st.markdown(
        f"""
        <style>
        .stApp {{
            background: url(data:img/{last};base64,{base64.b64encode(open(img, 'rb').read()).decode()});
            background-size: cover
        }}
        </style>
        """,
        unsafe_allow_html = True,
    )


page = st.sidebar.radio('江北联校潮汐终端', ['联校官方推荐', '图片处理工具', '资料查询终端', '终端留言区','江北联校阅读','世界地图'])
def img_change(img,rc,gc,bc):
            width,height=img.size
            img_array=img.load()
            for x in range(width):
                for y in range(height):
                    r=img_array[x,y][rc]
                    g=img_array[x,y][gc]
                    b=img_array[x,y][bc]
                    img_array[x,y]=(r,g,b)
            return img
def ciyvn(str):
    w=wordcloud.WordCloud(font_path='fangzheng.TTF',background_color='white',max_words=2000,width=2000,height=2000)
    w.generate(str)
    w.to_file('shortstory.png')
    img = Image.open('shortstory.png')
    return img
def page_1():
    '''联校官方推荐'''
    with open('主页面.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('2024-07-17 191848.png')
    st.write('联校官方动漫推荐')
    st.write(':orange[(十分推荐)]')
    st.write('《物理魔法使马修》    《孤独摇滚》    《时光代理人》')
    st.write(':orange[(推荐)]')
    st.write('《罗小黑战记》    《凹凸世界》')
    st.write('-----------------------------')
    st.write('联校官方游戏推荐')
    st.write(':orange[(十分推荐)]')
    st.write('《脑叶公司》    《Minecraft（我的世界）')
    st.write(':orange[(推荐)]')
    st.write('《赛博朋克2077》    《原子之心》')
    st.write('-----------------------------')
    st.write('联校官方书籍推荐')
    st.write(':orange[(十分推荐)]')
    st.write('《江北联校》')
    st.write(':orange[(推荐)]')
    st.write('《记忆传授人》    《历史刺绣人》    《森林送信人》')
    st.write('-----------------------------')
    st.write('联校官方习题集推荐')
    st.write(':orange[(你居然想内卷？！！？没门！好好听老师上课！)]')
    st.write('-----------------------------')

def page_2():
    '''图片处理工具'''
    with open('选题.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('2024-07-17 191848.png')
    st.write(':orange[图片改色小工具]')
    st.write('-----------------------------')
    uploaded_file=st.file_uploader('上传图片',type=['png','jpg','jpeg'])
    if uploaded_file:
        file_name=uploaded_file.name
        file_type=uploaded_file.type
        file_size=uploaded_file.size
        img=Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5,tab6,tab7,tab8,tab9,tab10 = st.tabs(['原色','改色1','改色2','改色3','改色4','改色5','改色6','改色7','改色8','改色9'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img,0,2,1))
        with tab3:
            st.image(img_change(img,1,2,0))
        with tab4:
            st.image(img_change(img,1,0,2))
        with tab5:
            st.image(img_change(img,0,2,1))
        with tab6:
            st.image(img_change(img,1,2,0))
        with tab7:
            st.image(img_change(img,1,0,2))
        with tab8:
            st.image(img_change(img,1,2,0))
        with tab9:
            st.image(img_change(img,1,0,2))
        with tab10:
            st.image(img_change(img,1,0,2))
    else:
        pass
    st.write('-----------------------------')
    st.write(':orange[词云生成小工具]')
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        # 将上传的文件转换成文本
        string_data = uploaded_file.read().decode("utf-8")
        st.image(ciyvn(string_data))
    else:
        pass

def page_3():
    '''资料查询终端'''
    with open('答题.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('2024-07-17 191848.png')
    
    st.write('智慧词典')
    with open('words_space.txt','r',encoding='utf-8')as f:
        words_list=f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i]=words_list[i].split('#')
    words_dict={}
    for i in words_list:
        words_dict[i[1]]=[int(i[0]),i[2]]
    with open('check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word=st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word][1])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        if word=='python':
            st.code('''
                   #恭喜你触发彩蛋，这里有一条秘密咒语
                   print('hello world')
                   #快把他输入到海龟编辑器里叭！''')
        if word=='snow':
            st.snow()
        if word=='birthday':
            st.balloons()
        if word=='balloon':
            st.balloons()
def page_4():
    '''终端留言区'''
    with open('选题.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('2024-07-17 191848.png')
    # 从文件中加载内容，并处理成列表
    with open('leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '宣雨':
            with st.chat_message('✨'):
                st.write(i[1],':',i[2])
        elif i[1] == '叶然':
            with st.chat_message('🍥'):
                st.write(i[1],':',i[2])
        elif i[1] == '罗萧':
            with st.chat_message('🌕'):
                st.write(i[1],':',i[2])
        elif i[1] == '诗岚':
            with st.chat_message('🌠'):
                st.write(i[1],':',i[2])
        elif i[1] == '叶铭':
            with st.chat_message('🍖'):
                st.write(i[1],':',i[2])
        elif i[1] == '叶明':
            with st.chat_message('🍉'):
                st.write(i[1],':',i[2])
        elif i[1] == '兰伊':
            with st.chat_message('🍜'):
                st.write(i[1],':',i[2])
        elif i[1] == '李家千金':
            with st.chat_message('🍣'):
                st.write(i[1],':',i[2])
        elif i[1] == '德斯':
            with st.chat_message('🍶'):
                st.write(i[1],':',i[2])
    name = st.selectbox('我是……', ['宣雨', '叶然','罗萧','诗岚','叶铭','叶明','兰伊','李家千金','德斯'])
    new_message = st.text_input('想要说的话……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    
def page_5():
    with open('选题.mp3', 'rb') as f:
        mymp3 = f.read()
    st.audio(mymp3, format='audio/mp3', start_time=0)
    st.image('2024-07-17 191848.png')
    with open('江北.txt', 'r',encoding='utf-8') as file:
            content = file.read()
    st.write(content)

def page_6():
    data = {
        'latitude': [113.321775, 28.174687, 40.7128],
        'longitude': [-122.4194, -118.2437, -74.0060],
        'name': ['San Francisco', 'Los Angeles', 'New York']
    }
     
    st.map(data, zoom=4, use_container_width=True)
    
if page == '联校官方推荐':
    page_1()
    bar_bg('bg.png')
    page_bg('cbg.png')
elif page == '图片处理工具':
    page_2()
    bar_bg('bg.png')
    page_bg('cbg.png')
elif page == '资料查询终端':
    page_3()
    bar_bg('bg.png')
    page_bg('cbg.png')
elif page == '终端留言区':
    page_4()
    bar_bg('bg.png')
    page_bg('cbg.png')
elif page == '江北联校阅读':
    page_5()
    bar_bg('bg.png')
    page_bg('cbg.png')
elif page=='世界地图':
    page_6()
    bar_bg('bg.png')
    page_bg('cbg.png')