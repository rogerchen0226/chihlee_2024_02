import widget # 匯入tools.py檔案

while True:
    kg = 0  # 清除變數
    cm = 0  # 清除變數
    cm, kg = widget.input_data()  # 呼叫function

    print(f'身高={cm},體重={kg}')

    BMI = widget.calculate_bmi(cm1=cm, kg1=kg)

    print(f'BMI={BMI}')
    print(widget.get_status(BMI))

    play_again = input("還要繼續嗎?(y,n)")
    if play_again == "n":
        break
print('程式結束')
