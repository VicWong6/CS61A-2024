from itertools import chain

def shuffle(s):
    """Return a shuffled list that interleaves the two halves of s.

    >>> shuffle(range(6))
    [0, 3, 1, 4, 2, 5]
    >>> letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    >>> shuffle(letters)
    ['a', 'e', 'b', 'f', 'c', 'g', 'd', 'h']
    >>> shuffle(shuffle(letters))
    ['a', 'c', 'e', 'g', 'b', 'd', 'f', 'h']
    >>> letters  # Original list should not be modified
    ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    """
    assert len(s) % 2 == 0, 'len(seq) must be even'
    "*** YOUR CODE HERE ***"

    "=======官方解法，只用一次循环==============="
    """
    half = len(s) // 2
    result = []
    for i in range(half):
        result.append(s[i])
        result.append(s[i + half])
    return result
    """

    "=======个人解法，运用刚学的zip函数==============="
    half = len(s) // 2 # len(s) must be even, so quotient must integer
    left, right = s[0:half], s[half:] # left: [0, 1, 2], right: [3, 4, 5]
    mix = list(zip(left, right)) # mix: [(0, 3), (1, 4), (2, 5)]

    "=========以下是将mix转换为一个列表的多种方法===================="
    # 方式一：解包所有元组，chain 串联
    # result = list(chain(*mix))

    # 方式二：The fastest performance in big data scenarios because there is no need to unpack
    result = list(chain.from_iterable(mix)) # best in big data

    # 方式三：原理：[] + (0,3) + (1,4) + (2,5)，元组自动转为列表拼接
    # 此方法时间复杂度为 O (n²)，数据量大时不推荐。
    # result = sum(mix, [])
    
    return result


def deep_map(f, s):
    """Replace all non-list elements x with f(x) in the nested list s.

    >>> six = [1, 2, [3, [4], 5], 6]
    >>> deep_map(lambda x: x * x, six)
    >>> six
    [1, 4, [9, [16], 25], 36]
    >>> # Check that you're not making new lists
    >>> s = [3, [1, [4, [1]]]]
    >>> s1 = s[1]
    >>> s2 = s1[1]
    >>> s3 = s2[1]
    >>> deep_map(lambda x: x + 1, s)
    >>> s
    [4, [2, [5, [2]]]]
    >>> s1 is s[1]
    True
    >>> s2 is s1[1]
    True
    >>> s3 is s2[1]
    True
    """
    "*** YOUR CODE HERE ***"

    for i in range(len(s)):
        if type(s[i]) != list:
            s[i] = f(s[i])
        else:
            deep_map(f, s[i])


HW_SOURCE_FILE=__file__


def planet(mass):
    """Construct a planet of some mass."""
    assert mass > 0
    "*** YOUR CODE HERE ***"
    return ['planet', mass]

def mass(p):
    """Select the mass of a planet."""
    assert is_planet(p), 'must call mass on a planet'
    "*** YOUR CODE HERE ***"
    return p[1]

def is_planet(p):
    """Whether p is a planet."""
    return type(p) == list and len(p) == 2 and p[0] == 'planet'

def examples():
    t = mobile(arm(1, planet(2)),
               arm(2, planet(1)))
    u = mobile(arm(5, planet(1)),
               arm(1, mobile(arm(2, planet(3)),
                             arm(3, planet(2)))))
    v = mobile(arm(4, t), arm(2, u))
    return t, u, v

def total_mass(m):
    """Return the total mass of m, a planet or mobile.

    >>> t, u, v = examples()
    >>> total_mass(t)
    3
    >>> total_mass(u)
    6
    >>> total_mass(v)
    9
    """
    if is_planet(m):
        return mass(m)
    else:
        assert is_mobile(m), "must get total mass of a mobile or a planet"
        return total_mass(end(left(m))) + total_mass(end(right(m)))

