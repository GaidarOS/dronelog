# Complete list of parameters in an APM Pixhawk log file
# fieldnames = ("PARM_TimeUS", "PARM_Name", "PARM_Value", "GPS_TimeUS", "GPS_Status", "GPS_GMS", "GPS_GWk", "GPS_NSats", "GPS_HDop", "GPS_Lat", "GPS_Lng", "GPS_Alt", "GPS_Spd", "GPS_GCrs", "GPS_VZ", "GPS_U", "GPS2_TimeUS", "GPS2_Status", "GPS2_GMS", "GPS2_GWk", "GPS2_NSats", "GPS2_HDop", "GPS2_Lat", "GPS2_Lng", "GPS2_Alt", "GPS2_Spd", "GPS2_GCrs", "GPS2_VZ", "GPS2_U", "GPSB_TimeUS", "GPSB_Status", "GPSB_GMS", "GPSB_GWk", "GPSB_NSats", "GPSB_HDop", "GPSB_Lat", "GPSB_Lng", "GPSB_Alt", "GPSB_Spd", "GPSB_GCrs", "GPSB_VZ", "GPSB_U", "GPA_TimeUS", "GPA_VDop", "GPA_HAcc", "GPA_VAcc", "GPA_SAcc", "GPA_VV", "GPA_SMS", "GPA2_TimeUS", "GPA2_VDop", "GPA2_HAcc", "GPA2_VAcc", "GPA2_SAcc", "GPA2_VV", "GPA2_SMS", "GPAB_TimeUS", "GPAB_VDop", "GPAB_HAcc", "GPAB_VAcc", "GPAB_SAcc", "GPAB_VV", "GPAB_SMS", "IMU_TimeUS", "IMU_GyrX", "IMU_GyrY", "IMU_GyrZ", "IMU_AccX", "IMU_AccY", "IMU_AccZ", "IMU_EG", "IMU_EA", "IMU_T", "IMU_GH", "IMU_AH", "IMU_GHz", "IMU_AHz", "MSG_TimeUS", "MSG_Message", "RCIN_TimeUS", "RCIN_C1", "RCIN_C2", "RCIN_C3", "RCIN_C4", "RCIN_C5", "RCIN_C6", "RCIN_C7", "RCIN_C8", "RCIN_C9", "RCIN_C10", "RCIN_C11", "RCIN_C12", "RCIN_C13", "RCIN_C14", "RCOU_TimeUS", "RCOU_C1", "RCOU_C2", "RCOU_C3", "RCOU_C4", "RCOU_C5", "RCOU_C6", "RCOU_C7", "RCOU_C8", "RCOU_C9", "RCOU_C10", "RCOU_C11", "RCOU_C12", "RCOU_C13", "RCOU_C14", "RSSI_TimeUS", "RSSI_RXRSSI", "BARO_TimeUS", "BARO_Alt", "BARO_Press", "BARO_Temp", "BARO_CRt", "BARO_SMS", "BARO_Offset", "BARO_GndTemp", "POWR_TimeUS", "POWR_Vcc", "POWR_VServo", "POWR_Flags", "CMD_TimeUS", "CMD_CTot", "CMD_CNum", "CMD_CId", "CMD_Prm1", "CMD_Prm2", "CMD_Prm3", "CMD_Prm4", "CMD_Lat", "CMD_Lng", "CMD_Alt", "RAD_TimeUS", "RAD_RSSI", "RAD_RemRSSI", "RAD_TxBuf", "RAD_Noise", "RAD_RemNoise", "RAD_RxErrors", "RAD_Fixed", "CAM_TimeUS", "CAM_GPSTime", "CAM_GPSWeek", "CAM_Lat", "CAM_Lng", "CAM_Alt", "CAM_RelAlt", "CAM_GPSAlt", "CAM_Roll", "CAM_Pitch", "CAM_Yaw", "TRIG_TimeUS", "TRIG_GPSTime", "TRIG_GPSWeek", "TRIG_Lat", "TRIG_Lng", "TRIG_Alt", "TRIG_RelAlt", "TRIG_GPSAlt", "TRIG_Roll", "TRIG_Pitch", "TRIG_Yaw", "ARSP_TimeUS", "ARSP_Airspeed", "ARSP_DiffPress", "ARSP_Temp", "ARSP_RawPress", "ARSP_Offset", "ARSP_U", "CURR_TimeUS", "CURR_Volt", "CURR_Curr", "CURR_CurrTot", "CURR_Temp", "CURR_V1", "CURR_V2", "CURR_V3", "CURR_V4", "CURR_V5", "CURR_V6", "CURR_V7", "CURR_V8", "CURR_V9", "CURR_V10", "CUR2_TimeUS", "CUR2_Volt", "CUR2_Curr", "CUR2_CurrTot", "CUR2_Temp", "CUR2_V1", "CUR2_V2", "CUR2_V3", "CUR2_V4", "CUR2_V5", "CUR2_V6", "CUR2_V7", "CUR2_V8", "CUR2_V9", "CUR2_V10", "ATT_TimeUS", "ATT_DesRoll", "ATT_Roll", "ATT_DesPitch", "ATT_Pitch", "ATT_DesYaw", "ATT_Yaw", "ATT_ErrRP", "ATT_ErrYaw", "MAG_TimeUS", "MAG_MagX", "MAG_MagY", "MAG_MagZ", "MAG_OfsX", "MAG_OfsY", "MAG_OfsZ", "MAG_MOfsX", "MAG_MOfsY", "MAG_MOfsZ", "MAG_Health", "MAG_S", "MODE_TimeUS", "MODE_Mode", "MODE_ModeNum", "MODE_Rsn", "RFND_TimeUS", "RFND_Dist1", "RFND_Orient1", "RFND_Dist2", "RFND_Orient2", "DMS_TimeMS", "DMS_N", "DMS_Dp", "DMS_RT", "DMS_RS", "DMS_Er", "DMS_Fa", "DMS_Fmn", "DMS_Fmx", "DMS_Pa", "DMS_Pmn", "DMS_Pmx", "DMS_Sa", "DMS_Smn", "DMS_Smx", "BCN_TimeUS", "BCN_Health", "BCN_Cnt", "BCN_D0", "BCN_D1", "BCN_D2", "BCN_D3", "BCN_PosX", "BCN_PosY", "BCN_PosZ", "IMU2_TimeUS", "IMU2_GyrX", "IMU2_GyrY", "IMU2_GyrZ", "IMU2_AccX", "IMU2_AccY", "IMU2_AccZ", "IMU2_EG", "IMU2_EA", "IMU2_T", "IMU2_GH", "IMU2_AH", "IMU2_GHz", "IMU2_AHz", "IMU3_TimeUS", "IMU3_GyrX", "IMU3_GyrY", "IMU3_GyrZ", "IMU3_AccX", "IMU3_AccY", "IMU3_AccZ", "IMU3_EG", "IMU3_EA", "IMU3_T", "IMU3_GH", "IMU3_AH", "IMU3_GHz", "IMU3_AHz", "AHR2_TimeUS", "AHR2_Roll", "AHR2_Pitch", "AHR2_Yaw", "AHR2_Alt", "AHR2_Lat", "AHR2_Lng", "AHR2_Q1", "AHR2_Q2", "AHR2_Q3", "AHR2_Q4", "POS_TimeUS", "POS_Lat", "POS_Lng", "POS_Alt", "POS_RelHomeAlt", "POS_RelOriginAlt", "SIM_TimeUS", "SIM_Roll", "SIM_Pitch", "SIM_Yaw", "SIM_Alt", "SIM_Lat", "SIM_Lng", "SIM_Q1", "SIM_Q2", "SIM_Q3", "SIM_Q4", "NKF1_TimeUS", "NKF1_Roll", "NKF1_Pitch", "NKF1_Yaw", "NKF1_VN", "NKF1_VE", "NKF1_VD", "NKF1_dPD", "NKF1_PN", "NKF1_PE", "NKF1_PD", "NKF1_GX", "NKF1_GY", "NKF1_GZ", "NKF2_TimeUS", "NKF2_AZbias", "NKF2_GSX", "NKF2_GSY", "NKF2_GSZ", "NKF2_VWN", "NKF2_VWE", "NKF2_MN", "NKF2_ME", "NKF2_MD", "NKF2_MX", "NKF2_MY", "NKF2_MZ", "NKF2_MI", "NKF3_TimeUS", "NKF3_IVN", "NKF3_IVE", "NKF3_IVD", "NKF3_IPN", "NKF3_IPE", "NKF3_IPD", "NKF3_IMX", "NKF3_IMY", "NKF3_IMZ", "NKF3_IYAW", "NKF3_IVT", "NKF4_TimeUS", "NKF4_SV", "NKF4_SP", "NKF4_SH", "NKF4_SM", "NKF4_SVT", "NKF4_errRP", "NKF4_OFN", "NKF4_OFE", "NKF4_FS", "NKF4_TS", "NKF4_SS", "NKF4_GPS", "NKF4_PI", "NKF5_TimeUS", "NKF5_NI", "NKF5_FIX", "NKF5_FIY", "NKF5_AFI", "NKF5_HAGL", "NKF5_offset", "NKF5_RI", "NKF5_rng", "NKF5_Herr", "NKF5_eAng", "NKF5_eVel", "NKF5_ePos", "NKF6_TimeUS", "NKF6_Roll", "NKF6_Pitch", "NKF6_Yaw", "NKF6_VN", "NKF6_VE", "NKF6_VD", "NKF6_dPD", "NKF6_PN", "NKF6_PE", "NKF6_PD", "NKF6_GX", "NKF6_GY", "NKF6_GZ", "NKF7_TimeUS", "NKF7_AZbias", "NKF7_GSX", "NKF7_GSY", "NKF7_GSZ", "NKF7_VWN", "NKF7_VWE", "NKF7_MN", "NKF7_ME", "NKF7_MD", "NKF7_MX", "NKF7_MY", "NKF7_MZ", "NKF7_MI", "NKF8_TimeUS", "NKF8_IVN", "NKF8_IVE", "NKF8_IVD", "NKF8_IPN", "NKF8_IPE", "NKF8_IPD", "NKF8_IMX", "NKF8_IMY", "NKF8_IMZ", "NKF8_IYAW", "NKF8_IVT", "NKF9_TimeUS", "NKF9_SV", "NKF9_SP", "NKF9_SH", "NKF9_SM", "NKF9_SVT", "NKF9_errRP", "NKF9_OFN", "NKF9_OFE", "NKF9_FS", "NKF9_TS", "NKF9_SS", "NKF9_GPS", "NKF9_PI", "NKF0_TimeUS", "NKF0_ID", "NKF0_rng", "NKF0_innov", "NKF0_SIV", "NKF0_TR", "NKF0_BPN", "NKF0_BPE", "NKF0_BPD", "NKF0_OFH", "NKF0_OFL", "NKF0_OFN", "NKF0_OFE", "NKF0_OFD", "NKQ1_TimeUS", "NKQ1_Q1", "NKQ1_Q2", "NKQ1_Q3", "NKQ1_Q4", "NKQ2_TimeUS", "NKQ2_Q1", "NKQ2_Q2", "NKQ2_Q3", "NKQ2_Q4", "XKF1_TimeUS", "XKF1_Roll", "XKF1_Pitch", "XKF1_Yaw", "XKF1_VN", "XKF1_VE", "XKF1_VD", "XKF1_dPD", "XKF1_PN", "XKF1_PE", "XKF1_PD", "XKF1_GX", "XKF1_GY", "XKF1_GZ", "XKF2_TimeUS", "XKF2_AX", "XKF2_AY", "XKF2_AZ", "XKF2_VWN", "XKF2_VWE", "XKF2_MN", "XKF2_ME", "XKF2_MD", "XKF2_MX", "XKF2_MY", "XKF2_MZ", "XKF2_MI", "XKF3_TimeUS", "XKF3_IVN", "XKF3_IVE", "XKF3_IVD", "XKF3_IPN", "XKF3_IPE", "XKF3_IPD", "XKF3_IMX", "XKF3_IMY", "XKF3_IMZ", "XKF3_IYAW", "XKF3_IVT", "XKF4_TimeUS", "XKF4_SV", "XKF4_SP", "XKF4_SH", "XKF4_SM", "XKF4_SVT", "XKF4_errRP", "XKF4_OFN", "XKF4_OFE", "XKF4_FS", "XKF4_TS", "XKF4_SS", "XKF4_GPS", "XKF4_PI", "XKF5_TimeUS", "XKF5_NI", "XKF5_FIX", "XKF5_FIY", "XKF5_AFI", "XKF5_HAGL", "XKF5_offset", "XKF5_RI", "XKF5_rng", "XKF5_Herr", "XKF5_eAng", "XKF5_eVel", "XKF5_ePos", "XKF6_TimeUS", "XKF6_Roll", "XKF6_Pitch", "XKF6_Yaw", "XKF6_VN", "XKF6_VE", "XKF6_VD", "XKF6_dPD", "XKF6_PN", "XKF6_PE", "XKF6_PD", "XKF6_GX", "XKF6_GY", "XKF6_GZ", "XKF7_TimeUS", "XKF7_AX", "XKF7_AY", "XKF7_AZ", "XKF7_VWN", "XKF7_VWE", "XKF7_MN", "XKF7_ME", "XKF7_MD", "XKF7_MX", "XKF7_MY", "XKF7_MZ", "XKF7_MI", "XKF8_TimeUS", "XKF8_IVN", "XKF8_IVE", "XKF8_IVD", "XKF8_IPN", "XKF8_IPE", "XKF8_IPD", "XKF8_IMX", "XKF8_IMY", "XKF8_IMZ", "XKF8_IYAW", "XKF8_IVT", "XKF9_TimeUS", "XKF9_SV", "XKF9_SP", "XKF9_SH", "XKF9_SM", "XKF9_SVT", "XKF9_errRP", "XKF9_OFN", "XKF9_OFE", "XKF9_FS", "XKF9_TS", "XKF9_SS", "XKF9_GPS", "XKF9_PI", "XKF0_TimeUS", "XKF0_ID", "XKF0_rng", "XKF0_innov", "XKF0_SIV", "XKF0_TR", "XKF0_BPN", "XKF0_BPE", "XKF0_BPD", "XKF0_OFH", "XKF0_OFL", "XKF0_OFN", "XKF0_OFE", "XKF0_OFD", "XKQ1_TimeUS", "XKQ1_Q1", "XKQ1_Q2", "XKQ1_Q3", "XKQ1_Q4", "XKQ2_TimeUS", "XKQ2_Q1", "XKQ2_Q2", "XKQ2_Q3", "XKQ2_Q4", "XKFD_TimeUS", "XKFD_IX", "XKFD_IY", "XKFD_IZ", "XKFD_IVX", "XKFD_IVY", "XKFD_IVZ", "TERR_TimeUS", "TERR_Status", "TERR_Lat", "TERR_Lng", "TERR_Spacing", "TERR_TerrH", "TERR_CHeight", "TERR_Pending", "TERR_Loaded", "UBX1_TimeUS", "UBX1_Instance", "UBX1_noisePerMS", "UBX1_jamInd", "UBX1_aPower", "UBX1_agcCnt", "UBX2_TimeUS", "UBX2_Instance", "UBX2_ofsI", "UBX2_magI", "UBX2_ofsQ", "UBX2_magQ", "UBY1_TimeUS", "UBY1_Instance", "UBY1_noisePerMS", "UBY1_jamInd", "UBY1_aPower", "UBY1_agcCnt", "UBY2_TimeUS", "UBY2_Instance", "UBY2_ofsI", "UBY2_magI", "UBY2_ofsQ", "UBY2_magQ", "GRAW_TimeUS", "GRAW_WkMS", "GRAW_Week", "GRAW_numSV", "GRAW_sv", "GRAW_cpMes", "GRAW_prMes", "GRAW_doMes", "GRAW_mesQI", "GRAW_cno", "GRAW_lli", "GRXH_TimeUS", "GRXH_rcvTime", "GRXH_week", "GRXH_leapS", "GRXH_numMeas", "GRXH_recStat", "GRXS_TimeUS", "GRXS_prMes", "GRXS_cpMes", "GRXS_doMes", "GRXS_gnss", "GRXS_sv", "GRXS_freq", "GRXS_lock", "GRXS_cno", "GRXS_prD", "GRXS_cpD", "GRXS_doD", "GRXS_trk", "SBFE_TimeUS", "SBFE_TOW", "SBFE_WN", "SBFE_Mode", "SBFE_Err", "SBFE_Lat", "SBFE_Lng", "SBFE_Height", "SBFE_Undul", "SBFE_Vn", "SBFE_Ve", "SBFE_Vu", "SBFE_COG", "ESC1_TimeUS", "ESC1_RPM", "ESC1_Volt", "ESC1_Curr", "ESC1_Temp", "ESC2_TimeUS", "ESC2_RPM", "ESC2_Volt", "ESC2_Curr", "ESC2_Temp", "ESC3_TimeUS", "ESC3_RPM", "ESC3_Volt", "ESC3_Curr", "ESC3_Temp", "ESC4_TimeUS", "ESC4_RPM", "ESC4_Volt", "ESC4_Curr", "ESC4_Temp", "ESC5_TimeUS", "ESC5_RPM", "ESC5_Volt", "ESC5_Curr", "ESC5_Temp", "ESC6_TimeUS", "ESC6_RPM", "ESC6_Volt", "ESC6_Curr", "ESC6_Temp", "ESC7_TimeUS", "ESC7_RPM", "ESC7_Volt", "ESC7_Curr", "ESC7_Temp", "ESC8_TimeUS", "ESC8_RPM", "ESC8_Volt", "ESC8_Curr", "ESC8_Temp", "MAG2_TimeUS", "MAG2_MagX", "MAG2_MagY", "MAG2_MagZ", "MAG2_OfsX", "MAG2_OfsY", "MAG2_OfsZ", "MAG2_MOfsX", "MAG2_MOfsY", "MAG2_MOfsZ", "MAG2_Health", "MAG2_S", "MAG3_TimeUS", "MAG3_MagX", "MAG3_MagY", "MAG3_MagZ", "MAG3_OfsX", "MAG3_OfsY", "MAG3_OfsZ", "MAG3_MOfsX", "MAG3_MOfsY", "MAG3_MOfsZ", "MAG3_Health", "MAG3_S", "ACC1_TimeUS", "ACC1_SampleUS", "ACC1_AccX", "ACC1_AccY", "ACC1_AccZ", "ACC2_TimeUS", "ACC2_SampleUS", "ACC2_AccX", "ACC2_AccY", "ACC2_AccZ", "ACC3_TimeUS", "ACC3_SampleUS", "ACC3_AccX", "ACC3_AccY", "ACC3_AccZ", "GYR1_TimeUS", "GYR1_SampleUS", "GYR1_GyrX", "GYR1_GyrY", "GYR1_GyrZ", "GYR2_TimeUS", "GYR2_SampleUS", "GYR2_GyrX", "GYR2_GyrY", "GYR2_GyrZ", "GYR3_TimeUS", "GYR3_SampleUS", "GYR3_GyrX", "GYR3_GyrY", "GYR3_GyrZ", "PIDR_TimeUS", "PIDR_Des", "PIDR_P", "PIDR_I", "PIDR_D", "PIDR_FF", "PIDR_AFF", "PIDP_TimeUS", "PIDP_Des", "PIDP_P", "PIDP_I", "PIDP_D", "PIDP_FF", "PIDP_AFF", "PIDY_TimeUS", "PIDY_Des", "PIDY_P", "PIDY_I", "PIDY_D", "PIDY_FF", "PIDY_AFF", "PIDA_TimeUS", "PIDA_Des", "PIDA_P", "PIDA_I", "PIDA_D", "PIDA_FF", "PIDA_AFF", "PIDS_TimeUS", "PIDS_Des", "PIDS_P", "PIDS_I", "PIDS_D", "PIDS_FF", "PIDS_AFF", "PIDL_TimeUS", "PIDL_Des", "PIDL_P", "PIDL_I", "PIDL_D", "PIDL_FF", "PIDL_AFF", "BAR2_TimeUS", "BAR2_Alt", "BAR2_Press", "BAR2_Temp", "BAR2_CRt", "BAR2_SMS", "BAR2_Offset", "BAR2_GndTemp", "BAR3_TimeUS", "BAR3_Alt", "BAR3_Press", "BAR3_Temp", "BAR3_CRt", "BAR3_SMS", "BAR3_Offset", "BAR3_GndTemp", "VIBE_TimeUS", "VIBE_VibeX", "VIBE_VibeY", "VIBE_VibeZ", "VIBE_Clip0", "VIBE_Clip1", "VIBE_Clip2", "IMT_TimeUS", "IMT_DelT", "IMT_DelvT", "IMT_DelaT", "IMT_DelAX", "IMT_DelAY", "IMT_DelAZ", "IMT_DelVX", "IMT_DelVY", "IMT_DelVZ", "IMT2_TimeUS", "IMT2_DelT", "IMT2_DelvT", "IMT2_DelaT", "IMT2_DelAX", "IMT2_DelAY", "IMT2_DelAZ", "IMT2_DelVX", "IMT2_DelVY", "IMT2_DelVZ", "IMT3_TimeUS", "IMT3_DelT", "IMT3_DelvT", "IMT3_DelaT", "IMT3_DelAX", "IMT3_DelAY", "IMT3_DelAZ", "IMT3_DelVX", "IMT3_DelVY", "IMT3_DelVZ", "ORGN_TimeUS", "ORGN_Type", "ORGN_Lat", "ORGN_Lng", "ORGN_Alt", "RPM_TimeUS", "RPM_rpm1", "RPM_rpm2", "GMB1_TimeMS", "GMB1_dt", "GMB1_dax", "GMB1_day", "GMB1_daz", "GMB1_dvx", "GMB1_dvy", "GMB1_dvz", "GMB1_jx", "GMB1_jy", "GMB1_jz", "GMB2_TimeMS", "GMB2_es", "GMB2_ex", "GMB2_ey", "GMB2_ez", "GMB2_rx", "GMB2_ry", "GMB2_rz", "GMB2_tx", "GMB2_ty", "GMB2_tz", "GMB3_TimeMS", "GMB3_rl_torque_cmd", "GMB3_el_torque_cmd", "GMB3_az_torque_cmd", "RATE_TimeUS", "RATE_RDes", "RATE_R", "RATE_ROut", "RATE_PDes", "RATE_P", "RATE_POut", "RATE_YDes", "RATE_Y", "RATE_YOut", "RATE_ADes", "RATE_A", "RATE_AOut", "RALY_TimeUS", "RALY_Tot", "RALY_Seq", "RALY_Lat", "RALY_Lng", "RALY_Alt", "VISO_TimeUS", "VISO_dt", "VISO_AngDX", "VISO_AngDY", "VISO_AngDZ", "VISO_PosDX", "VISO_PosDY", "VISO_PosDZ", "VISO_conf", "SBPH_TimeUS", "SBPH_CrcError", "SBPH_LastInject", "SBPH_IARhyp", "SBR1_TimeUS", "SBR1_msg_type", "SBR1_sender_id", "SBR1_msg_len", "SBR1_d1", "SBR2_TimeUS", "SBR2_msg_type", "SBR2_d2", "SBR2_d3", "SBR2_d4", "ATUN_TimeUS", "ATUN_Axis", "ATUN_TuneStep", "ATUN_Targ", "ATUN_Min", "ATUN_Max", "ATUN_RP", "ATUN_RD", "ATUN_SP", "ATUN_ddt", "ATDE_TimeUS", "ATDE_Angle", "ATDE_Rate", "PTUN_TimeUS", "PTUN_Param", "PTUN_TunVal", "PTUN_CtrlIn", "PTUN_TunLo", "PTUN_TunHi", "OF_TimeUS", "OF_Qual", "OF_flowX", "OF_flowY", "OF_bodyX", "OF_bodyY", "NTUN_TimeUS", "NTUN_DPosX", "NTUN_DPosY", "NTUN_PosX", "NTUN_PosY", "NTUN_DVelX", "NTUN_DVelY", "NTUN_VelX", "NTUN_VelY", "NTUN_DAccX", "NTUN_DAccY", "CTUN_TimeUS", "CTUN_ThI", "CTUN_ABst", "CTUN_ThO", "CTUN_ThH", "CTUN_DAlt", "CTUN_Alt", "CTUN_BAlt", "CTUN_DSAlt", "CTUN_SAlt", "CTUN_TAlt", "CTUN_DCRt", "CTUN_CRt", "PM_TimeUS", "PM_NLon", "PM_NLoop", "PM_MaxT", "PM_PMT", "PM_I2CErr", "PM_INSErr", "PM_LogDrop", "PM_Mem", "MOTB_TimeUS", "MOTB_LiftMax", "MOTB_BatVolt", "MOTB_BatRes", "MOTB_ThLimit", "EV_TimeUS", "EV_Id", "D16_TimeUS", "D16_Id", "D16_Value", "DU16_TimeUS", "DU16_Id", "DU16_Value", "D32_TimeUS", "D32_Id", "D32_Value", "DU32_TimeUS", "DU32_Id", "DU32_Value", "DFLT_TimeUS", "DFLT_Id", "DFLT_Value", "ERR_TimeUS", "ERR_Subsys", "ERR_ECode", "HELI_TimeUS", "HELI_DRRPM", "HELI_ERRPM", "PL_TimeUS", "PL_Heal", "PL_TAcq", "PL_pX", "PL_pY", "PL_vX", "PL_vY", "GUID_TimeUS", "GUID_Type", "GUID_pX", "GUID_pY", "GUID_pZ", "GUID_vX", "GUID_vY", "GUID_vZ", "THRO_TimeUS", "THRO_Stage", "THRO_Vel", "THRO_VelZ", "THRO_Acc", "THRO_AccEfZ", "THRO_Throw", "THRO_AttOk", "THRO_HgtOk", "THRO_PosOk", "PRX_TimeUS", "PRX_Health", "PRX_D0", "PRX_D45", "PRX_D90", "PRX_D135", "PRX_D180", "PRX_D225", "PRX_D270", "PRX_D315", "PRX_DUp", "PRX_CAn", "PRX_CDis")

