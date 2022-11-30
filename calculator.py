#!/usr/bin/python3
# SPDX-FileCopyrightText: 2022 Ikuo Shige
# SPDX-License-Identifier: BSD-3-Clause
def Fourarithmeticoperations(sym, b, results, c):
    if sym == '+':
        results += b
    if sym == '-':
        results -= b
    if sym == '*':
        results *= b
    if sym == '/':
        results /=b
    #if sym == 's':
    #    result 
    #print("==={}".format(results))
    return results

def showresult(results, c):
    if c == 0:
        print("cancel")
    else:
        print("{}".format(results))
        #print("result == {}".format(results))
        #print("you did it !")
    return results

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

def main(line):
    c = 0
    i = 0
    results = 0
    #print("input number :")
    while True:
        #line = input().split()
        mode = line[i]
        if mode == 'q':
            break
        elif mode == 'h':
            set_boad()
            #print("input number :")
            #continue
            break
        elif c == 0:
            results, sym, b = float(line[i]), line[i+1],float(line[i+2])
            i += 2
        elif i == (len(line) + 1) / 2: #@
            break                      #@
        else:
            sym, b, = line[2*i -1], float(line[2*i])
            i += 1

        results = Fourarithmeticoperations(sym, b, results, c)
        c += 1
    showresult(results, c)

if __name__ == "__main__":
    #set_boad()
    main(input().split())