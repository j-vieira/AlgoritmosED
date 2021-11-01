saldo = float(input("Informe seu saldo bancario: "))

if saldo<100:
    print("Isento do ISS.")
elif 100<=saldo<1000:
    print("O ISS:", 0.01*saldo)
elif 1000<=saldo<10000:
    print("O ISS:", 0.02*saldo)
elif 10000<=saldo<100000:
    print("O ISS:", 0.03*saldo)
else:
    print("O ISS:", 0.05*saldo)
