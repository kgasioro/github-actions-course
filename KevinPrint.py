def print_large_text(text):
    """
    Prints the given text in large ASCII art characters.
    """
    # Define large characters (7 lines high)
    large_chars = {
        'K': [
            "K    K",
            "K   K ",
            "K  K  ",
            "KKK   ",
            "K  K  ",
            "K   K ",
            "K    K"
        ],
        'E': [
            "EEEEE",
            "E    ",
            "E    ",
            "EEEE ",
            "E    ",
            "E    ",
            "EEEEE"
        ],
        'V': [
            "V     V",
            "V     V",
            " V   V ",
            " V   V ",
            "  V V  ",
            "  V V  ",
            "   V   "
        ],
        'I': [
            "IIIII",
            "  I  ",
            "  I  ",
            "  I  ",
            "  I  ",
            "  I  ",
            "IIIII"
        ],
        'N': [
            "N     N",
            "NN    N",
            "N N   N",
            "N  N  N",
            "N   N N",
            "N    NN",
            "N     N"
        ]
    }
    
    # Print each line of the characters
    for line_idx in range(7):
        line = ""
        for char in text:
            if char in large_chars:
                line += large_chars[char][line_idx] + "  "
            else:
                line += "     "  # Space for unknown characters
        print(line)

if __name__ == "__main__":
    print_large_text("KEVIN")
