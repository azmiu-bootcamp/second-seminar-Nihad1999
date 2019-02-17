Student: Nihad abdulla
  3- cu mesele



import  time

""" localtime """

sunday = 0
monday = 1
tuesday = 2
wednesday = 3
thursday = 4
friday = 5
saturday = 6

hour = 00
minute =00

day = int(input("0 - dan 6-ya qeder reqem daxil edin:-> "))

vocation = bool(input())

while True:
 if vocation == False and day == 0 or day == 1 or day == 2 or day == 3 or day == 4:
        hour = 7
        minute = 0
        break
 elif vocation == False and day == 5 or day == 6:
     hour = 10
     minute = 0
     break

 elif vocation == True and day == 0 or day == 1 or day == 2 or day == 3 or day == 4:
        hour = 10
        minute = 0
        break



 else:
     print("Bu gun tetildir. Dincelin")
     break


print(vocation)
print(minute)


while True:
    saat = time.localtime(time.time())
    if hour == saat.tm_hour and minute == saat.tm_min:
        print("Alarm caldi!\nSaat", saat.tm_hour, ":", saat.tm_min)
        break
    else:

        pass

print("Dongu bitdi")


