#!/usr/bin/python3
# GNSS_TYPE      : ALL TYPE OF GNSS DATA
# Author         : Chang Chuntao
# Copyright(C)   : The GNSS Center, Wuhan University & Chinese Academy of Surveying and mapping
# Latest Version : 1.24
# Creation Date  : 2022.03.27 - Version 1.00
# Date           : 2022.10.10 - Version 1.24


"""
    2022-03-27 :    所有支持的数据类型 by Chang Chuntao -> Version : 1.00
    2022-04-12 :    新增P1C1、P1P2、P2C2、GRACE_SLR、BEIDOU_SLR、MGEX_WHU_OSB、GLO_IGL_sp3、GPS_IGS_clk_30s资源
                    by Chang Chuntao  -> Version : 1.10
    2022-04-22 :    新增TRO内资源IGS_zpd、COD_tro、 JPL_tro、 GRID_1x1_VMF3、 GRID_2.5x2_VMF3、 GRID_5x5_VMF3
                    by Chang Chuntao  -> Version : 1.11
    2022-05-24 :    + 新增ION内资源WURG_ion、CODG_ion、CORG_ion、UQRG_ion、UPRG_ion、JPLG_ion、JPRG_ion、CASG_ion、
                    CARG_ion、ESAG_ion、ESRG_ion
                    by Chang Chuntao  -> Version : 1.13
    2022-05-31 :    + 新增BIA内资源MGEX_WHU_OSB_bia
                    > 修正BIA内资源MGEX_WHU_bia -> MGEX_WHU_ABS_bia
                    by Chang Chuntao  -> Version : 1.14
    2022-07-03 :    + 新增CLK内资源MGEX_WUHU_clk
                    + 新增ERP内资源WUHU_erp
                    + 新增OBX内资源MGEX_WUHU_obx
                    by Chang Chuntao  -> Version : 1.15
    2022-07-13 :    + 新增SpaceData一级类
                    + 新增SpaceData内资源SW_EOP
                    by Chang Chuntao  -> Version : 1.16
    2022-07-22 :    + 新增SP3内资源MGEX_WUH_Hour_sp3
                    + 新增CLK内资源MGEX_WUH_Hour_clk
                    + 新增ERP内资源WUH_Hour_erp
                    by Chang Chuntao  -> Version : 1.17
    2022-07-27 :    > 修正MGEX_GFZ_sp3 -> MGEX_GFZR_sp3
                    > 修正MGEX_GFZ_clk -> MGEX_GFZR_clk
                    > 修正MGEX_COD_clk资源
                    by Chang Chuntao  -> Version : 1.18
    2022-08-04 :    > 修正时序文件下载需求
                    by Chang Chuntao  -> Version : 1.19
    2022-09-16 :    + 新增RINEX内MGEX_HK_cors资源
                    by Chang Chuntao  -> Version : 1.21
    2022-09-20 :    > 修正TRO -> TROP
                    + 新增TROP内资源Meteorological
                    by Chang Chuntao  -> Version : 1.22
    2022-09-28 :    + 新增COSMIC一级类
                    + 新增COSMIC内资源'C1_L1a_leoAtt', 'C1_L1a_opnGps', 'C1_L1a_podCrx','C1_L1b_atmPhs', 'C1_L1b_gpsBit',
                    'C1_L1b_ionPhs', 'C1_L1b_leoClk', 'C1_L1b_leoOrb', 'C1_L1b_podTec', 'C1_L1b_scnLv1', 'C2_L1a_leoAtt',
                    'C2_L1a_opnGps', 'C2_L1a_podCrx', 'C2_L1b_conPhs', 'C2_L1b_leoOrb', 'C2_L1b_podTc2'
                    by Chang Chuntao  -> Version : 1.23
    2022-10-10 :    + 新增Tables一级类
                    + 新增Tables内资源'Panda_jpleph_de405', 'Panda_poleut1', 'Panda_EGM','Panda_oceanload',
                    'Panda_oceantide', 'Panda_utcdif','Panda_antnam', 'Panda_svnav', 'Panda_nutabl',
                    'Panda_ut1tid', 'Panda_leap_sec',
                    'Gamit_pmu_bull', 'Gamit_ut1usno', 'Gamit_poleusno','Gamit_dcb_dat', 'Gamit_soltab', 'Gamit_luntab',
                    'Gamit_leap_sec', 'Gamit_nutabl', 'Gamit_antmod','Gamit_svnav', 'Gamit_rcvant'
                    by Chang Chuntao  -> Version : 1.24
"""

