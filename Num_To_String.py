#98 -> Ninety Eight

a = input("Enter Number:-")

single_digit = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
double_digts = {'10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen','20':'Twenty','30':'Thirty','40':'Fourty','50':'Fifty','60':'Sixty','70':'Seventy','80':'Eighty','90':'Ninety'}
#treepal_digits = {'100':'Onehundred','200':'Twohundred','300':'Threehundred','400':'Fourhundred','500':'Fivehundred','600':'Sixhundred','700':'Sevenhundred'}
if len(a) == 1:
    print(single_digit[a])
elif len(a) == 2:
    if a in double_digts:
        print(double_digts[a])
    else:
        a1 = "%s0" % a[0]
        a2 = a[1]

        print(double_digts[a1], single_digit[a2])
elif len(a) == 3:
   
        a2 = a[2]
        a1 = ""
        if a[1] != "0":
           a1 = "%s0" % a[1]
        a3 = "%s Hundread" % single_digit[a[0]]

        if a1 == "":
            print(a3, single_digit[a2])
        else:
            print(a3, double_digts[a1],single_digit[a2])
elif len(a) == 4:
        a2 = a[2]
        a1 = ""
        if a[2] != "0":
            a2 = "%s0" % a[1]
       # a3 = "%s Hundread" % single_digit[a[0]]
        a4 = "%s Thousand" % single_digit[a[0]]
        
        if a1 != "":
            print(a4,single_digit[a2])
        else:
            print(a4,double_digts[a2],single_digit[a1])