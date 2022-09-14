from fileinput import filename

from exception import Lab5Exception


def set_union(collection_one, collection_two):
    """
        This function, as the name implies, should output 
        the result of union of two sets. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    union = list()
    for item in collection_one:
        if collection_one.count(item) !=1 :
            raise Lab5Exception("Duplicate values in the input")
        if item in collection_two:
            continue
        else:
            union.append(item)
    union.extend(collection_two)

    for item in collection_two:
        if collection_two.count(item) !=1 :
            raise Lab5Exception("Duplicate values in the input")

    return union
    

def set_intersection(collection_one, collection_two):
    """
        This function, as the name implies, should output 
        the result of intersection of two sets. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    for item in collection_two:
        if collection_two.count(item) !=1 :
            raise Lab5Exception("Duplicate values in the input")

    intersection = list()
    for item in collection_one:
        if collection_one.count(item) !=1 :
            raise Lab5Exception("Duplicate values in the input")
        if item in collection_two:
            intersection.append(item)
        else:
            continue

    return intersection

def set_equality(collection_one, collection_two):
    """
        This function, as the name implies, should check whether
        or not two sets are equal. Note that the input might not
        be valid sets. You are to check the validity. 

        You are expected to think of all possible corner cases of 
        you code and raise Exception accordingly.
    """
    for item in collection_two:
        if collection_two.count(item) !=1 :
            raise Lab5Exception("Duplicate values in the input")


    if(len(collection_one) != len(collection_two)):
        return False
    for item in collection_one:
        if collection_one.count(item) !=1 :
            raise Lab5Exception("Duplicate values in the input")
        if item in collection_two:
            continue
        else:
            return False

    return True

def parse_file(file_name):
    """
        This function is expected to parse a text (.txt) file
        and extract pairs of collections from it.

        Note that the parsed collections might not be valid sets.
        Please check and accordingly raise Exception. You should also
        think about other corner cases of your code and raise the Exception
        accordingly.
    """
    f = open(file_name,'r')
    l = list()
    for item in f.readlines():
        l1 = item.split("    ")
        l1[1] = l1[1].strip()
        l1[0] = eval(l1[0])
        l1[1] = eval(l1[1])
        l.append(l1)
    return l