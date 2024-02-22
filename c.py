def check_constraint(value: int, operator: str, constraint: int) -> bool:
    """Проверяет условие."""
    if operator == ">":
        return value > constraint
    elif operator == "<":
        return value < constraint
    else:
        return False


def calculate_sum(column_names: list[str], table: list[list[int]], constraints: list[tuple[str, str, int]]) -> int:
    total_sum = 0
    for row in table:
        for constraint in constraints:
            column_name, operator, constraint_value = constraint
            column_index = column_names.index(column_name)
            if not check_constraint(row[column_index], operator, constraint_value):
                break
        else:
            total_sum += sum(row)
    return total_sum


if __name__ == '__main__':

    N, M, Q = map(int, input().split())
    column_names = input().split()
    table = []
    for _ in range(N):
        row = list(map(int, input().split()))
        table.append(row)
    constraints = []
    for _ in range(Q):
        constraint = input().split()
        constraints.append((constraint[0], constraint[1], int(constraint[2])))

    result = calculate_sum(column_names, table, constraints)
    print(result)
