def main(list1):
    """
    Returns a list where only the first letter of each name is capitalized.
    Args:
        list1: list
    Returns:
        list: return  answer
    """
    s=[]
    for i in list1:
        if str(i).islower():
            s.append(str(i).capitalize())
    
    return s
print(main(['kamronbek','javoxir','diyor','ikrom']))