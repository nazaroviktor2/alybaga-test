def current_diversity(a_counts: dict[int, int], b_counts: dict[int, int]) -> int:


    unique_cards = set(a_counts.keys()) | set(b_counts.keys())
    diversity = 0

    for card in unique_cards:
        diversity += abs(a_counts.get(card, 0) - b_counts.get(card, 0))
    return diversity


def calculate_diversity(
    a_cards: list[int],
    b_cards: list[int],
    changes: list[tuple[int, str, int]],
) -> list[int]:
    # будем хранить - карта: количество таких карт
    a_counts = {}
    b_counts = {}

    for card in a_cards:
        a_counts[card] = a_counts.get(card, 0) + 1
    for card in b_cards:
        b_counts[card] = b_counts.get(card, 0) + 1

    results = []
    for change in changes:
        cart_type, player, card = change

        if player == "A":
            a_counts[card] = a_counts.get(card, 0) + cart_type

            # будем удалять карты, которые закончились
            if a_counts[card] <= 0:
                del a_counts[card]

        else:  # игрок B
            b_counts[card] = b_counts.get(card, 0) + cart_type

            # будем удалять карты, которые закончились
            if b_counts[card] <= 0:
                del b_counts[card]

        results.append(current_diversity(a_counts, b_counts))

    return results


if __name__ == "__main__":
    N, M, Q = list(map(int, input().split()))
    A_cards = list(map(int, input().split()))
    B_cards = list(map(int, input().split()))
    game_changes = []
    for _ in range(Q):
        change = input().split()
        game_changes.append((int(change[0]), str(change[1]), int(change[2])))

    print(calculate_diversity(A_cards, B_cards, game_changes))
