def letter_combinations(digits):
    leters = {
        '0':'.',
        '1': 'abc',
        '2': 'def',
        '3': 'ghi',
        '4': 'jkl',
        '5': 'mno',
        '6': 'pqr',
        '7': 'stu',
        '8': 'vwx',
        '9': 'yz'
    }
    output = [""]
    for i in digits:
        temp = []
        for j in output:
            for k in leters[i]:
                temp.append(j+k)
        output = temp
    
    return output

def main():
    digits = input('Ingrese un número: ')
    resultado = letter_combinations(digits)
    print(resultado)


if __name__ == '__main__':
    main()