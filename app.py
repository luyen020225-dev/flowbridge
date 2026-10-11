import streamlit as st

st.set_page_config(page_title="小红书 - FlowBridge", page_icon="📕", layout="centered")

# ==========================================
# 极致 CSS：1:1 还原深色模式小红书 + 手机外壳
# ==========================================
st.markdown("""
<style>
header {visibility: hidden;}
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
.stApp { background-color: #121212; }
.phone-frame {
max-width: 400px;
margin: 0 auto;
background-color: #000000;
border-radius: 32px;
padding: 16px;
box-shadow: 0 10px 40px rgba(255,255,255,0.1);
border: 1px solid #333;
font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
color: #ffffff;
position: relative;
min-height: 800px;
padding-bottom: 80px;
}
.app-header { display: flex; align-items: center; justify-content: space-between; padding-bottom: 12px; }
.app-header-left { display: flex; align-items: center; gap: 8px; }
.app-header-left img { width: 32px; height: 32px; border-radius: 50%; }
.app-header-left span { font-size: 15px; font-weight: 500; }
.follow-btn { background-color: transparent; border: 1px solid #ff2442; color: #ff2442; border-radius: 20px; padding: 4px 12px; font-size: 12px; font-weight: bold; }
.note-image { width: 100%; border-radius: 12px; margin-bottom: 12px; object-fit: cover; }
.note-content { font-size: 15px; line-height: 1.6; color: #e0e0e0; margin-bottom: 8px; }
.note-meta { font-size: 12px; color: #888; margin-bottom: 16px; display: flex; justify-content: space-between;}
.interaction-bar { display: flex; justify-content: space-between; font-size: 13px; color: #aaa; margin-bottom: 20px; border-bottom: 1px solid #222; padding-bottom: 12px; align-items: center;}
.comment-section-title { font-size: 14px; font-weight: bold; color: #fff; margin-bottom: 16px; }
.comment-item { display: flex; gap: 10px; margin-bottom: 18px; }
.comment-avatar { width: 32px; height: 32px; border-radius: 50%; background-color: #333; flex-shrink: 0; }
.comment-content { flex-grow: 1; }
.comment-user { font-size: 13px; font-weight: 600; color: #bbb; margin-bottom: 4px; }
.comment-text { font-size: 14px; color: #eee; line-height: 1.5; margin-bottom: 6px; }
.comment-meta { font-size: 12px; color: #666; display: flex; justify-content: space-between; }
.comment-reply { background-color: #1a1a1a; border-radius: 8px; padding: 8px; margin-top: 8px; font-size: 13px; color: #ccc; }
.bottom-bar { position: fixed; bottom: 0; left: 0; right: 0; max-width: 400px; margin: 0 auto; background-color: #111; border-top: 1px solid #222; padding: 12px 16px; display: flex; align-items: center; gap: 12px; border-bottom-left-radius: 32px; border-bottom-right-radius: 32px; }
.bottom-input { flex-grow: 1; background-color: #222; border-radius: 20px; padding: 8px 16px; font-size: 13px; color: #888; }
.bottom-icons { display: flex; gap: 16px; font-size: 20px; color: #fff; align-items: center;}
.bottom-icons span { font-size: 12px; vertical-align: middle; margin-left: 4px; }
/* FlowBridge 智能提取按钮的样式 */
.ai-extract-btn {
background: linear-gradient(135deg, #ff2442, #ff6b6b);
color: white;
border-radius: 20px;
padding: 6px 14px;
font-size: 12px;
font-weight: bold;
border: none;
cursor: pointer;
display: inline-flex;
align-items: center;
gap: 4px;
box-shadow: 0 4px 12px rgba(255,36,66,0.3);
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# HTML 结构渲染 (无缩进！完全按照截图)
# ==========================================
st.markdown("""
<div class="phone-frame">
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
<div class="interaction-bar">
<span>共 775 条评论 &or;</span>
<span class="ai-extract-btn">✨ 提炼评论推荐</span>
</div>
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
</div>
<div class="bottom-bar">
<div class="bottom-input">留下你的想法吧</div>
<div class="bottom-icons">
❤️<span>1113</span>
⭐<span>790</span>
💬<span>775</span>
</div>
</div>
""", unsafe_allow_html=True)
