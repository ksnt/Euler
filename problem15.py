# --*-- coding:utf-8 --*--

def main():
    result = []
    for i in range(1,41):
        result.append(i)
    ue = reduce(lambda x,y: x * y, result)

    a = []
    for i in range(1,21):
        a.append(i)
    shita = reduce(lambda x,y: x*y, a)
    print (ue / (shita * shita))


if __name__ == "__main__":
    main()

