import streamlit as st
from PIL import Image
import os

# --- 設定網頁標題與版面 ---
st.set_page_config(
    page_title="Nelly Chen's Portfolio",
    page_icon="💼",
    layout="wide"
)

# --- CSS 樣式優化 (讓文字排版更易讀) ---
st.markdown("""
<style>
    .big-font { font-size:20px !important; font-weight: 500;}
    .metric-card { background-color: #f0f2f6; padding: 15px; border-radius: 10px; border-left: 5px solid #FF4B4B;}
</style>
""", unsafe_allow_html=True)

# --- 側邊欄：個人檔案 ---
with st.sidebar:
    # 如果妳有大頭照，可以存成 profile.jpg 放在同目錄，並把下面這行解開註解
    # st.image("profile.jpg", width=150)
    
    st.title("陳俞寧 (Nelly)")
    st.write("📍 Taipei, Taiwan")
    st.caption("29歲 | 5年數位行銷經驗")
    
    st.divider()
    st.write("### 核心專長")
    st.markdown("""
    - **LINE OA 經營與規劃**
    - **社群行銷 (Social Media)**
    - **IMC 整合行銷傳播**
    - **數據成效分析**
    """)
    
    st.divider()
    st.write("📧 nellylemon0317@gmail.com")
    # st.write("📞 0988-569-145") # 視需求決定是否放電話

# --- 主頁面開始 ---

# 1. 簡介與工作經歷 (置頂)
st.title("Hi, I'm Nelly Chen ✨")
st.subheader("專精於社群與 LINE OA 規劃的資深行銷企劃")
st.write("擁有 5 年數位行銷經驗，擅長將創意結合數據，為品牌創造實際的商業價值。")

st.markdown("---")

st.header("📝 工作經歷 Work Experience")

# 使用兩欄佈局讓經歷看起來更清楚
col_exp1, col_exp2 = st.columns([1, 2])

with col_exp1:
    st.subheader("2023 - 2025")
    st.markdown("**網路基因資訊**")
    st.caption("Senior Account Executive")

with col_exp2:
    st.write("""
    * **LINE 行銷專家**：主導規劃與執行 LINE 行銷活動與 IMC 整合傳播案。
    * **品牌比稿**：參與航空、酒商、運動品牌等多項比稿，具備高強度的提案能力。
    * **代表客戶**：Nestle (克寧)、New Balance、The North Face 等。
    """)

st.divider()

col_exp3, col_exp4 = st.columns([1, 2])

with col_exp3:
    st.subheader("2020 - 2023")
    st.markdown("**偉門智威廣告**")
    st.caption("Social Media Planner")

with col_exp4:
    st.write("""
    * **社群內容策略**：規劃與執行車商 (NISSAN) 等品牌社群行銷活動。
    * **視覺創意統籌**：負責平面拍攝需求規劃，確保視覺產出符合品牌調性。
    * **病毒式擴散**：設計心理測驗互動，曾創造高分享率與聲量。
    """)

st.markdown("---")

# 2. 精選專案作品 (Project Highlights)
st.header("🏆 精選專案 Case Studies")
st.write("以下精選幾個具代表性的操作案例，涵蓋 LINE 互動、OMO 整合與銷售導購。")

# 定義一個函數來顯示專案，這樣程式碼比較整潔
def show_project(title, tags, description, metrics_dict, image_path=None):
    with st.container():
        st.subheader(f"📌 {title}")
        st.write(tags)
        
        c1, c2 = st.columns([1.5, 1]) # 左邊寬一點放圖或詳細文，右邊放數據
        
        with c1:
            st.markdown(f"**專案內容：**\n{description}")
            if image_path:
                try:
                    # 嘗試讀取圖片，如果找不到就顯示提示
                    st.image(image_path, caption=f"{title} 視覺呈現", use_column_width=True)
                except:
                    st.warning(f"請放入圖片檔案: {image_path}")
            else:
                st.info("💡 (此處可放入專案截圖，請將圖片上傳至資料夾並命名)")

        with c2:
            st.markdown('<div class="metric-card"><b>📊 專案成效</b></div>', unsafe_allow_html=True)
            for k, v in metrics_dict.items():
                st.metric(label=k, value=v)
        
        st.divider()

# --- 專案 1: CAFE!N x DUREX ---
show_project(
    title="CAFE!N x DUREX - LINE MGM Campaign",
    tags="`LINE行銷` `跨界聯名` `MGM機制`",
    description="""
    藉由聯名話題及獎項誘因帶動 LINE 新好友數。透過精準的誘因設計（MGM），
    鼓勵使用者分享給好友。
    """,
    metrics_dict={
        "新好友增加": "+9,716 人",
        "活動參與人數": "11,000+ 人",
        "成效": "品牌近期最佳操作"
    },
    image_path="project1.png" # 妳之後要把截圖命名為 project1.png
)

# --- 專案 2: NEW BALANCE CNY ---
show_project(
    title="NEW BALANCE CNY - 穿上NB「翻」走春趣",
    tags="`OMO整合` `節慶行銷` `互動遊戲`",
    description="""
    結合農曆年節氣氛，發展「翻牌」互動遊戲。運用 OMO 操作，
    除了線上賺取購物金，還能引導至門市印製春聯，成功串聯線上線下流量。
    """,
    metrics_dict={
        "遊戲參與人數": "61,000+ 人",
        "新好友增加": "+28,000+ 人",
        "轉換": "高購物金領取率"
    },
    image_path="project2.png"
)

# --- 專案 3: THE NORTH FACE ---
show_project(
    title="THE NORTH FACE - AI 撩山林",
    tags="`AI科技應用` `聊天機器人` `品牌互動`",
    description="""
    融合 AI 科技，發展「與山林對話」的概念。
    透過線上聊天室讓使用者與「山神」對話，呼籲民眾回歸山林，提升品牌好感度。
    """,
    metrics_dict={
        "新好友增加": "+36,000+ 人",
        "活動參與人數": "33,000+ 人",
        "互動親密度": "100% 達成"
    },
    image_path="project3.png"
)

# --- 專案 4: NESTLE KLIM CNY ---
show_project(
    title="NESTLE KLIM CNY - 登錄發票雙重抽",
    tags="`銷售導購` `發票登錄` `促銷活動`",
    description="""
    藉由「立即抽」與加碼「事後抽萬元大獎」雙重機制，
    強化消費者購買指定商品的意願，促進多單品項購買（Basket Size）。
    """,
    metrics_dict={
        "平均登錄發票": "2.1 次/人",
        "獎項": "iPhone / 萬元家電",
    },
    image_path="project4.png"
)

# --- 專案 5: NISSAN X-TRAIL ---
show_project(
    title="NISSAN X-TRAIL - 心理測驗病毒行銷",
    tags="`社群擴散` `心理測驗` `產品上市`",
    description="""
    藉由心理測驗結合車款 USP (獨特賣點)，加上分享誘因，
    促進用戶主動分享給好友，創造聲量並間接帶來預約試乘率。
    """,
    metrics_dict={
        "分享率": "96%",
        "參加人數": "5,847 人",
    },
    image_path="project5.png"
)

# --- 頁尾 ---
st.write("© 2026 Nelly Chen. Portfolio created with Python & Streamlit.")
