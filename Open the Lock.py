'''
Open the Lock
  Go to Discuss
You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
Example 4:
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.
'''
class Solution:
    def change(self, comb):
        res = []
        for i, c in enumerate(comb):
            c = int(c)
            for x in [-1, 1]:
                k = (c + x + 10) % 10
                res.append(comb[:i] + str(k) + comb[(i + 1):])
        return res
        
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if '0000' in deadends:
            return -1
        
        seen = set(deadends)
        left = set(['0000'])
        right = set([target])
        steps = 0
        while left:
            tmp = set()
            for comb in left:
                if comb in right:
                    return steps
                seen.add(comb)
                for word in self.change(comb):
                    if word not in seen:
                        tmp.add(word)
                
            steps += 1
            print('left', left, 'right', right, '\n')
            left = tmp
            left, right = right, tmp
        return -1

class Solution3:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        def dist(code):
            return sum(min(int(c), 10-int(c)) for c in code)
        
        def neighbors(code):
            for i in range(4):
                pre, x, sur = code[:i], int(code[i]), code[i + 1:]
                yield pre + str((x - 1) % 10) + sur
                yield pre + str((x + 1) % 10) + sur
        
        dead = set(deadends)
        if '0000' in dead or target in dead: return -1
        last_moves = set(neighbors(target)) - dead
        if not last_moves: return -1
        ans = dist(target)
        for code in last_moves:
            if dist(code) < ans: return ans
        return ans + 2


class Solution2:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """
        if '0000' in deadends: # important!!!
            return -1
        
        # Return the length of the shortest path between root and target node.
        import queue
        queue1 = queue.Queue()# store all nodes which are waiting to be processed
        used = set();     # store all the used nodes
        step = -1;       # it need to be -1 first, since from root to root is 0, number of steps neeeded from root to current node
        # initialize
        queue1.put('0000') # add root to queue
        used.update(deadends) # add root to used;
        # BFS
        while not queue1.empty():
            step = step + 1
            # iterate the nodes which are already in the queue1
            size = queue1.qsize()
            for _ in range(size):
                cur = queue1.get() # cur = the first node in queue1;
                # return step if cur is target;
                if cur == target:
                    return step 
                neighbors = self.get_neighbors(cur)
                for next in neighbors:
                    if (next not in used):
                        queue1.put(next) # add next to queue1;
                        used.add(next) # add next to used;
                # remove the first node from queue1;
        return -1;          # there is no path from root to target
   
    def get_neighbors(self, cur):
        """
        :type cur: str, '0000'
        :rtype: list[str], ['1000', '9000', '0100', '0900', '0010', '0090', '0001', '0009']
        """
        # important!!!
        for i in range(4):
            yield cur[:i]+str((int(cur[i])+1)%10)+cur[i+1:]
            yield cur[:i]+str((int(cur[i])-11)%10)+cur[i+1:]

        # neighbours = []
        # next = {'0':'19', '1':'20', '2':'31', '3':'42', '4':'53', '5':'64', '6':'75', '7':'86', '8':'97', '9':'08'}
        # wheels = list(cur) # '0000'->['0','0','0','0']
        # neighbours.append(next[wheels[0]][0]+wheels[1]+wheels[2]+wheels[3]) # '1000'
        # neighbours.append(next[wheels[0]][1]+wheels[1]+wheels[2]+wheels[3]) # '9000'
        # neighbours.append(wheels[0]+next[wheels[1]][0]+wheels[2]+wheels[3]) # '0100'
        # neighbours.append(wheels[0]+next[wheels[1]][1]+wheels[2]+wheels[3]) # '0900'  
        # neighbours.append(wheels[0]+wheels[1]+next[wheels[2]][0]+wheels[3]) # '0010'                
        # neighbours.append(wheels[0]+wheels[1]+next[wheels[2]][1]+wheels[3]) # '0090'   
        # neighbours.append(wheels[0]+wheels[1]+wheels[2]+next[wheels[3]][0]) # '0001'                                
        # neighbours.append(wheels[0]+wheels[1]+wheels[2]+next[wheels[3]][1]) # '0009' 
        # return neighbours

deadends = ["0201","0101","0102","1212","2002"] # '9000', '1000', '0100', '0900', '0010', '0090', '0001', '0009']
target = "0202"
print(Solution2().openLock(deadends, target))
