import streamlit as st
import urllib.parse

st.set_page_config(page_title="小红书 - FlowBridge原型", page_icon="📕", layout="wide")

# ==========================================
# 注入自定义 CSS，模拟小红书网页版 UI
# ==========================================
st.markdown("""
<style>
    /* 隐藏 Streamlit 默认的顶部和菜单 */
    header {visibility: hidden;}
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    
    /* 页面背景设为白色 */
    .stApp { background-color: #ffffff; }
    
    /* 笔记卡片样式 */
    .note-card {
        border: 1px solid #f0f0f0;
        border-radius: 12px;
        padding: 20px;
        max-width: 600px;
        margin: 0 auto;
        background-color: #fff;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    .note-author {
        font-size: 14px;
        font-weight: 600;
        color: #333;
        display: flex;
        align-items: center;
        gap: 8px;
    }
    .note-author img {
        width: 32px;
        height: 32px;
        border-radius: 50%;
    }
    .note-title {
        font-size: 18px;
        font-weight: 700;
        margin-top: 12px;
        color: #1a1a1a;
    }
    .note-content {
        font-size: 15px;
        line-height: 1.6;
        color: #333;
        margin-top: 10px;
    }
    .note-image {
        width: 100%;
        border-radius: 8px;
        margin-top: 12px;
    }
    .note-footer {
        display: flex;
        gap: 16px;
        margin-top: 12px;
        color: #666;
        font-size: 13px;
    }
    .comment-section {
        margin-top: 16px;
        padding-top: 16px;
        border-top: 1px solid #f0f0f0;
    }
    .comment-item {
        font-size: 13px;
        color: #555;
        margin-bottom: 8px;
    }
    .comment-user {
        font-weight: 600;
        color: #333;
        margin-right: 4px;
    }
    /* 模拟小红书红色标志 */
    .xhs-logo {
        color: #ff2442;
        font-weight: bold;
        font-size: 18px;
        display: flex;
        align-items: center;
        gap: 6px;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 模拟数据
# ==========================================
NOTES_DB = {
    "笔记1（内有未入驻品牌-雅诗兰黛）": {
        "author": "干皮小仙女",
        "avatar": "https://images.unsplash.com/photo-1494790108377-be9c29b29330?w=100&h=100&fit=crop",
        "title": "干皮救星！这几款粉底液真的绝了",
        "content": "最近干皮真的离不开雅诗兰黛沁水粉底液，滋润度绝了，比兰蔻菁纯更适合我，花西子的也不错但遮瑕弱一点。姐妹们冲！",
        "image": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=800&h=600&fit=crop",
        "likes": "1.2w",
        "comments": [
            {"user": "网友A", "text": "我也觉得雅诗兰黛好用！"},
            {"user": "网友B", "text": "花西子适合油皮吗？"},
            {"user": "商家自荐", "text": "我家有同款，点我主页！"}
        ]
    },
    "笔记2（内有已入驻品牌-花西子）": {
        "author": "国货挖掘机",
        "avatar": "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=100&h=100&fit=crop",
        "title": "花西子新品粉底液真实测评！",
        "content": "花西子这款粉底液真的惊艳到我了，遮瑕力和持妆度都在线，今天给大家详细测评一下。",
        "image": "https://images.unsplash.com/photo-1620916566398-39f1143ab7be?w=800&h=600&fit=crop",
        "likes": "856",
        "comments": [
            {"user": "网友C", "text": "哇，刚好想买！"},
            {"user": "网友D", "text": "持妆度怎么样？"}
        ]
    }
}

# 品牌库（这里直接定义真实的跳转URL）
BRAND_DB = {
    "花西子": {
        "in_xhs": True, 
        "xhs_shop_name": "花西子官方旗舰店",
        "xhs_url": "https://www.xiaohongshu.com/user/profile/5f3d5e5e0000000001009d5c", # 这里是一个模拟的店铺主页链接
        "price": "¥219"
    },
    "雅诗兰黛": {
        "in_xhs": False, 
        "external_url": "https://s.taobao.com/search?q=" + urllib.parse.quote("雅诗兰黛沁水粉底液"),
        "price": "¥490"
    },
    "兰蔻": {
        "in_xhs": False, 
        "external_url": "https://s.taobao.com/search?q=" + urllib.parse.quote("兰蔻菁纯粉底液"),
        "price": "¥560"
    }
}

def extract_brands(text):
    all_brands = list(BRAND_DB.keys())
    found = [b for b in all_brands if b in text]
    if not found:
        return "未知", []
    return found[0], found[1:]

# ==========================================
# 界面主体渲染
# ==========================================
col_left, col_main, col_right = st.columns([1, 4, 1])

with col_main:
    # 顶部红书 Logo
    st.markdown('<div class="xhs-logo">📕 小红书 · FlowBridge 内测版</div>', unsafe_allow_html=True)
    
    # 选择笔记
    selected_note = st.selectbox("切换笔记视图：", list(NOTES_DB.keys()), label_visibility="collapsed")
    note = NOTES_DB[selected_note]

    # 渲染笔记卡片 (HTML 注入)
    st.markdown(f"""
    <div class="note-card">
        <div class="note-author">
            <img src="{note['avatar']}" alt="avatar">
            <span>{note['author']}</span>
        </div>
        <div class="note-title">{note['title']}</div>
        <div class="note-content">{note['content']}</div>
        <img class="note-image" src="{note['image']}" alt="note image">
        <div class="note-footer">
            <span>❤️ {note['likes']}</span>
            <span>💬 {len(note['comments'])} 条评论</span>
        </div>
        <div class="comment-section">
            <div style="font-weight: 600; font-size: 14px; margin-bottom: 8px;">💬 评论区</div>
            {"".join([f'<div class="comment-item"><span class="comment-user">{c["user"]}：</span>{c["text"]}</div>' for c in note["comments"]])}
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    
    # ==========================================
    # FlowBridge 插件功能介入
    # ==========================================
    st.markdown("### 🔍 FlowBridge 智能识别与购买引导")
    
    full_text = note["content"] + " " + " ".join([c["text"] for c in note["comments"]])
    core_product, secondary_brands = extract_brands(full_text)

    if core_product in BRAND_DB:
        info = BRAND_DB[core_product]
        st.markdown(f"**检测到核心商品：<span style='color:#ff2442;'>{core_product}</span>**", unsafe_allow_html=True)
        
        # --- 情况1：已入驻小红书 (内部闭环跳转) ---
        if info["in_xhs"]:
            st.success(f"✅ 优先推荐小红书站内购买：{info['xhs_shop_name']} ({info['price']})")
            st.markdown("👉 点击下方按钮，直接打开 **小红书店铺主页**：")
            st.link_button(f"🛒 去小红书「{info['xhs_shop_name']}」购买", info["xhs_url"], type="primary", use_container_width=True)
            st.caption("提示：由于小红书网页版限制，当前跳转至其店铺主页。若在App内，将直接唤起商品下单页。")
            
        # --- 情况2：未入驻小红书 (外部开环跳转) ---
        else:
            st.warning(f"⚠️ {core_product} 暂未入驻小红书，为您匹配站外官方渠道：")
            st.markdown("👉 点击下方按钮，跳转至 **淘宝官方搜索页**：")
            st.link_button(f"🔗 去淘宝购买「{core_product}」预估 {info['price']}", info["external_url"], type="primary", use_container_width=True)
            st.caption("提示：该品牌未入驻小红书，跳转至第三方平台。平台将获得 CPS 佣金收入。")

    # 次要品牌折叠
    if secondary_brands:
        with st.expander(f"📎 文中还提及了 {len(secondary_brands)} 个其他品牌（已折叠，避免干扰）"):
            for b in secondary_brands:
                if b in BRAND_DB:
                    status = "已入驻" if BRAND_DB[b]["in_xhs"] else "未入驻"
                    st.write(f"- {b}（{status}）")
            st.caption("次要品牌不触发跳转卡片，保持阅读纯净。")

    st.markdown("---")
    st.caption("💡 测试提示：切换到【笔记1】看未入驻品牌的外部跳转，切换到【笔记2】看已入驻品牌的内部跳转。")
