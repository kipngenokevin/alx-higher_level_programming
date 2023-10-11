def common_elements(set_1, set_2):
    if not set_1 or not set_2:
        return
    else:
        c = list(set_1 & set_2)
        return c
