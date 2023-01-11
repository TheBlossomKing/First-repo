def N_2k(N):
    return 2 * N * N_2k(N - 1) if N > 0 else 1

try:
     print(N_2k(int(input("Enter a number: "))))
except ValueError:
    print("Ssssss")

def N_2k_1(N):
     return (2 * N - 1) * N_2k_1(N - 1) if N > 0 else 1

    print(N_2k_1(int(input("Enter a number: "))))
