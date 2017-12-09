import os

token = os.environ['BOT_TOKEN']

about_text_file = 'data/about_data/about_text_message'
help_text_file = 'data/help_data/help_text_message'
bl_text_file = 'data/bl_data/bl_text_messages'
bl_images_locations = 'data/bl_data/images/'
deer_messages_location = 'data/deer_data/messages'
math_test_file = 'data/tests/math'
test_files = {'math' : 'data/tests/math',
              'rus' : 'data/tests/rus',
              'phys' : 'data/tests/phys',
              'inf' : 'data/tests/inf'}

wolfram_appid = os.environ['WOLFRAM_APPID']
wolfram_bad_status_message = "Запрос не найдён.\nЕсли ты ввёл его на русском, то попробуй ввести его на английском."
wolfram_empty_query_message = "Использование: `/wolfram <запрос>` или `/wf <запрос>`"

tts_empty_query_message = "Использование: `/voice <запрос>` или `/tts <запрос>`"

pidor_already_registred_message = "Ты уже зарегистрирован в игре!"
pidor_noone_registred_message = "В игре нет зарегистрированных!"
pidor_now_registred = "Теперь ты учавствуешь в розыгрыше!"
pidor_one_registred_message = "Пока только один человек зарегистрировался в игре! Нужно как минимум два!"
pidor_recognized = "Пидоря дня — @"
pidor_registred = []
pidor_text_files = 'data/pidor_data/text_files/'
pidor_audio_files = 'data/pidor_data/audio_files/'

my_id = os.environ['MY_ID']

kek_message = "Вы ботом ошиблись.."

cho_pacani_anime_sticker = 'CAADAgADJwADtIuIDaIy4m-uZXREAg'
chto_pacani_pattern = r'(?iu).*чт?[оеё],? п[ао][цс][ао]ны'

