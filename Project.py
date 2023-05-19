def s_block(input_data, s_table):
    output_data = []
    for i in input_data:
        output_data.append(s_table[i])
    return output_data

def inverse_Sblock(input_data, s_table_inverse):
    output_data = []
    for i in input_data:
        output_data.append(s_table_inverse.index(i))
    return output_data

def p_block(input_data, permutation_table):
    output_data = []
    for i in permutation_table:
        output_data.append(input_data[i])
    return output_data

def inverse_pBlock(input_data, permutation_table_inverse):
    output_data = [0] * len(input_data)
    for i, value in enumerate(permutation_table_inverse):
        output_data[value] = input_data[i]
    return output_data

def test_s_block():
    # Test case 1
    input_data = [0, 1, 2, 3]
    s_table = [1, 3, 0, 2]
    expected_output = [1, 3, 0, 2]

    # Check forward transformation
    s_block_output = s_block(input_data, s_table)
    print("Forward transformation of S-block:")
    print("Input       :", input_data)
    print("Output      :", s_block_output)
    print("Expected    :", expected_output)

    # Check inverse transformation
    s_table_inverse = [2, 0, 3, 1]
    inverse_s_block_output = inverse_Sblock(s_block_output, s_table_inverse)
    print("Inverse transformation of S-block:")
    print("Input       :", s_block_output)
    print("Output      :", inverse_s_block_output)
    print("Expected    :", input_data)
    assert s_block_output == expected_output
    assert set(inverse_s_block_output) == set(input_data)

    # Test case 2
    s_table_inverse = [2, 0, 1, 3, 7, 4, 5, 6]
    input_data = [0, 1, 2, 3, 4, 5, 6, 7]
    s_table = [3, 0, 1, 2, 7, 4, 5, 6]
    expected_output = [3, 0, 1, 2, 7, 4, 5, 6]

    print("S-block transformation:")
    print("-----------------------")
    print("Input       | Output")
    print("-----------------------")
    for i in range(0, len(input_data), 2):
        input_value = input_data[i:i + 2]
        s_block_output = s_block(input_value, s_table)
        inverse_s_block_output = inverse_Sblock(s_block_output, s_table_inverse)
        print(f"{input_value}   | {s_block_output}")
        print(f"             | {inverse_s_block_output}")
    print("-----------------------")

    print("S-block test passed successfully.")

def test_p_block():
    # Test 1
    input_data = [0, 1, 2, 3]
    permutation_table = [3, 0, 1, 2]
    expected_output = [3, 0, 1, 2]

    p_block_output = p_block(input_data, permutation_table)
    print("Forward transformation of P-block:")
    print("Input       :", input_data)
    print("Output      :", p_block_output)
    print("Expected    :", expected_output)

    permutation_table_inverse = [1, 2, 3, 0]
    inverse_p_block_output = inverse_pBlock(p_block_output, permutation_table_inverse)
    print("Inverse transformation of P-block:")
    print("Input       :", p_block_output)
    print("Output      :", inverse_p_block_output)
    print("Expected    :", input_data)
    assert p_block_output == expected_output
    assert set(inverse_p_block_output) == set(input_data)

    # Test 2
    input_data = [0, 1, 2, 3, 4, 5, 6, 7]
    permutation_table = [3, 0, 1, 2, 7, 4, 5, 6]
    expected_output = [3, 0, 1, 2, 7, 4, 5, 6]

    p_block_output = p_block(input_data, permutation_table)
    print("Forward transformation of P-block:")
    print("Input       :", input_data)
    print("Output      :", p_block_output)
    print("Expected    :", expected_output)

    permutation_table_inverse = [1, 2, 3, 0, 7, 4, 5, 6]
    inverse_p_block_output = inverse_pBlock(p_block_output, permutation_table_inverse)
    print("Inverse transformation of P-block:")
    print("Input       :", p_block_output)
    print("Output      :", inverse_p_block_output)
    print("Expected    :", input_data)
    assert p_block_output == expected_output
    assert set(inverse_p_block_output) == set(input_data)

    print("P-block test passed successfully.")

test_s_block()
test_p_block()