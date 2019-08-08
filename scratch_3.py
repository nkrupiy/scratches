#from: C:\My\repo\sb_grc_utils\friday_breakthrouhg\lab_dm_toolkit1.py

# ^ if not ' ' in flags_table_or_query:
#     v_flg_tbl = flags_table_or_query
#     # подзапрос к таблице флагов (с инициализированным диапазоном дат)
#     v_flg_tbl_subq = """
#     (
#     SELECT *
#       FROM $flags_tbl_2pn$
#      WHERE part_trn_date BETWEEN '2017-01-01' AND '2019-01-09'
#     )"""
# else:
#     v_flg_tbl_subq = flags_table_or_query
#     if not v_flg_tbl_subq.strip().startswith('('):
#         v_flg_tbl_subq = '(' + v_flg_tbl_subq + ')'

# v_clt_tbl="$clients$", v_flg_tbl="$flags$",


#_________________________________________________________________________________________
#_________________________________________________________________________________________
#use global v_windows_list
#~ if v_windows_list and preres_db and tbl2pn_pref:
#_________________________________________________________________________________________


# ----------------------------------------------------------------------------
# from_step, to_step = 1, 3
# def step_demo():
#     # ---------------------------------------------
#     from_step, to_step = 1, 333
#     # res =
#     if not step(3, 'Сбор витрин в одну'): return 0
#     else:  # ... код шага
#         # prt(res)
#         prt('.. running step code:..')
#         # prn('step is out of defined from_step..to_step scope - goto finish..')
#
#     # ---------------------------------------------
#     from_step, to_step = 1, 2
#     if not step(3, 'Сбор витрин в одну'): return 0
#     else: prt('.. running step code:..')
