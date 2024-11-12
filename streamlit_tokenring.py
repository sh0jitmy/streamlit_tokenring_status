import streamlit as st
import plotly.graph_objs as go
import numpy as np
import time

# Token Ringのノード数
nodes = 5
node_positions = [
    (0.5 + 0.4 * np.cos(2 * np.pi * i / nodes), 
     0.5 + 0.4 * np.sin(2 * np.pi * i / nodes)) for i in range(nodes)
]

# 初期トークンの位置
token_position = 0

st.title("Token Ring Network")

# Token Ringネットワークをプロット
fig = go.Figure()

# ノード間の線を追加
for i in range(nodes):
    x0, y0 = node_positions[i]
    x1, y1 = node_positions[(i + 1) % nodes]
    fig.add_trace(go.Scatter(
        x=[x0, x1], y=[y0, y1],
        mode="lines",
        line=dict(color="gray", width=2),
        showlegend=False
    ))

# ノードの初期描画
for i, pos in enumerate(node_positions):
    color = "orange" if i == token_position else "lightgreen"
    fig.add_trace(go.Scatter(
        x=[pos[0]], y=[pos[1]], mode="markers+text",
        marker=dict(color=color, size=30),
        text=str(i), textposition="bottom center",
        showlegend=False
    ))

# Layout設定
fig.update_layout(
    xaxis=dict(range=[0, 1], showgrid=False, zeroline=False, showticklabels=False),
    yaxis=dict(range=[0, 1], showgrid=False, zeroline=False, showticklabels=False),
    width=600, height=600,
    margin=dict(l=20, r=20, t=20, b=20)
)

# 動的更新ループ
plot_placeholder = st.empty()  # プロットのプレースホルダー

while True:
    # ノードの色更新
    for i in range(nodes):
        color = "orange" if i == token_position else "lightgreen"
        fig.data[nodes + i].marker.color = color  # nodesの後に描画されているのでoffsetしています

    # プロット更新
    plot_placeholder.plotly_chart(fig, use_container_width=True)

    # トークンの位置を更新
    token_position = (token_position + 1) % nodes
    time.sleep(1)  # 1秒ごとにトークンを移動
