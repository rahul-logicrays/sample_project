import requests

data = requests.get("http://www.pythonchallenge.com/pc/def/ocr.html")

find_rare =data.text.split("<!--")[-1].replace("-->",'')

data ={}
for d in find_rare:
    if d in data.keys():
        data[d]+=1
    else:
        data[d]=1

print(data)

minimum_value = min(data.values())

#get keys with minimal value using list comprehension
minimum_keys = [key for key in data if data[key]==minimum_value]

#print the minimum keys
print("".join(minimum_keys))
print("".join(minimum_keys))
print("======================================================")
# data_list =[]
# if 1 in data.values():
    
#     data_list.append()


