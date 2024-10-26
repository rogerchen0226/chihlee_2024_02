import paho.mqtt.client as mqtt
from datetime import datetime
import os,csv
import sqlite3
from sqlite3 import Error

def insert_to_sqlite(values):
    try:
        conn = sqlite3.connect('./data/pico.db')
        print(conn)
        print(sqlite3.version)
    except Error as e:
        return
    sql = """
        INSERT INTO 雞舍 (時間,設備,值)
        VALUES (?,?,?);
    """
    cursor = conn.cursor()
    print(values)
    cursor.execute(sql,(values))
    conn.commit()
    cursor.close()
    conn.close()

def record(date:str,topic:str,value:str):
    '''
    # 檢查是否有data資料夾,如果沒有就建立data資料夾
    # 檢查是否有今天的檔案,如果沒有今天日期的.csv就建立今天日期的.csv,並寫入資料
    # parameters date:str -> 日期
    #            topic:str -> 主題
    #            value:str -> 值
    '''
    root_dir = os.getcwd()
    data_dir = os.path.join(root_dir, 'data')
    if not os.path.isdir(data_dir):    
            os.mkdir('data')
    
    today = datetime.today()
    filename = today.strftime("%Y-%m-%d") + ".csv"
    #get_file_abspath
    full_path = os.path.join(data_dir,filename)
    if not os.path.exists(full_path):
        #沒有這個檔,建立檔案
        print('沒有這個檔')
        with open(full_path,mode='w',encoding='utf-8',newline='') as file:
            file.write('時間,設備,值\n')
    
    with open(full_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([date,topic,value])
        insert_to_sqlite([date,topic,float(value)])


def on_connect(client, userdata, flags, reason_code, properties):
    print("Connected with result code " + str(properties))
    #連線bloker成功時,只會執行一次
    client.subscribe("SA-21/#")
    

def on_message(client, userdata, msg):
    global led_origin_value # 宣告全域變數
    global temp_origin_value # 宣告全域變數
    global light_origin_value # 宣告全域變數

    topic = msg.topic
    value = msg.payload.decode()
    #print(f"topic '{topic}' value '{value}' type '{type(value)}'")
    if topic == "SA-21/LED_LEVEL":
        led_value = int(value)
        if led_value != led_origin_value:
            led_origin_value = led_value
            print(f"led_value '{led_value}' ")
            today = datetime.today()
            now_str = today.strftime('%Y-%m-%d %H:%M:%S')
            #save_str = [now_str, topic,led_value]
            record(now_str,topic,led_value)

    if topic == "SA-21/TEMP":
        temp_value = "{:.2f}".format(round(float(value),ndigits=2))
        if temp_value != temp_origin_value:
            temp_origin_value = temp_value
            print(f"temp_value '{temp_value}' ")
            today = datetime.today()
            now_str = today.strftime('%Y-%m-%d %H:%M:%S')
            #save_str = [now_str, topic,temp_value]
            record(now_str,topic,temp_value)

    if topic == "SA-21/LIGHT":
        light_value = int(value)
        if light_value != light_origin_value:
            light_origin_value = light_value
            print(f"light_value '{light_value}' ")
            today = datetime.today()
            now_str = today.strftime('%Y-%m-%d %H:%M:%S')
            #save_str = [now_str, topic,temp_value]
            record(now_str,topic,light_value)

    #print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

def main():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    # 設定用戶名和密碼
    username = "pi"  # 替換為您的用戶名
    password = "raspberry"  # 替換為您的密碼
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message 
    client.connect("192.168.0.252", 1883, 60)
    client.loop_forever()


if __name__ == "__main__":
    led_origin_value = 0
    temp_origin_value = 0.0
    light_origin_value = 0
    main()
