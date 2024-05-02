text="""
 I have two daily routine- one for holiday and other for the days when I go to school.
My school starts at 7:30 a.m. and I reach home at 2 p.m. Firstly I have a bath and
take my lunch and then sleep for two hours. Sleeping in afternoon is a good idea. I
feel very fresh in the evening. It is like having two mornings in a day. From 5 p.m.
to 6 p.m. I do my home work. Then I go out to play with my friends. After coming back
I complete my remaining homework. I enjoy some TV serials at night. After dinner, I sleep 
at around 10 p.m. During holidays, I rose early and go for morning walk. I also like to 
watch matinee movie. It refreshes me for the coming week. I love to maintain a balance 
between studies and play.
"""
text = text.replace(".", " ")
text = text.replace(",", " ")
text = text.replace("'s", " ")
text = text.lower()
print(text)
word_list = text.split()
word_count = {}
for i in range(len(word_list)):
    count = 0
    for j in range(len(word_list)):
        if word_list[i] == word_list[j]:
            count += 1
    word_count[word_list[i]] = count
print("Tần suất xuất hiện của các từ trong đoạn văn là:")
print(word_count)
print("Số lượng từ trong đoạn văn là:", len(word_count))
cac_tu=text.split()
tu_dem={}
for tu in cac_tu:
    if tu in tu_dem:
        tu_dem[tu]+=1
    else:
        tu_dem[tu]=1
tu_nhieu_nhat=max(tu_dem,key=tu_dem.get)
tu_it_nhat=min(tu_dem,key=tu_dem.get)
print("Từ xuất hiện nhất là'{}' với {} lần xuất hiện".format(tu_nhieu_nhat,tu_dem[tu_nhieu_nhat]))            
print("Từ xuất hiện ít nhất là'{}' với {} lần xuẩ hiện".format(tu_it_nhat,tu_dem[tu_it_nhat]))