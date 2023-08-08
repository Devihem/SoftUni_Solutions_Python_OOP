from abc import ABC, abstractmethod
import time


class AbstractWork(ABC):

    @abstractmethod
    def work(self):
        pass


class AbstractEat(ABC):

    @abstractmethod
    def eat(self):
        pass


class Work(AbstractWork, AbstractEat):

    def work(self):
        print("I'm normal worker. I'm working.")

    def eat(self):
        print("Lunch break....(5 secs)")
        time.sleep(0)  # Default set to 5 ( Time is too precious to wait something so absurd)


class SuperWork(AbstractWork, AbstractEat):

    def work(self):
        print("I'm super worker. I work very hard!")

    def eat(self):
        print("Lunch break....(3 secs)")
        time.sleep(0)  # Default set to 3 ( Time is too precious to wait something so absurd)


class Robot(AbstractWork):

    def work(self):
        print("I'm a robot. I'm working....")


class AbstractManager(ABC):

    @abstractmethod
    def set_worker(self, worker):
        pass


class WorkManager(AbstractManager):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractWork), f"'worker' must be of type worker:{AbstractWork}"
        self.worker = worker

    def manage(self):
        self.worker.work()


class BreakManager(AbstractManager):

    def __init__(self):
        self.worker = None

    def set_worker(self, worker):
        assert isinstance(worker, AbstractEat), f"'worker' must be of type worker:{AbstractEat}"
        self.worker = worker

    def lunch_break(self):
        self.worker.eat()


# FILE TEST

work_manager = WorkManager()
break_manager = BreakManager()
work_manager.set_worker(Work())
break_manager.set_worker(Work())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(SuperWork())
break_manager.set_worker(SuperWork())
work_manager.manage()
break_manager.lunch_break()
work_manager.set_worker(Robot())
work_manager.manage()

try:
    break_manager.set_worker(Robot())
    break_manager.lunch_break()
except:
    pass
