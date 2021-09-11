# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 09:57:02 2021

@author: Acer
"""
# version 2, interpret a division operation a/b as integer division if bothoperands a and b are integers.

C = 21; F = 9/5*C + 32; print (F) # if 9/5 will become 1,result is 53


C = 21.0; F = (9/5)*C + 32; print (F) # if 9/5 will become 1,result is 53.0

C = 21.0; F = 9*C/5 + 32; print (F)
C = 21.0; F = 9.*(C/5.0) + 32; print (F)
C = 21.0; F = 9.0*C/5.0 + 32; print (F)

C = 21; F = 9*C/5 + 32; print (F)
# if 9*21/5 will  become 37,result is 69

C = 21.0; F = (1/5)*9*C + 32; print (F)
# if 1/5 will  become 0,result is 32

C = 21; F = (1./5)*9*C + 32; print (F)
