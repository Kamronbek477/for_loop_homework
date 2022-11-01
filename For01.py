import py_compile


def main(n):
    """
    Return numbers from zero to n in a list view.
    Args:
        n: int
    Returns:
        list: return  answer
    """
    list=[]
    i=0
    while i<n:
        list+=[i]
        i+=1
    
    return list
print(main(11))