def main(A,B):
    """
    Return the numbers from A to B in the form of a list.
    Args:
        A: int
        B: int
    Returns:
        list: return  answer
    """
    for i in range(A,B+1):
        return list(range(A,B+1))

print(main(2,9))