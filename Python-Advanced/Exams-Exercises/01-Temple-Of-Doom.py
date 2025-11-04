#Temple Of Doom

tools = [int(i) for i in input().split()]
substances = [int(i) for i in input().split()]

challenges = [int(i) for i in input().split()]

while True:
    if tools and substances:
        tool = tools[0]
        substance = substances[-1]
        result = tool * substance
        if result in challenges:
            challenges.remove(result)
            tools.pop(0)
            substances.pop(-1)
            if not challenges:
                print (f"Harry found an ostracon, which is dated to the 6th century BCE.")
                if tools:
                    print (f"Tools: {', '.join(map(str, tools))}")
                if substances:
                    print (f"Substances: {', '.join(map(str, substances))}")
                break
        else:
            #tools[0] += 1
            tools.pop(0)
            tools.append(tool + 1)
            if substance - 1 <= 0:
                substances.pop(-1)
            else:
                substances[-1] -= 1
    else:
        if challenges:
            print (f"Harry is lost in the temple. Oblivion awaits him.")
            if tools:
                print (f"Tools: {', '.join(map(str, tools))}")
            if substances:
                print (f"Substances: {', '.join(map(str, substances))}")
            print (f"Challenges: {', '.join(map(str, challenges))}")
            break