import sys,time
from typing import Any
from termcolor import colored

class progress_bar():
    def __init__(self, stop, start=0, bar_length=50):
        self.count = start
        self.stop = stop
        self.bar_length = bar_length
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.count == self.stop:
            print('')
            raise StopIteration
        
        elif self.count != self.stop:
            self.count += 1


            percentage = round(self.count * 100/self.stop, 2)
            bar_percentage = '〙' + str(percentage) + '%'
            
            if round(self.count * 100/self.stop, 2) == 100:
                bar_percentage = colored(bar_percentage, 'green')
            
            bar = colored('〘','green') + colored('█','green')*round((percentage*(self.bar_length/(100/self.bar_length))/self.bar_length)) + "-" * (round(self.bar_length-percentage*(self.bar_length/(100/self.bar_length))/self.bar_length)) # god pleaseh elp me i dont know what this math is oh my god ??? wtf is this what how why what
            sys.stdout.write(f"{bar}{bar_percentage} \r")
            sys.stdout.flush()
            return self.count

class progress_bar_manual():
    def __init__(self, total, bar_length=50):
        self.count = 0
        self.stop = total
        self.bar_length = bar_length
    
    def update(self, added_count):
        
        if self.count == self.stop:
            print('')
            raise StopIteration
        
        elif self.count != self.stop:
            self.count += added_count


            percentage = round(self.count * 100/self.stop, 2)
            bar_percentage = '〙' + str(percentage) + '%'
            
            if round(self.count * 100/self.stop, 2) == 100:
                bar_percentage = colored(bar_percentage, 'green')
            
            bar = colored('〘','green') + colored('█','green')*round((percentage*(self.bar_length/(100/self.bar_length))/self.bar_length)) + "-" * (round(self.bar_length-percentage*(self.bar_length/(100/self.bar_length))/self.bar_length)) # god pleaseh elp me i dont know what this math is oh my god ??? wtf is this what how why what
            sys.stdout.write(f"{bar}{bar_percentage} \r")
            sys.stdout.flush()


class animation():
    def __init__(self, stop, start=0):
        self.count = start
        self.stop = stop
    
    def __iter__(self):
        return self
    
    def __next__(self):
        
        if self.count == self.stop:
            print('')
            raise StopIteration
        
        elif self.count != self.stop:
            self.count += 1
            anim=r'-\|/'
            sys.stdout.write('[%s]\r' % (anim[self.count % 4]))
            sys.stdout.flush()
            return self.count

