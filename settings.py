

####### DATA VALUE (constant): ###########
NB_WAGONS : int = 3
NOM_BANDIT_1 : str = 'Shadow'
NOM_BANDIT_2 : str = 'Killer'
NB_ACTIONS : int = 4
NB_JOUEURS : int = 1
NB_TOURS : int = 1
NB_BALLES : int = 6



############ GAME DATA (for save and load): ############
saveGame : bool = False
gameOver : bool = False
startTheGame : bool = False
startPlanning : bool = False
pauseGame : bool = False

### for fixing value:
nb_wagons : int = NB_WAGONS
nb_actions : int = NB_ACTIONS
canPlusWG : bool = True
canClicAct : bool = True

#### set train carriages image size:
carSizeX : int = 298
carSizeY : int = 85
fullSizeX : int = 148
showFull : bool = False
canSeek : bool = False
pos_4_wagon_1_door_1 : int = 24
pos_4_wagon_1_door_2 : int = 272
pos_4_wagon_2_door_1 : int = 324
pos_4_wagon_2_door_2 : int = 572
pos_4_wagon_3_door_1 : int = 624
pos_4_wagon_3_door_2 : int = 872
pos_4_wagon_4_door_1 : int = 924
pos_4_wagon_4_door_2 : int = 1166

door_pos_4_wagon :list = [
        pos_4_wagon_1_door_1,
        pos_4_wagon_1_door_2,
        pos_4_wagon_2_door_1,
        pos_4_wagon_2_door_2,
        pos_4_wagon_3_door_1,
        pos_4_wagon_3_door_2,
        pos_4_wagon_4_door_1,
        pos_4_wagon_4_door_2,
]

pos_3_wagon_1_door_1 : int = 30
pos_3_wagon_1_door_2 : int = 360
pos_3_wagon_2_door_1 : int = 430
pos_3_wagon_2_door_2 : int = 760
pos_3_wagon_3_door_1 : int = 830
pos_3_wagon_3_door_2 : int = 1164

door_pos_3_wagon :list = [
        pos_3_wagon_1_door_1,
        pos_3_wagon_1_door_2,
        pos_3_wagon_2_door_1,
        pos_3_wagon_2_door_2,
        pos_3_wagon_3_door_1,
        pos_3_wagon_3_door_2,
]

#### set volume
volume : float = 0.0
volume_sound : float = 0.5
unmute : bool = True

#### player states:
playerState : list = ['idle', 'walk', 'attack', 'die']
state : str = str(playerState[0])
playerMove : bool = False
outsideTrain : bool = False
goUp : bool = False
goDown : bool = False
atWagon : int = 1
playerPosX : int = 80
playerPosY : int = 533
playerSizeX : int = 32
playerSizeY : int = 32

canRobItem : bool = False
stopAfterMove : bool = False
stopPointActions_wg3 : list = [110, 310, 510, 710, 910, 1100]
stopPointActions_wg4 : list = [80, 230, 380, 530, 680, 830, 980, 1130]
planningList : list = []

#### Gems:
gemsPosX : int = 533
gemsPosY : int = 300

#### set language:
listCBLangEN : tuple = ('English', 'French', 'Vietnamese')
listCBLangFR : tuple = ('Anglais', 'Fran??ais', 'Vietnamien')
listCBLangVN : tuple = ('Ti???ng Anh', 'Ti???ng Ph??p', 'Ti???ng Vi???t')
langList : list = [0, 1, 2] ### 0:EN / 1:FR / 2:VN
setLang : int = 0 ### set english as language default 


######## DATA COLOR #############
TEXT_BLACK : str = '#0a0403'
TEXT_PURPLE : str = '#603c60'

bg_color : str = TEXT_BLACK
text_color : str = 'purple'

######## FONT TYPE ##############
FONT_HELV : list = ("Helvetica", 15, "bold")


