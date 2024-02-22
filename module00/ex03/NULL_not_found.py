def NULL_not_found(object: any) -> int:
    types = {
        None : "Nothing:",
        float: "Cheese:",
        int: "Zero:",
        str: "Empty:",
        bool: "Fake:",
        dict: "Dict:",
    }
    if (object == None):
        print(f"{types[None]} {object} {type(object)}")
    elif (type(object) == float and object != object):
        print(f"{types[float]} {object} {type(object)}")
    elif (object == 0):
        print(f"{types[type(object)]} {object} {type(object)}")
    elif (object == ""):
        print(f"{types[type(object)]} {object} {type(object)}")
    elif (object == False):
        print(f"{types[type(object)]} {object} {type(object)}")
    else:
        print("Type not found!")
    return 1