__author__ = 'marco'

from utils import xor


def solve_q8(y1, y2):
    """ To solve the problem use the `decrypt` function, using the result as the cipher text,
        and ``123`` as the value for the ``key`` (``y2``).

    :return: solves for AES(y2, x2) in the stated problem, by executing XORs
    """
    aes_y1_x1 = '46622a0d2994e2c325e0e0e0dfbf6056'.decode('hex')
    return xor(xor(aes_y1_x1, y1), y2).encode('hex')


def solve_q9(y1):
    """ This returns directly the value for ``y2`` by using the same values for ``(x1, y1)`` as in the Q8 and the value
        ``deadbeef`` for ``x2``

    :return: the ``y2`` value for Q9
    """
    AES_x1_x1 = '6ed1f6dc4787e89dc8cb52512bd16761'.decode('hex')
    AES_x2_x2 = 'c9c8e978b869da4f76ad2d39e8f7a614'.decode('hex')
    return xor(xor(AES_x1_x1, y1), AES_x2_x2).encode('hex')


def main():
    x1 = 'ff000000000000000000000000000000'
    y1 = '10000000000000000000000000000000'
    x2 = 'deadbeef000000000000000000000000'
    y2 = '12300000000000000000000000000000'

    print("Q8.\nx1={}, y1={}\ny2={}, AES(y2, x2) = {}".format(x1, y1, y2, solve_q8(y1=y1.decode('hex'),
                                                                                  y2=y2.decode('hex'))))
    print("===\n")
    print("Q9.\nx1={}, y1={}\nx2={}, y2 = {}".format(x1, y1, x2, solve_q9(y1=y1.decode('hex'))))

if __name__ == "__main__":
    main()
