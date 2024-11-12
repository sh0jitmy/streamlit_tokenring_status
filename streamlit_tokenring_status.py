url = "http://localhost:8880/network_data.csv"  # RESTエンドポイントURL


import streamlit as st
import plotly.graph_objs as go
import requests
import csv
import io
import time
import numpy as np

# REST APIからCSVデータを取得する関数
def fetch_network_data(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

# CSVデータを解析し、ノード、接続情報、トークン保持状況を取得する関数
def parse_csv_data(csv_data):
    nodes = {}
    edges = []
    token_position = None
    reader = csv.DictReader(io.StringIO(csv_data))
    for row in reader:
        node_id = int(row['node_id'])
        connected_nodes = map(int, row['connected_to'].split(","))
        nodes[node_id] = (0, 0)  # 座標は後で設定
        for connected_to in connected_nodes:
            edges.append((node_id, connected_to))
        # トークン保持ノードの判定
        if row['has_token'].strip().lower() == 'true':
            token_position = node_id
    return nodes, edges, token_position

# ノード数に基づいて円周上に座標を自動設定する関数
def set_node_positions(nodes):
    num_nodes = len(nodes)
    for i, node_id in enumerate(nodes):
        angle = 2 * np.pi * i / num_nodes
        x = 0.5 + 0.4 * np.cos(angle)
        y = 0.5 + 0.4 * np.sin(angle)
        nodes[node_id] = (x, y)

# 初期設定
st.title("Token Ring Network")

# プロットのプレースホルダー
plot_placeholder = st.empty()

while True:
    # ネットワークデータを取得して解析
    csv_data = fetch_network_data(url)
    nodes, edges, token_position = parse_csv_data(csv_data)

    # ノードの座標を自動計算して設定
    set_node_positions(nodes)

    # Token Ringネットワークをプロット
    fig = go.Figure()

    # ノード間の接続線を描画
    for node_id, connected_to in edges:
        x0, y0 = nodes[node_id]
        x1, y1 = nodes[connected_to]
        fig.add_trace(go.Scatter(
            x=[x0, x1], y=[y0, y1],
            mode="lines",
            line=dict(color="gray", width=2),
            showlegend=False
        ))

    # ノードの描画
    for node_id, (x, y) in nodes.items():
        color = "orange" if node_id == token_position else "lightgreen"
        fig.add_trace(go.Scatter(
            x=[x], y=[y], mode="markers+text",
            marker=dict(color=color, size=30),
            text=str(node_id), textposition="bottom center",
            showlegend=False
        ))

    # Layout設定
    fig.update_layout(
        xaxis=dict(range=[0, 1], showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(range=[0, 1], showgrid=False, zeroline=False, showticklabels=False),
        width=600, height=600,
        margin=dict(l=20, r=20, t=20, b=20)
    )

    # プロットを更新
    plot_placeholder.plotly_chart(fig, use_container_width=True)

    # 定期的にデータを更新
    time.sleep(5)
