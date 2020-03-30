from setuptools import setup, find_packages
import versioneer

# read the contents of your README file
with open('README.md') as f:
    long_description = f.read()
    
setup(
    name='rna_tools',
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    url='https://github.com/mmagnus/rna-tools',
    scripts=['rna_tools/rna_pdb_toolsx.py',
             'rna_tools/rna_calc_fenergy.py',
             
             'rna_tools/tools/misc/rna_tools_which.py',
             'rna_tools/tools/rna_calc_rmsd/rna_calc_rmsd.py',
             'rna_tools/tools/rna_calc_rmsd/rna_calc_rmsd_all_vs_all.py',
             'rna_tools/tools/diffpdb/diffpdb.py',
             'rna_tools/tools/clanstix/rna_clanstix.py',
             'rna_tools/rna_dot2ct.py',
             'rna_tools/rna_secondary_structure_prediction.py',
             'rna_tools/tools/rna_prediction_significance/rna_prediction_significance.py',
             'rna_tools/tools/rna_multimodels/rna_pdb_merge_into_one.py',
             'rna_tools/tools/rna_calc_inf/rna_calc_inf.py',
             'rna_tools/tools/rna_convert_pseudoknot_formats/rna_pk_simrna_to_one_line.py',
             'rna_tools/tools/clarna_app/clarna_app.py',
             'rna_tools/tools/rna_helix_vis/rna_helix_vis.py',
             'rna_tools/tools/misc/rna_add_chain.py',
             'rna_tools/tools/rna_sali2dotbracket/rna_sali2dotbracket.py',



             'rna_tools/tools/rna_rosetta/rna_rosetta_run.py',
             'rna_tools/tools/rna_rosetta/rna_rosetta_cluster.py',
             'rna_tools/tools/rna_rosetta/rna_rosetta_min.py',
             'rna_tools/tools/rna_rosetta/rna_rosetta_n.py',
             'rna_tools/tools/rna_rosetta/rna_rosetta_extract_lowscore_decoys.py',
             'rna_tools/tools/rna_rosetta/rna_rosetta_check_progress.py',
             'rna_tools/tools/rna_rosetta/rna_rosetta_head.py',

             'rna_tools/tools/simrna_trajectory/rna_simrna_lowest.py',
             'rna_tools/tools/simrna_trajectory/rna_simrna_extract.py',
             'rna_tools/tools/simrna_trajectory/rna_simrna_cluster.py', 

             'rna_tools/tools/plotting/rna_plot_hist.py',
             'rna_tools/tools/plotting/rna_plot_density.py',

             'rna_tools/tools/simrna_trajectory/rna_simrna_lowest.py',
             'rna_tools/tools/simrna_trajectory/rna_simrna_extract.py',
             'rna_tools/tools/simrna_trajectory/rna_simrna_cluster.py',

             'rna_tools/tools/rna_filter/rna_filter.py',
             'rna_tools/tools/rna_filter/rna_ec2x.py',
             'rna_tools/tools/rna_filter/rna_pairs2SimRNArestrs.py',
             'rna_tools/tools/rna_filter/rna_ss_get_bps.py',
             'rna_tools/tools/rna_filter/rna_pairs_diff.py',

             'rna_tools/tools/rna_alignment/rna_align_seq_to_alignment.py',
             'rna_tools/tools/rna_alignment/rna_align_find_core.py',
             'rna_tools/tools/rna_alignment/rna_align_get_ss_from_stk.py',
             'rna_tools/tools/rna_alignment/rna_align_seq_to_alignment.py',
             'rna_tools/tools/rna_alignment/utils/rna_alignment_get_species.py',
             'rna_tools/tools/rna_alignment/utils/rna_alignment_process_id.py',
             'rna_tools/tools/rna_alignment/utils/rna_alignment_r2r.py',
             'rna_tools/tools/rna_alignment/rna_align_find_seq_in_alignment.py',
             'rna_tools/tools/rna_alignment/rna_align_foldability.py',
             'rna_tools/tools/rna_pdb_edit_occupancy_bfactor/rna_pdb_edit_occupancy_bfactor.py',
             'rna_tools/tools/rna_refinement/rna_refinement.py',
             'rna_tools/rna_simrnaweb_download_job.py',
             'rna_tools/tools/rna_calc_evo_rmsd/rna_calc_evo_rmsd.py',
             'rna_tools/tools/rna_calc_rmsd/rna_calc_rmsd_multi_targets.py',
             'rna_tools/tools/rna_calc_rmsd_trafl/rna_calc_rmsd_trafl.py',
             'rna_tools/tools/rna_calc_rmsd_trafl/rna_cal_rmsd_trafl_plot.py',
             'rna_tools/tools/rna_x3dna/rna_x3dna.py',
             'rna_tools/tools/renum_pdb_to_aln/renum_pdb_to_aln.py',
             'rna_tools/tools/pdbs_measure_atom_dists/pdbs_measure_atom_dists.py',
             'rna_tools/tools/rna_alignment/random_assignment_of_nucleotides.py',
             'rna_tools/tools/rna_seq_search_BLASTn_outfmt-6/select_seq_fromBLAStn_6outfm.py',
             'rna_tools/tools/pefx/pefx.py',
             'rna_tools/tools/misc/translate.py',
             'rna_tools/tools/misc/reverse.py',
             'rna_tools/tools/misc/reverse.py',
             'rna_tools/tools/rna_alignment/utils/rna_align_strip_stk.py',
             'rna_tools/tools/pymol_color_by_conserv/pymol_color_by_conserv.py',
             'rna_tools/tools/pymol_preview_generator/pymol_preview_generator.py',
             'rna_tools/tools/pymol_preview_generator/pymol_preview_install.py'

             'rna_tools/tools/rna_binding_affinity/rna_dG2kd.py',
             'rna_tools/tools/rna_binding_affinity/rna_dG2kd.py',
             'rna_tools/tools/rna_binding_affinity/rna_kd2dG.py'
             'rna_tools/tools/rna_binding_affinity/rna_kd2pkd.py',
             'rna_tools/tools/rna_binding_affinity/rna_pkd2dG.py',
             'rna_tools/tools/rna_binding_affinity/rna_pkd2kd.py',
             ],
    license='GPLv3',
    author='Marcin Magnus',
    author_email='mag_dex@o2.pl',
    description='a toolbox to analyze structures and simulations of RNA',
    long_description=long_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    install_requires=[
        'numpy',
        'biopython',
        #'forgi',
        'progressbar2',
        'sphinx==1.6.7',
        'sphinx-argparse==0.1.15',
        'sphinx-rtd-theme',
        'sphinxcontrib-napoleon',
        'urllib3',
        #'pandas',
        #'matplotlib',
        #'scipy',
        #'python-Levenshtein',
        'versioneer',
      ],
)

