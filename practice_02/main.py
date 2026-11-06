word = ['мир', 'страна', 'континент']
def candies_for_bag(candies, bags):
    assert bags != 0, 'Возьмите хотябы 1 пакет'
    assert candies != 0, 'Возьмите хотябы 1 конфету'
    assert bags >=0, 'Количество не может быть отрицательным'
    assert candies >=0, 'Количество не может быть отрицательным'
    return candies / bags
a = sorted(word, key = lambda word: len(word),reverse=True)
print(candies_for_bag(125,5))
print(a)
