import os

folder = input(r"""Enter the full path to the folder you wanna sort.
Example: H:\Downloads
Input: """)



def get_extensions():

    list_ex = []

    for file in os.listdir("."):

        exten = os.path.splitext(file)[-1]
        if exten == "":
            list_ex.append("No extension")
        else:
            list_ex.append(exten)

    return set(list_ex)

def create_folder(names):
    for name in names:
        if os.path.exists(name) == False:
            os.mkdir(name)

def get_files_names():
    return [f for f in os.listdir(".") if os.path.isfile(f)]


def replace_files(names_file,name_folder):
    for name in names_file:

        exten = os.path.splitext(name)[-1]
        if exten == "":
            exten = "No extension"
        if exten in name_folder and os.path.isdir(name) == False :
            os.replace(name,f"{exten}/{name}")

try:
    os.chdir(f"{folder}")
    extensions = get_extensions()
    ex = get_extensions()
    create_folder(ex)
    names = get_files_names()
    replace_files(names,ex)
    print(f"{len(names)} files have been successfully replaced.")
except:
    print(f"{folder} is not a valid folder.")




