class Solution:
    def get_minimizer(self, iterations: int, learning_rate: float, init: int) -> float:
        result = init

        for _ in range(iterations):
            derv = 2*result;
            result = result - learning_rate*derv

        return round(result,5)
