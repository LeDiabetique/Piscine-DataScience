def all_thing_is_obj(object : any) -> int:
    types = {
        tuple: "Tuple",
        list: "List",
        set: "Set",
        dict: "Dict",
        str: "str",
    }

    if (type(object) is str):
        print(f"{object} is in the kitchen : {type(object)}")
    elif (type(object) in types):
        print(f"{types[type(object)]} : {type(object)}")
    else:
        print("Type not found!")    
    return 42