math_variants = ['http://math.ege.sdamgia.ru/test?id=15625131', 'http://math.ege.sdamgia.ru/test?id=15625132', 'http://math.ege.sdamgia.ru/test?id=15625133', 'http://math.ege.sdamgia.ru/test?id=15625134', 'http://math.ege.sdamgia.ru/test?id=15625135', 'http://math.ege.sdamgia.ru/test?id=15625136', 'http://math.ege.sdamgia.ru/test?id=15625137', 'http://math.ege.sdamgia.ru/test?id=15625138', 'http://math.ege.sdamgia.ru/test?id=15625139', 'http://math.ege.sdamgia.ru/test?id=15625140', 'http://math.ege.sdamgia.ru/test?id=15625141', 'http://math.ege.sdamgia.ru/test?id=15625142', 'http://math.ege.sdamgia.ru/test?id=15625143', 'http://math.ege.sdamgia.ru/test?id=15625144', 'http://math.ege.sdamgia.ru/test?id=15625145', 'http://math.ege.sdamgia.ru/test?id=15416964', 'http://math.ege.sdamgia.ru/test?id=15416965', 'http://math.ege.sdamgia.ru/test?id=15416966', 'http://math.ege.sdamgia.ru/test?id=15416967', 'http://math.ege.sdamgia.ru/test?id=15416968', 'http://math.ege.sdamgia.ru/test?id=15416969', 'http://math.ege.sdamgia.ru/test?id=15416970', 'http://math.ege.sdamgia.ru/test?id=15416971', 'http://math.ege.sdamgia.ru/test?id=15416972', 'http://math.ege.sdamgia.ru/test?id=15416973', 'http://math.ege.sdamgia.ru/test?id=15416974', 'http://math.ege.sdamgia.ru/test?id=15416975', 'http://math.ege.sdamgia.ru/test?id=15416976', 'http://math.ege.sdamgia.ru/test?id=15416977', 'http://math.ege.sdamgia.ru/test?id=15416978', 'http://math.ege.sdamgia.ru/test?id=15164702', 'http://math.ege.sdamgia.ru/test?id=15164703', 'http://math.ege.sdamgia.ru/test?id=15164704', 'http://math.ege.sdamgia.ru/test?id=15164705', 'http://math.ege.sdamgia.ru/test?id=15164706', 'http://math.ege.sdamgia.ru/test?id=15164707', 'http://math.ege.sdamgia.ru/test?id=15164708', 'http://math.ege.sdamgia.ru/test?id=15164709', 'http://math.ege.sdamgia.ru/test?id=15164710', 'http://math.ege.sdamgia.ru/test?id=15164711', 'http://math.ege.sdamgia.ru/test?id=15164712', 'http://math.ege.sdamgia.ru/test?id=15164713', 'http://math.ege.sdamgia.ru/test?id=15164714', 'http://math.ege.sdamgia.ru/test?id=15164715', 'http://math.ege.sdamgia.ru/test?id=15164716', 'http://math.ege.sdamgia.ru/test?id=15106999', 'http://math.ege.sdamgia.ru/test?id=15107000', 'http://math.ege.sdamgia.ru/test?id=15107001', 'http://math.ege.sdamgia.ru/test?id=15107002', 'http://math.ege.sdamgia.ru/test?id=15107003', 'http://math.ege.sdamgia.ru/test?id=15107004', 'http://math.ege.sdamgia.ru/test?id=15107005', 'http://math.ege.sdamgia.ru/test?id=15107006', 'http://math.ege.sdamgia.ru/test?id=15107007', 'http://math.ege.sdamgia.ru/test?id=15107008', 'http://math.ege.sdamgia.ru/test?id=15107009', 'http://math.ege.sdamgia.ru/test?id=15107010', 'http://math.ege.sdamgia.ru/test?id=15107011', 'http://math.ege.sdamgia.ru/test?id=15107012', 'http://math.ege.sdamgia.ru/test?id=15107013', 'http://math.ege.sdamgia.ru/test?id=15057515', 'http://math.ege.sdamgia.ru/test?id=15057516', 'http://math.ege.sdamgia.ru/test?id=15057517', 'http://math.ege.sdamgia.ru/test?id=15057518', 'http://math.ege.sdamgia.ru/test?id=15057519', 'http://math.ege.sdamgia.ru/test?id=15057520', 'http://math.ege.sdamgia.ru/test?id=15057521', 'http://math.ege.sdamgia.ru/test?id=15057522', 'http://math.ege.sdamgia.ru/test?id=15057523', 'http://math.ege.sdamgia.ru/test?id=15057524', 'http://math.ege.sdamgia.ru/test?id=15057525', 'http://math.ege.sdamgia.ru/test?id=15057526', 'http://math.ege.sdamgia.ru/test?id=15057527', 'http://math.ege.sdamgia.ru/test?id=15057528', 'http://math.ege.sdamgia.ru/test?id=15057529', 'http://math.ege.sdamgia.ru/test?id=14598511', 'http://math.ege.sdamgia.ru/test?id=14598512', 'http://math.ege.sdamgia.ru/test?id=14598513', 'http://math.ege.sdamgia.ru/test?id=14598514', 'http://math.ege.sdamgia.ru/test?id=14598515', 'http://math.ege.sdamgia.ru/test?id=14598516', 'http://math.ege.sdamgia.ru/test?id=14598517', 'http://math.ege.sdamgia.ru/test?id=14598518', 'http://math.ege.sdamgia.ru/test?id=14598519', 'http://math.ege.sdamgia.ru/test?id=14598520', 'http://math.ege.sdamgia.ru/test?id=14598521', 'http://math.ege.sdamgia.ru/test?id=14598522', 'http://math.ege.sdamgia.ru/test?id=14598523', 'http://math.ege.sdamgia.ru/test?id=14598524', 'http://math.ege.sdamgia.ru/test?id=14598525', 'http://math.ege.sdamgia.ru/test?id=14645095', 'http://math.ege.sdamgia.ru/test?id=14645096', 'http://math.ege.sdamgia.ru/test?id=14645097', 'http://math.ege.sdamgia.ru/test?id=14645098', 'http://math.ege.sdamgia.ru/test?id=14645099', 'http://math.ege.sdamgia.ru/test?id=14645100', 'http://math.ege.sdamgia.ru/test?id=14645101', 'http://math.ege.sdamgia.ru/test?id=14645102', 'http://math.ege.sdamgia.ru/test?id=14645103', 'http://math.ege.sdamgia.ru/test?id=14645104', 'http://math.ege.sdamgia.ru/test?id=14645105', 'http://math.ege.sdamgia.ru/test?id=14645106', 'http://math.ege.sdamgia.ru/test?id=14645107', 'http://math.ege.sdamgia.ru/test?id=14645108', 'http://math.ege.sdamgia.ru/test?id=14645109', 'http://math.ege.sdamgia.ru/test?id=14097360', 'http://math.ege.sdamgia.ru/test?id=14097361', 'http://math.ege.sdamgia.ru/test?id=14097362', 'http://math.ege.sdamgia.ru/test?id=14097363', 'http://math.ege.sdamgia.ru/test?id=14097364', 'http://math.ege.sdamgia.ru/test?id=14097365', 'http://math.ege.sdamgia.ru/test?id=14097366', 'http://math.ege.sdamgia.ru/test?id=14097367', 'http://math.ege.sdamgia.ru/test?id=14097368', 'http://math.ege.sdamgia.ru/test?id=14097369', 'http://math.ege.sdamgia.ru/test?id=14097370', 'http://math.ege.sdamgia.ru/test?id=14097371', 'http://math.ege.sdamgia.ru/test?id=14097372', 'http://math.ege.sdamgia.ru/test?id=14097373', 'http://math.ege.sdamgia.ru/test?id=14097374', 'http://math.ege.sdamgia.ru/test?id=13589889', 'http://math.ege.sdamgia.ru/test?id=13589890', 'http://math.ege.sdamgia.ru/test?id=13589891', 'http://math.ege.sdamgia.ru/test?id=13589892', 'http://math.ege.sdamgia.ru/test?id=13589893', 'http://math.ege.sdamgia.ru/test?id=13589894', 'http://math.ege.sdamgia.ru/test?id=13589895', 'http://math.ege.sdamgia.ru/test?id=13589896', 'http://math.ege.sdamgia.ru/test?id=13589897', 'http://math.ege.sdamgia.ru/test?id=13589898', 'http://math.ege.sdamgia.ru/test?id=13589899', 'http://math.ege.sdamgia.ru/test?id=13589900', 'http://math.ege.sdamgia.ru/test?id=13589901', 'http://math.ege.sdamgia.ru/test?id=13589902', 'http://math.ege.sdamgia.ru/test?id=13589903', 'http://math.ege.sdamgia.ru/test?id=13137083', 'http://math.ege.sdamgia.ru/test?id=13137084', 'http://math.ege.sdamgia.ru/test?id=13137085', 'http://math.ege.sdamgia.ru/test?id=13137086', 'http://math.ege.sdamgia.ru/test?id=13137087', 'http://math.ege.sdamgia.ru/test?id=13137088', 'http://math.ege.sdamgia.ru/test?id=13137089', 'http://math.ege.sdamgia.ru/test?id=13137090', 'http://math.ege.sdamgia.ru/test?id=13137091', 'http://math.ege.sdamgia.ru/test?id=13137092', 'http://math.ege.sdamgia.ru/test?id=13137093', 'http://math.ege.sdamgia.ru/test?id=13137094', 'http://math.ege.sdamgia.ru/test?id=13137095', 'http://math.ege.sdamgia.ru/test?id=13137096', 'http://math.ege.sdamgia.ru/test?id=13137097', 'http://math.ege.sdamgia.ru/test?id=12757701', 'http://math.ege.sdamgia.ru/test?id=12757702', 'http://math.ege.sdamgia.ru/test?id=12757703', 'http://math.ege.sdamgia.ru/test?id=12757704', 'http://math.ege.sdamgia.ru/test?id=12757705', 'http://math.ege.sdamgia.ru/test?id=12757706', 'http://math.ege.sdamgia.ru/test?id=12757707', 'http://math.ege.sdamgia.ru/test?id=12757708', 'http://math.ege.sdamgia.ru/test?id=12757709', 'http://math.ege.sdamgia.ru/test?id=12757710', 'http://math.ege.sdamgia.ru/test?id=12757711', 'http://math.ege.sdamgia.ru/test?id=12757712', 'http://math.ege.sdamgia.ru/test?id=12757713', 'http://math.ege.sdamgia.ru/test?id=12757714', 'http://math.ege.sdamgia.ru/test?id=12757715', 'http://math.ege.sdamgia.ru/test?id=12511034', 'http://math.ege.sdamgia.ru/test?id=12511035', 'http://math.ege.sdamgia.ru/test?id=12511036', 'http://math.ege.sdamgia.ru/test?id=12511037', 'http://math.ege.sdamgia.ru/test?id=12511038', 'http://math.ege.sdamgia.ru/test?id=12511039', 'http://math.ege.sdamgia.ru/test?id=12511040', 'http://math.ege.sdamgia.ru/test?id=12511041', 'http://math.ege.sdamgia.ru/test?id=12511042', 'http://math.ege.sdamgia.ru/test?id=12511043', 'http://math.ege.sdamgia.ru/test?id=12511044', 'http://math.ege.sdamgia.ru/test?id=12511045', 'http://math.ege.sdamgia.ru/test?id=12511046', 'http://math.ege.sdamgia.ru/test?id=12511047', 'http://math.ege.sdamgia.ru/test?id=12511048']