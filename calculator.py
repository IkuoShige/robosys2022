def Fourarithmeticoperations(sym, b, results, c):
    if sym == '+':
        results += b
    if sym == '-':
        results -= b
    if sym == '*':
        results *= b
    if sym == '/':
        results /=b
    print("==={}".format(results))
    return results

def showresult(results, c):
    if c == 0:
        print("cancel")
    else:
        print("result == {}".format(results))
        print("you did it !")
    return

def set_boad():
    print("*   f:三角関数(until)  a: 四則演算   h: ヘルプ                    *");
    print("***************************************************************");
    print("*   ex: input |3 + 3            output |===6                  *");
    print("*             |+ 2                     |===8                  *");
    print("*             |- 1                     |===7                  *");
    print("*             |* 5                     |===35                 *");
    print("*             |/ 6                     |===5.833333333333333  *");
    print("*             |q                     finish                   *");
    print("***************************************************************");

def main():
    c = 0
    print("input number :")
    while True:
        y = input().split()
        mode = y[0]
        if mode == 'q':
            break
        elif mode == 'h':
            set_boad()
            print("input number :")
            continue
        elif c == 0:
            results, sym, b = float(y[0]), y[1],float(y[2])
        else:
            sym, b, = y[0], float(y[1])

        results = Fourarithmeticoperations(sym, b, results, c)
        c = c + 1
    showresult(results, c)

if __name__ == "__main__":
    set_boad()
    main()