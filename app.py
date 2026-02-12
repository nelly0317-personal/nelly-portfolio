import streamlit as st
import pandas as pd
import altair as alt

# 1. 頁面基礎設定
st.set_page_config(
    page_title="Nelly Chen | Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. 注入 CSS (這是讓網頁變漂亮的魔法)
st.markdown("""
<style>
    /* 引入 Google 字體：思源黑體 */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;500;700&display=swap');
    
    /* 全站字體設定 */
    html, body, [class*="css"] {
        font-family: 'Noto Sans TC', sans-serif;
        color: #424242;
    }
    
    /* 標題樣式 */
    h1, h2, h3 {
        color: #2C3E50;
        font-weight: 700;
    }
    
    /* 專案卡片樣式 (無圖片也能很美) */
    .project-card {
        background-color: #ffffff;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05);
        border-left: 6px solid #6C5CE7; /* 紫色系 */
        margin-bottom: 25px;
    }
    
    .metric-box {
        background-color: #F0F2F6;
        padding: 10px;
        border-radius: 8px;
        text-align: center;
    }
    
    .tag {
        display: inline-block;
        background-color: #dfe6e9;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 14px;
        margin-right: 5px;
        color: #2d3436;
    }
</style>
""", unsafe_allow_html=True)

# --- 側邊欄：簡潔有力的個人檔案 ---
with st.sidebar:
    st.markdown("## 👩‍💻 Nelly Chen")
    st.markdown("**陳俞寧**")
    st.caption("Taipei, Taiwan")
    
    st.markdown("---")
    
    st.success("✨ **求職狀態：** Open to Work")
    st.info("🎯 **目標職缺：** 資深數位行銷 / 社群經理")
    
    st.markdown("### 🛠 Tech Stack")
    # 用進度條展示技能，比文字更有感覺
    st.write("LINE OA & Social Marketing")
    st.progress(0.95)
    st.write("Data Analysis (GA4)")
    st.progress(0.80)
    st.write("Python & AI Tools")
    st.progress(0.40)

# --- 主頁面 ---

# Header 區域
st.title("用數據驅動創意的行銷人 🚀")
st.markdown("##### 擁有 5 年經驗，專精於社群經營、LINE OA 規劃與 OMO 整合行銷。")
st.markdown("我擅長不僅僅是發想創意，更懂得運用數據（如您所見，這個網頁是用 Python 建置的）來驗證與優化成效。")

st.markdown("---")

# 第一部分：工作經歷 (使用時間軸概念)
st.header("📌 工作經歷 Experience")

col1, col2 = st.columns([1, 3])

with col1:
    st.markdown("### 2023 - 2025")
    st.caption("2 年")
with col2:
    st.markdown("#### ✦ Senior Account Executive | 網路基因資訊")
    st.markdown("""
    - **LINE 行銷專家**：主導 Nestle、The North Face 等品牌的 LINE OA 經營與活動規劃。
    - **成效突破**：曾操作單檔活動創造 3.6 萬新好友，互動率達 100%。
    - **跨部門協作**：與工程、設計團隊緊密合作，執行複雜的 API 串接活動。
    """)

st.divider()

col3, col4 = st.columns([1, 3])

with col3:
    st.markdown("### 2020 - 2023")
    st.caption("3 年")
with col4:
    st.markdown("#### ✦ Social Media Planner | 偉門智威廣告")
    st.markdown("""
    - **社群內容策略**：負責 NISSAN 等汽車品牌社群維運，擅長轉化生硬規格為有趣內容。
    - **病毒式行銷**：設計「心理測驗」互動，創造 96% 的超高分享率。
    - **視覺統籌**：規劃平面拍攝，確保品牌視覺一致性。
    """)

st.markdown("---")

# 第二部分：精選專案 (無圖，但用 CSS 卡片和圖表來呈現)
st.header("🏆 精選專案 Highlights")
st.markdown("運用 Python 將過去專案的成效數據視覺化呈現：")

# --- 定義一個畫圖表的函數 (讓程式碼更簡潔) ---
def make_chart(data_dict, title):
    df = pd.DataFrame(list(data_dict.items()), columns=['Metric', 'Value'])
    chart = alt.Chart(df).mark_bar(cornerRadiusTopLeft=10, cornerRadiusTopRight=10).encode(
        x=alt.X('Metric', axis=None),
        y=alt.Y('Value', title='人數/次數'),
        color=alt.Color('Metric', legend=None, scale=alt.Scale(scheme='pastel1')),
        tooltip=['Metric', 'Value']
    ).properties(
        title=title,
        height=200
    )
    return chart

# 專案 1: NEW BALANCE
st.markdown('<div class="project-card">', unsafe_allow_html=True)
c1, c2 = st.columns([1.5, 1])
with c1:
    st.markdown("### 👟 NEW BALANCE CNY Campaign")
    st.markdown('<span class="tag">LINE OA</span> <span class="tag">OMO</span> <span class="tag">互動遊戲</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    **專案挑戰：** 農曆新年期間，如何透過線上互動帶動線下門市人流？
    
    **解決方案：**
    設計「翻牌」互動遊戲，使用者在 LINE 上玩遊戲賺購物金，並引導至門市印製實體春聯。
    
    **關鍵成果：**
    成功串聯 OMO，單月創造 **6 萬人** 參與互動。
    """)
with c2:
    # 這裡直接用 Python 畫圖，不用截圖
    chart_data = {"新好友 (+28K)": 28000, "總參與人數 (61K)": 61000}
    st.altair_chart(make_chart(chart_data, "活動流量漏斗"), use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)


# 專案 2: THE NORTH FACE
st.markdown('<div class="project-card" style="border-left-color: #00b894;">', unsafe_allow_html=True)
c3, c4 = st.columns([1.5, 1])
with c3:
    st.markdown("### 🏔️ The North Face AI 撩山林")
    st.markdown('<span class="tag">AI Chatbot</span> <span class="tag">品牌互動</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    **專案挑戰：** 如何利用 AI 話題，讓消費者重新對戶外活動產生興趣？
    
    **解決方案：**
    結合 AI 技術，打造「與山神對話」的聊天室體驗，透過感性溝通呼籲回歸山林。
    
    **關鍵成果：**
    高達 **100%** 的互動親密度，成功吸引 3.6 萬名新好友加入。
    """)
with c4:
    # 另一種圖表：圓環圖 (Donut Chart) 模擬
    # 這裡簡單用 Metrics 呈現，因為比較強調「達成率」
    st.metric("新好友增加", "36,000+", delta="超乎預期")
    st.metric("互動親密度", "100%", delta="達成")
st.markdown('</div>', unsafe_allow_html=True)


# 專案 3: NISSAN X-TRAIL
st.markdown('<div class="project-card" style="border-left-color: #fdcb6e;">', unsafe_allow_html=True)
c5, c6 = st.columns([1.5, 1])
with c5:
    st.markdown("### 🚗 NISSAN X-TRAIL 心理測驗")
    st.markdown('<span class="tag">社群擴散</span> <span class="tag">病毒行銷</span>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
    **專案挑戰：** 車款規格生硬，如何讓一般大眾願意主動分享產品資訊？
    
    **解決方案：**
    將產品 USP 包裝成「工作風格心理測驗」，利用「貼標籤」心理促使分享。
    
    **關鍵成果：**
    **96%** 的驚人分享率，低預算創造高擴散。
    """)
with c6:
    # 製作一個簡單的長條比較圖
    st.write("📊 **分享率成效對比**")
    share_data = pd.DataFrame({
        'Type': ['一般貼文平均', '本專案心理測驗'],
        'Rate': [15, 96]
    })
    share_chart = alt.Chart(share_data).mark_bar(color='#fdcb6e').encode(
        x=alt.X('Rate', title='互動/分享率 (%)'),
        y=alt.Y('Type', title=None, sort=None),
        text='Rate'
    )
    st.altair_chart(share_chart, use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# 頁尾
st.markdown("---")
st.caption("© 2026 Nelly Chen | Built with Python & Streamlit in Taipei.")
