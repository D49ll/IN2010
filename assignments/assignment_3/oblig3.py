import oblig3runner
import sys

def main(filename):
    large_n = False
    with open(filename, 'r') as f:
        A = [int(x) for x in f.readlines()]

    if len(A) >= 1000:
        large_n = True

    oblig3runner.run_algs_part1(A, filename, large_n)
    oblig3runner.run_algs_part2(A, filename, large_n)

if __name__ == '__main__':
    main(sys.argv[1])
