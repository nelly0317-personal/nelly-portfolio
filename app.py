import streamlit as st

# --- 1. 全域設定 (Page Config) ---
st.set_page_config(
    page_title="Nelly Chen | Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed" # 預設收起側邊欄，讓視覺更寬廣
)

# --- 2. 高質感 CSS 樣式 (這是讓網頁變美的關鍵) ---
st.markdown("""
<style>
    /* 引入 Google Fonts: Playfair Display (標題用，優雅) + Noto Sans TC (內文用，易讀) */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;700&family=Playfair+Display:wght@600&display=swap');

    /* 全局字體設定 */
    html, body, [class*="css"] {
        font-family: 'Noto Sans TC', sans-serif;
        color: #2c3e50;
        background-color: #fdfdfd; /* 極致灰白底，不刺眼 */
    }

    /* 標題專用字體 */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif; 
        color: #1e272e;
        margin-bottom: 0.5rem;
    }

    /* 強調文字顏色 */
    .highlight {
        color: #c0392b; /* 質感紅，呼應妳作品集裡的 NB 紅 */
        font-weight: bold;
    }

    /* 專案卡片容器 */
    .project-container {
        background-color: white;
        padding: 30px;
        border-radius: 12px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.05); /* 柔和陰影 */
        margin-bottom: 40px;
        border-left: 5px solid #2c3e50;
        transition: transform 0.3s;
    }
    .project-container:hover {
        transform: translateY(-5px); /* 滑鼠移過去會微微浮起 */
    }

    /* 標籤樣式 */
    .tag-badge {
        display: inline-block;
        padding: 5px 12px;
        margin-right: 8px;
        background-color: #f1f2f6;
        color: #57606f;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
    }

    /* 時間軸樣式 */
    .timeline-date {
        font-family: 'Playfair Display', serif;
        font-size: 1.5rem;
        color: #7f8c8d;
        text-align: right;
        padding-right: 20px;
        border-right: 2px solid #dfe6e9;
    }
    .timeline-content {
        padding-left: 20px;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. 頁首 Hero Section ---
col_hero1, col_hero2 = st.columns([2, 1])
with col_hero1:
    st.title("Nelly Chen.")
    st.markdown("### Digital Marketing Specialist")
    st.write("我是陳俞寧，具備5年數位行銷經驗。")
    
    # 社交按鈕區
    st.markdown("""
    <div style="margin-top: 20px;">
        <a href="mailto:nellylemon0317@gmail.com" style="text-decoration:none; color:#2c3e50; border:1px solid #2c3e50; padding:8px 16px; border-radius:30px; margin-right:10px;">📩 Contact Me</a>
        <span style="color:#b2bec3;">|</span> &nbsp; Taipei, Taiwan
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 4. 工作經歷 (Work Experience) - 雜誌時間軸風格 ---
st.header("01. Work Experience")
st.markdown("<br>", unsafe_allow_html=True) # 增加一點呼吸空間

# 經歷 1
c1, c2 = st.columns([1, 4])
with c1:
    st.markdown('<div class="timeline-date">2023<br>|<br>2025</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="timeline-content">', unsafe_allow_html=True)
    st.subheader("Senior Account Executive")
    [cite_start]st.markdown("**網路基因公司** [cite: 16]")
    st.markdown("""
    * **LINE 行銷專家**：主導規劃與執行 LINE 行銷與 IMC 整合活動，熟悉 API 串接與數據追蹤。
    * **品牌比稿提案**：參與航空、酒商、運動品牌比稿，具備從 0 到 1 的策略規劃能力。
    * [cite_start]**關鍵成效**：操作 Nestle Klim CNY 案，透過雙重抽獎機制，大幅提升發票登錄率 [cite: 76, 88]。
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 經歷 2
c3, c4 = st.columns([1, 4])
with c3:
    st.markdown('<div class="timeline-date">2020<br>|<br>2023</div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="timeline-content">', unsafe_allow_html=True)
    st.subheader("Social Media Planner")
    [cite_start]st.markdown("**偉門智威廣告公司** [cite: 22]")
    st.markdown("""
    * [cite_start]**社群內容策略**：負責 NISSAN 等車商客戶，將生硬規格轉化為消費者有感的內容 [cite: 113]。
    * **視覺創意統籌**：規劃平面拍攝需求，確保素材品質符合品牌高標準。
    * [cite_start]**病毒式擴散**：設計心理測驗互動，創造 **96% 分享率** 與 **5,800+ 參與人數** [cite: 123, 124]。
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- 5. 精選專案 (Selected Projects) - 雜誌圖文版面 ---
st.header("02. Selected Projects")
st.write("精選具代表性的 OMO 整合、LINE 經營與社群擴散案例。")
st.markdown("<br>", unsafe_allow_html=True)

# 定義專案顯示函數 (讓版面整齊劃一)
def project_layout(title, role, tags, content, metrics, image_placeholder_text, color_code):
    st.markdown(f'<div class="project-container" style="border-left-color: {color_code};">', unsafe_allow_html=True)
    
    # 標題區
    p1, p2 = st.columns([3, 1])
    with p1:
        st.subheader(title)
        st.markdown(f"**{role}**")
        # 顯示標籤
        tag_html = "".join([f'<span class="tag-badge">{t}</span>' for t in tags])
        st.markdown(tag_html, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 15px 0; border-top: 1px solid #eee;'>", unsafe_allow_html=True)

    # 內容區 (左圖右文)
    img_col, text_col = st.columns([1.5, 2])
    
    with img_col:
        # 這裡製作一個 "看起來像圖" 的色塊，直到妳放上真圖
        st.markdown(f"""
        <div style="
            background-color: {color_code}15; 
            border: 2px dashed {color_code}; 
            border-radius: 8px; 
            height: 200px; 
            display: flex; 
            align-items: center; 
            justify-content: center; 
            color: {color_code}; 
            text-align: center;
            font-weight: bold;
        ">
            {image_placeholder_text}<br><span style="font-size:0.8rem; font-weight:normal">(建議此處放 PDF 截圖)</span>
        </div>
        """, unsafe_allow_html=True)
        # 未來有圖時，把上面這段刪掉，換成 st.image("filename.png")

    with text_col:
        st.markdown("#### 📝 專案洞察")
        st.write(content)
        
        st.markdown("#### 📊 關鍵成效")
        # 使用 Streamlit 原生 Metrics 但排成一列
        m1, m2, m3 = st.columns(3)
        with m1:
            st.metric(label=metrics[0][0], value=metrics[0][1])
        with m2:
            st.metric(label=metrics[1][0], value=metrics[1][1])
        if len(metrics) > 2:
            with m3:
                st.metric(label=metrics[2][0], value=metrics[2][1])

    st.markdown('</div>', unsafe_allow_html=True)


# --- 專案 1: New Balance (紅色系) ---
project_layout(
    title="New Balance CNY - 穿上NB「翻」走春趣",
    role="Project Manager / Planner",
    tags=["LINE OA", "OMO 整合", "互動遊戲"],
    [cite_start]content="結合農曆年節氣氛，發展「翻牌」互動遊戲。運用 OMO 操作，除賺取購物金外，還能引導消費者前往門市印製實體春聯，成功將線上流量導流至線下 [cite: 61]。",
    metrics=[("參與人數", "61,000+"), ("新好友數", "+28,000"), ("轉換", "高領券率")],
    image_placeholder_text="📸 請截圖 PDF 第 6 頁<br>紅色新年主視覺",
    color_code="#e55039" # 紅色
)

# --- 專案 2: The North Face (綠色系) ---
project_layout(
    title="The North Face - AI 撩山林",
    role="Digital Planner",
    tags=["AI Chatbot", "品牌互動", "Tech"],
    [cite_start]content="融合 AI 科技，發展與山林對話的概念。透過線上聊天室與「山神」對話，呼籲民眾回歸山林。透過感性溝通，成功提升品牌好感度與黏著度 [cite: 129]。",
    metrics=[("新好友數", "+36,000"), ("互動親密度", "100%"), ("參與人數", "33K+")],
    image_placeholder_text="📸 請截圖 PDF 第 9 頁<br>綠色山林 AI 對話圖",
    color_code="#27ae60" # 綠色
)

# --- 專案 3: CAFE!N x DUREX (深藍色系) ---
project_layout(
    title="CAFE!N x DUREX - LINE MGM Campaign",
    role="Planner",
    tags=["MGM 機制", "跨界聯名", "會員增長"],
    [cite_start]content="藉由強強聯名話題及獎項誘因，帶動 LINE 新好友數。設計 MGM (Member Get Member) 機制，於短短一個月內創造驚人擴散效益 [cite: 31]。",
    metrics=[("新好友數", "+9,716"), ("參與人數", "11,000+")],
    image_placeholder_text="📸 請截圖 PDF 第 5 頁<br>聯名咖啡與保險套圖",
    color_code="#2f3542" # 深藍色
)

# --- 頁尾 ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #b2bec3; font-size: 0.8rem;">
    © 2026 Nelly Chen Portfolio. <br>
    Designed with Python (Streamlit) & Marketing Mindset.
</div>
""", unsafe_allow_html=True)
