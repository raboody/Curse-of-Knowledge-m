    blocks_to_remove = []


            blocks_to_remove.append(list(x))
            print(blocks_to_remove)
            for i in blocks_to_remove:
                if len(i) <= 1:
                    hypothesis_space.remove(i)
                elif len(i) > 1:
                    print(1)
            #print(x)
            #if len(x) <= 1:
                #hypothesis_space.remove(blocks_to_remove)
            #elif len(x) > 1:
 #               a = list(x) + ['AND']
#                b = list(x) + ['OR']
#                if a in hypothesis_space:
#                    hypothesis_space.remove(list(a))
#                if b in hypothesis_space:
#                    hypothesis_space.remove(list(b))




            if len(x) <= 1:
                hypothesis_space.remove(list(x))
            elif len(x) > 1:


                if a in hypothesis_space:
                    hypothesis_space.remove(list(a))
                if b in hypothesis_space:
                    hypothesis_space.remove(list(b))


            elif len(x) == len(machine_blocks):
                a = list(x) + ['AND']
                b = list(x) + ['OR']
                if a in hypothesis_space:
                    hypothesis_space.remove(list(a))
                if b in hypothesis_space:
                    hypothesis_space.remove(list(b))





                    

            elif len(x) > 1:
                for i in range(0, len(x) + 1):
                    for j in itertools.permutations(x, i):
                        if len(j) == len(x):
                            a = list(j) + ['AND']
                            b = list(j) + ['OR']
                            print(a, b)
                            if a in hypothesis_space:
                                hypothesis_space.remove(list(a))
                            if b in hypothesis_space:
                                hypothesis_space.remove(list(b)) 
