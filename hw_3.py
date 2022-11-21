#แทนค่่าเช่าแต่ละรายการ
cost_1,cost_2,cost_3,cost_4 = input().split()
cost_1 = int(cost_1)
cost_2 = int(cost_2)
cost_3 = int(cost_3)
cost_4 = int(cost_4)

#หนังสือนิยาย จ-ศ
book_1_1,book_1_2,book_1_3,book_1_4,book_1_5 = input().split()
book_1_1 = int(book_1_1)
book_1_2 = int(book_1_2)
book_1_3 = int(book_1_3)
book_1_4 = int(book_1_4)
book_1_5 = int(book_1_5)

#หนังสือสารคดี จ-ศ
book_2_1,book_2_2,book_2_3,book_2_4,book_2_5 = input().split()
book_2_1 = int(book_2_1)
book_2_2 = int(book_2_2)
book_2_3 = int(book_2_3)
book_2_4 = int(book_2_4)
book_2_5 = int(book_2_5)

#หนังสือท่องเที่ยว จ-ศ
book_3_1,book_3_2,book_3_3,book_3_4,book_3_5 = input().split()
book_3_1 = int(book_3_1)
book_3_2 = int(book_3_2)
book_3_3 = int(book_3_3)
book_3_4 = int(book_3_4)
book_3_5 = int(book_3_5)

#หนังสือการ์ตูน จ-ศ
book_4_1,book_4_2,book_4_3,book_4_4,book_4_5 = input().split()
book_4_1 = int(book_4_1)
book_4_2 = int(book_4_2)
book_4_3 = int(book_4_3)
book_4_4 = int(book_4_4)
book_4_5 = int(book_4_5)

#หนังสือเล่มแต่ละวัน
day_1 = book_1_1+book_2_1+book_3_1+book_4_1
day_2 = book_1_2+book_2_2+book_3_2+book_4_2
day_3 = book_1_3+book_2_3+book_3_3+book_4_3
day_4 = book_1_4+book_2_4+book_3_4+book_4_4
day_5 = book_1_5+book_2_5+book_3_5+book_4_5

#ราคาแต่ละวัน
cost_day_1 = (cost_1*book_1_1)+(cost_2*book_2_1)+(cost_3*book_3_1)+(cost_4*book_4_1)
cost_day_2 = (cost_1*book_1_2)+(cost_2*book_2_2)+(cost_3*book_3_2)+(cost_4*book_4_2)
cost_day_3 = (cost_1*book_1_3)+(cost_2*book_2_3)+(cost_3*book_3_3)+(cost_4*book_4_3)
cost_day_4 = (cost_1*book_1_4)+(cost_2*book_2_4)+(cost_3*book_3_4)+(cost_4*book_4_4)
cost_day_5 = (cost_1*book_1_5)+(cost_2*book_2_5)+(cost_3*book_3_5)+(cost_4*book_4_5)

#เช็คว่าวันไหนมากสุดให้แสดงวันนั้น
if day_1>=day_2 and day_1>=day_3 and day_1>=day_4 and day_1>=day_5:
    print("Mon",day_1)
    print(cost_day_1,cost_day_2,cost_day_3,cost_day_4,cost_day_5)
elif day_2>=day_1 and day_2>=day_3 and day_2>=day_4 and day_2>=day_5:
    print("Tues",day_2)
    print(cost_day_1,cost_day_2,cost_day_3,cost_day_4,cost_day_5)
elif day_3>=day_1 and day_3>=day_2 and day_3>=day_4 and day_3>=day_5:
    print("Wed",day_3)
    print(cost_day_1,cost_day_2,cost_day_3,cost_day_4,cost_day_5)
elif day_4>=day_1 and day_4>=day_2 and day_4>=day_3 and day_4>=day_5:
    print("Thu",day_4)
    print(cost_day_1,cost_day_2,cost_day_3,cost_day_4,cost_day_5)
elif day_5>=day_1 and day_5>=day_2 and day_5>=day_3 and day_5>=day_4:
    print("Fri",day_5)
    print(cost_day_1,cost_day_2,cost_day_3,cost_day_4,cost_day_5)



