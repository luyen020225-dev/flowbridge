import streamlit as st
import urllib.parse

st.set_page_config(page_title="小红书 - FlowBridge内测版", page_icon="📕", layout="centered")

# ==========================================
# 终极 CSS：模拟手机外壳、小红书界面、及悬浮气泡
# ==========================================
st.markdown("""
<style>
    /* 隐藏 Streamlit 默认的菜单和顶部 */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 全局背景设为浅灰，模拟手机外部环境 */
    .stApp {
        background-color: #f5f5f5;
    }
    
    /* 手机壳容器 */
    .phone-frame {
        max-width: 420px;
        margin: 0 auto;
        background-color: #ffffff;
        border-radius: 24px;
        padding: 16px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.08);
        border: 1px solid #e0e0e0;
        position: relative;
    }
    
    /* 笔记卡片 */
    .note-card {
        padding: 10px 0;
    }
    .note-author {
        display: flex;
        align-items: center;
        gap: 10px;
        font-size: 14px;
        font-weight: 600;
        color: #333;
        margin-bottom: 12px;
    }
    .note-author img {
        width: 36px;
        height: 36px;
        border-radius: 50%;
    }
    .note-title {
        font-size: 17px;
        font-weight: 700;
        margin-bottom: 8px;
        color: #1a1a1a;
    }
    .note-content {
        font-size: 15px;
        line-height: 1.6;
        color: #333;
        margin-bottom: 12px;
    }
    .note-image {
        width: 100%;
        border-radius: 12px;
        margin-bottom: 12px;
    }
    .note-footer {
        display: flex;
        gap: 20px;
        color: #666;
        font-size: 13px;
        margin-bottom: 16px;
    }
    .comment-section {
        background-color: #f9f9f9;
        border-radius: 12px;
        padding: 12px;
    }
    .comment-item {
        font-size: 13px;
        color: #444;
        margin-bottom: 8px;
    }
    .comment-user {
        font-weight: 600;
        color: #333;
        margin-right: 6px;
    }
    
    /* 悬浮 FlowBridge 气泡容器 */
    .bridge-bubble {
        position: fixed;
        right: 20px;
        bottom: 20px;
        z-index: 999;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 模拟数据（明确区分内外跳转）
# ==========================================
NOTES_DB = {
    "笔记1：有未入驻品牌（雅诗兰黛）": {
        "author": "干皮小仙女",
        "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop",
        "title": "干皮救星！这几款粉底液真的绝了",
        "content": "最近干皮真的离不开雅诗兰黛沁水粉底液，滋润度绝了，比兰蔻菁纯更适合我。",
        "image": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=800&h=600&fit=crop",
        "likes": "1.2w",
        "comments": [
            {"user": "网友A", "text": "我也觉得雅诗兰黛好用！"},
            {"user": "网友B", "text": "花西子适合油皮吗？"}
        ]
    },
    "笔记2：有已入驻品牌（花西子）": {
        "author": "国货挖掘机",
        "avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop",
        "title": "花西子新品粉底液真实测评！",
        "content": "花西子这款粉底液真的惊艳到我了，遮瑕力和持妆度都在线，今天给大家详细测评一下。",
        "image": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=800&h=600&fit=crop",
        "likes": "856",
        "comments": [
            {"user": "网友C", "text": "哇，刚好想买！"}
        ]
    }
}

# 品牌库配置真实跳转地址
BRAND_DB = {
    "花西子": {
        "in_xhs": True, 
        "xhs_shop_name": "花西子官方旗舰店",
        "xhs_url": "https://www.xiaohongshu.com/search_result?keyword=花西子官方旗舰店",
        "price": "¥219"
    },
    "雅诗兰黛": {
        "in_xhs": False, 
        # 用京东搜索页，不用登录，点击就能看到结果，保证演示不翻车
        "external_url": "https://search.jd.com/Search?keyword=" + urllib.parse.quote("雅诗兰黛沁水粉底液"),
        "price": "¥490"
    }
}

def extract_brands(text):
    all_brands = list(BRAND_DB.keys())
    found = [b for b in all_brands if b in text]
    if not found:
        return "未知", []
    return found[0], found[1:]

# ==========================================
# 渲染主体
# ==========================================
st.markdown('<div style="text-align:center; font-size:12px; color:#999; margin-bottom:10px;">📱 移动端模拟界面</div>', unsafe_allow_html=True)

# 模拟手机框
st.markdown('<div class="phone-frame">', unsafe_allow_html=True)

# 选择笔记 (为了演示方便，用一个隐藏的 selectbox)
selected_note = st.selectbox("切换模拟笔记：", list(NOTES_DB.keys()), label_visibility="collapsed")
note = NOTES_DB[selected_note]

# 渲染笔记内容 (纯 HTML，避免 Streamlit 原生组件破坏排版)
st.markdown(f"""
<div class="note-card">
    <div class="note-author">
        <img src="{note['avatar']}" alt="avatar">
        <span>@{note['author']}</span>
    </div>
    <div class="note-title">{note['title']}</div>
    <div class="note-content">{note['content']}</div>
    <img class="note-image" src="{note['image']}" alt="note image">
    <div class="note-footer">
        <span>❤️ {note['likes']}</span>
        <span>💬 {len(note['comments'])} 条评论</span>
    </div>
    <div class="comment-section">
        <div style="font-weight: 600; font-size: 13px; margin-bottom: 6px; color:#666;">评论区</div>
        {"".join([f'<div class="comment-item"><span class="comment-user">{c["user"]}：</span>{c["text"]}</div>' for c in note["comments"]])}
    </div>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True) # 关闭手机框

# ==========================================
# FlowBridge 插件功能（用 Popover 模拟悬浮气泡）
# ==========================================
st.write("") # 加一点空隙，防止挤在一起
st.markdown("### 👇 模拟浏览器右下角的 FlowBridge 智能气泡")

full_text = note["content"] + " " + " ".join([c["text"] for c in note["comments"]])
core_product, secondary_brands = extract_brands(full_text)

if core_product in BRAND_DB:
    info = BRAND_DB[core_product]
    
    # 使用 st.popover 模拟点击气泡后弹出的面板
    with st.popover(f"🔍 发现核心商品：{core_product}（点击查看跳转）", use_container_width=True):
        st.markdown(f"**核心商品：** {core_product}")
        
        if info["in_xhs"]:
            # 闭环跳转
            st.success(f"✅ 已入驻小红书，优先推荐站内购买")
            st.link_button(f"🛒 去小红书「{info['xhs_shop_name']}」购买", info["xhs_url"], type="primary", use_container_width=True)
            st.caption("提示：点击将在新标签页打开小红书官方搜索页。")
        else:
            # 开环跳转（外部）
            st.warning(f"⚠️ 未入驻小红书，为您跳转站外官方渠道")
            st.link_button(f"🔗 去京东购买「{core_product}」预估 {info['price']}", info["external_url"], type="primary", use_container_width=True)
            st.caption("提示：跳转至京东官方搜索页，平台将获得 CPS 佣金收入。")
        
        if secondary_brands:
            st.markdown("---")
            st.markdown("**📎 已自动折叠次要品牌（不干扰阅读）：**")
            for b in secondary_brands:
                st.write(f"- {b}")

    # 小提示：告诉测试者怎么切换
    st.caption("👉 你可以切换上方的下拉框，分别测试【花西子】和【雅诗兰黛】的跳转效果。")

else:
    st.info("未检测到可识别的核心商品。")

st.markdown("---")
st.caption("💡 这是一个模拟Demo。点击按钮会跳转至真实的平台页面（小红书/京东）。")
