#98 -> Ninety Eight

a = input("Enter Number:-")

single_digit = {'0':'Zero','1':'One','2':'Two','3':'Three','4':'Four','5':'Five','6':'Six','7':'Seven','8':'Eight','9':'Nine'}
double_digts = {'10':'Ten','11':'Eleven','12':'Twelve','13':'Thirteen','14':'Fourteen','15':'Fifteen','16':'Sixteen','17':'Seventeen','18':'Eighteen','19':'Nineteen','20':'Twenty','30':'Thirty','40':'Fourty','50':'Fifty','60':'Sixty','70':'Seventy','80':'Eighty','90':'Ninety'}
#treepal_digits = {'100':'Onehundred','200':'Twohundred','300':'Threehundred','400':'Fourhundred','500':'Fivehundred','600':'Sixhundred','700':'Sevenhundred'}

# remove any zero if present in front


if len(a) == 1:
    print(single_digit[a])
elif len(a) == 2:
    if a in double_digts:
        print(double_digts[a])
    else:
        ones_ = a[1]

        if a[0] == "0":
            print(single_digit[a[0]], single_digit[ones_])
        else:
            tens_ = "%s0" % a[0]
            print(double_digts[tens_], single_digit[ones_])
elif len(a) == 3:
   
        hundred_ = a[0]

        if a[1:] in double_digts.keys():

            print(f"{single_digit[hundred_]} Hundred {double_digts[a[1:]]}")

        else:

            tens_ = "%s0" % a[1]

            ones_ = a[0]

            print(f"{single_digit[hundred_]} Hundred {double_digts[tens_]} {single_digit[ones_]}")