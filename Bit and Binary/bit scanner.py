def scan_secret_code(secret_code: int, access_key: int, bit_width: int = 8):
    mask = (1 << bit_width) - 1
    secret = secret_code & mask
    key = access_key & mask

    print(f"Secret Code : {secret:3d} -> 0b{secret:0{bit_width}b}")
    print(f"Access Key  : {key:3d} -> 0b{key:0{bit_width}b}")
    print("-" * 45)

    # Compare bits
    common_bits = secret & key
    combined_bits = secret | key
    diff_bits = secret ^ key

    print(f"AND (Common 1s)  : {common_bits:3d} -> 0b{common_bits:0{bit_width}b}")
    print(f"OR  (Combined 1s): {combined_bits:3d} -> 0b{combined_bits:0{bit_width}b}")
    print(f"XOR (Differences): {diff_bits:3d} -> 0b{diff_bits:0{bit_width}b}")

    # Flip all bits within bit_width
    flipped_secret = (~secret) & mask
    print(f"Flipped Secret   : {flipped_secret:3d} -> 0b{flipped_secret:0{bit_width}b}")

    # Shift left and right (masked to bit_width)
    shifted_left = (secret << 1) & mask
    shifted_right = secret >> 1
    print(f"Shift Left 1     : {shifted_left:3d} -> 0b{shifted_left:0{bit_width}b}")
    print(f"Shift Right 1    : {shifted_right:3d} -> 0b{shifted_right:0{bit_width}b}")

    # Count set bits (1s)
    print(f"Set bits in Secret: {secret.bit_count()}")
    print(f"Set bits in Key   : {key.bit_count()}")
    print(f"Differing bits    : {diff_bits.bit_count()}")

    # Scan individual bit positions (0 = LSB)
    active_positions = [i for i in range(bit_width) if (secret >> i) & 1]
    print(f"Active bit indices in Secret (LSB=0): {active_positions}")


scan_secret_code(secret_code=0b10110100, access_key=0b11010010, bit_width=8)