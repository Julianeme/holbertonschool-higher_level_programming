def raise_exception_msg(message=""):
    try:
        raise (TypeError)
    except:
        print("{}".format(message))