gnss_type = [["BRDC", ["GPS_brdc", "MGEX_brdm"]],

             ["SP3", ["GPS_IGS_sp3", "GPS_IGR_sp3", "GPS_IGU_sp3", "GPS_GFZ_sp3", "GPS_GRG_sp3",
                      "MGEX_WUH_sp3", "MGEX_WUHU_sp3", "MGEX_GFZR_sp3", "MGEX_COD_sp3", "MGEX_SHA_sp3", "MGEX_GRG_sp3",
                      "GLO_IGL_sp3", "MGEX_WUH_Hour_sp3"]],

             ["RINEX", ["GPS_IGS_rnx", "MGEX_IGS_rnx", "GPS_USA_cors", "GPS_HK_cors", "GPS_EU_cors", "GPS_AU_cors",
                        "MGEX_HK_cors", "MGEX_IGS_rnx_hr"]],

             ["CLK", ["GPS_IGS_clk", "GPS_IGR_clk", "GPS_GFZ_clk", "GPS_GRG_clk", "GPS_IGS_clk_30s",
                      "MGEX_WUH_clk", "MGEX_COD_clk", "MGEX_GFZR_clk", "MGEX_GRG_clk", "WUH_PRIDE_clk", 'MGEX_WUHU_clk',
                      "MGEX_WUH_Hour_clk"]],

             ["ERP", ["IGS_erp", "WUH_erp", "COD_erp", "GFZ_erp", "IGR_erp", 'WUHU_erp', "WUH_Hour_erp"]],

             ["BIA", ["MGEX_WHU_ABS_bia", "MGEX_WHU_OSB_bia", "GPS_COD_bia", "MGEX_COD_bia", "MGEX_GFZ_bia"]],

             ["ION", ["IGSG_ion", "IGRG_ion", "WUHG_ion", "WURG_ion", "CODG_ion", "CORG_ion", "UQRG_ion", "UPRG_ion",
                      "JPLG_ion", "JPRG_ion", "CASG_ion", "CARG_ion", "ESAG_ion", "ESRG_ion"]],

             ["SINEX", ["IGS_day_snx", "IGS_week_snx", "IVS_week_snx", "ILS_week_snx", "IDS_week_snx"]],

             ["CNES_AR", ["CNES_post", "CNES_realtime"]],

             ["ATX", ["MGEX_IGS_atx"]],

             ["DCB", ["GPS_COD_dcb", "MGEX_CAS_dcb", "MGEX_WHU_OSB", "P1C1", "P1P2", "P2C2"]],

             ["Time_Series", ["IGS14_TS_ENU", "IGS14_TS_XYZ", "Series_TS_Plot"]],

             ["Velocity_Fields", ["IGS14_Venu", "IGS08_Venu", "PLATE_Venu"]],

             ["SLR", ["HY_SLR", "GRACE_SLR", "BEIDOU_SLR"]],

             ["OBX", ["GPS_COD_obx", "GPS_GRG_obx", "MGEX_WUH_obx", "MGEX_COD_obx", "MGEX_GFZ_obx", 'MGEX_WUHU_obx']],

             ["TROP", ["IGS_zpd", "COD_tro", "JPL_tro", "GRID_1x1_VMF3", "GRID_2.5x2_VMF1", "GRID_5x5_VMF3",
                       "Meteorological"]],

             ["SpaceData", ["SW_EOP"]],

             ["COSMIC", ['C1_L1a_leoAtt', 'C1_L1a_opnGps', 'C1_L1a_podCrx',
                         'C1_L1b_atmPhs', 'C1_L1b_gpsBit', 'C1_L1b_ionPhs',
                         'C1_L1b_leoClk', 'C1_L1b_leoOrb', 'C1_L1b_podTec',
                         'C1_L1b_scnLv1',
                         'C2_L1a_leoAtt', 'C2_L1a_opnGps', 'C2_L1a_podCrx',
                         'C2_L1b_conPhs', 'C2_L1b_leoOrb', 'C2_L1b_podTc2']],

             ['Tables', ['Panda_jpleph_de405', 'Panda_poleut1', 'Panda_EGM',
                         'Panda_oceanload', 'Panda_oceantide', 'Panda_utcdif',
                         'Panda_antnam', 'Panda_svnav', 'Panda_nutabl',
                         'Panda_ut1tid', 'Panda_leap_sec',
                         'Gamit_pmu_bull', 'Gamit_ut1usno', 'Gamit_poleusno',
                         'Gamit_dcb_dat', 'Gamit_soltab', 'Gamit_luntab',
                         'Gamit_leap_sec', 'Gamit_nutabl', 'Gamit_antmod',
                         'Gamit_svnav', 'Gamit_rcvant']]
             ]

# 2022-03-27 : 每个二级目录的个数 by Chang Chuntao -> Version : 1.00
objnum = []
for sub_type in gnss_type:
    objnum.append(len(sub_type[1]))

# 2022-03-27 : 输入为年， 起始年积日， 终止年积日 的数据类型 by Chang Chuntao -> Version : 1.23
objneedydqd2 = [1, 2, 4, 5, 6, 7, 8, 9, 11, 14, 15, 16, 18]

# 2022-03-27 : 输入为年， 起始年积日， 终止年积日, 站点文件 的数据类型 by Chang Chuntao -> Version : 1.00
objneedyd1d2loc = [3]

# 2022-8-04 : 输入为站点文件的数据类型 by Chang Chuntao -> Version : 1.19
objneedloc = [12]

# 2022-07-13 : 无需输入 的数据类型 by Chang Chuntao -> Version : 1.16
objneedn = [10, 13, 17, 19]


def isinGNSStype(datatype):
    """
    2022-03-27 : 判断数据类型是否支持 by Chang Chuntao -> Version : 1.00
    """
    for gt in gnss_type:
        if datatype in gt[1]:
            return True
        else:
            continue
    return False


#
def getobj(datatype):
    """
    2022-03-27 : 获取数据类型在gnss_type中的索引位置 by Chang Chuntao -> Version : 1.00
    """
    d1 = 0
    for gt in gnss_type:
        d2 = 0
        for dt in gt[1]:
            d2 += 0
            if datatype == dt:
                return d1, d2
        d1 += 1
