x = int(input("Dame un número: "))
signo ="+" if x>0 else ("-" if x<0 else "null")
par="par" if x%2==0 else "impar"
print(signo, par)