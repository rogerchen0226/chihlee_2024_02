try:
    height = float(input("請輸入您的身高(公分)"))
    if height > 300 or height <= 0:
        raise Exception("身高須以公分為單位並在0~300範圍內")            
    weight = float(input("請輸入您的體重(公斤)"))
    if weight <= 0:
        raise Exception("體重須以公斤為單位並大於0")
    gender = input("請輸入您的性別（男/女）：").strip()
    BMI = weight/(height/100) ** 2
    print(f'BMI = {BMI:.1f}')

    if gender == "男":
        if BMI < 20:
            category = "體重過輕"
        elif 20 <= BMI < 24:
            category = "正常範圍"
        elif 24 <= BMI < 27:
            category = "過重"
        elif 27 <= BMI < 30:
            category = "輕度肥胖"
        elif 30 <= BMI < 35:
            category = "中度肥胖"
        else:
            category = "重度肥胖"
    elif gender == "女":
        if BMI < 18:
            category = "體重過輕"
        elif 18 <= BMI < 22:
            category = "正常範圍"
        elif 22 <= BMI < 25:
            category = "過重"
        elif 25 <= BMI < 30:
            category = "輕度肥胖"
        elif 30 <= BMI < 35:
            category = "中度肥胖"
        else:
            category = "重度肥胖"
    else:
        category = "性別輸入錯誤"

    # 輸出體重類別
    if category != "性別輸入錯誤":
        print(f"範圍：{category}")
    else:
        print(category)
except ValueError:
    print("輸入格式有錯")
except Exception as e:
    print(f'錯誤訊息:{e}')
