string = input("Enter in a string: ")

new_string = string[:2:]
new_string2 = string[-2:]
new_string3 = new_string + new_string2
new_string4 = new_string3[::-1]

print(new_string4.capitalize())

#tekur á moti string change strenginn með því að taka fyrstu 2 stafi og seinsustu 2 stafi.
#svo Snúið strenginum við og hafið aðeins fyrsta stafinn hástaf.
# td Nintendo -> Nido -> odiN -> Odin 