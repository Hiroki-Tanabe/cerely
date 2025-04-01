import MySQLdb

try:
    conn = MySQLdb.connect(
        host="mysql",  # Docker Composeで指定したサービス名
        user="tana",
        passwd="tana",
        db="test_database"
    )
    print("接続成功！")
except Exception as e:
    print(f"接続失敗: {e}")