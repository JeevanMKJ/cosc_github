def main():

    with open('2-Zach_transcript.srt', 'r', encoding='utf-8') as transcript_file, open('transcript_only_text.txt', 'w') as text_file:
        text_lines = [line.strip() for line in transcript_file if has_text(line)]

        for line in text_lines:
            text_file.write(f"{line}\n")
            print(line)

def has_text(line):
    line = line.strip()
    if not line:  # Skip empty lines
        return False
    if line.isdigit():  # Skip number lines
        return False
    if "-->" in line:  # Skip timestamp lines
        return False
    return True

if __name__ == '__main__':
    main()