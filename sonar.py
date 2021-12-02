
def sonar(*args):
    total_increase =0
    for index in range(len(args)):
        if index ==0:
            print("NA")
        else:
            if args[index] > args[index -1]:
                print("Greater", args[index])
                total_increase += 1
            else:
                print("Smaller", args[index])
    print(total_increase)
    return total_increase


sonar(199,200, 208, 210, 200, 207, 240, 269, 260,263)