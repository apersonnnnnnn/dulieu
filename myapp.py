import psycopg2

# Thông tin kết nối tới database từ Render
DATABASE_URL = "postgresql://lhn:pDzkstHL6pU8tIhOUIt7SpfAbdvwLDXx@dpg-ctke393v2p9s7387pijg-a/databasedoaniot"

# Kết nối tới cơ sở dữ liệu
try:
    conn = psycopg2.connect(DATABASE_URL)
    cursor = conn.cursor()

    # Tạo bảng nếu chưa tồn tại
    create_table_query = """
    CREATE TABLE IF NOT EXISTS my_table (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        age INT
    );
    """
    cursor.execute(create_table_query)
    conn.commit()

    # Nhập dữ liệu vào bảng
    insert_query = "INSERT INTO my_table (name, age) VALUES (%s, %s);"
    data = [("John Doe", 30), ("Jane Smith", 25)]
    cursor.executemany(insert_query, data)
    conn.commit()

    print("Dữ liệu đã được nhập thành công!")

except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    if conn:
        cursor.close()
        conn.close()
        print("Đã đóng kết nối tới cơ sở dữ liệu.")
