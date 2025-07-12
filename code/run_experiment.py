
import matplotlib.pyplot as plt
from spiral_model import get_coordinates
from sympy import primerange

def run(start, end):
    primes = list(primerange(start, end + 1))
    coords = get_coordinates(primes)
    x_vals = [x for (_, x, _) in coords]
    y_vals = [y for (_, _, y) in coords]

    plt.figure(figsize=(8, 8))
    plt.scatter(x_vals, y_vals, s=10, alpha=0.6)
    plt.title(f"Prime Spiral from {start} to {end}")
    plt.axis("equal")
    plt.grid(True)
    plt.savefig(f"prime_spiral_{start}_{end}.png")
    plt.show()

if __name__ == "__main__":
    run(10000, 10500)
