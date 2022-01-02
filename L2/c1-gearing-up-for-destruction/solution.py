from fractions import Fraction


def solution(pegs):
    total_distance = pegs[-1] - pegs[0]
    # The coefficient of the radius of the first gear in this equation will
    # always be 3/2 or -1/2, depending on the parity of the length of pegs.
    c = Fraction(3, 2) if len(pegs) % 2 == 0 else Fraction(-1, 2)

    # Number of middle gears, also the number of terms to solve in the next step
    n = len(pegs) - 2

    memo = {}
    # Memoized function to add all the constants (distances between pegs)
    # of the nth term in the equation
    def nth_term(n):
        if n == 0:
            return pegs[1] - pegs[0]
        if n not in memo:
            memo[n] = pegs[n + 1] - pegs[n] - nth_term(n - 1)
        return memo[n]

    # Sum all the constants in terms for each middle gear,
    # then multiply by two because these are the middle gears' diameters
    all_terms = sum(nth_term(i) for i in range(n)) * 2

    first_gear = Fraction((total_distance - all_terms), c)

    # Calculate all subsequent gears, and make sure
    # they aren't an invalid size.
    previous_gear = first_gear
    for i in range(1, n):
        current_gear = pegs[i] - pegs[i - 1] - previous_gear
        if current_gear < 1:
            return [-1, -1]
        previous_gear = current_gear

    return (
        [first_gear.numerator, first_gear.denominator] if first_gear >= 1 else [-1, -1]
    )
