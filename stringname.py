def print_full_name(first, last):
    last = last+'!'
   
    print("Hello",first,last,"You just nailed into python")

if __name__ == '__main__':
    first_name = input()
    last_name = input()
    print_full_name(first_name, last_name)