import streamlit as st

# 1. 設定網頁標題與版面 (Page Configuration)
st.set_page_config(
    page_title="Nelly Chen's Portfolio",
    page_icon="✨",
    layout="wide"
)

# 2. 側邊欄：個人簡介 (Sidebar Profile)
with st.sidebar:
    st.title("陳俞寧 (Nelly Chen)")
    st.write("📍 Taipei, Taiwan")
    st.write("💼 5年數位行銷經驗 | 社群與 LINE OA 專家")
    
    st.divider()
    
    # 聯絡資訊 (建議面試展示時再開啟，或視需求保留)
    st.write("📧 nellylemon0317@gmail.com")
    st.write("🔗 [我的 YouTube 頻道](#)") # 妳可以放上妳的 YT 連結
    
    st.divider()
    
    st.write("### 🚀 關於我")
    st.info(
        """
        我是奶莉，一位熱愛生活的數位行銷人。
        專精於社群行銷與 LINE OA 規劃。
        目前正積極學習 Python 與 AI 技術，
        致力於結合創意與數據科技。
        """
    )
    
    # 下載 PDF 按鈕 (假設妳把 PDF 也上傳到了 GitHub，這裡可以放連結)
    # st.download_button("📥 下載完整履歷 PDF", data=..., file_name="Nelly_Resume.pdf")

# 3. 主頁面：歡迎與數據亮點 (Main Content)
st.title("Hi there! 我是 Nelly 👋")
st.subheader("用數據驅動創意的資深行銷企劃")

st.markdown("---")

# 4. 專案亮點：將 PDF 中的數據視覺化 (Key Metrics)
st.header("🏆 精選專案成效")
st.write("運用 Python 將我過去操作的 Campaign 數據視覺化呈現：")

# 建立三個欄位來放數據
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🐻 CAFE!N x DUREX")
    st.caption("LINE MGM Campaign")
    # 使用 st.metric 呈現大數字，非常有科技感
    st.metric(label="新好友加入數", value="9,716", delta="+ 近期最佳")
    st.metric(label="活動參與人數", value="11,000+")

with col2:
    st.markdown("### 👟 New Balance CNY")
    st.caption("OMO 互動遊戲")
    st.metric(label="新好友增加", value="28,000+", delta="高轉換")
    st.metric(label="遊戲參與人數", value="61,000+")

with col3:
    st.markdown("### 🏔️ The North Face")
    st.caption("AI 撩山林活動")
    st.metric(label="新好友增加", value="36,000+")
    st.metric(label="互動親密度", value="100%")

st.markdown("---")

# 5. 工作經歷 (Experience Timeline)
st.header("📝 工作經歷")

tab1, tab2 = st.tabs(["網路基因 (2023-2025)", "偉門智威 (2020-2023)"])

with tab1:
    st.subheader("Senior Account Executive")
    st.write("📍 網路基因資訊有限公司")
    st.write(
        """
        - **LINE 行銷規劃**：規劃與執行 LINE 行銷與 IMC 活動。
        - **品牌比稿**：參與航空、酒商、運動等各類品牌比稿案。
        - **成效突破**：操作 Nestle Klim CNY 活動，創造高發票登錄率。
        """
    )

with tab2:
    st.subheader("Social Media Planner")
    st.write("📍 偉門智威廣告公司")
    st.write(
        """
        - **社群行銷**：規劃與執行 NISSAN 等品牌社群活動。
        - **內容產製**：負責車商平面拍攝需求與創意發想。
        - **病毒式行銷**：設計心理測驗活動，創造 96% 分享率。
        """
    )

st.markdown("---")

# 6. AI 技術應用展示 (Showcase AI Learning)
st.header("🤖 持續學習：AI 與程式技能")
st.write("這是我目前正在學習的技能樹，這個網頁即是使用 Python (Streamlit) 建置的成果。")

# 用 Slider 展示技能熟練度（互動元件）
python_skill = st.slider("Python 基礎 & 網頁架設", 0, 100, 30)
ai_skill = st.slider("AI 工具應用 (ChatGPT/Gemini)", 0, 100, 85)
marketing_skill = st.slider("數位行銷 & 社群經營", 0, 100, 95)

st.caption("💡 拖動滑桿可以看到我對不同領域的掌握度自我評估")

st.markdown("---")
st.write("© 2026 Nelly Chen. Built with ❤️ and Python.")
