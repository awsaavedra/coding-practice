--list adding
numList = [1,2,3,4] ++ [9,10,11,12]
strList = "hello" ++ " " ++ "world"
wootList = ['w','o'] ++ ['o','t']

--adding to front of list
frontListAdd = 'A':" SMALL CAT"
frontListAdd2 = 5:[1,2,3,4,5]

-- !! ~ pop
popList = "Steve Buscemi" !! 6
popList2 = [9.4,33.2,96.2,11.2,23.25] !! 1

--list composites
list = [[1,2,3,4],[5,3,3,3],[1,2,2,3,4],[1,2,3]]
list2 = list ++ [[1,1,1,1]]
list3 = [6,6,6]:list
list4 = list !! 2

--basic list functions
  --head, tail, last, init,
  --length, null, reverse, take, drop,
  --maximum, minimum
  --sum, product, elem

listOf20 = [1..20]
alphabet = ['a'..'z']
twoStep = [2,4..20]
threeStep = [3,6..20]
noFloatingRanges = [0.1, 0.3 .. 1]

count = take 10 (cycle [1,2,3])
lol = take 12 (cycle "LOL ")  
