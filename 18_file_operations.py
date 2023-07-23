# File operations

f = open("sample_file.py","wt")
f.write("print('hai')")
f.close()

# with filename as:
    # depended operations
    # with automatically close opened file
with open("11_Atm_machine_Project.py","r") as f:
    x = f.read()
    print(x)