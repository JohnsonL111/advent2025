class Dial:
    def __init__(self, file: str, num=50):
        self.file = file
        self.num = num
        self.password = 0
        with open(file, 'r') as f:
            self.data = f.read()

    # 5 // 100 = 
    def findPassword(self):
        for line in self.data.split('\n'):
            # skip empty lines
            if not line:
                continue
            # valid line
            direction = int(line[1:]) 
            if line[0] == 'R':
                old = self.num
                self.num += direction
                new = self.num
                self.password += (new // 100) - (old // 100)

                self.num %= 100
            else:
                old = self.num
                self.num -= direction
                new = self.num
                self.password += ((old-1) // 100) - ((new-1)// 100)

                self.num %= 100

            # check password
            # if self.num == 0:
            #     self.password += 1

        print(f'password is {self.password}')
        return self.password


parser = Dial("in.txt");
parser.findPassword()
