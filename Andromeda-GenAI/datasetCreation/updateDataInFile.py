import re

def main():

    newData = ""

    customers = """
1001,32,M,Married,80000,Engineer,750,10000,Savings--Home Loan,5000,20000,Yes,Yes,Health--Life,Mutual Funds,High,Balanced,New York,Moderate
1002,45,F,Single,120000,Business Owner,650,50000,Savings--Credit Card,10000,5000,No,Yes,Health--Life--Auto,Stocks,Medium,Aggressive,Chicago,High
1003,29,F,Married,60000,Teacher,720,15000,Savings--Personal Loan,3000,10000,No,No,Health,Mutual Funds,Medium,Conservative,Boston,Low
1004,54,M,Divorced,150000,Doctor,800,20000,Savings--Home Loan--Credit Card,20000,30000,Yes,Yes,Health--Life--Home,Stocks--Bonds,High,Moderate,San Francisco,High
1005,38,M,Single,70000,IT Professional,680,10000,Savings--Credit Card,7000,15000,No,Yes,Health--Auto,Mutual Funds,Medium,Moderate,Austin,Moderate
1006,27,F,Married,90000,Lawyer,750,0,Savings,15000,25000,Yes,No,Health--Life,Stocks,High,Aggressive,Seattle,High
1007,43,M,Married,110000,Architect,690,30000,Savings--Home Loan,5000,10000,Yes,Yes,Health--Life--Home,Mutual Funds--Bonds,Medium,Conservative,Denver,Moderate
1008,35,F,Single,50000,Sales Representative,720,5000,Savings--Credit Card,2000,5000,No,No,Health,Stocks,Medium,Aggressive,Miami,High
1009,30,M,Single,80000,Engineer,740,20000,Savings--Car Loan,8000,20000,Yes,Yes,Health--Auto,Mutual Funds--Stocks,High,Balanced,Los Angeles,Moderate
1010,50,F,Married,130000,Manager,650,15000,Savings--Home Loan--Credit Card,10000,30000,Yes,Yes,Health--Life--Home,Stocks--Bonds,Medium,Aggressive,Chicago,High
1011,28,M,Single,55000,Graphic Designer,710,5000,Savings--Personal Loan,4000,8000,No,No,Health,Mutual Funds,Medium,Conservative,Houston,Low
1012,47,F,Divorced,95000,Real Estate Agent,680,30000,Savings--Home Loan,5000,10000,Yes,Yes,Health--Life,Stocks,Medium,Moderate,Boston,Moderate
1013,31,F,Married,75000,Marketing Specialist,740,10000,Savings--Credit Card,7000,15000,No,No,Health--Auto,Mutual Funds,High,Balanced,New York,Moderate
1014,52,M,Married,140000,Consultant,800,25000,Savings--Home Loan--Credit Card,15000,35000,Yes,Yes,Health--Life--Home,Stocks--Bonds,High,Moderate,San Francisco,High
1015,36,F,Single,65000,HR Manager,720,5000,Savings--Personal Loan,6000,12000,No,Yes,Health,Mutual Funds,Medium,Aggressive,Chicago,High
1016,29,M,Single,90000,Software Developer,750,15000,Savings--Car Loan,8000,20000,No,Yes,Health--Auto,Stocks--Mutual Funds,High,Balanced,Denver,Moderate
1017,42,F,Married,115000,Pharmacist,700,20000,Savings--Home Loan,5000,15000,Yes,Yes,Health--Life--Home,Mutual Funds--Bonds,Medium,Conservative,Seattle,Moderate
1018,34,M,Single,55000,Accountant,690,10000,Savings--Credit Card,3000,7000,No,No,Health,Stocks,Medium,Aggressive,Miami,High
1019,55,F,Married,150000,Engineer,750,25000,Savings--Home Loan--Credit Card,20000,40000,Yes,Yes,Health--Life--Home,Mutual Funds--Bonds,High,Moderate,Los Angeles,High
1020,27,M,Single,70000,Teacher,720,5000,Savings--Personal Loan,5000,10000,No,No,Health,Stocks,Medium,Balanced,Houston,Low
1021,48,F,Divorced,95000,Consultant,680,30000,Savings--Home Loan,6000,15000,Yes,Yes,Health--Life,Mutual Funds,Medium,Moderate,Boston,Moderate
1022,37,M,Married,80000,Sales Manager,740,10000,Savings--Credit Card,7000,15000,No,Yes,Health--Auto,Stocks,High,Balanced,New York,Moderate
1023,29,F,Single,60000,Nurse,730,5000,Savings--Personal Loan,4000,8000,No,No,Health,Mutual Funds,Medium,Conservative,Chicago,Low
1024,53,M,Married,125000,Doctor,800,20000,Savings--Home Loan--Credit Card,10000,25000,Yes,Yes,Health--Life--Home,Stocks--Bonds,High,Aggressive,San Francisco,High
1025,40,F,Single,70000,Engineer,680,10000,Savings--Credit Card,5000,10000,No,Yes,Health--Auto,Mutual Funds,Medium,Moderate,Denver,Moderate
1026,31,M,Married,85000,Software Developer,740,20000,Savings--Car Loan,8000,20000,Yes,Yes,Health--Life,Stocks--Mutual Funds,High,Balanced,Seattle,High
1027,46,F,Divorced,115000,Manager,720,30000,Savings--Home Loan,4000,10000,Yes,Yes,Health--Life--Home,Mutual Funds--Bonds,Medium,Conservative,Miami,Moderate
1028,28,M,Single,60000,Graphic Designer,710,5000,Savings--Personal Loan,3000,7000,No,No,Health,Stocks,Medium,Aggressive,Los Angeles,High
1029,49,F,Married,130000,Consultant,750,15000,Savings--Home Loan--Credit Card,10000,30000,Yes,Yes,Health--Life--Home,Mutual Funds--Bonds,High,Moderate,Houston,High
1030,35,M,Single,55000,Sales Representative,690,10000,Savings--Credit Card,2000,5000,No,No,Health,Stocks,Medium,Conservative,Boston,Low
1031,56,F,Married,150000,Engineer,800,25000,Savings--Home Loan--Credit Card,20000,40000,Yes,Yes,Health--Life--Home,Mutual Funds--Bonds,High,Aggressive,New York,High
1032,28,M,Single,70000,Teacher,720,5000,Savings--Personal Loan,5000,10000,No,No,Health,Stocks,Medium,Balanced,Chicago,Moderate
1033,47,F,Divorced,95000,Consultant,680,30000,Savings--Home Loan,6000,15000,Yes,Yes,Health--Life,Mutual Funds,Medium,Moderate,San Francisco,Moderate
1034,36,M,Married,80000,Sales Manager,740,10000,Savings--Credit Card,7000,15000,No,Yes,Health--Auto,Stocks,High,Balanced,Denver,High
1035,30,F,Single,60000,Nurse,730,5000,Savings--Personal Loan,4000,8000,No,No,Health,Mutual Funds,Medium,Conservative,Seattle,Low
1036,54,M,Married,125000,Doctor,800,20000,Savings--Home Loan--Credit Card,10000,25000,Yes,Yes,Health--Life--Home,Stocks--Bonds,High,Aggressive,Miami,High
1037,41,F,Single,70000,Engineer,680,10000,Savings--Credit Card,5000,10000,No,Yes,Health--Auto,Mutual Funds,Medium,Moderate,Los Angeles,Moderate
1038,32,M,Married,85000,Software Developer,740,20000,Savings--Car Loan,8000,20000,Yes,Yes,Health--Life,Stocks--Mutual Funds,High,Balanced,Houston,Moderate
1039,45,F,Divorced,115000,Manager,720,30000,Savings--Home Loan,4000,10000,Yes,Yes,Health--Life--Home,Mutual Funds--Bonds,Medium,Conservative,Boston,Moderate
1040,29,M,Single,60000,Graphic Designer,710,5000,Savings--Personal Loan,3000,7000,No,No,Health,Stocks,Medium,Aggressive,New York,High
1041,48,F,Married,130000,Consultant,750,15000,Savings--Home Loan--Credit Card,10000,30000,Yes,Yes,Health--Life--Home,Mutual Funds--Bonds,High,Moderate,Chicago,High
1042,37,M,Single,55000,Sales Representative,690,10000,Savings--Credit Card,2000,5000,No,No,Health,Stocks,Medium,Conservative,San Francisco,Low
1043,50,F,Married,150000,Engineer,800,25000,Savings--Home Loan--Credit Card,20000,40000,Yes,Yes,Health--Life--Home,Mutual Funds--Bonds,High,Aggressive,Denver,High
1044,27,M,Single,70000,Teacher,720,5000,Savings--Personal Loan,5000,10000,No,No,Health,Stocks,Medium,Balanced,Seattle,Moderate
1045,46,F,Divorced,95000,Consultant,680,30000,Savings--Home Loan,6000,15000,Yes,Yes,Health--Life,Mutual Funds,Medium,Moderate,Miami,Moderate
1046,34,M,Married,80000,Sales Manager,740,10000,Savings--Credit Card,7000,15000,No,Yes,Health--Auto,Stocks,High,Balanced,Los Angeles,High
1047,30,F,Single,60000,Nurse,730,5000,Savings--Personal Loan,4000,8000,No,No,Health,Mutual Funds,Medium,Conservative,Houston,Low
1048,53,M,Married,125000,Doctor,800,20000,Savings--Home Loan--Credit Card,10000,25000,Yes,Yes,Health--Life--Home,Stocks--Bonds,High,Aggressive,Boston,High
1049,39,F,Single,70000,Engineer,680,10000,Savings--Credit Card,5000,10000,No,Yes,Health--Auto,Mutual Funds,Medium,Moderate,New York,Moderate
1050,31,M,Married,85000,Software Developer,740,20000,Savings--Car Loan,8000,20000,Yes,Yes,Health--Life,Stocks--Mutual Funds,High,Balanced,Chicago,Moderate
1051,28,M,Single,65000,Software Developer,720,8000,Savings--Credit Card,3000,10000,No,No,Health,Stocks,High,Conservative,Boston,Moderate
1052,37,F,Married,90000,Teacher,680,20000,Savings--Home Loan,7000,15000,Yes,Yes,Life--Health,Mutual Funds,Medium,Balanced,San Francisco,Low
1053,50,M,Married,120000,Doctor,780,30000,Savings--Credit Card,15000,25000,Yes,Yes,Health--Life--Auto,Stocks--Bonds,High,Aggressive,Los Angeles,High
1054,23,F,Single,45000,Student,650,5000,Savings--Student Loan,2000,5000,No,No,None,Mutual Funds,Low,Conservative,Miami,Low
1055,40,M,Married,85000,Accountant,700,15000,Savings--Home Loan,8000,20000,Yes,Yes,Health,Real Estate,Medium,Balanced,Chicago,Moderate
1056,33,F,Single,75000,Marketing Manager,710,10000,Savings--Credit Card,5000,12000,No,Yes,Health--Life,Stocks,High,Aggressive,New York,High
1057,45,M,Married,110000,Lawyer,760,25000,Savings--Home Loan,12000,30000,Yes,Yes,Life--Auto,Stocks--Bonds,Medium,Balanced,Houston,Moderate
1058,27,F,Single,60000,Graphic Designer,690,7000,Savings--Credit Card,3500,8000,No,No,Health,Mutual Funds,High,Conservative,Seattle,Low
1059,39,M,Married,95000,Engineer,740,18000,Savings--Home Loan,9000,22000,Yes,Yes,Health--Life,Real Estate,Medium,Balanced,Denver,Moderate
1060,52,F,Married,130000,Architect,770,32000,Savings--Credit Card,16000,27000,Yes,Yes,Life--Health--Auto,Stocks--Bonds,High,Aggressive,San Diego,High
1061,30,M,Single,70000,Consultant,720,9000,Savings--Credit Card,4000,11000,No,No,Health,Mutual Funds,Medium,Conservative,Las Vegas,Low
1062,48,F,Married,105000,Pharmacist,750,23000,Savings--Home Loan,10000,24000,Yes,Yes,Life--Health,Real Estate,Medium,Balanced,San Antonio,Moderate
1063,35,M,Single,80000,IT Specialist,710,12000,Savings--Credit Card,6000,14000,No,Yes,Health--Life,Stocks,High,Aggressive,Phoenix,High
1064,41,F,Married,87000,Teacher,700,16000,Savings--Home Loan,8500,19000,Yes,Yes,Health,Mutual Funds,Medium,Balanced,Philadelphia,Moderate
1065,29,M,Single,65000,Graphic Designer,680,7000,Savings--Credit Card,3000,9000,No,No,None,Stocks,Low,Conservative,Orlando,Low
1066,38,F,Married,95000,Engineer,740,18000,Savings--Home Loan,9000,22000,Yes,Yes,Health--Life,Real Estate,Medium,Balanced,Denver,Moderate
1067,44,M,Married,110000,Financial Analyst,760,25000,Savings--Home Loan,12000,30000,Yes,Yes,Life--Auto,Stocks--Bonds,Medium,Balanced,Houston,Moderate
1068,26,F,Single,60000,Graphic Designer,690,7000,Savings--Credit Card,3500,8000,No,No,Health,Mutual Funds,High,Conservative,Seattle,Low
1069,39,M,Married,95000,Engineer,740,18000,Savings--Home Loan,9000,22000,Yes,Yes,Health--Life,Real Estate,Medium,Balanced,Denver,Moderate
1070,52,F,Married,130000,Architect,770,32000,Savings--Credit Card,16000,27000,Yes,Yes,Life--Health--Auto,Stocks--Bonds,High,Aggressive,San Diego,High
1071,30,M,Single,70000,Consultant,720,9000,Savings--Credit Card,4000,11000,No,No,Health,Mutual Funds,Medium,Conservative,Las Vegas,Low
1072,48,F,Married,105000,Pharmacist,750,23000,Savings--Home Loan,10000,24000,Yes,Yes,Life--Health,Real Estate,Medium,Balanced,San Antonio,Moderate
1073,35,M,Single,80000,IT Specialist,710,12000,Savings--Credit Card,6000,14000,No,Yes,Health--Life,Stocks,High,Aggressive,Phoenix,High
1074,41,F,Married,87000,Teacher,700,16000,Savings--Home Loan,8500,19000,Yes,Yes,Health,Mutual Funds,Medium,Balanced,Philadelphia,Moderate
1075,29,M,Single,65000,Graphic Designer,680,7000,Savings--Credit Card,3000,9000,No,No,None,Stocks,Low,Conservative,Orlando,Low
1076,38,F,Married,95000,Engineer,740,18000,Savings--Home Loan,9000,22000,Yes,Yes,Health--Life,Real Estate,Medium,Balanced,Denver,Moderate
1077,44,M,Married,110000,Financial Analyst,760,25000,Savings--Home Loan,12000,30000,Yes,Yes,Life--Auto,Stocks--Bonds,Medium,Balanced,Houston,Moderate
1078,26,F,Single,60000,Graphic Designer,690,7000,Savings--Credit Card,3500,8000,No,No,Health,Mutual Funds,High,Conservative,Seattle,Low
1079,39,M,Married,95000,Engineer,740,18000,Savings--Home Loan,9000,22000,Yes,Yes,Health--Life,Real Estate,Medium,Balanced,Denver,Moderate
1080,52,F,Married,130000,Architect,770,32000,Savings--Credit Card,16000,27000,Yes,Yes,Life--Health--Auto,Stocks--Bonds,High,Aggressive,San Diego,High
1081,30,M,Single,70000,Consultant,720,9000,Savings--Credit Card,4000,11000,No,No,Health,Mutual Funds,Medium,Conservative,Las Vegas,Low
1082,48,F,Married,105000,Pharmacist,750,23000,Savings--Home Loan,10000,24000,Yes,Yes,Life--Health,Real Estate,Medium,Balanced,San Antonio,Moderate
1083,35,M,Single,80000,IT Specialist,710,12000,Savings--Credit Card,6000,14000,No,Yes,Health--Life,Stocks,High,Aggressive,Phoenix,High
1084,41,F,Married,87000,Teacher,700,16000,Savings--Home Loan,8500,19000,Yes,Yes,Health,Mutual Funds,Medium,Balanced,Philadelphia,Moderate
1085,29,M,Single,65000,Graphic Designer,680,7000,Savings--Credit Card,3000,9000,No,No,None,Stocks,Low,Conservative,Orlando,Low
1086,38,F,Married,95000,Engineer,740,18000,Savings--Home Loan,9000,22000,Yes,Yes,Health--Life,Real Estate,Medium,Balanced,Denver,Moderate
1087,44,M,Married,110000,Financial Analyst,760,25000,Savings--Home Loan,12000,30000,Yes,Yes,Life--Auto,Stocks--Bonds,Medium,Balanced,Houston,Moderate
1088,26,F,Single,60000,Graphic Designer,690,7000,Savings--Credit Card,3500,8000,No,No,Health,Mutual Funds,High,Conservative,Seattle,Low
1089,39,M,Married,95000,Engineer,740,18000,Savings--Home Loan,9000,22000,Yes,Yes,Health--Life,Real Estate,Medium,Balanced,Denver,Moderate
1090,52,F,Married,130000,Architect,770,32000,Savings--Credit Card,16000,27000,Yes,Yes,Life--Health--Auto,Stocks--Bonds,High,Aggressive,San Diego,High
1091,30,M,Single,70000,Consultant,720,9000,Savings--Credit Card,4000,11000,No,No,Health,Mutual Funds,Medium,Conservative,Las Vegas,Low
1092,48,F,Married,105000,Pharmacist,750,23000,Savings--Home Loan,10000,24000,Yes,Yes,Life--Health,Real Estate,Medium,Balanced,San Antonio,Moderate
1093,35,M,Single,80000,IT Specialist,710,12000,Savings--Credit Card,6000,14000,No,Yes,Health--Life,Stocks,High,Aggressive,Phoenix,High
1094,41,F,Married,87000,Teacher,700,16000,Savings--Home Loan,8500,19000,Yes,Yes,Health,Mutual Funds,Medium,Balanced,Philadelphia,Moderate
1095,29,M,Single,65000,Graphic Designer,680,7000,Savings--Credit Card,3000,9000,No,No,None,Stocks,Low,Conservative,Orlando,Low
1096,38,F,Married,95000,Engineer,740,18000,Savings--Home Loan,9000,22000,Yes,Yes,Health--Life,Real Estate,Medium,Balanced,Denver,Moderate
1097,44,M,Married,110000,Financial Analyst,760,25000,Savings--Home Loan,12000,30000,Yes,Yes,Life--Auto,Stocks--Bonds,Medium,Balanced,Houston,Moderate
1098,26,F,Single,60000,Graphic Designer,690,7000,Savings--Credit Card,3500,8000,No,No,Health,Mutual Funds,High,Conservative,Seattle,Low
1099,39,M,Married,95000,Engineer,740,18000,Savings--Home Loan,9000,22000,Yes,Yes,Health--Life,Real Estate,Medium,Balanced,Denver,Moderate
1100,52,F,Married,130000,Architect,770,32000,Savings--Credit Card,16000,27000,Yes,Yes,Life--Health--Auto,Stocks--Bonds,High,Aggressive,San Diego,High
"""
    # Open the file in read mode
    with open('trainingData1.csv', 'r') as file:
        # Read the file
        trainingData = file.readlines()

        for data in trainingData:
            if starts_with_regex(data, r'[0-9]'):
                for customer in customers.split("\n"):
                    if starts_with_regex(customer, r'[0-9]') and data.split(",")[0] == customer.split(",")[0]:
                        print(customer)
                        data = data.replace(data.split(",")[0], customer + ",")
                        newData += data
                        break

    # Open the file in write mode
    with open('trainingData2.csv', 'w') as file:
        file.writelines(newData)

def starts_with_regex(text, pattern):
    # Compile the regex pattern
    regex = re.compile(pattern)
    
    # Check if the text starts with the regex pattern
    if regex.match(text):
        return True
    else:
        return False

main()