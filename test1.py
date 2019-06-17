# # 《笨办法学python3》习题8：打印，打印
#
# formatter = "{} {} {} {}"
#
# print(formatter.format(1, 2, 3, 4))
# print(formatter.format("one", "two", "three", "four"))
# print(formatter.format(formatter, formatter, formatter, formatter))


formatter = "%r %r %r %r"
print(formatter%("i have.", "you","she doesn\'t have an apple", "he said that"))