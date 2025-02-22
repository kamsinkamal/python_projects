import argparse

# Create parser
parser = argparse.ArgumentParser(description="Example CLI tool")

# Add arguments
parser.add_argument("--name", required=True, help="Your name")
parser.add_argument("--age", type=int, help="Your age")

# Parse arguments
args = parser.parse_args()

# Print user input
print(f"Hello {args.name}! Your age is {args.age}.")
