## APIの説明
本APIはFibonacci数列の第n項を得るためのAPIです。

本APIはリクエストに応じてjson形式で結果を返します。

エンドポイントURL: https://fibapp-427213.an.r.appspot.com/fib

### 使い方の説明
第k項の数字をjson形式で得る場合

1. ブラウザ上で取得する場合は、次のURLでリクエストして下さい
    ```url
    https://fibapp-427213.an.r.appspot.com/fib?n=k
    ```
2. CLIで取得する場合は、次のコマンドでリクエストしてください
    ```sh
    curl -X GET -H "Content-Type: application/json" "https://fibapp-427213.an.r.appspot.com/fib?n=k"
    ```

## 実装について

### 使用フレームワーク
以下のフレームワークを主に使用
- Django
- djangorestframework

### 対応しているステータスコード
- 200
    - 適切なリクエストの場合、Fibonacci数列の第n項の数字を返す
- 400
    - 不正なリクエストの場合、リクエストの間違いを示すメッセージを返す
- その他
    - 未対応。

### ディレクトリ構成
※ Djangoのスケルトンから大きく変更したのは、下で補足が付いているプログラム
```
\fib-api
|   .gcloudignore
|   app.yaml
|   db.sqlite3
|   manage.py
|   README.md
|   requirements.txt
|   
\---FibRestApiProject
|       asgi.py
|       settings.py        # djangoプロジェクトの設定
|       urls.py            # djangoプロジェクトのルーティング
|       wsgi.py
|       __init__.py
|       
\---fib_api
    |   admin.py
    |   apps.py
    |   models.py
    |   serializers.py
    |   tests.py            # UnitTest
    |   urls.py             # fib_apiのルーティング
    |   views.py            # リクエストに対して返すレスポンスを計算
    |   __init__.py
    |   
    \---migrations
```