import pandas as pd
import streamlit as st

# fake dog data
dog_data = pd.DataFrame(
    [
        {
            "name": "Lucky",
            "mbti": "ESFP",
            "activity": "高",
            "home": "大空間",
            "breed": "黃金獵犬",
        },
        {
            "name": "Bella",
            "mbti": "INFJ",
            "activity": "低",
            "home": "小空間",
            "breed": "法鬥",
        },
        {
            "name": "Max",
            "mbti": "ENTP",
            "activity": "高",
            "home": "大空間",
            "breed": "哈士奇",
        },
        {
            "name": "Coco",
            "mbti": "ISFJ",
            "activity": "中",
            "home": "小空間",
            "breed": "柯基",
        },
    ]
)

st.title("🐶 流浪狗配對系統")
st.write("請填寫以下問題，幫助我們找到最適合您的狗狗！")

# 使用者輸入
user_mbti = st.selectbox(
    "您的 MBTI 類型：", ["ESFP", "INFJ", "ENTP", "ISFJ", "ISTJ", "ENFP", "其他"]
)
user_activity = st.selectbox("您的運動習慣：", ["高", "中", "低"])
user_home = st.selectbox("您的居住空間：", ["大空間", "小空間"])


# 配對邏輯
def match_dogs(mbti, activity, home):
    matched = dog_data[(dog_data["activity"] == activity) & (dog_data["home"] == home)]
    return matched


if st.button("🔍 立即配對"):
    results = match_dogs(user_mbti, user_activity, user_home)
    if not results.empty:
        st.write("### 🐾 配對結果：")
        for _, row in results.iterrows():
            st.write(f"**{row['name']}** ({row['breed']})")
            st.write(f"- MBTI: {row['mbti']}")
            st.write(f"- 活動需求: {row['activity']}")
            st.write(f"- 適合居住環境: {row['home']}")
            st.write("---")
    else:
        st.write("抱歉，目前沒有完全匹配的狗狗，請試試其他選項！")
