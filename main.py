from random import *
users = ('좋아요!','안좋아요ㅠㅠ','보통이에요!','너무 좋아요!','너무 안좋아요')

users = list(users)



print(users)
shuffle(users)
print(users)

winners = sample(users,1)
print("--오늘 하루 운세보기--")

print("오늘의 운세 : {0}".format(winners[0]))

