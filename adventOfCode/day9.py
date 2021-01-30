from utils import open_puzzle_input

PREAMBLE = 25


class Que:
    def __init__(self):
        self.__inner_list = list()
        self.summation = 0

    def pop(self):
        popped = self.__inner_list.pop()
        self.summation -= popped
        return popped

    def append(self, item):
        self.summation += item
        self.__inner_list.insert(0, item)

    def __len__(self):
        return len(self.__inner_list)

    def __getattr__(self, item):
        return self.__inner_list.__getattribute__(item)

    def is_sum_of_two_distinct_items(self, sum):
        items_set = set(self.__inner_list)
        for cur_item in self.__inner_list:
            if (sum - cur_item) in items_set:
                return True
        return False

    def __iter__(self):
        return iter(self.__inner_list)

    def get_sum(self):
        return self.summation


def day9_1() -> int:
    q = Que()
    with open_puzzle_input(day=9) as fp:
        for idx, line in enumerate(fp):
            curr_num = int(line)
            if len(q) >= PREAMBLE:
                if not q.is_sum_of_two_distinct_items(curr_num):
                    return curr_num
                q.pop()
            q.append(curr_num)


def day9_2(ex1_res) -> int:
    q = Que()
    with open_puzzle_input(day=9) as fp:
        for line in fp:
            while q.get_sum() > ex1_res:
                q.pop()

            if q.get_sum() < ex1_res:
                q.append(int(line))

            elif q.get_sum() == ex1_res:
                print(max(q) , min(q))
                return max(q) + min(q)


ex1_res = day9_1()
print("ex1 res: ", ex1_res)
print("ex2 res: ", day9_2(ex1_res))
