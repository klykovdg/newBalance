from app.binary_tree.BinaryTree import BinaryTree


if __name__ == '__main__':
    bt = BinaryTree()
    k = [10, 4, 12, 2, 5, 11, 16, 1, 3, 7]
    v = ['ten', 'four my favorite number!', 'twelve', 'two', 'five', 'eleven', 'sixteen', 'one', 'three', 'seven']
    for i in range(len(k)):
        bt.add(k[i], v[i])
    print(bt.get(4))
