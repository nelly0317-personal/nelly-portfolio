import streamlit as st

# --- 1. 頁面基礎設定 (Page Configuration) ---
st.set_page_config(
    page_title="Nelly Chen | Portfolio",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 2. 高質感 CSS 樣式 (這是網頁變美的魔法) ---
st.markdown("""
<style>
    /* 引入 Google Fonts: Playfair Display (標題) + Noto Sans TC (內文) */
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+TC:wght@300;400;700&family=Playfair+Display:wght@700&display=swap');

    /* 全站字體與顏色設定 */
    html, body, [class*="css"] {
        font-family: 'Noto Sans TC', sans-serif;
        color: #2c3e50;
        background-color: #fdfdfd;
    }

    /* 標題專用字體 (雜誌感) */
    h1, h2, h3 {
        font-family: 'Playfair Display', serif;
        color: #1e272e;
        font-weight: 700;
    }

    /* 強調文字顏色 */
    .highlight { color: #c0392b; font-weight: bold; }

    /* 專案卡片 (Card) 設計 */
    .project-card {
        background-color: white;
        padding: 25px;
        border-radius: 10px;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05); /* 輕柔陰影 */
        border-left: 5px solid #bdc3c7; /* 預設邊框色 */
        margin-bottom: 30px;
        transition: transform 0.2s ease-in-out;
    }
    .project-card:hover {
        transform: translateY(-5px); /* 滑鼠滑過會微微浮起 */
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }

    /* 標籤 (Tag) 設計 */
    .tag-badge {
        display: inline-block;
        padding: 4px 12px;
        margin-right: 6px;
        margin-bottom: 6px;
        background-color: #f1f2f6;
        color: #57606f;
        border-radius: 15px;
        font-size: 0.8rem;
        font-weight: 500;
    }

    /* 時間軸樣式 */
    .year-label {
        font-family: 'Playfair Display', serif;
        font-size: 1.8rem;
        color: #7f8c8d;
        text-align: right;
        padding-right: 15px;
        border-right: 3px solid #dfe6e9;
        line-height: 1.2;
    }
    .exp-content {
        padding-left: 20px;
    }
    
    /* 連結按鈕樣式 */
    .contact-btn {
        text-decoration: none;
        color: #2c3e50;
        border: 1px solid #2c3e50;
        padding: 8px 20px;
        border-radius: 30px;
        font-weight: 500;
        transition: all 0.3s;
    }
    .contact-btn:hover {
        background-color: #2c3e50;
        color: white;
    }
</style>
""", unsafe_allow_html=True)

# --- 3. 頁首 Hero Section ---
col_hero1, col_hero2 = st.columns([2, 1])
with col_hero1:
    st.title("Nelly Chen.")
    st.markdown("### Digital Marketing Specialist")
    st.write("我是陳俞寧，一位數據驅動創意的資深行銷企劃。")
    st.markdown("擅長將冷冰冰的數據，轉化為有溫度的社群互動與商業價值。<br>這個網頁是我運用 Python (Streamlit) 建置的作品集。", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""
        <a href="mailto:nellylemon0317@gmail.com" class="contact-btn">📩 Contact Me</a>
        &nbsp;&nbsp; <span style="color:#b2bec3;">|</span> &nbsp;&nbsp; Taipei, Taiwan
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 4. 工作經歷 (Work Experience) - 雜誌時間軸風格 ---
st.header("01. Work Experience")
st.markdown("<br>", unsafe_allow_html=True)

# 經歷 1: 網路基因 (修正名稱)
c1, c2 = st.columns([1, 4])
with c1:
    st.markdown('<div class="year-label">2023<br>|<br>2025</div>', unsafe_allow_html=True)
with c2:
    st.markdown('<div class="exp-content">', unsafe_allow_html=True)
    st.subheader("Senior Account Executive")
    st.markdown("**網路基因 (WebGene)**") # <--- 已修正名稱
    st.markdown("""
    * **LINE 行銷專家**：主導規劃與執行 LINE 行銷與 IMC 整合活動，熟悉 API 串接與數據追蹤。
    * **品牌比稿提案**：參與航空、酒商、運動品牌比稿，具備從 0 到 1 的策略規劃能力。
    * **關鍵成效**：操作 Nestle Klim CNY 案，透過雙重抽獎機制，大幅提升發票登錄率。
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# 經歷 2: 偉門智威
c3, c4 = st.columns([1, 4])
with c3:
    st.markdown('<div class="year-label">2020<br>|<br>2023</div>', unsafe_allow_html=True)
with c4:
    st.markdown('<div class="exp-content">', unsafe_allow_html=True)
    st.subheader("Social Media Planner")
    st.markdown("**偉門智威廣告 (Wunderman Thompson)**")
    st.markdown("""
    * **社群內容策略**：負責 NISSAN 等車商客戶，將生硬規格轉化為消費者有感的內容。
    * **視覺創意統籌**：規劃平面拍攝需求，確保素材品質符合品牌高標準。
    * **病毒式擴散**：設計心理測驗互動，創造 **96% 分享率** 與 **5,800+ 參與人數**。
    """)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("---")

# --- 5. 精選專案 (Selected Projects) ---
st.header("02. Selected Projects")
st.write("精選具代表性的 OMO 整合、LINE 經營與社群擴散案例。")
st.markdown("<br>", unsafe_allow_html=True)

# 定義專案顯示函數 (讓程式碼更整潔，且方便重複使用)
def show_project(title, role, tags, desc, metrics, color_hex, icon):
    st.markdown(f'<div class="project-card" style="border-left-color: {color_hex};">', unsafe_allow_html=True)
    
    # 上半部：標題與標籤
    p1, p2 = st.columns([3, 1])
    with p1:
        st.subheader(f"{icon} {title}")
        st.markdown(f"**Role:** {role}")
        # 產生標籤 HTML
        tags_html = "".join([f'<span class="tag-badge">{t}</span>' for t in tags])
        st.markdown(tags_html, unsafe_allow_html=True)
    
    st.markdown("<hr style='margin: 15px 0; border: 0; border-top: 1px solid #eee;'>", unsafe_allow_html=True)
    
    # 下半部：內容與數據 (左右分欄)
    col_desc, col_metrics = st.columns([1.5, 1])
    
    with col_desc:
        st.markdown("#### 📝 專案洞察")
        st.write(desc)
        # 預留圖片位置的提示 (更有設計感)
        st.markdown(f"""
        <div style="margin-top:15px; padding:15px; background-color:{color_hex}10; border-radius:5px; color:{color_hex}; font-size:0.9rem;">
            💡 <b>Visual Concept:</b> 結合品牌調性與互動科技，打造沈浸式體驗。
        </div>
        """, unsafe_allow_html=True)

    with col_metrics:
        st.markdown("#### 📊 關鍵成效")
        # 使用 Streamlit 原生 metric 元件，乾淨俐落
        for label, value in metrics:
            st.metric(label=label, value=value)
            
    st.markdown('</div>', unsafe_allow_html=True)

# --- 專案 1: New Balance (紅) ---
show_project(
    title="New Balance CNY - 翻走春趣",
    role="Project Manager",
    tags=["LINE OA", "OMO 整合", "互動遊戲"],
    desc="結合農曆年節氣氛，發展「翻牌」互動遊戲。運用 OMO 操作，除賺取購物金外，還能引導消費者前往門市印製實體春聯，成功將線上流量導流至線下。",
    metrics=[("參與人數", "61,000+"), ("新好友數", "+28,000")],
    color_hex="#e55039",
    icon="🧧"
)

# --- 專案 2: The North Face (綠) ---
show_project(
    title="The North Face - AI 撩山林",
    role="Digital Planner",
    tags=["AI Chatbot", "品牌互動", "Tech"],
    desc="融合 AI 科技，發展與山林對話的概念。透過線上聊天室與「山神」對話，呼籲民眾回歸山林。透過感性溝通，成功提升品牌好感度與黏著度。",
    metrics=[("新好友數", "+36,000"), ("互動親密度", "100%")],
    color_hex="#27ae60",
    icon="🏔️"
)

# --- 專案 3: CAFE!N x DUREX (深藍) ---
show_project(
    title="CAFE!N x DUREX - 聯名 Campaign",
    role="Planner",
    tags=["MGM 機制", "跨界聯名", "會員增長"],
    desc="藉由強強聯名話題及獎項誘因，帶動 LINE 新好友數。設計 MGM (Member Get Member) 機制，鼓勵使用者分享好友，於一個月內創造驚人擴散。",
    metrics=[("新好友數", "+9,716"), ("參與人數", "11,000+")],
    color_hex="#2f3542",
    icon="☕"
)

# --- 頁尾 ---
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; color: #b2bec3; font-size: 0.8rem;">
    © 2026 Nelly Chen | Built with ❤️ and Python Streamlit
</div>
""", unsafe_allow_html=True)
