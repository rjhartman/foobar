from fractions import Fraction
    
def solution(pegs):
    total_distance = pegs[-1] - pegs[0]
    c = Fraction(3, 2) if len(pegs) % 2 == 0 else Fraction(-1, 2)
    n = len(pegs) - 2

    memo = {}
    def nth_term(n):
        if n == 0:
            return pegs[1] - pegs[0]
        if n not in memo:
            memo[n] = (pegs[n + 1] - pegs[n]) - nth_term(n - 1)
        return memo[n]
    
    all_terms = sum(nth_term(i) for i in range(n)) * 2

    gear_radius = Fraction((total_distance - all_terms), c)

    return [gear_radius.numerator, gear_radius.denominator] if gear_radius >= 1 else [-1, -1]
