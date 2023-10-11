def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return
    else:
        a = set(set_1)
        b = set(set_2)
        c = (a & b)
        return c
