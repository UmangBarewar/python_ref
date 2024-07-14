class Solution:
    def countOfAtoms(self, formula: str) -> str:
        def parse():
            count = collections.Counter()
            while self.i < len(formula):
                if formula[self.i] == '(':
                    self.i += 1
                    inner_count = parse()
                    num = get_num()
                    for name, c in inner_count.items():
                        count[name] += c * num
                elif formula[self.i] == ')':
                    self.i += 1
                    return count
                else:
                    name = get_name()
                    num = get_num()
                    count[name] += num
            return count

        def get_name():
            name = formula[self.i]
            self.i += 1
            while self.i < len(formula) and formula[self.i].islower():
                name += formula[self.i]
                self.i += 1
            return name

        def get_num():
            num = 0
            while self.i < len(formula) and formula[self.i].isdigit():
                num = num * 10 + int(formula[self.i])
                self.i += 1
            return max(1, num)

        self.i = 0
        count = parse()
        return ''.join(name + (str(count[name]) if count[name] > 1 else '') 
                       for name in sorted(count))
