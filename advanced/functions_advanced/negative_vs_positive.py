def sum_num(nums: list):
    positives = [int(num) for num in nums if num > 0]
    negatives = [int(num) for num in nums if num < 0]

    def sum_negatives():
        return sum(negatives)

    def sum_positives():
        return sum(positives)

    p_result = sum_positives()
    n_result = sum_negatives()

    print(n_result)
    print(p_result)

    if abs(p_result) > abs(n_result):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(num) for num in input().split()]


sum_num(numbers)
