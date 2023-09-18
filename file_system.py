"""
File:    file_system.py
Author:  Justin Obi
Date:    12/9/2022
Section: 35
E-mail:  wr64574@umbc.edu
Description:
  making a simple shell that has some file system capabilities,
  similar to the one that you interact with on the GL Linux server
"""


DIRECTORIES_KEY = 'directories'
FILES_KEY = 'files'
ROOT_DIRECTORY_NAME = 'home'


def rm(file, system, path):
    """
           A function that removes a file in a specific directory
           :param file: string of name of file
           :param system: the entire dictionary
           :param path: list of the path directory
           :return: none
           """
    for ele in path:
        filesys = system[ele][FILES_KEY]
        system = system[ele][DIRECTORIES_KEY]
    if file in filesys:
        filesys.remove(file)
    else:
        print(file,"not found.")

def touch(name, system, path):
    """
               A function that adds a file in a specific directory
               :param name: string of name of file
               :param system: the entire dictionary
               :param path: list of the path directory
               :return: none
               """
    for ele in path:
        filesys = system[ele][FILES_KEY]
        system = system[ele][DIRECTORIES_KEY]
    #system[FILES_KEY].append(name)
    filesys.append(name)


def locate(file, system, path):
    """
               A function that locates a file in a specific directory
               :param file: string of name of file
               :param system: the entire dictionary
               :param path: list of the path directory
               :return: none
               """
    for ele in path:
        location_F = system[ele][FILES_KEY]
        location_D = system[ele][DIRECTORIES_KEY]
        if file in location_F:
            output = '/'
            for ele in path:
                output += ele + '/'
            output += file
            print(output)
        else:
            new_path = path[1:]
            locate(file, system, new_path)



def ispath(path, system):
    """
               A function that checks if the path is a path in the Dictionary
               :param system: the entire dictionary
               :param path: list of the path directory
               :return: path
               """
    flag = True
    for ele in path:
        if ele in system:
            system = system[ele][DIRECTORIES_KEY]
        else:
            flag = False


    if flag is True:
        return path
    else:
        print("Path not in directory")


def convert_to_list(user_input):
    """
               A function that converts a string into a list
               :param user_input: list of the path directory
               :return: an updated user_input
               """
    if user_input[0] == '/':
        user_input = 'home' + user_input
    if user_input[-1] == '/':
        user_input = user_input[:-1]
    user_input = user_input.split('/')
    return user_input


def make_dir(name, system, path):
    """
               A function that creates a directory in a specific path
               :param name: string of name of directory
               :param system: the entire dictionary
               :param path: list of the path directory
               :return: none
               """
    if len(path) == 0:
        system[ROOT_DIRECTORY_NAME][name] = {DIRECTORIES_KEY: {}, FILES_KEY: {}}
    else:
        for ele in path:
            system = system[ele][DIRECTORIES_KEY]
        system[name] = {DIRECTORIES_KEY: {}, FILES_KEY: []}


def current_direct_abs(system, path, old_path):
    """
               A function that changes the directory in absolute
               :param system: the entire dictionary
               :param path: list of path directory
               :param old_path:  old list of the path directory
               :return: newpath or old path
               """
    new_path = convert_to_list(path)
    if ispath(new_path, system):
        return new_path
    else:
        return old_path



def current_direct_2(user_input, system, path):
    """
                   A function that changes the directory with a relative path
                   :param user_input: a string of a relative path
                   :param system: the entire dictionary
                   :param path:   list of the path directory
                   :return: new_path or path
                   """
    new_path = path + convert_to_list(user_input)
    if ispath(new_path, system):
        return new_path
    else:
        return path




def current_direct(user_input, path, system):
    """
                       A function that changes the directory
                       :param user_input: a string of a relative path
                       :param system: the entire dictionary
                       :param path:   list of the path directory
                       :return: new_path or path
                       """
    if '..' in user_input:
        if len(path) < 2:
            new_path = [ROOT_DIRECTORY_NAME]
        else:
            new_path = path[:-1]
        return new_path
    elif '.' in user_input or '' == user_input or ' ' == user_input:
        return path
    elif '/' in user_input:
        if '/' == user_input:
            new_path = [ROOT_DIRECTORY_NAME]
            return new_path
        else:
            if user_input[0] == '/':
                return current_direct_abs(system, user_input, path)

            else:
                return current_direct_2(user_input, system, path)

    else:
        if len(path) == 0:
            path = [ROOT_DIRECTORY_NAME]
        #system = system[ROOT_DIRECTORY_NAME]
        for ele in path:
            system = system[ele][DIRECTORIES_KEY]
        if user_input in system:
            if user_input not in path:
                path.append(user_input)
                return path
            else:
                return path
        if user_input not in system:
            print("No such directory")
            return path


