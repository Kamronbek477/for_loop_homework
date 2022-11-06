def main(price):
    """
    The price of a kilogram of sweets is given. Return the price of a dessert from one to ten kg in the form of a list.
    Args:
        price: int
    Returns:
        list: return  answer
    """
    s=[]
    l=price
    for i in range(1,11):
        s.append(price)

        price+=l
    return s
print(main(1.5))
