def uppercase(str):
    #for ch in range(ord('A'), ord('Z') + 1):
        if 'a' <= str <= 'z':
            print("{}".format(chr(ord(str) - 32)))
        else:
            return str
