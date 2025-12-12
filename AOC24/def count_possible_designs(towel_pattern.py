def count_possible_designs(towel_patterns, designs):
    towel_set = set(towel_patterns)
    possible_count = 0
    
    for design in designs:
        n = len(design)
        dp = [False] * (n + 1)
        dp[0] = True
        
        for i in range(1, n + 1):
            for towel in towel_set:
                towel_length = len(towel)
                if i >= towel_length and design[i-towel_length:i] == towel:
                    if dp[i-towel_length]:
                        dp[i] = True
                        break
        
        if dp[n]:
            possible_count += 1
            
    return possible_count

def read_input_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        
    # Split the lines into towel patterns and designs
    towel_patterns = []
    designs = []
    
    # Flag to indicate when we are in the designs section
    reading_designs = False
    
    for line in lines:
        line = line.strip()  # Remove any leading/trailing whitespace
        if line == "":
            reading_designs = True  # Switch to reading designs after the blank line
            continue
            
        if reading_designs:
            designs.append(line)  # Add to designs
        else:
            towel_patterns.append(line)  # Add to towel patterns
    
    return towel_patterns, designs

# Main script
filename = 'day 10.txt'  # Replace with your actual file name
towel_patterns, designs = read_input_file(filename)
result = count_possible_designs(towel_patterns, designs)
print(result)