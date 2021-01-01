class Fibonacci:

	def fib(self, n: int) -> int:
		if n == 0:
			return n
		ultimo: int = 0
		proximo: int = 1
		for _ in range(1, n):
			ultimo, proximo = proximo, ultimo + proximo
		return proximo

