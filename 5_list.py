                # List  Data Structure

# MUTABLE, ANY DATATYPE

languages = ["Python", "C", "Java", ]
domain = ["Machine Learning", "Core level programming", "Android development"]
dob = [1991, 1970, 1985, 1996, 2019]
print("Data type: ",type(languages))
print("Languages: ",languages[1])
print("Length: ",len(languages))

# replacing java with cpp
languages[2] = "Cpp"
print(languages)

# appending 2 more languages
languages.append("Mojo")
languages.append("Java")
print(languages)

# appending 2 lists
languages.append(domain)
print(languages)

languages.append(dob)
print(languages)