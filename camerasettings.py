
xt_sensor = {
    'sensor':                    ['16:9', '4:3', '6:5 (4:3 Cropped)', 'Open Gate'],
    '16:9 HD Apple ProRes':      ['HD', '2K', '3.2K'],
    '4:3 Apple ProRes':          '2K',
    '16:9 ARRIRAW':              '2.8K',
    '6:5 (4:3 Cropped) ARRIRAW': '2.6K',
    'Open Gate ARRIRAW':         '3.4K',
}
mini_cb = {
    'Apple ProRes': ['S16 HD','HD','HD Ana.','2K','2.39:1 2K Ana.','3.2K','4K UHD','4:3 2.8K'],
    'ARRIRAW':      ['2.8K','Open Gate 3.4K','4:3 2.8K (OG 3.4K)','16:9 HD Ana. (OG 3.4K)','2.39:1 2K Ana. (OG 3.4K)'],
}

amira_cb = {
    'Apple ProRes': ['S16 HD','HD','2K','3.2K','4K UHD','2.8K',],
    'ARRIRAW':      ['2.8K']
}
minilf_cb = {
    'Apple ProRes': ['LF 16:9 HD', 'LF 16:9 2K', ],
    'ARRIRAW':      ['LF 16:9 UHD','LF 2.39:1 4.5K', 'LF Open Gate 4.5K']
}
cams = [
    "ALEXA Classic","ALEXA XT",
    "ALEXA SXT","ALEXA Mini",
    "Amira","ALEXA Mini LF",
    "ALEXA LF" ,"ALEXA 65"
    ]
