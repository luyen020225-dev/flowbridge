import streamlit as st
import urllib.parse

st.set_page_config(page_title="FlowBridge", page_icon="🌉", layout="centered")

# ========== 模拟数据 ==========
# 这里模拟了小红书上的3篇笔记
NOTES_DB = {
    "笔记1：干皮救星粉底液推荐": {
        "author": "美妆小达人",
        "title": "干皮救星！这几款粉底液真的绝了",
        "content": "最近干皮真的离不开雅诗兰黛沁水粉底液，滋润度绝了，比兰蔻菁纯更适合我，花西子的也不错但遮瑕弱一点。姐妹们冲！",
        "image": "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=600&h=400&fit=crop",
        "likes": "1.2w",
        "comments": [
            {"user": "网友A", "text": "我也觉得雅诗兰黛好用！"},
            {"user": "网友B", "text": "花西子适合油皮吗？"},
            {"user": "商家自荐", "text": "我家有同款，点我主页！"}
        ]
    },
    "笔记2：平价项链分享": {
        "author": "穿搭日记",
        "title": "几十块钱的平价项链，质感绝了",
        "content": "今天分享几条我最近常戴的平价项链，都是925银的，不到一百块。第一条是花西子联名的，第二条是周大福的平替，真的很好看！",
        "image": "https://images.unsplash.com/photo-1599643478518-a784e5dc4c8f?w=600&h=400&fit=crop",
        "likes": "856",
        "comments": [
            {"user": "网友C", "text": "求链接！"},
            {"user": "商家自荐", "text": "我们家有同款，私我！"}
        ]
    }
}

# ========== 品牌数据库 ==========
BRAND_DB = {
    "花西子": {"in_xhs": True, "xhs_shop": "花西子官方旗舰店", "price": "¥219"},
    "雅诗兰黛": {"in_xhs": False, "xhs_shop": None, "price": None, "search_keyword": "雅诗兰黛沁水粉底液"},
    "兰蔻": {"in_xhs": False, "xhs_shop": None, "price": None, "search_keyword": "兰蔻菁纯粉底液"},
    "沁水": {"in_xhs": False, "xhs_shop": None, "price": None, "search_keyword": "雅诗兰黛沁水粉底液"},
}

def extract_brands(note_text):
    all_brands = list(BRAND_DB.keys())
    found = [b for b in all_brands if b in note_text]
    if not found:
        return "未知", []
    return found[0], found[1:4]

# ========== 界面渲染 ==========

st.title("🌉 FlowBridge")
st.caption("模拟小红书笔记页面 | 智能识别商品并跳转购买")

# 选择笔记
selected_note = st.selectbox("选择一篇笔记进行浏览：", list(NOTES_DB.keys()))
note = NOTES_DB[selected_note]

# === 模拟小红书笔记卡片 ===
st.markdown("---")
col1, col2 = st.columns([1, 4])
with col1:
    st.markdown(f"**@{note['author']}**")
with col2:
    st.markdown(f"### {note['title']}")

# 图片
st.image(note["image"], use_container_width=True)

# 正文
st.write(note["content"])

# 点赞评论栏
st.markdown(f"❤️ {note['likes']}  💬 {len(note['comments'])} 条评论")
st.markdown("---")

# 评论区
st.markdown("**💬 评论区**")
for comment in note["comments"]:
    with st.chat_message("user"):
        st.write(f"**{comment['user']}**：{comment['text']}")

st.markdown("---")

# === FlowBridge 插件功能介入 ===
st.markdown("### 🔍 FlowBridge 智能识别结果")
core_product, secondary_brands = extract_brands(note["content"] + " " + " ".join([c["text"] for c in note["comments"]]))

st.subheader("🛍️ 识别到核心商品")

if core_product in BRAND_DB:
    info = BRAND_DB[core_product]
    if info["in_xhs"]:
        st.success(f"**{core_product}** 已入驻小红书")
        st.markdown(f"**优先推荐：** {info['xhs_shop']}  {info['price']}")
        # === 真实的跳转链接 ===
        xhs_search_url = f"https://www.xiaohongshu.com/search_result?keyword={urllib.parse.quote(info['xhs_shop'])}"
        st.link_button("🛒 去小红书购买", xhs_search_url)
        st.caption("✅ 平台担保交易，售后有保障")
    else:
        st.warning(f"**{core_product}** 暂未入驻小红书")
        st.markdown("**站外官方渠道推荐：**")
        # === 真实的跳转链接 ===
        tb_search_url = f"https://s.taobao.com/search?q={urllib.parse.quote(info['search_keyword'])}"
        col_a, col_b = st.columns([3, 1])
        with col_a:
            st.markdown(f"**淘宝官方旗舰店** 预估 ¥490")
        with col_b:
            st.link_button("🔗 去淘宝购买", tb_search_url)
        st.caption("⚠️ 该品牌未入驻小红书，跳转至淘宝官方渠道。平台将获得佣金收入。")
else:
    st.info(f"未匹配到「{core_product}」的入驻信息。")

# 次要品牌折叠
if secondary_brands:
    with st.expander(f"📎 文中还提及了 {len(secondary_brands)} 个其他品牌（已折叠，避免干扰）"):
        for b in secondary_brands:
            if b in BRAND_DB:
                status = "已入驻" if BRAND_DB[b]["in_xhs"] else "未入驻"
                st.write(f"- {b}（{status}）")
            else:
                st.write(f"- {b}（暂无数据）")
        st.caption("次要品牌不触发跳转卡片，保持阅读纯净。")

st.markdown("---")
st.caption("💡 这是一个模拟Demo。点击按钮会跳转到真实的平台搜索页（小红书/淘宝）。")
