#python test-html
#my_html = open('myfile.html', 'r+')
#my_html.write('<i>These should be in italics</i>')
#my_html.write("\n\nlet's try matching parens. (italic?) not italic (but italic?)")
#my_html.close()

my_html = open('myfile.html', 'r+')
thislist = my_html.read().split(",")
print thislist
assert isinstance(thislist, list)
for i in range(len(thislist)):
    if thislist[i] == "(":
        thislist[i+1].insert("<i>")
    elif thislist[i] == ")":
        thislist[i+1].insert("</i>")
print thislist
#my_html.write("\na\n\n")
#my_html.write(str(thislist))
my_html.close()