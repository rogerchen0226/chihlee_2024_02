try:

    height_cm = float(input("請輸入身高(公分)"))
    if height_cm <= 0:
        raise Exception("輸入身高格式錯誤")
    weight = float(input("請輸入體重(公斤)"))
    if weight <= 0:
        raise Exception("輸入體重格式錯誤")
    height_m = float(height_cm)/100
    BMI = weight/height_m ** 2
    print(f"BMI值:{BMI}")
    if BMI >= 35:
        print("重度肥胖")
    elif BMI >= 30:
        print("中度肥胖")
    elif BMI >= 27:
        print("輕度肥胖")
    elif BMI >= 24:
        print("過重肥胖")
    elif BMI >= 18.5:
        print("健康體重")
except ValueError:
    print("輸入格式錯誤")
except Exception as e:
    print(f"錯誤說明:{e}")
except Exception:
    print("不可預期的錯誤")
print("結束BMI運算程式")
