# make_html_list.py
#def main():
outfile = open("makeList.html", "w")
result = ""
names = [""] * 10

for i in range(len(names)):
    names[i] = input("enter a string: ")
    
for i in range(10):
    result += str("\t<li>" + names[i] + "</li>\n")
    #print(str(names[i]))

# writes result to the file
outfile.write("<ul>\n" + str(result) + "</ul>")

# close the file
outfile.close()

print("Data writen to numbers.txt")

# call the main function
#main()
