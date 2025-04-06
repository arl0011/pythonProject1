class Computer:
    def __init__(self, cpu, memory):
        self.__cpu = cpu
        self.__memory = memory

    @property
    def cpu(self):
        return self.__cpu

    @property
    def memory(self):
        return self.__memory

    @cpu.setter
    def cpu(self, value):
        self.__cpu = value

    @memory.setter
    def memory(self, value):
        self.__memory = value

    def make_computations(self):
        print(f'Sum: {self.__cpu + self.__memory}')
        print(f'Difference: {self.__cpu - self.__memory}')
        print(f'Product: {self.__cpu * self.__memory}')
        if self.__memory != 0:
            print(f'Division: {self.__cpu / self.__memory}')
        else:
            print('Division: На ноль делить нельзя')

    def __str__(self):
        return f'CPU: {self.__cpu}, Memory: {self.__memory}'

    def __eq__(self, other):
        return self.__memory == other.memory
.
    def __ne__(self, other):
        return self.__memory != other.memory

    def __lt__(self, other):
        return self.__memory < other.memory

    def __le__(self, other):
        return self.__memory <= other.memory

    def __gt__(self, other):
        return self.__memory > other.memory

    def __ge__(self, other):
        return self.__memory >= other.memory


class Phone:
    def __init__(self, sim_cards_list):
        self.__sim_cards_list = sim_cards_list

    @property
    def sim_cards_list(self):
        return self.__sim_cards_list

    @sim_cards_list.setter
    def sim_cards_list(self, value):
        self.__sim_cards_list = value

    def call(self, sim_card_number, call_to_number):
        try:
            sim = self.__sim_cards_list[sim_card_number - 1]
            print(f'Идет звонок на номер {call_to_number} с сим-карты-{sim_card_number} - {sim}')
        except IndexError:
            print('Такой сим-карты нет')

    def __str__(self):
        return f'SIM cards: {", ".join(self.__sim_cards_list)}'


class SmartPhone(Computer, Phone):
    def __init__(self, cpu, memory, sim_cards_list):
        Computer.__init__(self, cpu, memory)
        Phone.__init__(self, sim_cards_list)

    def use_gps(self, location):
        print(f'Построение маршрута до {location}... GPS активирован!')

    def __str__(self):
        return f'CPU: {self.cpu}, Memory: {self.memory}, SIM cards: {", ".join(self.sim_cards_list)}'


computer1 = Computer(4, 8)
phone1 = Phone(['Beeline', 'O!', 'MegaCom'])
smartphone1 = SmartPhone(8, 16, ['Beeline', 'MegaCom'])
smartphone2 = SmartPhone(6, 12, ['O!'])

print(computer1)
print(phone1)
print(smartphone1)
print(smartphone2)

print(f'Smartphone1 is greater than Computer1: {smartphone1 > computer1}')
print(f'Smartphone2 is less than Computer1: {smartphone2 < computer1}')
print(f'Computer1 is equal to Smartphone2: {computer1 == smartphone2}')

print(f'Sum of CPU and Memory of Computer1:')
computer1.make_computations()

print(f'\nCall examples:')
phone1.call(1, '+996 777 99 88 11')
smartphone1.call(2, '+996 700 00 00 00')

print(f'\nUsing GPS on Smartphone1:')
smartphone1.use_gps('ЦУМ, Бишкек')
