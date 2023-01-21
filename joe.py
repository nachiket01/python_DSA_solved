d = {0:["","",0,0,0],
     1:["nachiket","Tekade",98,67,65],
     2:["Leonardo","vinci",99,97,95],
     3:["Henry","Ford",70,97,95],
     4:["Nikola","Tesla",99,97,48],
     5:["sarabhai","patel",99,97,55],
     6:["Rishabh","Pant",99,97,65],
     7:["Pat","Cummins",99,87,95],
     8:["Abdul","Kalam",96,97,95],
     9:["Ratan ","Tata",94,77,95],
    10:["C","raman",99,97,93],
    11:["Vipin","rawat",99,97,99],
    12:["Yogi","adityanath",99,97,55],
    13:["Narendar","Modi",99,91,95],
    14:["Valdmir","Pune",99,97,25],}

def calculate_percentage(d):
    print("enter Roll number of students ")
    temp  = int(input())
    if temp < len(d) and temp > 0:    
        ls = d[temp][2:5]
        ans = sum(ls)/3
        return ans,d[temp][0],d[temp][1]
    else:
        temp = 0
        return 0,d[temp][0],d[temp][1]

def validate_percentage(d):
    percentage,first_name, last_name = calculate_percentage(d)
    
    if percentage == 0 :
        return "Please enter valid number"

    if percentage >= 80:
        return f"{first_name} {last_name} Passed with A Grade"
    elif percentage >= 60 and percentage < 80:
        return f"{first_name} {last_name} Passed with B Grade"

    elif percentage >= 40 and percentage < 60:
        return f"{first_name} {last_name} Passed with C Grade"

    else:
        return f"{first_name} {last_name} Falied with F Grade"


print(validate_percentage(d))