######## SOURCES PATH ##################
### sounds:
path_train_sound : str = "./assets/Sound/start_train_sound.wav"
path_credit_menu_music : str = "./assets/Sound/credit_music.wav"
path_click_sound : str = "./assets/Sound/click_01.wav"
### images:
path_vol_icon_play : str = "./assets/Images/volume-icon-play.png"
path_vol_icon_pause : str = "./assets/Images/volume-icon-pause.png"
path_plus_icon : str = "./assets/Images/plus-icon.png"
path_minus_icon : str = "./assets/Images/minus-icon.png"
path_pause_icon : str = "./assets/Images/pause-icon.png"
path_unpause_icon : str = "./assets/Images/unpause-icon.png"
path_eye_can_look : str = "./assets/Images/eye_can_look.png"
path_eye_can_not_look : str = "./assets/Images/eye_can_not_look.png"
path_arrow_icon_up : str = "./assets/Images/arrow_up.png"
path_github_icon : str = "./assets/Images/github_icon.png"
path_info_icon : str = "./assets/Images/information-icon.png"
path_blue_gem : str = "./assets/Images/Items/blue_diamond.png"
path_green_gem : str = "./assets/Images/Items/green_diamond.png"
path_red_gem : str = "./assets/Images/Items/red_diamond.png"
path_sack_icon : str = "./assets/Images/Items/sack.png"
path_arrow_bullet : str = "./assets/Images/Items/arrow.png"
path_train_car : str = './assets/Images/Train/TrainBack.png'
path_start_menu_bg : str = './assets/Images/Background/pixel_train_city.gif'
path_background_city : str = "./assets/Images/Background/BackgroundCity.png"
path_cloud_bg : str = './assets/Images/Background/clouds1.png'
path_cloud_2_bg : str = './assets/Images/Background/clouds2.png'
path_cloud_3_bg : str = './assets/Images/Background/clouds3.png'
path_train_full_green : str = "./assets/Images/Train/TrainFullGreen.png"
path_train_full_gray : str = "./assets/Images/Train/TrainFullGray.png"
path_train_test_1 : str = "./assets/Images/Train/Train_Test1.png"
path_train_test_2 : str = "./assets/Images/Train/Train_Test2.png"
path_thief_IdleRight : str = "./assets/Images/Caracters/Thief/IdleRight/Idle_"
path_thief_IdleLeft : str = "./assets/Images/Caracters/Thief/IdleLeft/Idle_"
path_thief_WalkRight : str = "./assets/Images/Caracters/Thief/WalkRight/Walk_"
path_thief_WalkLeft : str = "./assets/Images/Caracters/Thief/WalkLeft/Walk_"
path_thief_AttackRight : str = "./assets/Images/Caracters/Thief/AttackRight/Attack_"
path_thief_AttackLeft : str = "./assets/Images/Caracters/Thief/AttackLeft/Attack_"
path_thief_DieRight : str = "./assets/Images/Caracters/Thief/DieRight/Die_"
path_thief_DieLeft : str = "./assets/Images/Caracters/Thief/DieLeft/Die_"
path_night_thief_IdleRight : str = './assets/Images/Caracters/NightThief/IdleRight/Idle_'
path_night_thief_IdleLeft : str = './assets/Images/Caracters/NightThief/IdleLeft/Idle_'
### link url website:
url_github_project : str = "https://github.com/Viet281101/Colt_Express_Tkinter"

gems : list = [path_red_gem, path_blue_gem, path_green_gem]

#################################### LANGUE TEXT SETTING ###########################################
english_text : dict = {
    'play' : "Play",
    'start' : "Start",
    'rule' : "Rules",
    'setting' : "Setting",
    'language' : "Language",
    'music' : "Music",
    'sound' : "Sound",
    'volume' : "the volume",
    'color' : "Color",
    'text' : "Text",
    'change' : "Change",
    'planning' : "Planning",
    'action' : "Action",
    'apply' : "Apply",
    'credit' : "Credit",
    'exit' : "Exit",
    'quit' : "Quit",
    'return' : "Return",
    'lang_not_title': "Language Notification",
    'lang_not' : "Press 'Apply' to load the language !",
    'confirm_quit' : "Are you sure to quit the game ? \nYour data will not be saved !",
    'caracter_move_lr' : "Move one car forward or backward, staying on the same floor.",
    'caracter_move_ud' : "Go inside or climb onto the roof of their current wagon.",
    'caracter_rob' : "Rob a traveler to retrieve loot (or simply loot loot that has been left there).",
    'caracter_shoot' : "Shoot another nearby bandit to make him drop his loot.",
}

