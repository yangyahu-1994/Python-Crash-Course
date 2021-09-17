# 编写函数
def make_shirt(size, typeface):
    """显示T恤的尺寸和标志"""
    print(f"\nThe size of the T-shirt is: {size} and the words of the T-shirt are: {typeface.title()}.")

make_shirt('XXL', 'I love you!')
make_shirt(size='XXL', typeface='I love you!')