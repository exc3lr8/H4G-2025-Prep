from Crypto.Util.number import long_to_bytes
import sympy

def decrypt_candies():
    with open('output.txt', 'r') as f:
        lines = f.readlines()
    
    v1 = int(lines[0].split('=')[1].strip())
    v2 = int(lines[1].split('=')[1].strip())
    v3 = int(lines[2].split('=')[1].strip())
    v4 = int(lines[3].split('=')[1].strip())

    # Create symbols for the unknown candies
    cnd1, cnd2, cnd3 = sympy.symbols('cnd1 cnd2 cnd3')

    # Set up the system of equations
    eq1 = sympy.Eq(cnd1**3 + cnd3**2 + cnd2, v1)
    eq2 = sympy.Eq(cnd2**3 + cnd1**2 + cnd3, v2)
    eq3 = sympy.Eq(cnd3**3 + cnd2**2 + cnd1, v3)
    eq4 = sympy.Eq(cnd1 + cnd2 + cnd3, v4)

    # Solve the system of equations
    solution = sympy.solve((eq1, eq2, eq3, eq4), (cnd1, cnd2, cnd3))

    # Convert the solution to integers
    candies = [int(sol) for sol in solution[0]]

    # Reconstruct the flag
    flag = b''.join(long_to_bytes(candy) for candy in candies)
    
    return flag

decrypted_flag = decrypt_candies()
print(f"Decrypted flag: {decrypted_flag.decode()}")