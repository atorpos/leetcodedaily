class reorganizestring:

    def reorganizeString(self, S: str):
        # if not S:
        #     return ""
        d = {}
        str = ""
        for c in S:
            d[c] = d.get(c, 0) + 1
        max_count = max(d.values())
        # if max_count > (len(S) + 1) // 2:
        #     return ""
        print(d.keys())

        for key in d:
            print(f"{d[key]} {key}")
            if d[key] >0:
                str += key
                d[key] -= 1
        print(str)