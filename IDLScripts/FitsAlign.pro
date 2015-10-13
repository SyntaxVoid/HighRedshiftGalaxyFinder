

;-----f125w------
print, 'Aligning and adding f125w maps'
f125w_im1 = mrdfits('~/HalfMaps_ORIGINAL/gs_f125w_half1.skymap.fits',0,f125w_head1)
f125w_im2 = mrdfits('~/HalfMaps_ORIGINAL/gs_f125w_half2.skymap.fits',0,f125w_head2)
hastrom, f125w_im1, f125w_head1, new_f125w, new_f125w_head, f125w_head2
f125w_full = (f125w_im2 + new_f125w) / 2.
hextract, f125w_full, f125w_head2, f125w_crop, f125w_crop_head, 754, 4353, 770, 6844
mwrfits, f125w_crop, 'FullMaps/gs_f125w_cropped.fits', f125w_crop_head, /create

;-----f160w------
print, 'Aligning and adding f160w maps'
f160w_im1 = mrdfits('~/HalfMaps_ORIGINAL/gs_f160w_half1.skymap.fits',0,f160w_head1)
f160w_im2 = mrdfits('~/HalfMaps_ORIGINAL/gs_f160w_half2.skymap.fits',0,f160w_head2)
hastrom, f160w_im1, f160w_head1, new_f160w, new_f160w_head, f160w_head2
f160w_full = (f160w_im2 + new_f160w) / 2.
hextract, f160w_full, f160w_head2, f160w_crop, f160w_crop_head, 754, 4353, 770, 6844
mwrfits, f160w_crop, 'FullMaps/gs_f160w_cropped.fits', f160w_crop_head, /create

;-----f606w------
print, 'Aligning and adding f606w maps'
f606w_im1 = mrdfits('~/HalfMaps_ORIGINAL/gs_f606w_half1.skymap.fits',0,f606w_head1)
f606w_im2 = mrdfits('~/HalfMaps_ORIGINAL/gs_f606w_half2.skymap.fits',0,f606w_head2)
hastrom, f606w_im1, f606w_head1, new_f606w, new_f606w_head, f606w_head2
f606w_full = (f606w_im2 + new_f606w) / 2.
hextract, f606w_full, f606w_head2, f606w_crop, f606w_crop_head, 754, 4353, 770, 6844
mwrfits, f606w_crop, 'FullMaps/gs_f606w_cropped.fits', f606w_crop_head, /create

;-----f775w------
print, 'Aligning and adding f775w maps'
f775w_im1 = mrdfits('~/HalfMaps_ORIGINAL/gs_f775w_half1.skymap.fits',0,f775w_head1)
f775w_im2 = mrdfits('~/HalfMaps_ORIGINAL/gs_f775w_half2.skymap.fits',0,f775w_head2)
hastrom, f775w_im1, f775w_head1, new_f775w, new_f775w_head, f775w_head2
f775w_full = (f775w_im2 + new_f775w) / 2.
hextract, f775w_full, f775w_head2, f775w_crop, f775w_crop_head, 754, 4353, 770, 6844
mwrfits, f775w_crop, 'FullMaps/gs_f775w_cropped.fits', f775w_crop_head, /create

;-----f850l------
print, 'Aligning and adding f850l maps'
f850l_im1 = mrdfits('~/HalfMaps_ORIGINAL/gs_f850l_half1.skymap.fits',0,f850l_head1)
f850l_im2 = mrdfits('~/HalfMaps_ORIGINAL/gs_f850l_half2.skymap.fits',0,f850l_head2)
hastrom, f850l_im1, f850l_head1, new_f850l, new_f850l_head, f850l_head2
f850l_full = (f850l_im2 + new_f850l) / 2.
hextract, f850l_full, f850l_head2, f850l_crop, f850l_crop_head, 754, 4353, 770, 6844
mwrfits, f850l_crop, 'FullMaps/gs_f850l_cropped.fits', f850l_crop_head, /create




