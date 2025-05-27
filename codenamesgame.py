import random
from dataclasses import dataclass
from colorama import init, Fore, Back, Style
init(autoreset=True)
@dataclass
class WordCard():
    word: str
    team: str

def load_word_list(path: str) -> list[str]:
    with open(path, 'r', encoding='utf-8') as f:
        return [line.strip() for line in f if line.strip()]


def deal_codenames_board(words: list[str],
                         red_count: int = 9,
                         blue_count: int = 8,
                         neutral_count: int = 7,
                         assassin_count: int = 1
                         ) -> list[WordCard]:
    selected = random.sample(words, red_count + blue_count + neutral_count + assassin_count)

    roles = (
        ["RED"] * red_count +
        ["BLUE"] * blue_count +
        ["NEUTRAL"] * neutral_count +
        ["ASSASSIN"] * assassin_count
    )
    random.shuffle(roles)

    return [WordCard(word, team) for word, team in zip(selected, roles)]

COLOR_MAP = {
    "RED":      Fore.RED,
    "BLUE":     Fore.BLUE,
    "NEUTRAL":  Fore.LIGHTBLACK_EX,
    "ASSASSIN": Back.WHITE + Fore.BLACK,
}
def print_board(board: list[WordCard]):
    for row in range(5):
        row_cards = board[row*5:(row+1)*5]
        styled = []
        for c in row_cards:
            color = COLOR_MAP.get(c.team, Style.RESET_ALL)
            styled.append(f"{color}{c.word:<10}{Style.RESET_ALL}")
        print(" ".join(styled))

if __name__ == "__main__":
    words = load_word_list("codenames.txt")
    starter = random.choice(["RED", "BLUE"])
    red_ct, blue_ct = (9, 8) if starter=="RED" else (8, 9)
    print(f"{starter} team goes first (they get {max(red_ct,blue_ct)} words)\n")

    board = deal_codenames_board(words,
                                 red_count=red_ct,
                                 blue_count=blue_ct,
                                 neutral_count=7,
                                 assassin_count=1)
    print_board(board)