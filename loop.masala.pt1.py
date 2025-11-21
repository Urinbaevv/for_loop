#1-masala
# for i in range(1, 11):
#     print(i)

#2-masala
# ismlar = ["Ali", "Vali", "Hasan", "Malika", "Zuhra"]
# print("Do'stlarim:")
# for ism in ismlar:
#     print(f"Salom, {ism}!")

#3-masala
#for i in range(2, 101, 2):
#    print(i, end=' ')
#print()

#4-masala
# son = 0
# for son1 in range(1,51):
#     son = son + son1
#     print(son)

#5-masala
# matn = input("Matn kiriting: ")
# uzunlik = 0
# for belgi in matn:
#     uzunlik = uzunlik + 1
# print(f"Matn uzunligi: {uzunlik} belgi")

#6-masala
# start = 1
# end = 50
# count = 0
# found = []
# for n in range(start, end + 1):
#     if n % 3 == 0:
#         found.append(str(n))
#         count += 1
# print("1 dan 50 gacha 3 ga bo'linadigan sonlar:")
# print(" ".join(found))
# print()
# print(f"Jami: {count} ta son")

#7-masala
# matn = input("\nMatn kiriting: ")
# unlilar = "aeiouаеёиоуыэюя"
# sanoq = 0
# for belgi in matn.lower():
#     if belgi in unlilar:
#         sanoq = sanoq + 1
#     print("Jami  unli harflar:", sanoq, "ta")

#8-masala
# sonlar = [23, 67, 12, 89, 45, 34, 91, 56, 78]
# eng_katta = sonlar[0]
# for son in sonlar:
#     if son < eng_katta:
#         eng_katta = son
#         print(f"Yangi eng katta son:{eng_katta}")
#     print(f"listdagi eng katta son: {eng_katta}")

#9-masala
# son = input("Son kiritng: ")
# son = son.lstrip('-')
# yigindi = 0
# for raqam in son:
#      yigindi += int(raqam)
# print(f"Raqamlar yig'indisi: {yigindi}")

#10-masala
# son = int(input("Son kiritng (faktorial): "))
# if son < 0:
#     print("Manfiy sonni faktoriali aniqlandi")
# else:
#     fakt = 1
#     for i in range(1, son + 1):
#         fakt = fakt * i
#     print(son, "ning faktorili =", fakt)

#11-masala
# def print_multiplication_table(rows=10, cols=10):
#     title = "MULTIPLIKATSIYA JADVALI"
#     row_label_width = 3
#     cell_width = 5
#     print(title)
#     total_width = row_label_width + 3 + cols * cell_width
#     print("=" * total_width)

##12-masala
# balandlik = int(input("Piramida balandligini kiriting: "))
# print("\n YULDUZLI PIRAMIDA\n")
# for qator in range(1, balandlik + 1):
#     # Bo'sh joylar
#     for _ in range(balandlik - qator):
#         print(" ", end="")
#     # Yulduzchalar
#     for _ in range(2 * qator - 1):
#         print("*", end="")
#     print()

##13-masala
#a = 0
#b = 1
# print("Fibonachchining birinchi 10 ta soni:")
# for _ in range(10):
#     print(a, end=" ")
#     a, b = b, a + b

##14-masala
# print("1 dan 100 gacha tub sonlar:")
# tub_sonlar = []
# for son in range(2, 101):
#     tub = True
#     for boluvchi in range(2, son):
#         if son % boluvchi == 0:
#             tub = False
#             break
#     if tub:
#         tub_sonlar.append(son)
# for s in tub_sonlar:
#     print(s, end=" ")
# print("\nJami:", len(tub_sonlar), "ta tub son")

##15-masala
# print("Raqamli soat simuliyatori")
# print("========================================")
# sanash = 0
# for soat in range(24):
#     for minut in range(60):
#         for sekund in range(60):
#             print(f"{soat:02d}:{minut:02d}:{sekund:02d}")
#             sanash += 1
# print("\nJami:", sanash, "ta vaqt")