francais_texte : dict = {
    'play' : "Jouer",
    'start' : "Partir",
    'rule' : "R??gle",
    'setting' : "Param??tre",
    'language' : "Langue",
    'music' : "Musique",
    'sound' : "Son",
    'volume' : "le volume",
    'color' : "Couleur",
    'text' : "Texte",
    'change' : "Changer",
    'planning' : "Planification",
    'action' : "Action",
    'apply' : "Applique",
    'credit' : "Cr??dit",
    'exit' : "Sortir",
    'quit' : "Quitt??",
    'return' : "Retourne",
    'lang_not_title': "Langue Notification",
    'lang_not' : "Appuyez sur 'Appliquer' pour charger la langue !",
    'confirm_quit' : "Etes-vous s??r de quitter le jeu ? \nVos donn??es ne seront pas enregistr??es !",
    'caracter_move_lr' : "Se d??placer d'un wagon en avant ou en arri??re, en restant au m??me ??tage.",
    'caracter_move_ud' : "Aller ?? l'int??rieur ou grimper sur le toit de leur wagon actuel.",
    'caracter_rob' : "Braquer un voyageur pour r??cup??rer du butin (ou simplement r??cup??rer un butin qui a ??t?? abandonn?? l??).",
    'caracter_shoot' : "Tirer sur un autre bandit proche pour lui faire l??cher son butin.",
}

vietnamese_text : dict = {
    'play' : "Ch??i",
    'start' : "B???t ?????u",
    'rule' : "Quy t???c",
    'setting' : "C??i ?????t",
    'language' : "Ng??n ng???",
    'music' : "??m nh???c",
    'sound' : "??m thanh",
    'volume' : "??m l?????ng",
    'apply' : "??p d???ng",
    'color' : "M??u S???c",
    'text' : "Ch???",
    'change' : "Thay ?????i",
    'planning' : "L???p k??? ho???ch",
    'action' : "H??nh ?????ng",
    'credit' : "D??? ??n",
    'exit' : "Tho??t",
    'quit' : "Tho??t",
    'return' : "Tr??? v???",
    'lang_not_title': "Th??ng b??o ng??n ng???",
    'lang_not' : "Nh???n '??p d???ng' ????? t???i ng??n ng??? !",
    'confirm_quit' : "B???n c?? ch???c ch???n tho??t kh???i tr?? ch??i? \nD??? li???u c???a b???n s??? kh??ng ???????c l??u !",
    'caracter_move_lr' : "Di chuy???n m???t toa t??u v??? ph??a tr?????c ho???c ph??a sau, ho???c ??? tr??n c??ng m???t t???ng.",
    'caracter_move_ud' : "??i v??o b??n trong ho???c tr??o l??n n??c toa xe hi???n t???i c???a h???.",
    'caracter_rob' : "C?????p kh??ch du l???ch ????? l???y chi???n l???i ph???m (ho???c ????n gi???n l?? c?????p chi???n l???i ph???m ???? b??? b??? l???i ??? ????).",
    'caracter_shoot' : "B???n m???t t??n c?????p kh??c g???n ???? ????? khi???n h???n ????nh r??i chi???n l???i ph???m c???a m??nh.",
}




############################################ GAME RULE: ###################################################
game_rule_EN : str = '''


        Overview of game rules:

        The game takes place on board a train, consisting of a locomotive and a number of equal carriages to the number of players. 
        Players embody bandits who have jumped on board to rob the passengers. 
        Objective: collect as much loot as possible, each for himself. 
        This is a game of programming, in which one alternates between two phases:

        - Planning: each player secretly decides on a certain number of actions, which his character will perform in order.

        - Action: perform all the actions number 1, then all the number 2, and this until the end.

        The bandits can be in the wagons or the locomotive, and for each of these elements either indoors or on the roof. 
        In this statement, by abuse of language, we will designate by car a any element of the train, which may be the locomotive. 
        The possible actions for bandits are:

        - Move one car forwards or backwards, staying on the same floor.

        - Go inside or climb onto the roof of their current wagon.

        - Rob a traveler to collect loot (or simply loot loot that has been left there).

        - Shoot another nearby bandit to make him drop his loot. The loot recoverable on board the train are:

        - Purses worth ???100 or ???200, from passengers, inside the wagons.

        - Jewelry worth ???500, from passengers, inside the wagons.

        - A hoard worth ???1000, inside the locomotive, in the custody of the Marshall. 
        A Marshall is present on board the train and can move between the locomotive and the wagons, always staying inside. 
        He shoots at all the bandits who are in the same position as him and forced to take refuge on the roof.

'''

