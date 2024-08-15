from collections import deque

tools = deque([int(x) for x in input().split()])
substances = deque([int(x) for x in input().split()])

challenges = [int(x) for x in input().split()]

while tools and substances and challenges:
    curr_tool = tools.popleft()
    curr_subst = substances.pop()

    result = curr_tool * curr_subst

    if result in challenges:
        challenges.remove(result)
    else:
        tools.append(curr_tool + 1)
        substances.append(curr_subst - 1)

        if substances[-1] == 0:
            substances.pop()

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

if tools:
    print(f"Tools: {', '.join([str(el) for el in tools])}")
if substances:
    print(f"Substances: {', '.join([str(el) for el in substances])}")
if challenges:
    print(f"Challenges: {', '.join([str(el) for el in challenges])}")