# -------------->>>  CAMERA SETTINGS. ---------------->>>
cam_settngs = {
    'Alexa Classic sensor':               ['16:9','4:3'],
    'Alexa Classic format':               ['Apple Pro Res'],
    'Alexa Classic 16:9 HD Apple ProRes': [['2880','1620','1920','1080'],'3K',['HD','2K']],
    'Alexa Classic 16:9 2K Apple ProRes': [['2868','1614','2048','1152'],'3K',['HD','2K']],
    'Alexa Classic 4:3 2K Apple ProRes':  [['2868','2152','2048','1536'],'3K','2K'],
    # ---------- XT ------------#
    'Alexa XT sensor':                         ['16:9','4:3','6:5 (4:3 Cropped)','Open Gate'],
    'Alexa XT format':                         ['Apple Pro Res','ARRIRAW'],
    'Alexa XT 16:9 2K Apple ProRes':           [['2868','1614','1920','1080'],'3K',['HD','2K','3.2K']],
    'Alexa XT 16:9 HD Apple ProRes':           [['2880','1620','3164','1778'],'3K',['HD','2K','3.2K']],
    'Alexa XT 16:9 3.2K Apple ProRes':         [['3168','1782','2868','1614'],'3K',['HD','2K','3.2K']],
    'Alexa XT 4:3 2K Apple ProRes':            [['2868','2152','2048','1536'],'3K',['2K']],
    'Alexa XT 16:9 2.8K ARRIRAW':              [['2880','1620','2880','1620'],'3K',['2.8K']],
    'Alexa XT 4:3 2.8K ARRIRAW':               [['2880','2160','2880','2160'],'3K',['2.8K']],
    'Alexa XT 6:5 (4:3 Cropped) 2.6K ARRIRAW': [['2578','2160','2578','2160'],'3K',['2.6K']],
    'Alexa XT Open Gate 3.4K ARRIRAW':         [['3424','2202','3414','2198'],'3.4K',['3.4K']],
    # ---------- SXT ------------#
    'Alexa SXT sensor':                        ['16:9','6:5','4:3','Open Gate'],
    'Alexa SXT 16:9 HD Apple ProRes':           [['2880','1620','1920','1080'],'3K',['HD','2K','3.2K','4K UHD']],
    'Alexa SXT 16:9 2K Apple ProRes':           [['2880','1620','2048','1152'],'3K',['HD','2K','3.2K','4K UHD']],
    'Alexa SXT 16:9 3.2K Apple ProRes':         [['3200','1800','3200','1800'],'3K',['HD','2K','3.2K','4K UHD']],
    'Alexa SXT 16:9 4K UHD Apple ProRes':       [['3200','1800','3840','2160'],'3K',['HD','2K','3.2K','4K UHD']],
    'Alexa SXT 6:5 2K Ana Apple ProRes':        [['2560','2146','2048','858'],'3K',['2K Anamorphic','4K Cine Anamorphic']],
    'Alexa SXT 6:5 4K Cine Ana Apple ProRes':   [['2560','2146','4096','1716'],'3K',['2K Anamorphic','4K Cine Anamorphic']],
    'Alexa SXT 4:3 2.8K Apple ProRes':          [['2880','2160','2880','2160'],'3K',['2.8K']],
    'Alexa SXT Open Gate 3.4K Apple ProRes':    [['3424','2202','3424','2202'],'3K',['3.4K', '4K Cine']],
    'Alexa SXT Open Gate 4K Cine Apple ProRes': [['3414','2198','4096','2636'],'3K',['3.4K', '4K Cine']],
    'Alexa SXT 16:9 2.8K ARRIRAW':              [['2880','1620','2880','1620'],'3K',['2.8K','3.2K']],
    'Alexa SXT 16:9 3.2K ARRIRAW':              [['3168','1782','3168','1782'],'3.2K',['2.8K','3.2K']],
    'Alexa SXT 6:5 2.6K ARRIRAW':               [['2592','2160','2578','2160'],'3K',['2.6K']],
    'Alexa SXT 4:3 2.8K ARRIRAW':               [['2880','2160','2880','2160'],'3K',['2.8K']],
    'Alexa SXT Open Gate 3.4K ARRIRAW':         [['3424','2202','3424','2202'],'3.4K',['3.4K']],
    # ---------- Mini ------------#
    'Alexa Mini Apple ProRes':               ['S16 HD','HD','HD Ana.','2K','2.39:1 2K Ana.','3.2K','4K UHD','4:3 2.8K'],
    'Alexa Mini ARRIRAW':                    ['2.8K','Open Gate 3.4K','4:3 2.8K (OG 3.4K)','16:9 HD Ana. (OG 3.4K)',
                                              '2.39:1 2K Ana. (OG 3.4K)'],
    'Alexa Mini S16 HD Apple ProRes':        [['1600','900','1920','1080'],'3K'],
    'Alexa Mini HD Apple ProRes':            [['2880','1620','1920','1080'],'3K'],
    'Alexa Mini HD Ana Apple ProRes':        [['1920','2160','1920','1080'],'3K'],
    'Alexa Mini 2K Apple ProRes':            [['2868','1612','2048','1152'],'3K'],
    'Alexa Mini 2.39:1 2K Ana Apple ProRes': [['2560','2145','2048','858'],'3K'],
    'Alexa Mini 3.2K Apple ProRes':          [['3200','1800','3200','1800'],'3K'],
    'Alexa Mini 4K UHD Apple ProRes':        [['3200','1800','3840','2160'],'3K'],
    'Alexa Mini 4:3 2.8K Apple ProRes':      [['2880','2160','2880','2160'],'3K'],
    'Alexa Mini 2.8K ARRIRAW':               [['2880','1620','2880','1620'],'3K'],
    'Alexa Mini Open Gate 3.4K ARRIRAW':     [['3424','2202','3424','2202'],'3.4K'],
    'Alexa Mini 4:3 2.8K ARRIRAW':           [['2880','2160','2880','2160'],'3K'],
    'Alexa Mini 16:9 HD Ana ARRIRAW':        [['1920','2160','1920','2160'],'3K'],
    'Alexa Mini 2.39:1 2K Ana ARRIRAW':      [['2560','2145','2560','2145'],'3K'],
    # ---------- Amira ------------#
    'Amira S16 HD Apple ProRes': ['1600','900','1920','1080'],
    'Amira HD Apple ProRes':     [['2880','1620','1920','1080'],'3K'],
    'Amira 2K Apple ProRes':     [['2868','1612','2048','1152'],'3K'],
    'Amira 3.2K Apple ProRes':   [['3200','1800','3200','1800'],'3K'],
    'Amira 4K UHD Apple ProRes': [['3200','1800','3840','2160'],'3K'],
    'Amira 2.8K ARRIRAW':        [['2880','1620','2880','1620'],'3K'],
    # ---------- Mini LF ------------#
    'Alexa Mini LF LF 16:9 HD Apple ProRes':        [['3840','2160','1920','1080'],'4K'['HD','2K','4K UHD',]],
    'Alexa Mini LF LF 16:9 2K Apple ProRes':        [['3840','2160','2048','2160'],'4K'['HD','2K','4K UHD',]],
    'Alexa Mini LF LF 16:9 4K UHD Apple ProRes':    [['3840','2160','3840','2160'],'4K'],
    'Alexa Mini LF LF 2.39:1 4.5K Apple ProRes':    [['4448','1856','4448','1856'],'4.5K'],
    'Alexa Mini LF LF Open Gate 4.5K Apple ProRes': [['4448','3096','4448','3096'],'4.5K'],
    'Alexa Mini LF LF 16:9 ARRIRAW 4K UHD':         [['3840','2160','3840','2160'],'4K'],
    'Alexa Mini LF LF LF 2.39:1 ARRIRAW 4.5K':      [['4448','1856','4448','1856'],'4.5K'],
    'Alexa Mini LF LF Open Gate ARRIRAW 4.5K':      [['4448','3096','4448','3096'],'4.5K'],
    # ---------- LF ------------#
    'Alexa LF sensor':                         ['LF 16:9','LF 2.39:1','LF Open Gate'],
    'Alexa LF LF 16:9 HD Apple ProRes':        [['3840','2160','1920','1080'],'4K',['HD','2K','4K UHD',]],
    'Alexa LF LF 16:9 2K Apple ProRes':        [['3840','2160','2048','1152'],'4K',['HD','2K','4K UHD',]],
    'Alexa LF LF 16:9 4K UHD Apple ProRes':    [['3840','2160','3840','2160'],'4K',['HD','2K','4K UHD',]],
    'Alexa LF LF 2.39:1 4.5K Apple ProRes':    [['4448','1856','4448','1856'],'4.5K',['4.5K']],
    'Alexa LF LF Open Gate 4.5K Apple ProRes': [['4448','3096','4448','3096'],'4.5K',['4.5K']],
    'Alexa LF LF 16:9 4K UHD ARRIRAW':         [['3840','2160','4448','1856'],'4K',['4K UHD']],
    'Alexa LF LF 2.39:1 4.5K ARRIRAW':         [['4448','1856','3840','2160'],'4.5K',['4.5K']],
    'Alexa LF LF Open Gate 4.5K ARRIRAW':      [['4448','3096','4448','3096'],'4.5K',['4.5K']],
    # ---------- 65 ------------#
    'Alexa 65 sensor':       ['Open Gate','5.1K','4.3K','4K UHD''LF Open Gate'],
    'Alexa 65 Open Gate':    [['6560','3100'],['6560 x 3100'],'6.5K'],
    'Alexa 65 5.1K':         [['5120','2880'],['5120 x 2880'],'5K'],
    'Alexa 65 4.3K':         [['4320','2880'],['4320 x 2880'],'4K'],
    'Alexa 65 4K UHD':       [['3840','2160'],['3840 x 2160'],'4K'],
    'Alexa 65 LF Open Gate': [['4448','3096'],['4448 x 3096'],'4K'],
}
