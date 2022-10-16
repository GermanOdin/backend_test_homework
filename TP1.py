from typing import Sequence, Dict, List, Tuple, Set, Union


def series_sum(incoming: List[Union[str, float]]) ->str:
    
    """Принимает на вход список из строк и чисел с плавающей точкой, приводит его элементы к строкам и конкатенирует их.
    """
    result = ''
    for i in incoming:
        result += str(i)
    return result

rt = series_sum([1,2,4,8,8.2])
print(rt)