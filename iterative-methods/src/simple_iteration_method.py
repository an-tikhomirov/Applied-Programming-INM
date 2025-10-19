import numpy as np


class IterativeSolver():

    def __init__(self, A, n, b, x0, tolerance, tau, Nmax):
        self.A = A
        self.n = n
        self.b = b
        self.x0 = x0
        self.tol = tolerance
        self.tau = tau
        self.N = Nmax

    def preprocess(self):
        self.A = np.array(self.A).reshape(self.n, self.n)
        self.b = np.array(self.b)
        self.x0 = np.array(self.x0)

        if self.A.shape[0] != self.b.shape[0]:
            raise ValueError("The sizes of A and b do not match")

        if self.b.shape[0] != self.x0.shape[0]:
            raise ValueError("The sizes of b and x0 do not match")

        if np.linalg.det(self.A) == 0:
            raise ValueError("Matrix A is singular")

    def Solver(self):
        x = self.x0.copy()
        temp = np.dot(self.A, x) - self.b
        for i in range(self.N):
            x = x - self.tau * temp
            temp = np.dot(self.A, x) - self.b
            error = np.linalg.norm(temp, ord=np.inf)
            if np.linalg.norm(temp, ord=np.inf) <= self.tol:
                print(f"Converged in {i + 1} iterations")
                return x, i+1, error

        print(f"Reached maximum of iterations {self.N}")
        return x, self.N, error
