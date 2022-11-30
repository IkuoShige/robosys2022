#!/bin/bash -xv
# SPDX-FileCopyrightText: 2022 Ikuo Shige
# SPDX-License-Identifier: BSD-3-Clause

ng (){
     echo NG at Line $1
     res=1
}

res=0

return_value (){
RET = $?
if [ ${RET} -eq 0 ]; then
     echo "ok"
else
     echo "error"
fi
}

### I/O TEST ###
out=$(echo '1 + 1' | ./calculator.py)
[ "${out}" = 2.0 ] || ng ${LINENO}
out=$(echo '1 + 1 * 1' | ./calculator.py)
[ "${out}" = 2.0 ] || ng ${LINENO}
out=$(echo '1 + 1 * 1 / 1 - 1' | ./calculator.py)
[ "${out}" = 1.0 ] || ng ${LINENO}
#out=$(echo 'h' | ./calculator.py)
#[ "${out}" = "*   f:三角関数(until)  a: 四則演算   h: ヘルプ                    *
#***************************************************************
#*   ex: input |3 + 3            output |===6                  *
#*             |+ 2                     |===8                  *
#*             |- 1                     |===7                  *
#*             |* 5                     |===35                 *
#*             |/ 6                     |===5.833333333333333  *
#*             |q                     finish                   *
#***************************************************************
#cancel" ] || ng ${LINENO}
out=$(echo 'q' | ./calculator.py)
[ "${out}" = "cancel" ] || ng ${LINENO}

[ "$res" = 0 ] && echo OK
exit $res