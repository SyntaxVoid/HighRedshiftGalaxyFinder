###                         ###
# Authored by John Gresl 2015 #
###                         ###
import os

print("If you get a \"sextractor not found\" error, then the program will automatically try using the \"sex\" command instead.")

    #f125w
print('---f125w---')
os.system("sextractor -c SExtractorConfig/f125w.sex FullMaps/gs_f125w_cropcal.fits"+ \
          "|| sex -c SExtractorConfig/f125w.sex FullMaps/gs_f125w_cropcal.fits")
    #Smooth parameters -> Gaussian 6 (in Saods9)

    #f160w
print('---f160w---')
os.system("sextractor -c SExtractorConfig/f160w.sex FullMaps/gs_f160w_cropcal.fits"+ \
          "|| sex -c SExtractorConfig/f160w.sex FullMaps/gs_f160w_cropcal.fits")
    #Smooth parameters -> Gaussian 6 (in Saods9)

    #f606w
print('---f606w---')
os.system("sextractor -c SExtractorConfig/f606w.sex FullMaps/gs_f606w_cropcal.fits"+ \
          "|| sex -c SExtractorConfig/f606w.sex FullMaps/gs_f606w_cropcal.fits")
    #Smooth parameters -> Gaussian 6 (in Saods9)

    #f775w
print('---f775w---')
os.system("sextractor -c SExtractorConfig/f775w.sex FullMaps/gs_f775w_cropcal.fits"+ \
          "|| sex -c SExtractorConfig/f775w.sex FullMaps/gs_f775w_cropcal.fits")
    #Smooth parameters -> Gaussian 6 (in Saods9)

    #f850l
print('---f850l---')
os.system("sextractor -c SExtractorConfig/f850l.sex FullMaps/gs_f850l_cropcal.fits"+ \
          "|| sex -c SExtractorConfig/f850l.sex FullMaps/gs_f850l_cropcal.fits")
    #Smooth parameters -> Gaussian 6 (in Saods9)



