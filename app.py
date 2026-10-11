import streamlit as st
import os
import json

st.set_page_config(page_title="FlowBridge", page_icon="🌉", layout="centered")
st.title("🌉 FlowBridge")
st.caption("小红书笔记商品智能跳转助手 —— 优先站内，站外兜底，克制展示")

BRAND_DB = {
    "花西子": {"in_xhs": True, "xhs_shop": "花西子官方旗舰店", "price": "¥219", "third_party": None},
    "完美日记": {"in_xhs": True, "xhs_shop": "完美日记官方旗舰店", "price": "¥129", "third_party": None},
    "雅诗兰黛": {"in_xhs": False, "xhs_shop": None, "price": None, "third_party": [
        {"platform": "天猫", "shop": "雅诗兰黛官方旗舰店", "price": "¥490"},
        {"platform": "京东", "shop": "雅诗兰黛京东自营", "price": "¥480"},
    ]},
    "兰蔻": {"in_xhs": False, "xhs_shop": None, "price": None, "third_party": [
        {"platform": "天猫", "shop": "兰蔻官方旗舰店", "price": "¥560"},
        {"platform": "京东", "shop": "兰蔻京东自营", "price": "¥550"},
    ]},
    "沁水": {"in_xhs": False, "xhs_shop": None, "price": None, "third_party": [
        {"platform": "天猫", "shop": "雅诗兰黛官方旗舰店", "price": "¥490"},
    ]},
}

def fallback_extract(note_text):
    all_brands = list(BRAND_DB.keys())
    found = [b for b in all_brands if b in note_text]
    if not found:
        return "未知", []
    return found[0], found[1:4]

def render_card(core_product, secondary_brands):
    st.markdown("---")
    st.subheader("🛍️ 识别到核心商品")
    
    if core_product in BRAND_DB:
        info = BRAND_DB[core_product]
        if info["in_xhs"]:
            st.success(f"**{core_product}** 已入驻小红书")
            st.markdown(f"**优先推荐：** {info['xhs_shop']}  {info['price']}")
            st.button("🛒 去小红书购买", key="buy_xhs")
            st.caption("✅ 平台担保交易，售后有保障")
        else:
            st.warning(f"**{core_product}** 暂未入驻小红书")
            st.markdown("**站外官方渠道推荐：**")
            for tp in info["third_party"]:
                col1, col2, col3 = st.columns([2, 2, 1])
                col1.write(tp['platform'])
                col2.write(tp['shop'])
                col3.write(tp['price'])
            st.button("🔗 跳转站外购买（合作广告位）", key="buy_out")
            st.caption("⚠️ 该品牌未入驻小红书，跳转至官方渠道。平台将获得佣金收入。")
    else:
        st.info(f"未匹配到「{core_product}」的入驻信息。")
    
    if secondary_brands:
        with st.expander(f"📎 文中还提及了 {len(secondary_brands)} 个其他品牌（已折叠，避免干扰）"):
            for b in secondary_brands:
                if b in BRAND_DB:
                    status = "已入驻" if BRAND_DB[b]["in_xhs"] else "未入驻"
                    st.write(f"- {b}（{status}）")
                else:
                    st.write(f"- {b}（暂无数据）")
            st.caption("次要品牌不触发跳转卡片，保持阅读纯净。")

note_text = st.text_area(
    "粘贴小红书笔记内容",
    height=200,
    placeholder="例如：最近干皮真的离不开雅诗兰黛沁水粉底液，滋润度绝了，比兰蔻菁纯更适合我……"
)

if st.button("🔍 分析笔记", type="primary"):
    if not note_text.strip():
        st.warning("请先粘贴笔记内容")
    else:
        core, secondary = fallback_extract(note_text)
        render_card(core, secondary)
