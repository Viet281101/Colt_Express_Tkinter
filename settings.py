

####### DATA VALUE (constant): ###########
NB_WAGONS : int = 4
NOM_BANDIT_1 : str = 'Shadow'
NOM_BANDIT_2 : str = 'Killer'
NB_ACTIONS : int = 4
NB_JOUEURS : int = 1
NB_TOURS : int = 1
NB_BALLES : int = 6


#### set train carriages image size:
carSizeX : int = 298
carSizeY : int = 85

#### set volume
volume : float = 0.0
volume_sound : float = 0.5
unmute : bool = True

#### player states:
playerState : list = ['idle', 'walk', 'shoot', 'die']
state : str = str(playerState[0])
canSeek : bool = False
playerPosX : int = 80
playerPosY : int = 533


#### set language:
listCBLangEN : tuple = ('English', 'French', 'Vietnamese')
listCBLangFR : tuple = ('Anglais', 'Français', 'Vietnamien')
listCBLangVN : tuple = ('Tiếng Anh', 'Tiếng Pháp', 'Tiếng Việt')
langList : list = [0, 1, 2] ### 0:EN / 1:FR / 2:VN
setLang : int = 0 ### set english as language default 


######## DATA COLOR #############
TEXT_PURPLE : str = '#0a0403'
TEXT_BLACK : str = '#603c60'

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
path_eye_can_look : str = "./assets/Images/eye_can_look.png"
path_eye_can_not_look : str = "./assets/Images/eye_can_not_look.png"
path_arrow_icon_up : str = "./assets/Images/arrow_up.png"
path_github_icon : str = "./assets/Images/github_icon.png"
path_sack_icon : str = "./assets/Images/Items/sack.png"
path_train_car : str = './assets/Images/Train/TrainBack.png'
path_start_menu_bg : str = './assets/Images/Background/pixel_train_city.gif'
path_background_city : str = "./assets/Images/Background/BackgroundCity.png"
path_cloud_bg : str = './assets/Images/Background/cloud.png'
path_train_full_green : str = "./assets/Images/Train/TrainFullGreen.png"
path_train_full_gray : str = "./assets/Images/Train/TrainFullGray.png"
path_thief_IdleRight : str = "./assets/Images/Caracters/Thief/IdleRight/Idle_"
path_thief_IdleLeft : str = "./assets/Images/Caracters/Thief/IdleLeft/Idle_"
path_thief_WalkRight : str = "./assets/Images/Caracters/Thief/WalkRight/Walk_"
path_thief_WalkLeft : str = "./assets/Images/Caracters/Thief/WalkLeft/Walk_"

url_github_project : str = "https://github.com/Viet281101/Colt_Express_Tkinter"


######## LANGUE TEXT SETTING ###########
english_text : dict = {
    'start' : "Start",
    'rule' : "Rules",
    'setting' : "Setting",
    'language' : "Language",
    'music' : "Music",
    'sound' : "Sound",
    'volume' : "the volume",
    'apply' : "Apply",
    'credit' : "Credit",
    'exit' : "Exit",
    'quit' : "Quit",
    'return' : "Return",
    'caracter_move_lr' : "Move one car forward or backward, staying on the same floor.",
    'caracter_move_ud' : "Go inside or climb onto the roof of their current wagon.",
    'caracter_rob' : "Rob a traveler to retrieve loot (or simply loot loot that has been left there).",
    'caracter_shoot' : "Shoot another nearby bandit to make him drop his loot.",
}

francais_texte : dict = {
    'start' : "Jouer",
    'rule' : "Règle",
    'setting' : "Paramètre",
    'language' : "Langue",
    'music' : "Musique",
    'sound' : "Son",
    'volume' : "le volume",
    'apply' : "Applique",
    'credit' : "Crédit",
    'exit' : "Sortir",
    'quit' : "Quitté",
    'return' : "Retourne",
    'caracter_move_lr' : "Se déplacer d'un wagon en avant ou en arrière, en restant au même étage.",
    'caracter_move_ud' : "Aller à l'intérieur ou grimper sur le toit de leur wagon actuel.",
    'caracter_rob' : "Braquer un voyageur pour récupérer du butin (ou simplement récupérer un butin qui a été abandonné là).",
    'caracter_shoot' : "Tirer sur un autre bandit proche pour lui faire lâcher son butin.",
}

vietnamese_text : dict = {
    'start' : "Bắt đầu",
    'rule' : "Quy tắc",
    'setting' : "Cài đặt",
    'language' : "Ngôn ngữ",
    'music' : "Âm nhạc",
    'sound' : "Âm thanh",
    'volume' : "âm lượng",
    'apply' : "Áp dụng",
    'credit' : "Credit",
    'exit' : "Thoát",
    'quit' : "Thoát",
    'return' : "Return",
    'caracter_move_lr' : "Di chuyển một toa tàu về phía trước hoặc phía sau, hoặc ở trên cùng một tầng.",
    'caracter_move_ud' : "Đi vào bên trong hoặc trèo lên nóc toa xe hiện tại của họ.",
    'caracter_rob' : "Cướp khách du lịch để lấy chiến lợi phẩm (hoặc đơn giản là cướp chiến lợi phẩm đã bị bỏ lại ở đó).",
    'caracter_shoot' : "Bắn một tên cướp khác gần đó để khiến hắn đánh rơi chiến lợi phẩm của mình.",
}

########## CREDIT TEXT ######################
credits_text_eng = '''
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


credits_text_fr = '''
---------------------- LE CRÉDIT ----------------------

            
            
            
            CHEF DE PROJET:
                    Viet Nguyen
            

            
            
            
            
            TESTEUR DE PROJET DE JEU:
                    Viet Nguyen
            

            
            
            
            
            PROGRAMMATEUR DE SCRIPTS:
                    Viet Nguyen


            


            ANIMATIONS/GRAPHIQUES:
                    par Viêt Nguyen

            avec les sources de :
                OpenGameArt.com
                Pixelartmaker.com
                LibreSprite
                démangeaison.io

            


            
            MUSIQUE/SFX:
                    par Viêt Nguyen
            
            avec les sources de :
                Dictaphone
                rfxgen



            


            IDÉE DE PROJET:
                    par Oumaima El Joubari
                    (professeure)



            

            INFORMATIONS SUR LE PRODUCTEUR:
                    Nom : Viet Nguyen
                    Numéro d'étudiant : 20006303
                    Groupe/classe : L2_A




---------------------- MERCI ----------------------

'''


credits_text_vn = '''
---------------------- CREDIT ----------------------

            
            
            
            GIÁM SÁT DỰ ÁN:
                    Việt Nguyễn
            

            
            
            
            
            NGƯỜI THỬ NGHIỆM DỰ ÁN TRÒ CHƠI:
                    Việt Nguyễn
            

            
            
            
            
            LẬP TRÌNH KẾ HOẠCH:
                    Việt Nguyễn


            


            HOẠT HÌNH/HÌNH ẢNH:
                    Việt Nguyễn

            với các nguồn từ:
                OpenGameArt.com
                Pixelartmaker.com
                Tự doSprite
                itch.io

            


            
            ÂM NHẠC/SFX:
                    Việt Nguyễn
            
            với các nguồn từ:
                Máy đọc chính tả
                rfxgen



            


            Ý TƯỞNG DỰ ÁN:
                    của Oumaima El Joubari
                    (giáo sư)



            

            THÔNG TIN NHÀ SẢN XUẤT:
                    Tên: Việt Nguyễn
                    Mã số sinh viên: 20006303
                    Nhóm/lớp : L2_A




---------------------- THANK YOU ----------------------
'''

