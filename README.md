# streamlit_tokenring_status
以下が日本語版のREADME.mdです。

# トークンリングネットワーク可視化

このプロジェクトは、StreamlitとPlotlyを用いてトークンリングネットワークのトークン受け渡し状況を可視化します。ネットワーク構成とトークンの保持状況は、REST APIから定期的に取得したCSVデータをもとに更新されます。

## 機能

- **動的トークンリング可視化**: ノードを円形に配置し、接続線でノード間を表示します。
- **トークンの受け渡し表示**: トークン保持ノードが色で強調表示され、CSVデータに基づき更新されます。
- **REST API連携**: ネットワーク構成とトークン保持状況を定期的にREST APIから取得し、リアルタイムで反映します。

## CSVフォーマット

ネットワーク構成はCSVファイルで指定し、次の形式で記載します：

```csv
node_id,connected_to,has_token
0,1,2,True
1,2,3,False
2,3,4,False
3,4,0,False
4,0,1,False

	•	node_id: ノードのID
	•	connected_to: 接続先のノードIDをカンマ区切りで指定
	•	has_token: Trueの場合はトークンを保持していることを示す

インストール

	1.	リポジトリをクローンします。
	2.	必要なパッケージをインストールします：

pip install streamlit plotly numpy requests


	3.	アプリを起動します：

streamlit run streamlit_tokenring_status.py



設定

app.py内のurl変数に、CSVデータを提供するREST APIエンドポイントのURLを設定してください。

使用方法

アプリを実行すると、ブラウザにトークンリングネットワークが表示されます。ネットワーク構成やトークン保持状況は5秒ごとに自動更新されます。

ライセンス

このプロジェクトはMITライセンスのもとで公開されています。

この`README.md`で、プロジェクトの基本的な設定と使用方法を簡潔に説明しています。

