doubleMe x = x + x
doubleUs x y = x*2 + y*2

doubleUs x y = doubleMe x + doubleMe y

doubleSmallNumber x = if x > 100
                         then x
                         else x*2
--alernative notation to above
doubleSmallNumber' x = (if x > 100 then x else x*2) + 1

conanO'Brien = "It's a-me, Conan O'Brien!"

-- !! ~ pop
popList = "Steve Buscemi" !! 6
popList2 = [9.4,33.2,96.2,11.2,23.25] !! 1  
