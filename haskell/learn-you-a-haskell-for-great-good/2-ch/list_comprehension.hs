list = [x*2 | x <- [1..10]]

list2 = [x*2 | x <- [1..10], x*2 >= 12] --predicate 
--take we want only the element which, when doubled, are >= 12
--think of predicate as the output filter, only outputs satisfying the
--constraint will be shown

--we want all numbers, x, from 50 to 100 whose remainder when divided w/ the 
--number 7 is 3
list3 = [x | x <- [50..100], x `mod` 7 == 3]

--weeding out lists by predicates AKA filtering
boomBangs xs = [ if x < 10 then "Boom!" else "Bang!" | x <- xs, odd x] 
--function odd returns True on ODD numbers and False otherwise
--example use in ghci 
-- boomBangs [7..13]
--

--How many predicates does this have?
list4 = [x | x <- [10..20], x /= 13, x /= 15, x /= 19]

list5 = [x*y | x <- [2,5,10], y <- [8,10,11]] -- equiv (2,5,10)*(8,10,11)

list6 = [ x*y | x <- [2,5,10], y <- [8,10,11], x*y > 50] 

nouns = ["hobo", "frog", "pope"]
adjectives = ["lazy", "grouchy", "scheming"]
list7 = [adjective ++ " " ++ noun | adjective <- adjectives, noun <- nouns] 


