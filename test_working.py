

from working import convert

import pytest

def main() :

    testing_hours()
    testing_righthours()
    testing_formathours()

    
def testing_hours() :
    with pytest.raises(ValueError) :
        convert("13 AM to 17 PM")

def testing_righthours() :

 assert convert("9:00 AM to 7:30 PM") == '09:00 to 19:30'
 assert convert("8:30 AM to 6:30 PM") == '08:30 to 18:30'
 
def testing_formathours() :
    with pytest.raises(ValueError) :
        convert(" 9:00 AM - 7:30 PM")

    
if __name__ == "__main__":
    main()


