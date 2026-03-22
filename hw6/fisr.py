import struct

import matplotlib.pyplot as plt
import numpy as np


def fast_inv_sqrt(x, newton_iters=1):
    # i am converting float to integer bit pattern
    i = struct.unpack("<i", struct.pack("<f", x))[0]
    i = 0x5F3759DF - (i >> 1)
    # i am convertin back to float
    y = struct.unpack("<f", struct.pack("<i", i))[0]

    # Newton method iterations- y = y * (1.5 - 0.5 * x * y^2)
    x2 = x * 0.5
    for _ in range(newton_iters):
        y = y * (1.5 - x2 * y * y)
    return y


# i am generating test values
x_vals = np.linspace(0.1, 1000, 1000)
true_vals = 1.0 / np.sqrt(x_vals)
fisr_vals = np.array([fast_inv_sqrt(x, newton_iters=1) for x in x_vals])

plt.figure(figsize=(12, 6))
plt.plot(x_vals, true_vals, label="True x^(-0.5)", linewidth=2)
plt.plot(x_vals, fisr_vals, "--", label="FISR (1 Newton step)", linewidth=2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Fast Inverse Square Root vs. True Value")
plt.legend()
plt.grid(alpha=0.3)
plt.show()


# i am plotting error curves here
error = np.abs(fisr_vals - true_vals)
plt.figure(figsize=(12, 6))
plt.plot(x_vals, error, color="red")
plt.xlabel("x")
plt.ylabel("Absolute Error")
plt.title("Error of Fast Inverse Square Root (1 Newton step)")
plt.grid(alpha=0.3)
plt.ylim(0, 0.005)
plt.show()


# i am adding more newton iterations here

fisr_1 = np.array([fast_inv_sqrt(x, newton_iters=1) for x in x_vals])
fisr_2 = np.array([fast_inv_sqrt(x, newton_iters=2) for x in x_vals])
fisr_3 = np.array([fast_inv_sqrt(x, newton_iters=3) for x in x_vals])

error_1 = np.abs(fisr_1 - true_vals)
error_2 = np.abs(fisr_2 - true_vals)
error_3 = np.abs(fisr_3 - true_vals)

plt.figure(figsize=(12, 8))
plt.semilogy(x_vals, error_1, label="1 Newton step")
plt.semilogy(x_vals, error_2, label="2 Newton steps")
plt.semilogy(x_vals, error_3, label="3 Newton steps")
plt.xlabel("x")
plt.ylabel("Absolute Error (log scale)")
plt.title("Error Reduction with Additional Newton Iterations")
plt.legend()
plt.grid(alpha=0.3)
plt.show()
