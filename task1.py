    """
    Calculates the area of a rectangle given its side lengths

    :param a: first side of the rectangle
    :param b: second side of the rectangle
    :return: area of the rectangle
    :raises ValueError: if either number was negative
    """
  def rectangle_area(a, b):
    if a<0 or b<0:
        raise ValueError("if either number was negative")
    return a*b

