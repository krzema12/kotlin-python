from output import execute20, execute20Doubled

print(execute20Doubled())


def myPrinterAdder(x: int) -> int:
    print(x)
    return x + 1


print(execute20(myPrinterAdder))
print(execute20(lambda y: y + 123))
