class Car:
    totalDoors = 4
    totalTires = 4

    def doors(self):
        print(f'{self.totalDoors} doors')

    def tires(self):
        print(f'{self.totalTires} tires')


def main():
    ferrari = Car()
    ferrari.doors()
    ferrari.tires()


if __name__ == '__main__':
    main()
