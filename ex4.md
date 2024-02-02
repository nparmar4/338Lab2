1. Describe the algorithm you will use to find the room. Assume all the information you have is the one given by the sign; you have no knowledge of the floor plan [0.5 pts]

    Considering the information given on the sign, the individual will likely enter the loop from the side farthest from room 128. The individual should use a linear search method for this search. They would check the number of each room sequentially until they have found the room they are looking for. The room numbers resemble a sorted array, and this will make the search easier. 

2. How many ”steps” it will take to find room EY128? And what is a “step” in this case? [0.25 pts]

    This process will take 15 steps. Each step in this case is checking an individual room's number, then entering it if it is the corect room or moving to the next room if it is not. 

3. Is this a best-case scenario, worst-case scenario, or neither? [0.25 pts]
    This is neither a best-case or worst-case scenerio. This is because the room we are looking for is neither the first room (best-case) or the last room (worst case) in the loop we are checking. 


4. With this particular sign and floor layout, explain what a worst-case or best- case scenario would look like [0.5 pts]

    The best-case scenario would be if the person is looking for room number 100, and follows the sign to find the room. Room 100 will be the first room they see. The worst case scenario is if the individual is looking for room number 130, and follows the sign to get there. This is because room 130 is the last room in the section specified on the sign, and they took the longer way to get there.

5. Suppose after a few weeks in the term you memorize the layout of the floor. How would you improve the algorithm to make it more efficient? [0.5 pts]

    I would improve the algorithm by making it conduct a search more similar to a binary search. I would do this by allowing it to check the numbers of the first and last room, then entering the loop from the side with a number closer to the desired number. Then, I would make the algorithm repeat its linear search approach but this time from the opposite side. That way, it will reach room 128 much quicker. 