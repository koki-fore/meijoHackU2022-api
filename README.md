# meijoHackU2022-api
fastAPIをMySQLと接続してDockerで構築

## Set up
Dockerでbuild
```bash
Docker-compose build
```
Dockerを起動（-dでバックで起動）
```bash
Docker-compose up -d
```

# Swagger UI
localhost:8080/docs

# MySQLとの接続を確認
```bash
docker-compose exec db mysql meijoHackU2022-db
```

# MySQLにデータベースを作成する方法
## 初めて作成
dockerコンテナの中に入る
create_db.pyのあるディレクトリで
```
python create_db.py
```
## データベース作り直す場合
dockerコンテナの中に入る
```
python rebuild_db.py
```
