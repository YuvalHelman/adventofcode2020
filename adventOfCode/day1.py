from typing import List


def find_sum_indices(items: List[int], sum_of_items) -> (int, int):
    start_idx, last_idx = 0, len(items) - 1

    for i in range(2 * len(items)):
        if start_idx >= last_idx:
            return None
        if items[start_idx] + items[last_idx] < sum_of_items:
            start_idx += 1
        elif items[start_idx] + items[last_idx] > sum_of_items:
            last_idx -= 1
        else:
            return start_idx, last_idx
    return None


def ex1(items: List[int], sum_of_items: int) -> int:
    items = sorted(items)
    res = find_sum_indices(items, sum_of_items)
    if res is None:
        print("Failed to find")
    first_idx, scd_idx = res
    print("ex1 items: ", items[first_idx], items[scd_idx])
    return items[first_idx] * items[scd_idx]


def ex2(items: List[int], sum_of_items: int) -> int:
    items = sorted(items)
    for i in range(len(items)):
        res = find_sum_indices(items, sum_of_items - items[i])
        if res is None:
            continue
        first_idx, scd_idx = res
        if items[first_idx] + items[scd_idx] + items[i] == sum_of_items:
            print("ex2 items: ",items[first_idx], items[scd_idx], items[i])
            return items[first_idx] * items[scd_idx] * items[i]


if __name__ == "__main__":
    items = [1310, 1960, 1530, 1453, 1572, 1355, 1314, 1543, 1439, 1280, 1367, 1368, 1313, 1423, 1771, 1868, 1555, 1635,
             1200, 2009, 1649, 1824, 1979, 1523, 1548, 1415, 1371, 101, 1836, 1570, 1494, 1850, 1624, 1151, 1408, 1220,
             1372, 1871, 1712, 1765, 1950, 1654, 1797, 1814, 1592, 1747, 1566, 1600, 1445, 1297, 1374, 1916, 274, 1735,
             1392, 1977, 1957, 1672, 249, 1980, 1791, 1733, 1962, 1641, 1487, 1486, 1741, 1751, 1309, 1342, 1567, 1353,
             1909, 1657, 1837, 1438, 1510, 1811, 1939, 1558, 1215, 2010, 1891, 1929, 1208, 1459, 1272, 1696, 1820, 1206,
             1414, 1795, 1884, 1734, 1745, 421, 1908, 1986, 1329, 932, 1468, 1720, 1769, 1402, 1913, 1580, 1707, 1799,
             1185, 1587, 1521, 1428, 1210, 1822, 194, 1973, 2000, 1940, 1481, 1509, 1563, 1697, 1924, 1671, 1516, 1758,
             1552, 1996, 2002, 1883, 1539, 1089, 1794, 1337, 1875, 1736, 1683, 1682, 1354, 1846, 1427, 1359, 1854, 1574,
             1198, 359, 1859, 1517, 1706, 1537, 1915, 1983, 1482, 1941, 1703, 1954, 1597, 1903, 1991, 53, 1515, 1259,
             1421, 1384, 1948, 1776, 1965, 1625, 1478, 1629, 1949, 1144, 1951, 1656, 1137, 1349, 1910, 1483, 1229, 1480,
             1324, 1664, 1604, 1764, 1564, 1673, 1686, 1841, 1640, 1627, 1984, 1258, 1376, 855, 1413, 1261, 1429, 1863,
             1540, 692]
    items = sorted(items)
    print("ex1 res: ", ex1(items, 2020))
    print("ex2 res: ", ex2(items, 2020))
