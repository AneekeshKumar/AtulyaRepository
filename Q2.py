def cc_numb_(numb):
    array = list(str(numb))
    l = len(array)
    end_4 = array[l - 4:]
    output = "x" * (l - 4) + ''.join(end_4)
    print(l, len(output))
    return output


print(cc_numb_(65297652394397))
