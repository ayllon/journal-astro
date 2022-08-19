import os.path
import warnings
import numpy as np
from glob import glob
from astropy.coordinates import SkyCoord, match_coordinates_sky
from astropy.table import Table, hstack
from astropy import units as u


def load_catalogs(base_dir: str, tile_id: int):
    with warnings.catch_warnings():
        warnings.simplefilter("ignore")
        mer_cat = Table.read(glob(os.path.join(base_dir, f'EUC_MER_FINAL-CAT_TILE{tile_id}-*.fits'))[0])[['OBJECT_ID', 'RIGHT_ASCENSION', 'DECLINATION']]
        gal_tu = Table.read(glob(os.path.join(base_dir, f'EUC_MER_TU-GALAXY-CAT_TILE{tile_id}-*.fits'))[0])
        star_tu = Table.read(glob(os.path.join(base_dir, f'EUC_MER_TU-STAR-CAT_TILE{tile_id}-*.fits'))[0])
        phz_cat = Table.read(glob(os.path.join(base_dir, f'EUC_PHZ_PHZCAT__*.fits'))[0], hdu=1)
        gal_sed = Table.read(glob(os.path.join(base_dir, f'EUC_PHZ_GALAXYSED__*.fits'))[0])
        star_sed = Table.read(glob(os.path.join(base_dir, f'EUC_PHZ_STARSED__*.fits'))[0])
    
        mer_coord = SkyCoord(mer_cat['RIGHT_ASCENSION'], mer_cat['DECLINATION'])

        n_gal = len(gal_tu)
        tu_ra = np.concatenate([gal_tu['RA_MAG'], star_tu['RA']]) * gal_tu['RA_MAG'].unit
        tu_dec = np.concatenate([gal_tu['DEC_MAG'], star_tu['DEC']]) * gal_tu['DEC_MAG'].unit
        tu_coord = SkyCoord(tu_ra, tu_dec)

        tu_idxs, _, _ = match_coordinates_sky(mer_coord, tu_coord)
        gal_mask = tu_idxs < n_gal
        star_mask = tu_idxs >= n_gal

        mer_gal = hstack([mer_cat[gal_mask], gal_tu[tu_idxs[gal_mask]]])
        mer_star = hstack([mer_cat[star_mask], star_tu[tu_idxs[star_mask] - n_gal]])
        mer_cat['TRUE_CLASS'] = gal_mask * 2 + star_mask * 1
    
    return phz_cat, mer_cat, gal_sed, star_sed, mer_gal, mer_star
