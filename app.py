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
