
from matplotlib.colors import LinearSegmentedColormap
from numpy import nan, inf

# Used to reconstruct the colormap in pycam02ucs.cm.viscm
parameters = {'xp': [21.08555470468832, 30.211106249012431, 45.30336457231769, 32.317002759241092, 13.363934167183317, 2.4834688643353502],
              'yp': [-10.17348576012833, -17.19314079422378, -0.34596871239466509, 20.362013638186966, 19.660048134777412, 1.4089450461291904],
              'min_Jp': 15.067114094,
              'max_Jp': 97.9530201342}

cm_data = [[ 0.21091105,  0.04030139,  0.19250061],
       [ 0.21551701,  0.04174524,  0.19719814],
       [ 0.22015155,  0.04312545,  0.20185817],
       [ 0.22481488,  0.04444609,  0.20647712],
       [ 0.22950698,  0.04570915,  0.21105128],
       [ 0.23422764,  0.04691689,  0.21557686],
       [ 0.23897643,  0.04807181,  0.22005004],
       [ 0.24375355,  0.04917501,  0.22446776],
       [ 0.24855831,  0.05022926,  0.22882619],
       [ 0.25338864,  0.0512401 ,  0.23312052],
       [ 0.25824333,  0.05221116,  0.23734714],
       [ 0.26312107,  0.0531462 ,  0.24150261],
       [ 0.26802183,  0.05404644,  0.24558454],
       [ 0.27294229,  0.05491955,  0.24958864],
       [ 0.27788075,  0.05577001,  0.25351213],
       [ 0.28283572,  0.05660179,  0.25735261],
       [ 0.28780573,  0.05741891,  0.26110794],
       [ 0.29278802,  0.05822782,  0.26477578],
       [ 0.29778074,  0.05903323,  0.26835457],
       [ 0.30278237,  0.05983915,  0.27184309],
       [ 0.30779062,  0.0606511 ,  0.27524024],
       [ 0.31280359,  0.06147378,  0.27854536],
       [ 0.31781954,  0.06231155,  0.28175809],
       [ 0.32283665,  0.06316887,  0.28487836],
       [ 0.32785331,  0.06404973,  0.28790637],
       [ 0.33286798,  0.06495789,  0.29084254],
       [ 0.3378788 ,  0.06589765,  0.29368763],
       [ 0.34288474,  0.06687162,  0.29644245],
       [ 0.34788455,  0.06788272,  0.29910804],
       [ 0.35287665,  0.06893437,  0.30168574],
       [ 0.35786001,  0.07002883,  0.30417692],
       [ 0.3628339 ,  0.07116771,  0.30658292],
       [ 0.36779738,  0.07235284,  0.30890528],
       [ 0.37274879,  0.07358723,  0.31114616],
       [ 0.37768812,  0.07487079,  0.31330685],
       [ 0.38261463,  0.0762046 ,  0.31538909],
       [ 0.38752752,  0.07758976,  0.3173948 ],
       [ 0.39242569,  0.07902773,  0.31932631],
       [ 0.39730922,  0.08051781,  0.32118494],
       [ 0.40217762,  0.08206025,  0.32297255],
       [ 0.40703035,  0.08365524,  0.32469111],
       [ 0.41186639,  0.08530363,  0.32634321],
       [ 0.41668605,  0.0870041 ,  0.32792998],
       [ 0.42148896,  0.08875633,  0.32945329],
       [ 0.4262748 ,  0.09055988,  0.33091498],
       [ 0.43104288,  0.09241481,  0.33231747],
       [ 0.43579309,  0.0943202 ,  0.33366237],
       [ 0.44052544,  0.09627505,  0.33495114],
       [ 0.44523968,  0.09827863,  0.33618554],
       [ 0.44993558,  0.1003302 ,  0.33736732],
       [ 0.4546126 ,  0.10242937,  0.33849883],
       [ 0.45927076,  0.10457504,  0.33958145],
       [ 0.46391003,  0.10676615,  0.34061655],
       [ 0.46853025,  0.10900188,  0.34160578],
       [ 0.47313123,  0.11128137,  0.34255077],
       [ 0.47771276,  0.11360383,  0.34345323],
       [ 0.48227446,  0.11596866,  0.34431531],
       [ 0.4868165 ,  0.11837468,  0.34513786],
       [ 0.49133873,  0.12082107,  0.34592237],
       [ 0.49584101,  0.12330703,  0.34667036],
       [ 0.50032319,  0.12583178,  0.3473833 ],
       [ 0.50478514,  0.12839457,  0.34806264],
       [ 0.50922653,  0.13099481,  0.34871043],
       [ 0.5136474 ,  0.13363162,  0.34932753],
       [ 0.51804765,  0.13630428,  0.34991524],
       [ 0.52242715,  0.13901213,  0.35047494],
       [ 0.52678576,  0.14175453,  0.35100796],
       [ 0.53112334,  0.14453086,  0.35151566],
       [ 0.53543974,  0.14734054,  0.35199935],
       [ 0.53973475,  0.15018303,  0.35246068],
       [ 0.54400828,  0.15305775,  0.35290077],
       [ 0.54826024,  0.15596417,  0.35332068],
       [ 0.55249046,  0.15890179,  0.35372168],
       [ 0.55669882,  0.16187014,  0.354105  ],
       [ 0.56088516,  0.16486876,  0.3544719 ],
       [ 0.56504932,  0.16789724,  0.35482358],
       [ 0.56919116,  0.17095514,  0.35516127],
       [ 0.5733105 ,  0.17404209,  0.35548626],
       [ 0.57740716,  0.17715771,  0.35579994],
       [ 0.58148103,  0.18030163,  0.35610318],
       [ 0.58553195,  0.18347353,  0.35639716],
       [ 0.58955975,  0.18667307,  0.35668306],
       [ 0.59356426,  0.18989996,  0.35696203],
       [ 0.59754531,  0.1931539 ,  0.35723524],
       [ 0.60150274,  0.19643462,  0.35750384],
       [ 0.60543637,  0.19974184,  0.35776898],
       [ 0.60934601,  0.20307532,  0.3580318 ],
       [ 0.61323149,  0.20643479,  0.35829358],
       [ 0.61709264,  0.20982001,  0.35855545],
       [ 0.62092927,  0.21323079,  0.3588184 ],
       [ 0.62474121,  0.2166669 ,  0.35908358],
       [ 0.62852826,  0.22012815,  0.35935211],
       [ 0.63229025,  0.22361434,  0.35962514],
       [ 0.63602698,  0.22712526,  0.35990378],
       [ 0.63973827,  0.23066075,  0.36018918],
       [ 0.64342393,  0.23422062,  0.36048247],
       [ 0.64708376,  0.23780469,  0.36078478],
       [ 0.65071758,  0.2414128 ,  0.36109725],
       [ 0.65432519,  0.24504478,  0.36142103],
       [ 0.65790642,  0.24870042,  0.36175737],
       [ 0.66146107,  0.25237962,  0.36210727],
       [ 0.66498894,  0.2560822 ,  0.36247186],
       [ 0.66848985,  0.25980803,  0.3628523 ],
       [ 0.6719636 ,  0.26355694,  0.36324973],
       [ 0.67541002,  0.26732877,  0.36366529],
       [ 0.6788289 ,  0.27112339,  0.36410013],
       [ 0.68222007,  0.27494063,  0.36455541],
       [ 0.68558335,  0.27878034,  0.36503228],
       [ 0.68891855,  0.28264237,  0.36553191],
       [ 0.69222551,  0.28652657,  0.36605543],
       [ 0.69550403,  0.29043276,  0.36660403],
       [ 0.69875397,  0.29436081,  0.36717885],
       [ 0.70197517,  0.2983105 ,  0.36778118],
       [ 0.70516745,  0.3022817 ,  0.36841205],
       [ 0.70833066,  0.30627426,  0.36907265],
       [ 0.71146465,  0.31028799,  0.36976413],
       [ 0.71456926,  0.31432273,  0.37048766],
       [ 0.71764437,  0.3183783 ,  0.3712444 ],
       [ 0.72068984,  0.32245451,  0.37203552],
       [ 0.72370554,  0.32655117,  0.37286217],
       [ 0.72669136,  0.33066809,  0.37372551],
       [ 0.7296472 ,  0.33480507,  0.37462669],
       [ 0.73257295,  0.3389619 ,  0.37556685],
       [ 0.73546853,  0.34313838,  0.37654715],
       [ 0.73833385,  0.34733429,  0.3775687 ],
       [ 0.74116885,  0.3515494 ,  0.37863265],
       [ 0.74397347,  0.35578349,  0.3797401 ],
       [ 0.7467477 ,  0.36003629,  0.3808922 ],
       [ 0.7494915 ,  0.36430755,  0.38209006],
       [ 0.75220484,  0.36859705,  0.3833347 ],
       [ 0.75488771,  0.37290454,  0.3846272 ],
       [ 0.75754011,  0.37722976,  0.3859686 ],
       [ 0.76016208,  0.38157243,  0.38735994],
       [ 0.76275364,  0.38593227,  0.38880222],
       [ 0.76531487,  0.39030901,  0.39029646],
       [ 0.76784582,  0.39470236,  0.3918436 ],
       [ 0.77034658,  0.39911201,  0.39344462],
       [ 0.77281727,  0.40353766,  0.39510042],
       [ 0.77525801,  0.40797899,  0.39681191],
       [ 0.77766894,  0.4124357 ,  0.39857996],
       [ 0.78005022,  0.41690746,  0.4004054 ],
       [ 0.78240204,  0.42139393,  0.40228905],
       [ 0.7847246 ,  0.42589477,  0.40423167],
       [ 0.78701811,  0.43040966,  0.40623402],
       [ 0.78928282,  0.43493823,  0.4082968 ],
       [ 0.791519  ,  0.43948014,  0.41042068],
       [ 0.79372691,  0.44403503,  0.41260629],
       [ 0.79590688,  0.44860254,  0.41485421],
       [ 0.79805921,  0.45318229,  0.41716501],
       [ 0.80018427,  0.45777393,  0.41953918],
       [ 0.8022824 ,  0.46237708,  0.42197721],
       [ 0.80435401,  0.46699137,  0.4244795 ],
       [ 0.8063995 ,  0.47161641,  0.42704644],
       [ 0.8084193 ,  0.47625183,  0.42967836],
       [ 0.81041386,  0.48089725,  0.43237554],
       [ 0.81238364,  0.48555229,  0.43513824],
       [ 0.81432914,  0.49021658,  0.43796664],
       [ 0.81625086,  0.49488972,  0.44086089],
       [ 0.81814934,  0.49957135,  0.44382109],
       [ 0.82002511,  0.50426109,  0.44684731],
       [ 0.82187874,  0.50895857,  0.44993954],
       [ 0.82371081,  0.51366341,  0.45309776],
       [ 0.82552192,  0.51837524,  0.45632188],
       [ 0.82731267,  0.52309372,  0.45961177],
       [ 0.82908369,  0.52781848,  0.46296727],
       [ 0.83083563,  0.53254916,  0.46638816],
       [ 0.83256914,  0.53728543,  0.46987418],
       [ 0.83428487,  0.54202694,  0.47342504],
       [ 0.83598351,  0.54677336,  0.4770404 ],
       [ 0.83766575,  0.55152438,  0.48071989],
       [ 0.83933228,  0.55627966,  0.4844631 ],
       [ 0.8409838 ,  0.56103891,  0.48826958],
       [ 0.84262102,  0.56580183,  0.49213884],
       [ 0.84424467,  0.57056812,  0.49607039],
       [ 0.84585546,  0.57533751,  0.50006368],
       [ 0.84745413,  0.58010973,  0.50411812],
       [ 0.84904139,  0.58488452,  0.50823314],
       [ 0.850618  ,  0.58966163,  0.5124081 ],
       [ 0.85218529,  0.59444047,  0.5166421 ],
       [ 0.85374411,  0.59922075,  0.52093439],
       [ 0.85529461,  0.60400262,  0.52528451],
       [ 0.85683753,  0.60878586,  0.52969176],
       [ 0.8583736 ,  0.61357028,  0.53415539],
       [ 0.85990356,  0.6183557 ,  0.53867468],
       [ 0.86142814,  0.62314195,  0.54324886],
       [ 0.86294807,  0.62792887,  0.54787717],
       [ 0.86446406,  0.63271632,  0.55255883],
       [ 0.86597747,  0.63750381,  0.55729271],
       [ 0.86749012,  0.64229066,  0.56207733],
       [ 0.86900114,  0.6470776 ,  0.56691276],
       [ 0.87051124,  0.65186451,  0.57179821],
       [ 0.8720211 ,  0.65665132,  0.57673288],
       [ 0.8735314 ,  0.66143793,  0.58171596],
       [ 0.87504282,  0.66622429,  0.58674665],
       [ 0.87655744,  0.67100963,  0.5918232 ],
       [ 0.87807646,  0.67579368,  0.59694439],
       [ 0.87959876,  0.68057725,  0.60211059],
       [ 0.88112499,  0.68536033,  0.60732099],
       [ 0.88265576,  0.69014289,  0.61257483],
       [ 0.8841917 ,  0.69492494,  0.61787133],
       [ 0.88573651,  0.69970503,  0.6232074 ],
       [ 0.8872889 ,  0.70448408,  0.62858361],
       [ 0.88884845,  0.70926258,  0.63399994],
       [ 0.89041574,  0.71404055,  0.63945565],
       [ 0.89199133,  0.71881803,  0.64495   ],
       [ 0.89357956,  0.7235934 ,  0.65047925],
       [ 0.8951785 ,  0.72836784,  0.65604456],
       [ 0.89678759,  0.73314188,  0.66164611],
       [ 0.89840734,  0.73791559,  0.66728321],
       [ 0.90003981,  0.7426884 ,  0.67295388],
       [ 0.90168809,  0.74745931,  0.67865517],
       [ 0.90334876,  0.75223008,  0.68438972],
       [ 0.90502229,  0.7570008 ,  0.6901569 ],
       [ 0.90671002,  0.76177121,  0.69595528],
       [ 0.90841694,  0.76653961,  0.70178017],
       [ 0.9101383 ,  0.77130822,  0.70763553],
       [ 0.91187455,  0.77607716,  0.71352074],
       [ 0.91362804,  0.78084581,  0.71943347],
       [ 0.91540219,  0.78561312,  0.72537025],
       [ 0.9171927 ,  0.7903811 ,  0.73133486],
       [ 0.91899998,  0.79514987,  0.73732675],
       [ 0.9208291 ,  0.7999178 ,  0.74334085],
       [ 0.92267845,  0.80468582,  0.74937844],
       [ 0.92454592,  0.80945502,  0.75544141],
       [ 0.92643337,  0.814225  ,  0.76152773],
       [ 0.92834588,  0.8189942 ,  0.76763213],
       [ 0.93027778,  0.82376502,  0.77376005],
       [ 0.93222943,  0.8285376 ,  0.77991098],
       [ 0.93420833,  0.83330957,  0.78607705],
       [ 0.93620863,  0.83808331,  0.792264  ],
       [ 0.93822985,  0.84285929,  0.79847217],
       [ 0.94027833,  0.8476356 ,  0.80469472],
       [ 0.94235076,  0.85241371,  0.81093487],
       [ 0.94444521,  0.85719456,  0.81719447],
       [ 0.94656768,  0.86197641,  0.82346684],
       [ 0.9487157 ,  0.86676042,  0.82975437],
       [ 0.95088675,  0.87154773,  0.83605955],
       [ 0.95308734,  0.87633648,  0.84237496],
       [ 0.95531414,  0.88112809,  0.84870392],
       [ 0.9575649 ,  0.88592359,  0.85504863],
       [ 0.95984737,  0.8907208 ,  0.86140002],
       [ 0.96215582,  0.89552187,  0.86776412],
       [ 0.96448946,  0.90032737,  0.87414138],
       [ 0.96685678,  0.90513495,  0.8805216 ],
       [ 0.96924935,  0.90994759,  0.88691379],
       [ 0.97167031,  0.91476464,  0.8933137 ],
       [ 0.97412312,  0.9195854 ,  0.89971651],
       [ 0.97660168,  0.9244121 ,  0.90612835],
       [ 0.97911222,  0.92924323,  0.91254089],
       [ 0.98165182,  0.93408006,  0.91895621],
       [ 0.98421788,  0.93892381,  0.9253758 ],
       [ 0.98681863,  0.94377248,  0.93178805],
       [ 0.9894452 ,  0.94862921,  0.93820109],
       [ 0.99210219,  0.95349321,  0.94460663],
       [ 0.99478939,  0.95836515,  0.95100138],
       [ 0.99750216,  0.96324712,  0.9573864 ]]

test_cm = LinearSegmentedColormap.from_list(__file__, cm_data)


if __name__ == "__main__":
    import matplotlib.pyplot as plt
    import numpy as np

    try:
        from pycam02ucs.cm.viscm import viscm
        viscm(test_cm)
    except ImportError:
        print("pycam02ucs not found, falling back on simple display")
        plt.imshow(np.linspace(0, 100, 256)[None, :], aspect='auto',
                   cmap=test_cm)
    plt.show()