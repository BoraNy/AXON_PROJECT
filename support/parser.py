import argparse
import math

parser = argparse.ArgumentParser()
parser.add_argument(
    'square',
    help='return square of input number',
    type=float
)

parser.add_argument(
    'square_root',
    help='return the square root of input number',
    type=float
)

args = parser.parse_args()

print(f'Square of {args.square} = {args.square**2}')
print(f'Square root of {args.square_root} = {math.sqrt(args.square_root)}')