import csv
import json
import os
from math import pi, sqrt
from datetime import datetime, timedelta
from app.log_parser.sdlog2_dump import SDLog2Parser
from app.log_parser.transverse_mercator import tranmerc
# from sdlog2_dump import SDLog2Parser
# from transverse_mercator import tranmerc


class log_parse():
    def __init__(self):
        pass

    def file_creation(self, filename):

        # Init Params
        debug_out = False
        correct_errors = False
        msg_filter = [('PARM', ['Value']), ('GPS', ['GMS', 'GWk', 'Lat', 'Lng', 'Alt']), ('CURR', ['Volt']), ('POS', ['RelHomeAlt'])]
        msg_filters = ["PARM_Value", "GPS_GMS", "GPS_GWk", "GPS_Lat", "GPS_Lng", "GPS_Alt", "CURR_Volt", "POS_RelHomeAlt"]
        csv_null = ""
        csv_delim = ","
        time_msg = "TIME"
        file_name = "out_to_csv.csv"
        opt = None

        parser = SDLog2Parser()
        parser.setCSVDelimiter(csv_delim)
        parser.setCSVNull(csv_null)
        parser.setMsgFilter(msg_filter)
        parser.setTimeMsg(time_msg)
        parser.setFileName(file_name)
        parser.setDebugOut(debug_out)
        parser.setCorrectErrors(correct_errors)
        parser.process(filename)

        print("CSV Created!!")

        csvfile = open('out_to_csv.csv', 'r')
        reader = csv.DictReader(csvfile, msg_filters)

        with open('json_from_csv.json', 'w') as jsonfile:
            jsonfile.write('[')
            for row in reader:
                json.dump(row, jsonfile)
                jsonfile.write(',\n')
            jsonfile.write(']')
        csvfile.close()

        with open('json_from_csv.json', 'r') as infile, \
                open('json_clean.json', 'w') as outfile:
            data = infile.read()
            data = data.replace(",\n]", "]")
            outfile.write(data)

        os.remove('out_to_csv.csv')
        os.remove('json_from_csv.json')
        os.rename('json_clean.json', 'json_from_csv.json')
        print("JSON Created!!")

    def weeksecondstoutc(self, gpsweek, gpsseconds, leapseconds):
        datetimeformat = "%Y-%m-%d %H:%M:%S:%f"
        epoch = datetime.strptime("1980-01-06 00:00:00:000", datetimeformat)
        elapsed = timedelta(days=(gpsweek*7), seconds=(gpsseconds + leapseconds))
        return datetime.strftime(epoch + elapsed, datetimeformat)

    def json_parse(self):
        first_GWk, first_GMS, last_GWk, last_GMS = 0, 0, 0, 0
        max_alt = -10
        flights = []
        coords = []
        with open('json_from_csv.json') as parseData:
            jsn = json.load(parseData)
            for i in range(10, len(jsn)):
                if float(jsn[i]["POS_RelHomeAlt"]) > 0.5:
                    if not first_GMS:
                        first_GMS = jsn[i]["GPS_GMS"]
                        first_GWk = jsn[i]["GPS_GWk"]
                        home_lat = jsn[i]["GPS_Lat"]
                        home_lng = jsn[i]["GPS_Lng"]
                        coords.append([home_lat + "," + home_lng])
                        flights.append([first_GMS, first_GWk, last_GMS, last_GWk, home_lat, home_lng, coords, max_alt])
                    last_GMS = jsn[i]["GPS_GMS"]
                    last_GWk = jsn[i]["GPS_GWk"]
                    coords.append([jsn[i]["GPS_Lat"] + "," + jsn[i]["GPS_Lng"]])
                    if float(jsn[i]["POS_RelHomeAlt"]) > max_alt:
                        max_alt = float(jsn[i]["POS_RelHomeAlt"])
                    flights[-1] = [first_GMS, first_GWk, last_GMS, last_GWk, home_lat, home_lng, coords, max_alt]
                else:
                    if first_GMS:
                        first_GWk, first_GMS, last_GWk, last_GMS = 0, 0, 0, 0
                        coords = []
                        max_alt = -10
        print("Timestamps calculated!!")
        return flights

    def calculate_distance(self, coords):
        # WGS-84 defines
        wgs84_a = 6378137.0  # WGS84 semi-major axis of ellipsoid [m]
        wgs84_f = 1 / 298.257223563  # WGS84 flattening of ellipsoid
        deg2rad = pi / 180.0

        # UTM defines
        utm_false_easting = 500000.0
        utm_scale_factor = 0.9996
        utm_origin_latitude = 0.0

        # UTM zone defines
        false_northing = 0.0
        central_meridian = 9.0

        distance = 0

        tm = tranmerc(wgs84_a, wgs84_f, utm_origin_latitude, central_meridian*deg2rad, utm_false_easting, false_northing, utm_scale_factor)

        for coord in coords:
            if coord == coords[0]:
                coord = coord[0].split(",")
                (e_old, n_old) = tm.geodetic_to_tranmerc(float(coord[0])*deg2rad, float(coord[1])*deg2rad)
                continue
            coord = coord[0].split(",")
            (e_new, n_new) = tm.geodetic_to_tranmerc(float(coord[0])*deg2rad, float(coord[1])*deg2rad)
            distance += sqrt((e_new - e_old)**2 + (n_new - n_old)**2)
            (e_old, n_old) = (e_new, n_new)
        return distance

    def log_generation(self, flights, pilot):
        CET = 3600
        CEST = 2 * CET
        logs = []
        for flight in flights:
            log = {}
            first_tmstmp = self.weeksecondstoutc(int(flight[1]), int(flight[0]) / 1000 + CEST, 37)
            last_tmstmp = self.weeksecondstoutc(int(flight[3]), int(flight[2]) / 1000 + CEST, 37)
            max_alt = flight[-1]

            FMT = "%Y-%m-%d %H:%M:%S:%f"

            tdelta = datetime.strptime(last_tmstmp, FMT) - datetime.strptime(first_tmstmp, FMT)

            log["date"] = first_tmstmp[:10]
            log["time"] = first_tmstmp[11:16]
            drtn = tdelta.__str__().split(".")[0].split(":")
            log["duration"] = "{}".format(drtn[1] + ":" + drtn[2])
            # print("Tm_Delta: ", tdelta.__str__())
            # print("Duration: ", log['duration'])
            log["regNum"] = 4775767
            log["droneNum"] = 11534
            log["pilot"] = pilot
            log["pilotNum"] = None
            log["location"] = "{},{}".format(flight[4], flight[5])
            log["altitude"] = round(max_alt, 3)
            log["weather"] = "Sunny"
            log["distance"] = "{}".format(int(self.calculate_distance(flight[-2])))
            log["notes"] = ""
            logs.append(log)
        return logs