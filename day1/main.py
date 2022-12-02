filename = "/Users/imiller/Desktop/non-anduril/aoc22/day1/input.txt"

def generate_elf_list():
    finalList = []
    best = 0
    localTotal = 0
    for line in open(filename):
        listWords = line.split("\t")
        try:
            num = int(listWords[0])
            localTotal += num
        except:
            if localTotal > best:
                best = localTotal
            finalList.append(localTotal)
            localTotal = 0
        
    return finalList

elf_cal_list = generate_elf_list()
num1 = max(elf_cal_list)
elf_cal_list.remove(num1)
num2 = max(elf_cal_list)
elf_cal_list.remove(num2)
num3 = max(elf_cal_list)

top3 = [num1, num2, num3]
print("Top elf calories:", num1)
print("Top 3 elf calories combined:", sum(top3))


