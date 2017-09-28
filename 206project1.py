import os
import filecmp
from datetime import date

def getData(file):
	a = open(file, 'r+')
	ab = a.read()
	ab = ab.split()
	heading = ab[0]
	nonheading = ab[1:]
	allinfo = []
	for i in nonheading:
		newdict = {}
		asdf = i.split()
		nohead = i.split(',')
		heads = heading.split()
		aish = heads[0].split(',')
		for j in range(len(aish)):
			newdict[aish[j]] = nohead[j]
		allinfo.append(newdict)
	return allinfo



#Sort based on key/column
def mySort(data,col):
	final = sorted(data, key=lambda x: x[col])
	yolo = (final[0]["First"] + " " + final[0]["Last"])
	return yolo


#Create a histogram
def classSizes(data):
	aish = {}
	aish["Senior"] = 0
	aish["Junior"] = 0
	aish["Sophomore"] = 0
	aish["Freshman"] = 0
	for i in data:
		aish[i["Class"]] += 1
	final = sorted(aish.items(), key = lambda x:x[1], reverse = True)
	return final


# Find the most common day of the year to be born
def findDay(a):
	dates = {}
	for i in a:
		date = i["DOB"]
		if date[-5] and date[-7] == '/':
			finalDate = date[-6]
			finalDate = int(finalDate)
			if finalDate not in dates:
				dates[finalDate] = 0
			dates[finalDate] += 1
		else:
			finalDate = date[-7:-5]
			finalDate = int(finalDate)
			if finalDate not in dates:
				dates[finalDate] = 0
			dates[finalDate] += 1
	final = sorted(dates.items(), key = lambda x:x[1], reverse = True)
	return final[0][0]



# Find the average age (rounded) of the Students
def findAge(a):
	total = []
	for p in a:
		yearF = int(p['DOB'][-4:])
		if p['DOB'][1] == '/':
			monthF = int(p['DOB'][0])
		else:
			monthF = int(p['DOB'][:2])
		if p["DOB"][-5] and p["DOB"][-7] == '/':
			dateF = int(p['DOB'][-6])
		else:
			dateF = int(p['DOB'][-7:-5])
		today = date.today()
		age = today.year - yearF - ((today.month, today.day) < (monthF, dateF))
		total.append(age)
	aish = sum(total)
	aish = float(aish)
	leng = len(total)
	final = aish/leng
	return(round(final))

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
	final = sorted(a, key=lambda x: x[col])
	outfile = open(fileName, "w")
	for i in final:
		outfile.write("{},{},{},\n".format(i["First"],i["Last"],i["Email"]))
	outfile.close()




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)

	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()
