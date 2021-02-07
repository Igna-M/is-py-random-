import random
import statistics

def randomList():
    randNumbers = []
    for i in range(1501):
        number = random.randint(0, 9)
        randNumbers.append(str(number))
    return randNumbers

def separate(string):
    str0 = string.count('0')
    str1 = string.count('1')
    str2 = string.count('2')
    str3 = string.count('3')
    str4 = string.count('4')
    str5 = string.count('5')
    str6 = string.count('6')
    str7 = string.count('7')
    str8 = string.count('8')
    str9 = string.count('9')
    listOfDigits = [str0, str1, str2, str3, str4, str5, str6, str7, str8, str9]
    print(listOfDigits)
    analysis(listOfDigits)

def analysis(theList):
    larger.append(max(theList))
    smaller.append(min(theList))
    allMedian.append(statistics.median(theList))
    allDev.append(round(statistics.stdev(theList), 1))

smaller = []
larger = []
allMedian = []
allDev = []

'''###### ###### ###### ###### ###### ###### ###### ###### '''

pi_1500 = "3141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117067982148086513282306647093844609550582231725359408128481117450284102701938521105559644622948954930381964428810975665933446128475648233786783165271201909145648566923460348610454326648213393607260249141273724587006606315588174881520920962829254091715364367892590360011330530548820466521384146951941511609433057270365759591953092186117381932611793105118548074462379962749567351885752724891227938183011949129833673362440656643086021394946395224737190702179860943702770539217176293176752384674818467669405132000568127145263560827785771342757789609173637178721468440901224953430146549585371050792279689258923542019956112129021960864034418159813629774771309960518707211349999998372978049951059731732816096318595024459455346908302642522308253344685035261931188171010003137838752886587533208381420617177669147303598253490428755468731159562863882353787593751957781857780532171226806613001927876611195909216420198938095257201065485863278865936153381827968230301952035301852968995773622599413891249721775283479131515574857242454150695950829533116861727855889075098381754637464939319255060400927701671139009848824012858361603563707660104710181942955596198946767837449448255379774726847104047534646208046684259069491293313677028989152104752162056966024058038150193511253382430035587640247496473263914199272604269922796782354781636009341721641219924586315030286182974555706749838505494588586926995690927210797509302955"

results = []

# print("Pi Original:")
separate(pi_1500)

for i in range(50):
    oneList = randomList()
    # print('')
    # print("Lista:", i+1)
    separate(oneList)


print('Smaller:', smaller)
print('Larger:', larger)
print('Meadian:', allMedian)
print('Deviation:', allDev)