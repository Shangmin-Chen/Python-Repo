a = ['asd','aasdd','fasdd','asasdasd','wadsad','gkhl']

# this is the easiest way, the string in "".join is the separater.
b = "\n".join(a)
print(b)


# if theres a number in your list, the star operator gets rid of potential TypeError error.
print(*a, sep="\n")
