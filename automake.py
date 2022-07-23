projname = input("Project Name? : ")
source = input("Source Folder? : ")

makefile = f"""SOURCE = $(wildcard {source})

{projname}.out: $(SOURCE)
    gcc $^ -o $@
"""

f = open("makefile", "w")
f.write(makefile)
