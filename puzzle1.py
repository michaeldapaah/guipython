# n, count = 5, 0
# for _ in range(n):
#     n -= 1
#     count +=1
# print(count) answer is 5
#

# s = 'abc'
# for _ in range(1):
#     s = tuple(s)
# print(s)
# print(len(s)) answer is 3

# t = [1,2,3,4]
# x = t.pop() > t.pop() > t.pop()
# t.append(x)
# print(len(t)) answer is 2


# spam = ['cat','bat','rat','elephant']
# alphabet = ['x','y','z']
# del spam[2]
# print(spam[0][1])

# catNames = []
# while True:
#     print('Enter the name of the cat' + str(len(catNames) + 1) + "(or enter nothing to stop.'):")
#     name = input()
#     if name == '':
#         break
#     catNames = catNames + [name]
# print('The cat names are:')####
# for name in catNames:
#     print(' ' + name)


# catName = []
# while True:
#     print("Enter the name of the cat" + str(len(catName) + 1) + 'or press enter to exit:')
#     name = input()
#     if name == '':
#         break
#     catName = catName + [name]  # list concatenation
# print('The cat names are:')
# for name in catName:
#     print(' ' + name)


# supplies = ['pens', 'staplers', 'flame-throwers', 'binders']
# for i in range(len(supplies)):
#     print('INDEX ' + str(i) + ' in supplies is ' + supplies[i])

# myPets = ['Zophie', 'Pooka', 'Fat-tail']
# while True:
#     print('Enter a pet name')
#     name = input()
#     if name not in myPets:
#         print('I do not have a pet named ' + name)
#     else:
#         print(name + 'is my pet')


# cat = ['fat', 'black', 'loud']
# size, color, disposition = cat
#
# cat.append('Mouse')
# cat.insert(1, 'whity')
# cat.remove('whity')
# cat.sort(reverse=True)
# cat.sort(key=str.lower)
# print(cat)








# import random
#
# messages = ['It is certain', 'It is decidely so','Yes definitely', 'Reply hazy try again', 'Ask again later', 'Concentrate and ask again', 'My reply is no', 'Outlook not so good', 'Very doubtful']
# while True:
#     print(messages[random.randint(0, len(messages) - 1)])
#     break


class GameCharacter:

    weight = 90
    hair_color = 'black'
    height = 190
    name = 'michael'

    def say(self):
        print(f'Hello, My name is {GameCharacter.name}')

michael = GameCharacter()

print("Michael's Name: ", michael.name)
print("Michael's Hair color: ", michael.hair_color)
print("Michael is saying: ", michael.say())