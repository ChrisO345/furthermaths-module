"""Binomial Distribution"""


# TODO fix this


# def factorial(n):
#     return (1 * factorial(n-1)) if n != 1 else 1


# def binomial_distribution(successes: int, trials: int, prob: float) -> float:
#     """
#     Return probability of k successes out of n tries, with p probability for one
#     success
#     """
#     if successes > trials:
#         raise ValueError("successes must be lower or equal to trials")
#     if trials < 0 or successes < 0:
#         raise ValueError("the function is defined for non-negative integers")
#     if not isinstance(successes, int) or not isinstance(trials, int):
#         raise ValueError("the function is defined for non-negative integers")
#     if not 0 < prob < 1:
#         raise ValueError("prob has to be in range of 1 - 0")
#     probability = (prob**successes) * ((1 - prob) ** (trials - successes))
#     # Calculate the binomial coefficient: n! / k!(n-k)!
#     coefficient = float(factorial(trials))
#     coefficient /= factorial(successes) * factorial(trials - successes)
#     return probability * coefficient


# if __name__ == "__main__":
#     pass
