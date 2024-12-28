# import pathlib

# print(pathlib.Path().resolve())  # Prints the current directory




def truncate_file(filename, line_number):
    # Open the file in read mode or create it if it doesn't exist
    try:
        with open(filename, "r") as file:
            lines = file.readlines()
            deps = set()
            new_lines = []
            for item in lines:
                if item not in deps:
                    new_lines.append(item)
                    deps.add(item)
                    
            print(len(lines))
            print(lines)
            print(len(new_lines))
            print(new_lines)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Creating a new file.")
        lines = [
            "aijgpijpgnwrgiwr giwagrgw",
            "wrgpijwrpjPWGJIWRG.GRWGPOKWOGWOMPJ",
            "go 2-inh   509hjnhi    ohi5hnphjpp5h bij   b",
            "hamipojwo hoinhkjNIJP0HJA HInHONITH PEAIN[ IOPNANH]",
            "wrgpijwrpjPWGJIWRG.GRWGPOKWOGWOMPJ",
        ]

        # Keep only lines up to the specified line number

        lines_to_keep = lines[:line_number]
        print(len(lines_to_keep))
        print(lines_to_keep)

        # Write back the truncated content
        with open(filename, "w") as file:
            for i in lines_to_keep:
                file.writelines(f"{i}\n")


# Example usage
truncate_file("example.txt", 10)
