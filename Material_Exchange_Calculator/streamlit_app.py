import streamlit as st

st.set_page_config(page_title="材料交換計算器", page_icon="🔢", layout="centered")

st.title("🔢 材料交換計算器 (Streamlit)")

st.markdown("""
輸入三個 **正整數**，系統會計算平均值 `k` (取整數)，
再輸出 `x2, y2, z2`：
- 正數 ➝ **可交換(多的)**
- 負數 ➝ **需要(短缺)**
- 0 ➝ **剛好平衡**
""")

# --- 使用者輸入 ---
col1, col2, col3 = st.columns(3)
with col1:
    x1 = st.number_input("x1", min_value=1, step=1, value=10)
with col2:
    y1 = st.number_input("y1", min_value=1, step=1, value=7)
with col3:
    z1 = st.number_input("z1", min_value=1, step=1, value=5)

# --- 計算平均 k (整數版) ---
def compute_int_k(x1:int, y1:int, z1:int):
    total = x1 + y1 + z1
    if total % 3 == 0:
        return total // 3, None  # 無需調整

    nums = [x1, y1, z1]
    max_val = max(nums)
    for dec in (1, 2):
        if (total - dec) % 3 == 0 and max_val - dec >= 1:
            return (total - dec) // 3, dec

    # fallback: 向下取整
    return total // 3, None

def sign_hint(n: int) -> str:
    if n > 0: return "✅ 可交換(多的)"
    if n < 0: return "❌ 需要(短缺)"
    return "⚖️ 剛好平衡"

# --- 執行計算 ---
if st.button("開始計算"):
    k, adj = compute_int_k(x1, y1, z1)
    x2, y2, z2 = x1 - k, y1 - k, z1 - k

    st.subheader("計算結果")
    if adj:
        st.info(f"因為平均不是整數，已將最大值調整 -{adj} 後再計算。")

    st.write(f"**平均 k = {k}**")
    st.write(f"x2 = {x2} → {sign_hint(x2)}")
    st.write(f"y2 = {y2} → {sign_hint(y2)}")
    st.write(f"z2 = {z2} → {sign_hint(z2)}")
