import sys
import os

def main():
    if len(sys.argv) < 2:
        print("Usage: python generate.py <filename.py>")
        sys.exit(1)

    out_file = sys.argv[1]
  
    if not out_file.endswith(".py"):
        out_file += ".py"
    if os.path.exists(out_file):
        print(f"Error: '{out_file}' already exists.")
        sys.exit(1)

    template = f"""\
      import os
        
      def part_one():
          # TODO: implement part one
          return
    
      def part_two():
          # TODO: implement part two
          return
      
      def main():
          print("Welcome to {out_file}!")
          # part_one()
          # part_two()
      if __name__ == "__main__":
          main()
      """
    with open(out_file, "w") as f:
        f.write(template)
    print(f"Generated boilerplate file: {out_file}")

if __name__ == "__main__":
    main()
