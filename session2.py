#EX 1
#name = input("Insert name:")
#rate = int(input("Insert rate:"))
#gajiKotor = str(rate * 90)
#print("My name is" , name, "and my pay is", gajiKotor)

#EX 2
#2.1
#print("My name is Ray")
#2.2
#print("Python's is easy, bro")
#2.3
#print('"Guk guk guk", aku mendegar suara anjing hitam itu"')
#2.4
#numOne = float(input("Insert first number:"))
#numTwo = float(input("Insert second number:"))
#numThree = float(input("Insert third number:"))
#
#result1 = numOne + numTwo * numThree
#result2 = numOne / numTwo - numThree
#result3 = numOne + numTwo * numThree
#result4 = (numOne + numTwo) * numThree
#result5 = numOne / (numTwo - numThree)
#result6 = numOne + numTwo * numThree
#
#results = [result2, result3, "example", result4, result4, result5]
#results.insert(0, result1)
#results.pop(4)
#results.remove("example")
#results.append(result6)
#
#for item_result in results:
#    print(format(item_result,"13,.2f"))
#
#print("There are a total of", len(results), "results")

#2.5
#firstNum = float(input("Input first number:"))
#secondNum = float(input("Input second number:"))
#thirdNum = float(input("Input third number:"))
#
#numbers = [firstNum, secondNum, thirdNum]
#sumNumbers = 0
#
#for value in numbers:
#    sumNumbers += value
#
#mean = sumNumbers/len(numbers)
#print(mean)

#2.6
#fruits = ("apel", "pisang", "mangga", "jeruk", "anggur")
#otherFruits = (fruits[1], fruits[3])
#print(otherFruits)

#2.7
#mahasiswa = {"Budi" : 85, "Siti" : 90, "Andi" : 78}
#for x in mahasiswa:
#    print("Name:", x, "Age:", mahasiswa[x])

#EX 
#meanRating = int(input("Insert mean rating:"))
#
#if meanRating > 90:
#    finalRating = "A"
#if meanRating > 80 and meanRating <= 90:
#    finalRating = "B"
#if meanRating > 70 and meanRating <=80:
#    finalRating = "C"
#if meanRating <= 70: 
#    finalRating = "D"
#
#if finalRating == "A" or "B" or "C":
#    conclusion = "layak di bayar mahal"
#if finalRating == "D":
#    conclusion = "tidak layak dibayar mahal"
#
#print(str(meanRating))
#print("Final rating is", finalRating, "so", conclusion)

