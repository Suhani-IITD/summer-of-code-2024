import psycopg2
import psycopg2.extras

conn = psycopg2.connect("dbname=dsocdb user=postgres password=root")

cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)


def add_product(item_sku,item_name,item_description,item_price,item_qty):
    item = get_product(item_sku)
    if(item==None):
        query = f"""INSERT INTO INVENTORYITEM (item_sku, item_name, item_description, item_price, item_qty)
    VALUES ({item_sku},'{item_name}','{item_description}',{item_price},{item_qty});"""
        cur.execute(query)
        conn.commit()
        return None
    else:
        return item


def get_product(item_sku):
    if(item_sku):
        query = f"SELECT * FROM INVENTORYITEM WHERE item_sku = {item_sku};"
        cur.execute(query)
        item = cur.fetchone()
    else:
        query = f"SELECT * FROM INVENTORYITEM;"
        cur.execute(query)
        item = cur.fetchall()
    return item


def alter_product(item_sku,col,val):
    query = f"UPDATE INVENTORYITEM SET {col}='{val}' WHERE item_sku={item_sku}"
    cur.execute(query)
    conn.commit()
    return 'done'

def remove_product(item_sku):
    query = f"DELETE FROM INVENTORYITEM WHERE item_sku={item_sku}"
    cur.execute(query)
    conn.commit()
    return "done"




# def create_table():
#     create_table_query = """
#     CREATE TABLE Transaction (
#     t_ID INT PRIMARY KEY,
#     c_ID INT NOT NULL,
#     s_ID INT NOT NULL,
#     Item_SKU INT NOT NULL,
#     t_date TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
#     t_amount DECIMAL(10, 2) NOT NULL,
#     t_category VARCHAR(100),
#     FOREIGN KEY (c_ID) REFERENCES Customer(c_ID),
#     FOREIGN KEY (s_ID) REFERENCES Staff(s_ID),
#     FOREIGN KEY (Item_SKU) REFERENCES InventoryItem(Item_SKU)
# );"""
#     cur.execute(create_table_query)
#     print('done')
#     conn.commit()
#     conn.close()