# 모눈 그리기
import turtle as t

t.setup(1600, 1024)
t.speed(0)


def draw_mesh(length = 100, grid = 5):
    """
    grid x grid 격자를 그립니다
    :param length: 한 변의 길이
    :param grid: 격자 개수
    :return: None
    """
    for i in range(grid + 1):
        t.forward(length * grid)
        t.up()
        t.goto(0, (i+1) * length)
        t.down()
    t.up()
    t.home()
    for i in range(grid + 1):
        t.setheading(90)
        t.down()
        t.forward(length * grid)
        t.up()
        t.goto((i+1) * length, 0)
    t.home()


# draw_mesh(50, 7)
draw_mesh()
t.exitonclick()


