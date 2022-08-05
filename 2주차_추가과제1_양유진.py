word_list = list(str(input().lower()))

dic = dict()
for al in word_list:
    try: dic[al] = dic[al] + 1
    except: dic[al] = 1

max_key =  max(dic, key = dic.get)
all_values = dic.values()

count = 0
for key, value in dic.items():
 if value == max(all_values):
  count = count + 1

if(count > 1):
    print("?")
else:
    print(max_key.upper())