def print_list(xlist):
    """
       A function to print each item in the list
       :param xlist: list of what ever needs to be printed
       :return: none
       """
    #prints each item in the list
    for element in xlist:
        print(element)


def pwd(path):
    """
                       A function that changes the directory with a relative path
                       :param path: a list of path directory
                       :return: string of path
                       """
    string = "/"
    for ele in path:
        string+= ele+'/'
    return string


def list_content(system, path):
    """
                       A function that checks the contents of the directory
                       :param system: the entire dictionary
                       :param path:   list of the path directory
                       :return: none
                       """
    print("Contents for", pwd(path))
    xlist = []
    for ele in path:
        filesys = system[ele][FILES_KEY]
        system = system[ele][DIRECTORIES_KEY]


    for ele in system:
        xlist.append(ele)
    for ele in filesys:
        xlist.append(ele)
    print_list(xlist)


def list_content_2(user_input,system, path):
    """
                           A function that checks the contents of the directory from relative directory
                           :param system: the entire dictionary
                           :param user_input: string of path
                           :param path:   list of the path directory
                           :return: none
                           """
    path = path + convert_to_list(user_input)

    if ispath(path, system):
        print("Contents for", pwd(path))
        xlist = []
        for ele in path:
            filesys = system[ele][FILES_KEY]
            system = system[ele][DIRECTORIES_KEY]


        for ele in system:
            xlist.append(ele)
        for ele in filesys:
            xlist.append(ele)
        print_list(xlist)



def list_content_abs(system, path):
    """
                               A function that checks the contents of the directory from absolute path
                               :param system: the entire dictionary
                               :param path:  string of the path directory
                               :return: none
                               """
    path = convert_to_list(path)
    if ispath(path, system):
        print("Contents for", pwd(path))
        xlist = []
        for ele in path:
            filesys = system[ele][FILES_KEY]
            system = system[ele][DIRECTORIES_KEY]


        for ele in system:
            xlist.append(ele)
        for ele in filesys:
            xlist.append(ele)
        print_list(xlist)



if __name__ == '__main__':
    # initialized with the home directory and some inner directories
    # notice how every time I create a directory,
    # I initialize a dictionary within that
    # (each inner dictionary (directory)
    # should have the ability to store its own directories and files)
    path = [ROOT_DIRECTORY_NAME] #This is a list that keeps track of the path

    my_file_system = {
        ROOT_DIRECTORY_NAME: {
            DIRECTORIES_KEY: {'dir1': {
                DIRECTORIES_KEY: {'dir1_in_dir2': {
                    DIRECTORIES_KEY: {},
                    FILES_KEY: ['gg']}},
                FILES_KEY: ['ex1_in_dir1.txt', 'ex2_1_in_dir2.txt']
            }
            },
            FILES_KEY: ['ex1_in_dir1.txt']
        },
        FILES_KEY: []
    }
    user_input = ""
    while user_input != "exit": #while the input is not exit the code keeps looping
        user_input = input("[cmsc201 proj3]$ ")
        user_input = user_input.strip()
        if "mkdir" == user_input[0:5]:
            if "/" in user_input[:-1] or '.' in user_input or user_input[5:] == '':
                print("Invalid input")
            else:
                make_dir(user_input[5:].strip(), my_file_system, path)
        elif "ls" == user_input[0:2]:
            if len(user_input) == 2:
                list_content(my_file_system, path)
            else:
                if user_input[3] == '/':
                    list_content_abs(my_file_system, user_input[3:])
                else:
                    list_content_2(user_input[3:], my_file_system, path)
        elif "pwd" == user_input[0:3]:
            print(pwd(path))
        elif "rm " == user_input[0:3]:
            rm(user_input[3:], my_file_system, path)
        elif "touch " == user_input[0:6]:
            if "/" in user_input or user_input[5:] == '':
                print("Invalid input")
            else:
                touch(user_input[6:].strip(), my_file_system, path)
        elif "locate " == user_input[0:7]:

            locate(user_input[7:].strip(), my_file_system, path)
        elif "cd" == user_input[0:2]:
            if 'cd ' in user_input:
                path = current_direct(user_input[3:], path, my_file_system)
            else:
                print("Invalid Input")



