#1. hf
import sys

def count_of_local_maximums() -> int:
    if len(sys.argv) < 4:
        return 0

    counter = 0
    for i in range(1, len(sys.argv) - 1):
        if int(sys.argv[i]) > int(sys.argv[i - 1]) and int(sys.argv[i]) > int(sys.argv[i + 1]):
            counter += 1

    return counter

def main():
    result = count_of_local_maximums()
    print(result)

if __name__ == "__main__":
    main()
