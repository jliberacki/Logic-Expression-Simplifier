from tools import * 

def compare_values(x,y):
    for el_x, el_y in zip(x,y):
        if(el_x == '-' or el_x==el_y):
            continue
        else:
            return False
    return True
    
def parent_dec_value(values):
    output = []
    for value in values:
        tmp_bin = [0 for i in value]
        parents = []
        for i in range(2 ** len(value)):
            if compare_values(value, tmp_bin):
                parents.append(bin_to_dec(tmp_bin))
            tmp_bin = add_one(tmp_bin)
        output.append(parents)
    return output

def group_expressions(values, variables_num):
    output = [[] for i in range(variables_num + 1)]
    for value in values:
        output[value.count(1)].append(value)
    return output

def search_prime(groups):
    groups = remove_duplicates(groups)
    groups_numbers = parent_dec_value([subgroup for subgroup in groups if subgroup])
    primes = []
    for group, number_group in zip(groups, groups_numbers):
        for num in number_group:
            if ([item for slist in groups_numbers for item in slist].count(num) == 1 and group not in primes):
                primes.append(group)
    return primes

def simplify_values(x, y):
    diff_control=0
    output = []
    for el_x, el_y in zip(x, y):
        if (el_x != el_y):
            output.append('-')
            diff_control += 1
        else:
            output.append(el_x)
    if diff_control==1:
        return output
    else:
        return []

def qm(values, prime_values, variables_num):
    assigned_groups = group_expressions(values, variables_num)
    merged_groups = []
    not_prime_v = []
    for group_index in range(len(assigned_groups) - 1):
        for value_one in assigned_groups[group_index]:
            for value_two in assigned_groups[group_index + 1]:
                merged_value = simplify_values(value_one, value_two)
                if not merged_value:
                    continue
                else:
                    merged_groups.append(merged_value)
                    if value_one not in not_prime_v:
                        not_prime_v.append(value_one)
                    if value_two not in not_prime_v:
                        not_prime_v.append(value_two)
    prime_values.extend([v for v in values if v not in not_prime_v])
    if merged_groups == []:
        return search_prime(prime_values)
    else:
        return qm(merged_groups, prime_values, variables_num)

def get_result(groups, vars):
    result = []
    for element in groups:
        for var, token in zip(vars, element):
            if (token == '-'):
                continue
            elif token == 0:
                result.extend(['(', '~', var, ')', '&'])
            else:
                result.extend([var, '&'])
        result = result[:-1]
        result.extend(['|'])
    result = result[:-1]
    return result if result != [] else '1'



