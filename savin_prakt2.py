print("Здравствуйте")
print("Назовите первый вид рода человек (homo)")
vid=input()
print("... второй вид")
vid2=input()
print("... третий ...")
vid3=input()
print("... четвертый ...")
vid4=input()
print("... пятый ...")
vid5=input()
print("... шестой ...")
vid6=input()
print("... седьмой ...")
vid7=input()
print("... восьмой ...")
vid8=input()
print("... и последний (на данный момент)")
vid9=input()


print()
print("Ваш ответ: ")
print(vid,vid2,vid3,vid4,vid5,vid6,vid7,vid8,vid9,sep="=>")

print()
print("Правильный ответ: ")
print("rudolfensis=>habilis=>ergaster=>erectus=>antecessor=>heidelbergensis=>denisovensis->neanderthalensis=>sapience(idaltu, sapience)")

# Хотя более правильно использовать цикл while, что-то типа такого:
# vid = ""
# i=0
# while i<9:
#     print("Назовите ",i+1,"-й вид рода человек")
#     vid=vid+input()+"=>"
#     i=i+1
# print(vid)
#
# Но мы этого ещё не проходили )
