"""
Module give_bmi
Provides functions to calculate BMI values and check them against a limit.
"""

from typing import List, Union

Number = Union[int, float]


def give_bmi(height: List[Number], weight: List[Number]) -> List[Number]:
    """
    Calculate BMI values from lists of heights and weights.

    Args:
        height (List[int | float]): List of heights in meters.
        weight (List[int | float]): List of weights in kilograms.

    Returns:
        List[int | float]: List of BMI values.

    Raises:
        ValueError: If the lists are not the same size.
        TypeError: If the lists contain elements that are not int or float.
    """
    if len(height) != len(weight):
        raise ValueError("Height and weight lists must have the same length.")

    if not all(isinstance(h, (int, float)) for h in height):
        raise TypeError("Height list must contain only int or float values.")

    if not all(isinstance(w, (int, float)) for w in weight):
        raise TypeError("Weight list must contain only int or float values.")

    return [w / (h ** 2) for h, w in zip(height, weight)]


def apply_limit(bmi: List[Number], limit: int) -> List[bool]:
    """
    Check whether BMI values exceed a given limit.

    Args:
        bmi (List[int | float]): List of BMI values.
        limit (int): The threshold BMI value.

    Returns:
        List[bool]: True if the BMI is greater than the limit, False otherwise.

    Raises:
        TypeError: If bmi contains invalid types or limit is not an int.
    """
    if not all(isinstance(b, (int, float)) for b in bmi):
        raise TypeError("BMI list must contain only int or float values.")

    if not isinstance(limit, int):
        raise TypeError("Limit must be an integer.")

    return [b > limit for b in bmi]


