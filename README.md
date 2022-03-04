# sam-local-tools

DynamoDB-local と AWS SAM をローカルで実行するための環境を用意します

ツールを利用するための各コマンドは Python の invoke で、タスクとして実行できるようになっています

## Requirements

- Python 3.8.11
- aws-sam-cli = ^1.37.0
- awscli = ^1.22.54

以上のツールは poetry で利用できるようになっています

## Usage

1. コンテナ環境を準備

```
sh init.sh
```

or

```
poetry run invoke init
```

このスクリプトで DynamoDB-local イメージのコンテナが作成されます

作成と共に、ローカル実行用の DynamoDB テーブルを作成します

2. SAM テンプレートをビルドし、ローカル実行する

- ビルド

```
poetry run sam build -p -t app/template.yaml
```

or

```
poetry run invoke build
```

`Build Succeeded`と表示されれば実行可能な状態となっています

- ローカル実行

```
poetry run sam local start-api --env-vars app/env.json --docker-network sam-local-tools_sam-local-tools
```

or

```
poetry run invoke start
```

`yyyy-mm-dd hh:mm:ss * Running on http://127.0.0.1:3000/ (Press CTRL+C to quit)`となればリクエスト受付状態となっています

3. ローカルで実行中の SAM へリクエスト

ターミナル等で別セッションを開き、以下のフォーマットのリクエストを行います

- PUT リクエスト

```
curl -i -X PUT http://127.0.0.1:3000/put -H 'Name:Taro'
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 34
Server: Werkzeug/1.0.1 Python/3.8.11
Date: Sat, 12 Feb 2022 10:24:20 GMT

{"message": "put_item finished!!"}
```

- GET リクエスト

```
curl -i http://127.0.0.1:3000/get -H 'Name:Taro' -X GET
HTTP/1.0 200 OK
Content-Type: application/json
Content-Length: 64
Server: Werkzeug/1.0.1 Python/3.8.11
Date: Sat, 12 Feb 2022 10:53:56 GMT

{"resp": {"Time": "2022-02-12 10:52:18.478965", "Name": "Taro"}}
```

4. コンテナ環境の片付け

```
sh delete.sh
```

or

```
poetry run invoke delete
```

以上のスクリプトで DynamoDB 情報とコンテナの削除を行います

## 参考

- https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/serverless-sam-cli-using-start-api.html
- https://docs.aws.amazon.com/ja_jp/serverless-application-model/latest/developerguide/sam-cli-command-reference-sam-local-start-api.html
- https://selmertsx.hatenablog.com/entry/2019/04/25/SAM_Local%E3%82%92%E5%88%A9%E7%94%A8%E3%81%97%E3%81%A6Local%E3%81%A7%E5%8B%95%E3%81%8B%E3%81%97%E3%81%A6%E3%81%84%E3%82%8BAWS_Lambda_%E3%81%8B%E3%82%89dynamodb-local%E3%81%AB%E3%82%A2%E3%82%AF
- https://qiita.com/gzock/items/e0225fd71917c234acce
