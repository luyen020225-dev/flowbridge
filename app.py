import streamlit as st
import urllib.parse

st.set_page_config(page_title="小红书 - FlowBridge", page_icon="📕", layout="centered")

# ==========================================
# 终极 CSS：手机壳 + 深色模式 + 定制 Popover 按钮
# ==========================================
st.markdown("""
<style>
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stApp { background-color: #f0f0f0; }

/* 手机壳容器 */
.block-container {
    max-width: 420px !important;
    margin: 0 auto !important;
    background-color: #000000 !important;
    border-radius: 32px !important;
    padding: 20px !important;
    box-shadow: 0 10px 40px rgba(0,0,0,0.15) !important;
    border: 1px solid #333 !important;
    position: relative;
}

/* 隐藏 Streamlit 默认的selectbox边框，让它融入界面 */
div[data-testid="stSelectbox"] { margin-bottom: 0 !important; }
div[data-testid="stSelectbox"] > div { border: none !important; background: transparent !important; }
div[data-testid="stSelectbox"] label { display: none !important; }

/* 顶部导航 */
.app-header { display: flex; align-items: center; justify-content: space-between; padding-bottom: 12px; }
.app-header-left { display: flex; align-items: center; gap: 8px; }
.app-header-left img { width: 32px; height: 32px; border-radius: 50%; }
.app-header-left span { font-size: 15px; font-weight: 500; color: #fff; }
.follow-btn { background-color: transparent; border: 1px solid #ff2442; color: #ff2442; border-radius: 20px; padding: 4px 12px; font-size: 12px; font-weight: bold; }

/* 笔记内容 */
.note-image { width: 100%; border-radius: 12px; margin-bottom: 12px; object-fit: cover; }
.note-content { font-size: 15px; line-height: 1.6; color: #e0e0e0; margin-bottom: 8px; }
.note-meta { font-size: 12px; color: #888; margin-bottom: 16px; display: flex; justify-content: space-between; }

/* 互动栏（评论数 + 跳转按钮） */
.interaction-bar { display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px; border-bottom: 1px solid #222; padding-bottom: 12px; }

/* 评论区 */
.comment-section-title { font-size: 14px; font-weight: bold; color: #fff; margin-bottom: 16px; }
.comment-item { display: flex; gap: 10px; margin-bottom: 18px; }
.comment-avatar { width: 32px; height: 32px; border-radius: 50%; background-color: #333; flex-shrink: 0; }
.comment-content { flex-grow: 1; }
.comment-user { font-size: 13px; font-weight: 600; color: #bbb; margin-bottom: 4px; }
.comment-text { font-size: 14px; color: #eee; line-height: 1.5; margin-bottom: 6px; }
.comment-meta { font-size: 12px; color: #666; display: flex; justify-content: space-between; }
.comment-reply { background-color: #1a1a1a; border-radius: 8px; padding: 8px; margin-top: 8px; font-size: 13px; color: #ccc; }

/* 定制“评论区好物直达”的 Popover 按钮样式 */
div[data-testid="stPopover"] > button {
    background: linear-gradient(135deg, #ff2442, #ff6b6b) !important;
    color: white !important;
    border-radius: 20px !important;
    padding: 6px 14px !important;
    font-size: 12px !important;
    font-weight: bold !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(255,36,66,0.3) !important;
    width: 100%;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# 模拟数据与品牌库
# ==========================================
BRAND_DB = {
    "香奈儿": {"in_xhs": False, "url": "https://s.taobao.com/search?q=" + urllib.parse.quote("香奈儿持妆粉底液")},
    "CPB": {"in_xhs": False, "url": "https://search.jd.com/Search?keyword=" + urllib.parse.quote("CPB晶钻粉霜")},
    "植村秀": {"in_xhs": True, "url": "https://www.xiaohongshu.com/search_result?keyword=" + urllib.parse.quote("植村秀0卡粉底液")},
    "娇兰": {"in_xhs": False, "url": "https://s.taobao.com/search?q=" + urllib.parse.quote("娇兰金钻粉底液")}
}

# ==========================================
# 渲染 HTML 结构 (无缩进)
# ==========================================
st.markdown("""
<div class="app-header">
<div class="app-header-left">
<span style="font-size: 20px;">&larr;</span>
<img src="https://api.dicebear.com/7.x/notionists/svg?seed=Felix" alt="avatar">
<span>干皮小仙女</span>
</div>
<div><span class="follow-btn">关注</span></div>
</div>
<img class="note-image" src="https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=800&h=600&fit=crop" alt="note image">
<div class="note-content">到底有没有适合干皮的粉底液啊😭</div>
<div class="note-meta"><span>8月15日 甘肃</span><span>😒 不喜欢</span></div>
""", unsafe_allow_html=True)

# === 互动栏（左：评论数，右：Popover跳转按钮）===
col1, col2 = st.columns([1, 1])
with col1:
    st.markdown('<div style="color:#aaa; font-size:13px; margin-top:6px;">共 775 条评论 &or;</div>', unsafe_allow_html=True)
with col2:
    with st.popover("✨ 评论区好物直达"):
        st.markdown("### 🛒 评论区同款购买直达")
        for brand, info in BRAND_DB.items():
            st.markdown(f"**{brand}**")
            if info["in_xhs"]:
                st.link_button("去小红书官方旗舰店", info["url"], use_container_width=True)
            else:
                st.link_button("去外部平台购买", info["url"], use_container_width=True)
            st.markdown("---")

# === 评论区 HTML ===
st.markdown("""
<div class="comment-section-title">评论区</div>
<div class="comment-item">
<div class="comment-avatar" style="background-image: url('https://api.dicebear.com/7.x/notionists/svg?seed=Aneka'); background-size: cover;"></div>
<div class="comment-content">
<div class="comment-user">椰椰奶黄包</div>
<div class="comment-text">去用 香奈儿持妆°！！我干敏！！！</div>
<div class="comment-meta"><span>08-16 江苏</span><span>❤️ 8</span></div>
<div class="comment-reply"><span style="color:#aaa;">偶不言：</span>真的吗姐妹我也是干敏</div>
</div>
</div>
<div class="comment-item">
<div class="comment-avatar" style="background-image: url('https://api.dicebear.com/7.x/notionists/svg?seed=Leo'); background-size: cover;"></div>
<div class="comment-content">
<div class="comment-user">嘟噜噜🐥</div>
<div class="comment-text">cpb晶钻粉霜°</div>
<div class="comment-meta"><span>08-17 河北</span><span>❤️ 8</span></div>
</div>
</div>
<div class="comment-item">
<div class="comment-avatar" style="background-image: url('https://api.dicebear.com/7.x/notionists/svg?seed=Jack'); background-size: cover;"></div>
<div class="comment-content">
<div class="comment-user">音乐学考研馨馨学姐</div>
<div class="comment-text">植村秀0卡</div>
<div class="comment-meta"><span>08-16 河北</span><span>❤️ 6</span></div>
<div class="comment-reply"><span style="color:#aaa;">momo：</span>容易暗沉吗😘</div>
</div>
</div>
<div class="comment-item">
<div class="comment-avatar" style="background-image: url('https://api.dicebear.com/7.x/notionists/svg?seed=Mia'); background-size: cover;"></div>
<div class="comment-content">
<div class="comment-user">篱&烬墨</div>
<div class="comment-text">娇兰金钻</div>
<div class="comment-meta"><span>08-16 浙江</span><span>❤️ 4</span></div>
</div>
</div>
""", unsafe_allow_html=True)
