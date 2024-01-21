def print_formatted(number):
        print(number,oct(number),hex(number),bin(number),end='')
    

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)