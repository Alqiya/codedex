#1. user input
numeral_input=input("Enter the roman numerals:")

#2. define roman to itn function
def roman_to_int(numeral):
    final_answer=0
    for i in numeral:
        #solving the edge cases like IV makes 4 etc
        #this is done by adding the required ans to final ans and then replacing that particular string
        #with an empty string....ex if its CMI then cm==900 and then I=1 so total 901
        if "CM" in numeral:
            final_answer += 900
            numeral = numeral.replace("CM", "")
        if "CD" in numeral:
            final_answer += 400
            numeral = numeral.replace("CD", "")
        if "XC" in numeral:
            final_answer += 90
            numeral = numeral.replace("XC", "")
        if "XL" in numeral:
            final_answer += 40
            numeral = numeral.replace("XL", "")
        if "IX" in numeral:
            final_answer += 9
            numeral = numeral.replace("IX", "")
        if "IV" in numeral:
            final_answer += 4
            numeral = numeral.replace("IV", "")
        if i=='M':
            final_answer+=1000
        elif i=='D':
            final_answer+=500
        elif i=='C':
            final_answer+=100
        elif i=='L':
            final_answer+=50
        elif i=='X':
            final_answer+=10
        elif i=='V':
            final_answer+=5
        elif i=='I':
            final_answer+=1
        else:
            print("invalid input!")
    print(f"the roman numerals you entered converts to {final_answer} as an integer.")

roman_to_int(numeral_input)
