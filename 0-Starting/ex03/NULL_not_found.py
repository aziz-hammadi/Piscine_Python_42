def NULL_not_found(object: any) -> int:
    match object:
        case False:
            print(f"Fake {object} {type(object)}")
        case None:
            print(f"Nothing: None {type(object)}")
        case 0:
            print(f"Zero: {object} {type(object)}")
        case '':
            print(f"Empty: {object} {type(object)}")
        case float() if object != object:
                print(f"Cheese: {object} {type(object)}")
        case _:
            print("Type not found")
            return 1
    return 0