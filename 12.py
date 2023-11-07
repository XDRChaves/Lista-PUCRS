for _ in range(20):
    n = int(input("Digite um valor para n: "))
    print(f"Tabuada de 1 até {n}:\n")
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            print(f"{i} x {j} = {i * j}")
        print()