def balanced(m):
    """Return whether m is balanced.

    ![Balanced Image](https://file.notion.so/f/f/da765eaf-5964-4902-8df7-82bae0b88a33/30369d50-f4db-482a-9449-49da15b3ee5a/image.png?table=block&id=2d1903dc-eab7-80d3-8b83-fed8314b015d&spaceId=da765eaf-5964-4902-8df7-82bae0b88a33&expirationTimestamp=1766448000000&signature=EOPMUAaWDiDwFhyb8KLLPH3bKptjMe3QtEx0LnH1Xo0&downloadName=image.png)

    >>> t, u, v = examples()
    >>> balanced(t)
    True
    >>> balanced(v)
    True
    >>> p = mobile(arm(3, t), arm(2, u))
    >>> balanced(p)
    False
    >>> balanced(mobile(arm(1, v), arm(1, p)))
    False
    >>> balanced(mobile(arm(1, p), arm(1, v)))
    False
    >>> from construct_check import check
    >>> # checking for abstraction barrier violations by banning indexing
    >>> check(HW_SOURCE_FILE, 'balanced', ['Index'])
    True
    """
    "*** YOUR CODE HERE ***"

    # 1. Base Case: 如果 m 是一个星球 (planet)，它本身就是平衡的（没有力矩需要比较）。
    if is_planet(m):
        return True
    else:
        # 2. 获取左右臂末端挂着的东西（可能是 planet 也可能是另一个 mobile）
        left_end, right_end = end(left(m)), end(right(m))

        # 3. 计算力矩 (Torque = Length * Mass)
        # 注意：这里需要调用 total_mass 来获取挂在末端物体的总质量
        torque_left = length(left(m)) * total_mass(left_end)
        torque_right = length(right(m)) * total_mass(right_end)

        # 4. 递归判断三个条件：
        # (1) 当前层的力矩是否相等
        # (2) 左边的子装置是否内部平衡
        # (3) 右边的子装置是否内部平衡
        return torque_left == torque_right and balanced(left_end) and balanced(right_end)

    """
        Official Solution:
        
        The fact that planets are balanced is important, since we will be solving this recursively like many other tree problems (even though this is not explicitly a tree).

        Base case: if we are checking a planet, then we know that this is balanced. Why is this an appropriate base case? There are two possible approaches to this:

        Because we know that our data structures so far are trees, planets are the simplest possible tree since we have chosen to implement them as leaves.
        We also know that from a data abstraction standpoint, planets are the terminal item in a mobile. There can be no further mobile structures under this planet, so it makes sense to stop check here.
        Otherwise: note that it is important to do a recursive call to check if both arms are balanced. However, we also need to do the basic comparison of looking at the total mass of both arms as well as their length. For example if both arms are a planet, trivially, they will both be balanced. However, the torque must be equal in order for the entire mobile to balanced (i.e. it's insufficient to just check if the arms are balanced).
    """




def berry_finder(t):
    """Returns True if t contains a node with the value 'berry' and 
    False otherwise.

    >>> scrat = tree('berry')
    >>> berry_finder(scrat)
    True
    >>> sproul = tree('roots', [tree('branch1', [tree('leaf'), tree('berry')]), tree('branch2')])
    >>> berry_finder(sproul)
    True
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> berry_finder(numbers)
    False
    >>> t = tree(1, [tree('berry',[tree('not berry')])])
    >>> berry_finder(t)
    True
    """
    "*** YOUR CODE HERE ***"
    if label(t) == 'berry':
        return True
    
    # 方法一：
    # return any(berry_finder(b) for b in branches(t))

    # 方法二
    for b in branches(t):
        if berry_finder(b):
            return True
    return False

    

HW_SOURCE_FILE=__file__


def max_path_sum(t):
    """Return the maximum root-to-leaf path sum of a tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t) # 1, 10
    11
    >>> t2 = tree(5, [tree(4, [tree(1), tree(3)]), tree(2, [tree(10), tree(3)])])
    >>> max_path_sum(t2) # 5, 2, 10
    17
    """
    "*** YOUR CODE HERE ***"
    
    if is_leaf(t):
        return label(t)
    else:
        # 算出所有子树的最大路径和，取其中最大的一个
        max_num = max([ max_path_sum(b) for b in branches(t)])
        # 加上自己的值返回
        return label(t) + max_num


def mobile(left, right):
    """Construct a mobile from a left arm and a right arm."""
    assert is_arm(left), "left must be an arm"
    assert is_arm(right), "right must be an arm"
    return ['mobile', left, right]

def is_mobile(m):
    """Return whether m is a mobile."""
    return type(m) == list and len(m) == 3 and m[0] == 'mobile'

def left(m):
    """Select the left arm of a mobile."""
    assert is_mobile(m), "must call left on a mobile"
    return m[1]

def right(m):
    """Select the right arm of a mobile."""
    assert is_mobile(m), "must call right on a mobile"
    return m[2]

def arm(length, mobile_or_planet):
    """Construct an arm: a length of rod with a mobile or planet at the end."""
    assert is_mobile(mobile_or_planet) or is_planet(mobile_or_planet)
    return ['arm', length, mobile_or_planet]

def is_arm(s):
    """Return whether s is an arm."""
    return type(s) == list and len(s) == 3 and s[0] == 'arm'

def length(s):
    """Select the length of an arm."""
    assert is_arm(s), "must call length on an arm"
    return s[1]

def end(s):
    """Select the mobile or planet hanging at the end of an arm."""
    assert is_arm(s), "must call end on an arm"
    return s[2]



# Tree Data Abstraction

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

