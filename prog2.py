import argparse

parser = argparse.ArgumentParser()
parser.add_argument("square", help="give the square root of a given number", type=float)
args = parser.parse_args()
print(args.square**2)







'''parser = argparse.ArgumentParser()
parser.add_argument("echo1", help='echo string 1')
parser.add_argument("echo2", help='echo string 2')
args = parser.parse_args()
print(args.echo1)
print(args.echo2)'''








'''
parser = argparse.ArgumentParser(description="calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print(f"{args.x} to the power {args.y} equals {answer}")
else:
    print(f"{args.x}^{args.y} == {answer}")
'''

