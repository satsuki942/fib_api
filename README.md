### APIの説明
本APIはFibonacci数列の第n項を得るためのAPIです。

本APIはリクエストに応じてjson形式で結果を返します。

エンドポイントURL: https://fibapp-427213.an.r.appspot.com/fib/

### 使い方の説明
第k項の数字をjson形式で得る場合

1. ブラウザ上で取得する場合は、次のURLでリクエストして下さい
    ```url
    https://fibapp-427213.an.r.appspot.com/fib/?format=json&n=k
    ```
2. CLIで取得する場合は、次のコマンドでリクエストしてください
    ```sh
    curl -X GET -H "Content-Type: application/json" "https://fibapp-427213.an.r.appspot.com/fib/?format=json&n=k"
    ```

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
```
C:.
|   .gcloudignore
|   app.yaml
|   db.sqlite3
|   manage.py
|   README.md
|   requirements.txt
|   tree.txt
|   
+---FibRestApiProject
|       asgi.py
|       settings.py
|       urls.py
|       wsgi.py
|       __init__.py
|       
\---fib_api
    |   admin.py
    |   apps.py
    |   models.py
    |   serializers.py
    |   tests.py
    |   urls.py
    |   views.py
    |   __init__.py
    |   
    \---migrations
            0001_initial.py
            __init__.py
```