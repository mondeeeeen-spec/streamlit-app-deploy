import streamlit as st

st.title("サンプルアプリ①: 簡単なWebアプリ")

# 一行入力フォーム（返り値が文字列）
input_message = st.text_input(label="文字数のカウント対象となるテキストを入力してください。")

# Pythonのlen()で文字数カウント
text_count = len(input_message)

# ボタンが押された瞬間だけ下の処理が実行される
if st.button("実行"):
    # Markdown（**太字**）で出力
    st.write(f"文字数: **{text_count}**")
