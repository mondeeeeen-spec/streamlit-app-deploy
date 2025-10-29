import streamlit as st

st.title("サンプルアプリ②: 少し複雑なWebアプリ")

# 説明文（Markdownの ### / ##### で見出し）
st.write("##### 動作モード1: 文字数カウント")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで文字数をカウントできます。")
st.write("##### 動作モード2: BMI値の計算")
st.write("身長と体重を入力することで、肥満度を表す体型指数のBMI値を算出できます。")

# ラジオボタンでモード切り替え
selected_item = st.radio(
    "動作モードを選択してください。",
    ["文字数カウント", "BMI値の計算"]
)

st.divider()  # 区切り線

# モードに応じて入力欄を切り替える
if selected_item == "文字数カウント":
    input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")
    text_count = len(input_message)
else:
    height = st.text_input(label="身長（cm）を入力してください。")
    weight = st.text_input(label="体重（kg）を入力してください。")

# 実行ボタン
if st.button("実行"):
    st.divider()
    if selected_item == "文字数カウント":
        if input_message:
            st.write(f"文字数: **{text_count}**")
        else:
            st.error("カウント対象のテキストを入力してから「実行」を押してください。")
    else:
        # BMIモード
        if height and weight:
            try:
                # 文字列→整数に変換（例外が出たら except へ）
                h = int(height) / 100  # cm → m
                w = int(weight)
                bmi = round(w / (h ** 2), 1)
                st.write(f"BMI値: {bmi}")
            except ValueError:
                st.error("身長と体重は半角の数値で入力してください。")
        else:
            st.error("身長と体重をどちらも入力してください。")
