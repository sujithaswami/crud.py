
#create

attendees = ["sujitha", "anusha", "madhuha"]
attendees.append("delip")
attendees.append("anusha")
print(attendees)
attendees.insert(3 ,"ramya")
#read
print(attendees.index("ramya"))
print(attendees.count("anusha"))
print(attendees.count("durga"))
if(attendees.count("durga")>0):
    print(attendees.index("durga"))
#update
attendees1 = ["sri", "raji", "kusuma"]
print(attendees1)
lst = []
lst.append('aa')
print(lst)
attendees.extend(lst)
print(attendees)
#delete
attendees.remove('sujitha')
print(attendees)
attendees.pop()
attendees.pop()
print(attendees)
attendees.pop(4)
print(attendees)





