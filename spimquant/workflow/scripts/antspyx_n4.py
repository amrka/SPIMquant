import ants
from zarrnii import ZarrNii


level=int(snakemake.wildcards.level)


znimg = ZarrNii.from_ome_zarr(snakemake.params.spim_uri,level=level)
print(znimg.darr)
znimg.to_nifti(snakemake.output.spim_ds)

#now perform ants
antsimg = ants.image_read(snakemake.output.spim_ds)

antsimg_bias = ants.n4_bias_field_correction(antsimg,spline_param=(16,16,16),shrink_factor=8,return_bias_field=True)

#write out nifti
ants.image_write(antsimg_bias,snakemake.output.n4_bf_ds)


