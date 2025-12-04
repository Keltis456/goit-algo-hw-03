import turtle


def koch_snowflake(t, length, level):
    if level == 0:
        t.forward(length)
    else:
        koch_snowflake(t, length / 3, level - 1)
        t.left(60)
        koch_snowflake(t, length / 3, level - 1)
        t.right(120)
        koch_snowflake(t, length / 3, level - 1)
        t.left(60)
        koch_snowflake(t, length / 3, level - 1)


def main():
    try:
        level = int(input("Вкажіть рівень рекурсії (напр. 3): "))
    except ValueError:
        print("Будь ласка, введіть ціле число.")
        return

    length = 300  # Довжина сторони сніжинки

    screen = turtle.Screen()
    screen.title("Сніжинка Коха")
    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()

    # Центруємо сніжинку
    t.penup()
    t.goto(-length / 2, length / 3)
    t.pendown()

    for _ in range(3):
        koch_snowflake(t, length, level)
        t.right(120)

    turtle.done()


if __name__ == "__main__":
    main()
