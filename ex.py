class valuelarge(Exception):
    pass
class valuesmall(Exception):
    pass

def guess(num):
    while True:
        try:
            user=int(input())
            if user>num:
                raise 
            if user<num:
                raise valuesmall
            else:
                print("You win")
                exit()
        except valuelarge:
            print("value is too large")
        except valuesmall:
            print("value is too small")
if __name__ == "__main__":
    # num=24
    guess(3)