game_rule_FR : str = '''


        Aper??u des r??gles du jeu :

        Le jeu se d??roule ?? bord d'un train, compos?? d'une locomotive et d'un nombre de wagons ??gal au nombre de joueurs.
        Les joueurs incarnent des bandits qui ont saut?? ?? bord pour voler les passagers. 
        Objectif : r??colter le plus de butin possible, chacun pour soi.
        Il s'agit d'un jeu de programmation, dans lequel on alterne entre deux phases :

        - Planification : chaque joueur d??cide secr??tement d'un certain nombre d'actions, que son personnage effectuera dans l'ordre.

        - Action : effectuez toutes les actions num??ro 1, puis toutes les actions num??ro 2, et ce jusqu'?? la fin.

        Les bandits peuvent ??tre dans les wagons ou la locomotive, et pour chacun de ces ??l??ments soit ?? l'int??rieur soit sur le toit.
        Dans cet ??nonc??, par abus de langage, on d??signera par voiture un ??l??ment quelconque du train, qui peut ??tre la locomotive.
        Les actions possibles pour les bandits sont :

        - Avancer ou reculer une voiture en restant au m??me ??tage.

        - Entrez ou montez sur le toit de leur wagon actuel.

        - Voler un voyageur pour r??cup??rer du butin (ou simplement piller le butin qui y a ??t?? laiss??).

        - Tirez sur un autre bandit ?? proximit?? pour lui faire l??cher son butin. Les butins r??cup??rables ?? bord du train sont :

        - Les bourses d'une valeur de 100 ??? ou 200 ???, des passagers, ?? l'int??rieur des wagons.

        - Bijoux d'une valeur de 500 ???, provenant des passagers, ?? l'int??rieur des wagons.

        - Un tr??sor d'une valeur de 1000 ???, ?? l'int??rieur de la locomotive, sous la garde du Mar??chal.
        Un mar??chal est pr??sent ?? bord du train et peut se d??placer entre la locomotive et les wagons, en restant toujours ?? l'int??rieur.
        Il tire sur tous les bandits qui se trouvent dans la m??me position que lui et contraints de se r??fugier sur le toit.

'''


game_rule_VN : str = '''


        T???ng quan lu???t ch??i:

        Tr?? ch??i di???n ra tr??n m???t ??o??n t??u bao g???m m???t ?????u m??y v?? m???t s??? toa xe b???ng v???i s??? l?????ng ng?????i ch??i.
        Ng?????i ch??i h??a th??n th??nh nh???ng t??n c?????p ???? nh???y l??n t??u ????? c?????p h??nh kh??ch. 
        M???c ti??u: thu th???p c??ng nhi???u chi???n l???i ph???m c??ng t???t, m???i ng?????i cho m??nh.
        ????y l?? m???t tr?? ch??i l???p tr??nh, trong ???? ch??ng t??i xen k??? gi???a hai giai ??o???n:

        - L???p k??? ho???ch: m???i ng?????i ch??i b?? m???t quy???t ?????nh m???t s??? h??nh ?????ng m?? nh??n v???t c???a m??nh s??? th???c hi???n theo th??? t???.

        - ?????ng t??c: th???c hi???n h???t ?????ng t??c s??? 1, r???i ?????n ?????ng t??c s??? 2, cho ?????n h???t.

        K??? c?????p c?? th??? ??? trong toa xe ho???c ?????u m??y xe l???a, v?? ?????i v???i t???ng b??? ph???n n??y ??? b??n trong ho???c tr??n m??i nh??.
        Trong tuy??n b??? n??y, b???ng c??ch l???m d???ng ng??n ng???, ch??ng t??i s??? ch??? ?????nh b???ng ?? t?? b???t k??? ph???n t??? n??o c???a ??o??n t??u, c?? th??? l?? ?????u m??y.
        C??c h??nh ?????ng c?? th??? cho k??? c?????p l??:

        - Ti???n ho???c l??i xe khi v???n ??? tr??n c??ng m???t m???t s??n.

        - ??i v??o ho???c tr??o l??n n??c toa xe hi???n t???i c???a h???.

        - C?????p kh??ch du l???ch ????? l???y chi???n l???i ph???m (ho???c ch??? c?????p chi???n l???i ph???m c??n l???i ??? ????).

        - B???n m???t t??n c?????p kh??c g???n ???? ????? khi???n h???n ????nh r??i chi???n l???i ph???m c???a m??nh. Chi???n l???i ph???m c?? th??? l???y ???????c tr??n t??u l??:

        - V?? tr??? gi?? ???100 ho???c ???200 ?????i v???i h??nh kh??ch ????? trong toa xe.

        - ????? trang s???c tr??? gi?? ???500, c???a h??nh kh??ch, b??n trong toa t??u.

        - M???t kho b??u tr??? gi?? ???1000, b??n trong ?????u m??y, do Nguy??n so??i qu???n th??c.
        M???t c???nh s??t tr?????ng c?? m???t tr??n t??u v?? c?? th??? di chuy???n gi???a ?????u m??y v?? c??c toa xe, lu??n ??? b??n trong.
        Anh ta b???n v??o t???t c??? nh???ng t??n c?????p ??? c??ng v??? tr?? v???i anh ta v?? bu???c ph???i tr?? ???n tr??n m??i nh??.

'''



