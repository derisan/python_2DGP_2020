# 이름 쓰기
import turtle as t

FIRST_FLOOR = 50
SECOND_FLOOR = 0
THIRD_FLOOR = -100
FOURTH_FLOOR = -170
HORIZONTAL_LEN = 100
VOWEL_GAP = 50
LETTER_GAP = 200
FIRST_WORD_X = -300
RADIUS = 35


def move(x, y):
    """
    :param x: 화면 x 좌표
    :param y: 화면 y 좌표
    :return: None
    """
    t.penup()
    t.goto((x, y))
    t.pendown()


def draw_mieum(left_top, right_bottom):
    """
    'ㅁ' 자를 그립니다
    :param left_top:
    :param right_bottom:
    :return:
    """
    t.goto(right_bottom[0], left_top[1])
    t.goto(right_bottom[0], right_bottom[1])
    t.goto(left_top[0], right_bottom[1])
    t.goto(left_top[0], left_top[1])


def draw_name():
    # ㄱ
    move(FIRST_WORD_X, SECOND_FLOOR)
    t.goto((FIRST_WORD_X + HORIZONTAL_LEN, SECOND_FLOOR))
    t.goto((FIRST_WORD_X, THIRD_FLOOR))
    # l
    move(FIRST_WORD_X + HORIZONTAL_LEN + VOWEL_GAP, FIRST_FLOOR)
    t.goto((FIRST_WORD_X + HORIZONTAL_LEN + VOWEL_GAP, THIRD_FLOOR))
    # ㅁ
    move(FIRST_WORD_X, THIRD_FLOOR)
    draw_mieum((FIRST_WORD_X, THIRD_FLOOR), (FIRST_WORD_X + HORIZONTAL_LEN + VOWEL_GAP, FOURTH_FLOOR))
    SECOND_WORD_X = FIRST_WORD_X + LETTER_GAP
    # ㅁ
    move(SECOND_WORD_X, SECOND_FLOOR)
    draw_mieum((SECOND_WORD_X, SECOND_FLOOR), (SECOND_WORD_X + HORIZONTAL_LEN, THIRD_FLOOR))
    # ㅕ
    move(SECOND_WORD_X + HORIZONTAL_LEN + VOWEL_GAP, FIRST_FLOOR)
    t.goto(SECOND_WORD_X + HORIZONTAL_LEN + VOWEL_GAP, THIRD_FLOOR)
    move(SECOND_WORD_X + HORIZONTAL_LEN + VOWEL_GAP, SECOND_FLOOR - 10)
    t.goto(SECOND_WORD_X + HORIZONTAL_LEN, SECOND_FLOOR - 10)
    move(SECOND_WORD_X + HORIZONTAL_LEN + VOWEL_GAP, THIRD_FLOOR + 10)
    t.goto(SECOND_WORD_X + HORIZONTAL_LEN, THIRD_FLOOR + 10)
    # ㅇ
    move(SECOND_WORD_X + HORIZONTAL_LEN, FOURTH_FLOOR)
    t.circle(RADIUS)
    THIRD_WORD_X = SECOND_WORD_X + LETTER_GAP
    # ㄱ
    move(THIRD_WORD_X, SECOND_FLOOR)
    t.goto((THIRD_WORD_X + HORIZONTAL_LEN, SECOND_FLOOR))
    t.goto((THIRD_WORD_X + HORIZONTAL_LEN, THIRD_FLOOR))
    # ㅠ
    move(THIRD_WORD_X - 20, THIRD_FLOOR)
    t.goto((THIRD_WORD_X + HORIZONTAL_LEN + 20, THIRD_FLOOR))
    move(THIRD_WORD_X, THIRD_FLOOR)
    t.goto((THIRD_WORD_X, FOURTH_FLOOR))
    move(THIRD_WORD_X + HORIZONTAL_LEN, THIRD_FLOOR)
    t.goto((THIRD_WORD_X + HORIZONTAL_LEN, FOURTH_FLOOR))


t.speed(0)
draw_name()
t.exitonclick()
