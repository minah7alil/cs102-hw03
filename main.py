import sys
from statistics import mean


def main():
    assert len(sys.argv) > 1, "No input file path specified."

    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    with open (input_file_path, "r") as f:
        for inputs in f:
            inputs = inputs.strip("\n")
            inputs_ting = inputs.split(",")
            minah = []
            for x in inputs_ting:
                minah.append(float(x))
                average = mean(minah)
            print(f"{average}")


if __name__ == "__main__":
    main()