####################################### CREDIT TEXT ############################################################
credits_text_eng : str = '''
---------------------- CREDIT ----------------------

            
            
            
            PROJECT SUPERVISOR:
                    Viet Nguyen
            

            
            
            
            
            GAME PROJECT TESTER:
                    Viet Nguyen
            

            
            
            
            
            SCRIPT PROGRAMMER:
                    Viet Nguyen


            


            ANIMATION/GRAPHIC:
                    by Viet Nguyen

            with the sources from:
                OpenGameArt.com
                Pixelartmaker.com
                LibreSprite
                itch.io

            


            
            MUSIC/SFX:
                    by Viet Nguyen
            
            with the sources from:
                Dictaphone
                rfxgen



            


            PROJECT IDEA:
                    by Oumaima El Joubari
                    (professor)



            

            PRODUCER INFO:
                    Name: Viet Nguyen
                    Student number: 20006303
                    Group/class : L2_A 




---------------------- THANK YOU ----------------------
'''


credits_text_fr : str = '''
---------------------- LE CR??DIT ----------------------

            
            
            
            CHEF DE PROJET:
                    Viet Nguyen
            

            
            
            
            
            TESTEUR DE PROJET DE JEU:
                    Viet Nguyen
            

            
            
            
            
            PROGRAMMATEUR DE SCRIPTS:
                    Viet Nguyen


            


            ANIMATIONS/GRAPHIQUES:
                    par Vi??t Nguyen

            avec les sources de :
                OpenGameArt.com
                Pixelartmaker.com
                LibreSprite
                d??mangeaison.io

            


            
            MUSIQUE/SFX:
                    par Vi??t Nguyen
            
            avec les sources de :
                Dictaphone
                rfxgen



            


            ID??E DE PROJET:
                    par Oumaima El Joubari
                    (professeure)



            

            INFORMATIONS SUR LE PRODUCTEUR:
                    Nom : Viet Nguyen
                    Num??ro d'??tudiant : 20006303
                    Groupe/classe : L2_A




---------------------- MERCI ----------------------

'''


credits_text_vn : str = '''
---------------------- CREDIT ----------------------

            
            
            
            GI??M S??T D??? ??N:
                    Vi???t Nguy???n
            

            
            
            
            
            NG?????I TH??? NGHI???M D??? ??N TR?? CH??I:
                    Vi???t Nguy???n
            

            
            
            
            
            L???P TR??NH K??? HO???CH:
                    Vi???t Nguy???n


            


            HO???T H??NH/H??NH ???NH:
                    Vi???t Nguy???n

            v???i c??c ngu???n t???:
                OpenGameArt.com
                Pixelartmaker.com
                LibreSprite
                itch.io

            


            
            ??M NH???C/SFX:
                    Vi???t Nguy???n
            
            v???i c??c ngu???n t???:
                M??y ?????c ch??nh t???
                rfxgen



            


            ?? T?????NG D??? ??N:
                    c???a Oumaima El Joubari
                    (gi??o s??)



            

            TH??NG TIN NH?? S???N XU???T:
                    T??n: Vi???t Nguy???n
                    M?? s??? sinh vi??n: 20006303
                    Nh??m/l???p : L2_A




---------------------- THANK YOU ----------------------
'''

