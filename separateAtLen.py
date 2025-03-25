def break_lines(s, k):
    words = s.split()
    lines = []
    line_length = 0
    start_index = 0

    for i, word in enumerate(words):
        if len(word) > k:
            # Word is too long for any line
            return None
        # Check if adding the word would exceed the limit
        if line_length + len(word) <= k:
            # Add the word to the current line
            if line_length > 0:
                line_length += 1  # Account for the space
            line_length += len(word)
        else:
            # Add the current line to the list and start a new line
            lines.append(" ".join(words[start_index:i]))
            start_index = i
            line_length = len(word)

    # Add the last line to the list if it's not empty
    if start_index < len(words):
        lines.append(" ".join(words[start_index:]))

    return lines if lines else None

# Example usage
s = "the quick brown fox jumps over the lazy dog"
k = 10
print(break_lines(s, k))