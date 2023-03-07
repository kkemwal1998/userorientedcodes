



# Problem set
import sys
import fpdf
from fpdf import FPDF 

class PDF() :


    def __init__(self, A) :   # We will be using __init__ in this function.

        self._pdf = FPDF()

        self._pdf.add_page()
        # Thus we will be adding the font.
        self._pdf.set_font("helvetica","B",60)
         

        self._pdf.cell(0,70,"CS50 Shirtificate", new_x = "LMARGIN", new_y= "NEXT", align= "C")

        # Thus we will using the image that we have downloaded ftom the assingment in png format.
        self._pdf.image("shirtificate.png", w=self._pdf.epw)

        self._pdf.set_font_size(40)           # We will be setting up the font size.
        # Therefore, I have added green text to my shirt.  
        self._pdf.set_text_color(0,225,0)     


        self._pdf.text(x= 50, y = 150, txt = f"{A} took CS50")  



    def save(self, A) :

        self._pdf.output(A)







A = input("Name :")
# I have added my name Kanishk as my input in the function. 
pdf = PDF( A)

pdf.save("Shirtificate.pdf")























