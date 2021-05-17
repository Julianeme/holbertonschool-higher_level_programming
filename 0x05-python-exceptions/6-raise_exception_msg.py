def raise_exception_msg(message=""):
    try:
        raise (NameError)
    except:
        print("{}".format(message))
