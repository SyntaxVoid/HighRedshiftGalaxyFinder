;Used to Align the gs_f435w map to fit the the rest of Ketron's maps


print, 'Aligning f435w'
f125w = mrdfits('~/KetronsMaps/gs_f125w_cropcal.fits',0,f125whead)
f435w = mrdfits('~/KetronsMaps/gs_f435w_cropcal.fits',0,f435whead)

hastrom, f435w, f435whead, f435wALIGNED, f435wheadALIGNED, f125whead


mwrfiits, f435wALIGNED, 'gs_f435w_aligned.fits', f435wheadALIGNED, /create