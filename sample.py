from Position_Builder.position_builder import *


def main():
    builder = position_builder(symbol="BTC/USDT")

    # option_1 = option_info(price=9088, option_type=option_type.PUT, lot=0.2, premium=219.5425, side=side.LONG)
    # option_2 = option_info(price=8988, option_type=option_type.PUT, lot=0.4, premium=106.5640, side=side.SHORT)
    # future = future_info(price=9188, future_type=side.SHORT, lot=0.2)

    option_1 = option_info(price=9300, option_type=option_type.CALL, lot=0.2, premium=219.5425, side=side.LONG)
    option_2 = option_info(price=9400, option_type=option_type.CALL, lot=0.4, premium=106.5640, side=side.SHORT)
    future = future_info(price=9188, future_type=side.LONG, lot=0.2)
    option_3 = option_info(price=9600, option_type=option_type.CALL, lot=0.2, premium=277.361, side=side.LONG)
    option_4 = option_info(price=9700, option_type=option_type.CALL, lot=0.4, premium=152.198, side=side.SHORT)
    future_2 = future_info(price=9520, future_type=side.LONG, lot=0.2)

    builder.add_future(future_info=future)
    builder.add_option(option_info=option_1)
    builder.add_option(option_info=option_2)
    builder.add_option(option_info=option_3)
    builder.add_option(option_info=option_4)
    builder.add_future(future_2)

    # option_1 = option_info(price=9300, option_type=option_type.CALL, lot=0.4, premium=269.0009, side=side.SHORT)
    # future = future_info(price=9188, future_type=side.SHORT, lot=0.2)

    # builder.add_option(option_info=option_1)
    # builder.add_future(future_info=future)

    fee = 2.570543 + 1.285223 + 0.2 * 9188 * 2 * 0.0007 + 4

    builder.build_position(fee=fee, step=1, scale=1000)
    plt.show()


if __name__ == '__main__':
    main()
